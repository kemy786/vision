import streamlit as st

# 친구 데이터
friends = {
    "박영서": "📘 모범생처럼 보이지만, 속엔 시커먼 본심이 숨어있는 '타격감 만렙' 인간...",
    "이혜연": "🎤 강자 앞에선 스윗, 약자 앞에선 깡패...",
    "백효슬": "💪 근육에 지능을 실은 마라탕 마스터...",
    "오찬이": "🎉 즉흥의 끝판왕...",
    "송수민": "🔥 외강내유의 화신...",
    "강수현": "🍔 먹는 게 인생...",
    "원민이": "🌿 나무늘보 그 자체..."
}

# 질문 데이터
questions = [
    {
        "question": "1. 주말에 뭐 하고 싶어?",
        "options": {
            "a": "책 읽고 혼자 시간 보내기",
            "b": "친구 만나서 수다 떨기",
            "c": "운동이나 땀나는 활동",
            "d": "집에서 넷플릭스 정주행",
        }
    },
    {
        "question": "2. 친구가 장난치면 넌?",
        "options": {
            "a": "일단 참다가 복수한다",
            "b": "같이 장난치며 논다",
            "c": "진심으로 삐진다",
            "d": "장난은 싫어한다",
        }
    },
    {
        "question": "3. 무인도에 간다면 챙길 것은?",
        "options": {
            "a": "물리책",
            "b": "거울과 화장품",
            "c": "휴대폰과 와이파이",
            "d": "마음의 평화",
        }
    }
]

# 점수 매핑
answer_map = {
    "a": ["박영서", "백효슬"],
    "b": ["이혜연", "강수현"],
    "c": ["송수민", "백효슬"],
    "d": ["오찬이", "원민이"]
}

# Streamlit UI 시작
st.title("🎯 친구 추천 성격 테스트")
st.write("당신의 성격에 맞는 친구를 찾아드릴게요!")

# 답변 저장용
user_answers = []

# 질문 출력
for idx, q in enumerate(questions):
    choice = st.radio(
        q["question"],
        options=list(q["options"].keys()),
        format_func=lambda x, q=q: f"{x}) {q['options'][x]}",
        key=f"q{idx}"
    )
    user_answers.append(choice)

# 제출 버튼
if st.button("결과 보기"):
    # 점수 계산
    scores = {name: 0 for name in friends}
    for ans in user_answers:
        for name in answer_map.get(ans, []):
            scores[name] += 1

    max_score = max(scores.values())
    winners = [name for name, score in scores.items() if score == max_score]

    if len(winners) == 1:
        st.subheader("🎉 당신에게 잘 맞는 친구는...")
        st.success(f"✨ {winners[0]} ✨\n\n{friends[winners[0]]}")
    else:
        st.subheader("🎉 당신과 잘 맞는 친구들:")
        for w in winners:
            st.markdown(f"**✨ {w} ✨**")
            st.write(friends[w])
