from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytz import timezone
import os
import sys

# 현재 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from prompts.constants import TEXT_STYLES
from prompts import get_prompt

app = Flask(__name__)

# SQLite 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conversations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 데이터베이스 모델 정의
class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.Text, nullable=False)
    converted_text = db.Column(db.Text, nullable=False)
    style = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone('Asia/Seoul')))

    def to_dict(self):
        return {
            'id': self.id,
            'original_text': self.original_text,
            'converted_text': self.converted_text,
            'style': self.style,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

client= OpenAI(api_key='your_key')# 여기에 실제 API 키를 넣어주세요

def format_text(input_text, style, max_retries=3):
    if not input_text:
        return "입력 텍스트가 없습니다."
        
    if style not in TEXT_STYLES:
        return "지원하지 않는 스타일입니다."
    
    system_prompt = get_prompt(style)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API 오류: {str(e)}")
        return f"변환 중 오류가 발생했습니다: {str(e)}"

@app.route('/')
def index():
    # 최근 변환 기록 가져오기
    recent_conversations = Conversation.query.order_by(Conversation.timestamp.desc()).limit(10).all()
    return render_template('index.html', styles=TEXT_STYLES, conversations=recent_conversations)

@app.route('/convert', methods=['POST'])
def convert_text():
    try:
        data = request.json
        text = data.get('text', '')
        style = data.get('style', 'formal')
        
        if not text:
            return jsonify({'error': '텍스트를 입력해주세요.'}), 400
            
        formatted_text = format_text(text, style)
        if "오류가 발생했습니다" in formatted_text:
            return jsonify({'error': formatted_text}), 500

        # 데이터베이스에 저장
        conversation = Conversation(
            original_text=text,
            converted_text=formatted_text,
            style=style
        )
        db.session.add(conversation)
        db.session.commit()

        return jsonify({'formatted_text': formatted_text})
        
    except Exception as e:
        print(f"API 엔드포인트 오류: {str(e)}")
        return jsonify({'error': f'서버 오류가 발생했습니다: {str(e)}'}), 500

# 변환 기록 조회 API
@app.route('/history', methods=['GET'])
def get_history():
    try:
        conversations = Conversation.query.order_by(Conversation.timestamp.desc()).limit(50).all()
        return jsonify([conv.to_dict() for conv in conversations])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 변환 기록 초기화 API
@app.route('/reset-history', methods=['POST'])
def reset_history():
    try:
        # 모든 대화 기록 삭제
        Conversation.query.delete()
        db.session.commit()
        return jsonify({'success': True, 'message': '모든 변환 기록이 삭제되었습니다.'})
    except Exception as e:
        db.session.rollback()  # 오류 발생 시 롤백
        return jsonify({'error': f'초기화 중 오류가 발생했습니다: {str(e)}'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 데이터베이스 테이블 생성
    
    if not client.api_key or client.api_key == '':
        print("경고: OpenAI API 키가 설정되지 않았습니다!")
        print("app.py 파일에서 client = OpenAI(api_key='your-api-key-here') 부분을 수정해주세요.")
    app.run(debug=True)
