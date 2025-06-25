import streamlit as st

st.title("🎯 성격으로 알아보는 롤 챔피언 추천기")

st.markdown("아래 질문에 답해보세요!")

# 질문 1
q1 = st.radio("Q1. 사람들과 어울릴 때 에너지가 생겨요", ("그렇다", "아니다"))
# 질문 2
q2 = st.radio("Q2. 계획보다는 즉흥적인 게 좋아요", ("그렇다", "아니다"))
# 질문 3
q3 = st.radio("Q3. 감정보다 논리적으로 판단해요", ("그렇다", "아니다"))
# 질문 4
q4 = st.radio("Q4. 직감보다는 경험이 더 중요해요", ("그렇다", "아니다"))

if st.button("결과 보기"):
    # MBTI 추정
    mbti = ""
    mbti += "E" if q1 == "그렇다" else "I"
    mbti += "P" if q2 == "그렇다" else "J"
    mbti += "T" if q3 == "그렇다" else "F"
    mbti += "S" if q4 == "그렇다" else "N"

    # 간단히 예시용으로 일부 MBTI만 정의
    champ_data = {
        "ENTP": {
            "champ": "이즈리얼",
            "desc": "당신은 창의적이고 도전적인 스타일! 이즈리얼처럼 전장을 누비며 자유롭게 플레이하는 챔피언이 딱 어울려요."
        },
        "ISTJ": {
            "champ": "말파이트",
            "desc": "당신은 계획적이고 책임감 강한 타입. 말파이트처럼 묵직하게 팀을 이끄는 안정적인 챔피언이 어울립니다."
        },
        "INFP": {
            "champ": "유미",
            "desc": "따뜻하고 배려심 깊은 당신에게는 팀을 도와주는 유미가 잘 어울려요. 함께하는 힘을 믿는 스타일!"
        }
        # 필요한 MBTI 더 추가 가능
    }

    st.subheader(f"🧠 당신의 성격 유형은: `{mbti}`")

    if mbti in champ_data:
        champ = champ_data[mbti]["champ"]
        desc = champ_data[mbti]["desc"]
        st.success(f"🎮 추천 챔피언: **{champ}**")
        st.markdown(f"📝 {desc}")
    else:
        st.warning("이 성격 유형은 아직 준비 중이에요!")
