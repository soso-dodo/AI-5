# T-T
AI 기반 문체 변환 시스템


## 💻프로젝트 소개
문자 변환기 프로그램은 사용자가 다양한 상황에서 적합한 문체를 사용할 수 있도록 문자를 변환해주는 도구입니다.


## 🕰️개발 기간
* 25.1.6 - 25.1.13


## 🧑‍💻멤버 구성
* 송동호 : 팀장, 프론트엔드 개발, 백엔드 개발
* 김태우 : 협업도구 운영, 프론트엔드 개발, 백엔드 개발
* 양유진 : 프론트엔드 개발, 백엔드 개발
* 이수진 : 백엔드 개발
* 지원배 : 백엔드 개발


## ⚙️개발 환경
- [`Python 3.12`](https://github.com/conda-forge, "conda-forge")
- `CSS`
- `JavaScript`
- **Flamework** : Flask
- **DB** : SQLite
- **패키지 매니저** : pip


## 🪄API
* OpenAI GPT API
* version : GPT-4o-mini


## ✔️사용법
1. cmd로 가상환경 만들기

   ```bash
   conda create -n project python=3.12

   conda activate project
   ```
   
2. dependencies 설치

   ```bash
   pip install flask

   pip install openai

   pip install python-dotenv
   ```

3. openai api key 삽입
   app.py에 있는 api key 넣는 부분에 key 넣어주기


4. 실행

   ```bash
    python app.py
   ```
