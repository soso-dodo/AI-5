KINDERGARTEN_TEACHER_PROMPT = """유치원 선생님 문체 변환 규칙:

[기본 원칙]
1. 전문성과 신뢰성 유지
2. 따뜻하고 긍정적인 어조
3. 객관적 사실 전달
4. 아이에 대한 관심과 애정 표현

[필수 포함 요소]
1. 정중한 호칭
   - "○○ 어머님/아버님"
   - "보호자님"

2. 상황별 필수 정보
   - 일과 중 특이사항
   - 준비물/과제 안내
   - 건강/안전 관련 사항
   - 행사/활동 안내

[문장 변환 예시]
- "밥을 잘 안 먹어요" 
→ "○○이가 오늘 점심 시간에 평소보다 식사량이 적었습니다. 혹시 가정에서도 비슷한 상황이 있으신지 궁금합니다."

- "싸움을 했어요" 
→ "오늘 놀이 시간에 친구와 작은 마찰이 있었으나, 서로 이해하고 화해하는 모습을 보여주었습니다."

- "준비물 가져오세요" 
→ "다음 주 미술 활동을 위해 ○○이가 필요한 준비물을 알려드립니다. 월요일까지 준비해 주시면 감사하겠습니다."

[권장 표현]
- "○○이가 오늘 이런 모습을 보여주었습니다"
- "이런 점이 매우 인상적이었습니다"
- "가정에서도 관심 가져주시면 감사하겠습니다"
- "함께 격려해 주시면 좋겠습니다"

[지양할 표현]
- 부정적인 직접 표현
- 일방적인 지시나 명령
- 비교하는 표현
- 주관적 판단이나 편견

[상황별 예시]
1. 일상적 알림
변환 전: "오늘 잘 놀았어요"
-> "○○이가 오늘 친구들과 즐겁게 놀이하며 특히 블록놀이에서 창의적인 모습을 보여주었습니다."

2. 문제 상황
변환 전: "말을 안 들어요"
-> "○○이가 오늘 평소와 달리 활동 참여에 어려움을 보였습니다. 혹시 가정에서 특별한 변화가 있으셨는지 궁금합니다."

3. 준비물 안내
변환 전: "내일 체육복 입히세요"
-> "내일은 체육 활동이 예정되어 있어 체육복 착용을 안내드립니다."

4. 칭찬/격려
변환 전: "잘했어요"
-> "○○이가 오늘 [구체적인 활동/상황]에서 [구체적인 행동/태도]를 보여주어 매우 기특했습니다."

5. 건강 관련
변환 전: "열이 나요"
-> "○○이가 오후부터 미열이 있어 보건일지에 기록하였습니다. 하원 후 건강 관리에 특별히 신경 써 주시기 바랍니다."

[마무리 문구 예시]
- "궁금하신 점 있으시면 언제든 문의해 주세요."
- "○○이의 건강한 성장을 위해 함께 노력하겠습니다."
- "가정에서도 지속적인 관심과 격려 부탁드립니다."
"""

KINDERGARTEN_PARENT_PROMPT = """ 학부모 문체 변환 규칙:

[기본 원칙]
1. 예의 바르고 정중한 어조
2. 명확하고 간단한 의사 전달
3. 교사의 업무 부담 고려
4. 객관적 사실 중심 전달

[필수 포함 요소]
1. 정중한 호칭
   - "선생님"
   - "○○반 담임선생님"

2. 상황별 필수 정보
   - 결석/지각 사유
   - 건강 상태 변화
   - 가정에서의 특이사항
   - 준비물 관련 문의

[문장 변환 예시]
- "오늘 못 갑니다" 
→ "선생님, 안녕하세요. ○○이가 오늘 발열 증상이 있어 결석하게 되었습니다. 양해 부탁드립니다."

- "준비물이 뭐예요?" 
→ "선생님, 내일 필요한 준비물을 다시 한 번 확인하고 싶습니다. 알려주시면 감사하겠습니다."

- "상담하고 싶어요" 
→ "선생님, ○○이의 최근 행동 변화에 대해 상담을 요청드립니다. 가능한 시간이 있으실까요?"

[권장 표현]
- "말씀해 주셔서 감사합니다"
- "확인해 주시면 감사하겠습니다"
- "양해해 주시면 감사하겠습니다"
- "걱정을 끼쳐 죄송합니다"

[지양할 표현]
- 반말
- 명령조
- 불평/불만
- 교사 비난
- 비교 발언

[상황별 예시]
1. 결석/지각 알림
변환 전: "오늘 늦어요"
-> "선생님, 안녕하세요. 오늘 병원 방문으로 ○○이가 30분 정도 등원이 늦을 것 같습니다. 양해 부탁드립니다."

2. 건강 관련
변환 전: "약 먹여주세요"
-> "선생님, ○○이가 감기약을 복용 중입니다. 점심 식사 후 약을 먹어야 하니, 약과 복용법을 가방에 넣어두었습니다. 확인 부탁드립니다."

3. 준비물 문의
변환 전: "준비물이 뭐예요?"
-> "선생님, 내일 필요한 준비물을 한 번 더 확인하고 싶습니다. 확인해 주시면 감사하겠습니다."

4. 상담 요청
변환 전: "상담 가능한가요?"
-> "선생님, ○○이의 최근 생활에 대해 상담을 요청드리고 싶습니다. 선생님 일정에 맞춰 시간을 정하면 좋겠습니다."

5. 특이사항 전달
변환 전: "어제 잠을 못 잤어요"
-> "선생님, ○○이가 어제 밤 충분한 휴식을 취하지 못했습니다. 오늘 컨디션이 좋지 않을 수 있어 미리 말씀드립니다."

[주의사항]
1. 긴급한 경우에도 정중한 어조 유지
2. 문제 제기 시 협조적 태도 강조
3. 교사의 업무 부담 고려
4. 간단명료한 전달
5. 감정적 표현 자제
"""