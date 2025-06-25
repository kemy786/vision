import streamlit as st

champ_data = {
    "INTJ": {
        "champ": "베이가",
        "desc": (
            "INTJ는 전략과 계획을 중시하는 유형입니다. 베이가는 작고 귀여운 외모와 달리 어둠의 마법으로 전장을 지배합니다. "
            "그는 치밀한 계산과 인내를 통해 점차 강해지며, INTJ의 체계적 사고와 완벽히 어울립니다. "
            "베이가는 후반 캐리어로 한타 지휘와 적 교란에 능하며, 전략적 플레이를 선호하는 당신에게 최고의 선택입니다. "
            "작은 마법사가 큰 힘을 발휘하는 모습은 INTJ의 끈기와 집중력을 상징하며, 정교한 계획 아래 상대를 압도하는 전략가의 면모를 보여줍니다."
        )
    },
    "INTP": {
        "champ": "하이머딩거",
        "desc": (
            "INTP는 깊은 호기심과 분석적 사고를 가진 유형입니다. 하이머딩거는 독창적인 발명가로, 기계장치를 활용해 전장을 통제합니다. "
            "복잡한 전략과 문제 해결을 즐기며, 창의적인 플레이를 선호하는 당신과 잘 맞습니다. "
            "상황에 맞는 발명품을 배치하며 기민하게 전투를 조율하는 것이 특징입니다. "
            "하이머딩거의 독특한 발명품과 전략적 배치는 INTP의 사고방식과 맞닿아 있으며, 논리적인 해결책을 모색하는 모습이 돋보입니다."
        )
    },
    "ENTJ": {
        "champ": "세트",
        "desc": (
            "ENTJ는 뛰어난 리더십과 추진력을 가진 유형입니다. 세트는 강력한 돌진과 제압 능력으로 팀을 이끕니다. "
            "결단력 있고 목표 지향적인 당신과 닮아 있으며, 전투의 중심에서 팀을 보호하고 적을 압도합니다. "
            "강력한 존재감으로 팀을 승리로 이끄는 전사형 리더 챔피언입니다. "
            "세트의 대담하고 거침없는 공격 스타일은 ENTJ의 카리스마와 통솔력을 잘 반영합니다."
        )
    },
    "ENTP": {
        "champ": "이즈리얼",
        "desc": (
            "ENTP는 모험과 도전을 즐기는 창의적 유형입니다. 이즈리얼은 높은 기동성과 정교한 스킬샷으로 전장을 누빕니다. "
            "즉흥적이고 변화무쌍한 플레이를 좋아하는 당신과 잘 어울리며, 새로운 전략을 탐색하는 탐험가 챔피언입니다. "
            "이즈리얼의 유연한 전투 방식은 ENTP의 독창적이고 활발한 사고방식을 잘 나타냅니다."
        )
    },
    "INFJ": {
        "champ": "카르마",
        "desc": (
            "INFJ는 내면의 신념과 타인 배려가 강한 이상주의자입니다. 카르마는 팀을 조율하고 보호하며 조용하지만 강력한 힘을 발휘합니다. "
            "깊은 통찰력과 배려심이 뛰어난 당신에게 최적화된 서포터 챔피언입니다. "
            "카르마의 균형 잡힌 지원 능력과 진중한 모습은 INFJ의 내면세계와 어우러집니다."
        )
    },
    "INFP": {
        "champ": "유미",
        "desc": (
            "INFP는 감성적이고 이상을 추구하는 치유자입니다. 유미는 아군에게 치유와 보호를 제공하며, 따뜻한 존재감으로 팀에 긍정적 영향을 미칩니다. "
            "섬세하고 배려심 깊은 당신과 완벽히 어울리는 서포터입니다. "
            "유미의 부드럽고 사랑스러운 스타일은 INFP의 다정한 성격과 깊은 감성을 잘 드러냅니다."
        )
    },
    "ENFJ": {
        "champ": "레오나",
        "desc": (
            "ENFJ는 사교적이고 헌신적인 리더입니다. 레오나는 돌진과 군중 제어로 팀 전투를 주도하며, 강인한 보호자 역할을 합니다. "
            "따뜻한 리더십과 강한 존재감을 가진 당신에게 잘 맞는 탱커형 챔피언입니다. "
            "레오나의 단호함과 신뢰감 있는 모습은 ENFJ의 사람을 이끄는 힘과 조화를 이룹니다."
        )
    },
    "ENFP": {
        "champ": "니달리",
        "desc": (
            "ENFP는 활기차고 자유로운 탐험가입니다. 니달리는 민첩한 정글러로, 빠른 적응력과 기습 능력이 뛰어납니다. "
            "열정적이고 호기심 많은 당신에게 어울리는 변화무쌍한 챔피언입니다. "
            "니달리의 민첩한 움직임과 다재다능한 플레이 스타일은 ENFP의 다채로운 성격을 반영합니다."
        )
    },
    "ISTJ": {
        "champ": "말파이트",
        "desc": (
            "ISTJ는 책임감 있고 신중한 유형입니다. 말파이트는 견고한 탱커로 팀의 앞을 지키며 신뢰받는 존재입니다. "
            "묵묵하고 꾸준한 당신과 닮은 플레이 스타일을 자랑합니다. "
            "말파이트의 강인한 방어력과 꾸준한 투지는 ISTJ의 근면성과 성실함을 상징합니다."
        )
    },
    "ISFJ": {
        "champ": "룰루",
        "desc": (
            "ISFJ는 다정하고 세심한 보호자입니다. 룰루는 아군을 변신시키고 보호하는 독특한 능력으로 팀을 돕습니다. "
            "꼼꼼하고 헌신적인 당신에게 완벽히 어울리는 서포터입니다. "
            "룰루의 장난기와 배려심 깊은 모습은 ISFJ의 따뜻한 마음을 잘 표현합니다."
        )
    },
    "ESTJ": {
        "champ": "오른",
        "desc": (
            "ESTJ는 현실적이고 조직적인 지도자입니다. 오른은 튼튼한 탱커이자 조력자로 팀 전력을 강화합니다. "
            "체계적이고 효율적인 당신과 잘 맞는 챔피언입니다. "
            "오른의 견고함과 안정적인 지원은 ESTJ의 실용적이고 책임감 강한 면모를 닮았습니다."
        )
    },
    "ESFJ": {
        "champ": "나미",
        "desc": (
            "ESFJ는 친절하고 사교적인 외교관입니다. 나미는 치유와 군중 제어로 팀을 지원하며 협력을 중시합니다. "
            "따뜻한 마음과 타인 배려가 뛰어난 당신과 잘 어울립니다. "
            "나미의 흐르는 듯한 유연함과 배려심은 ESFJ의 친화적 성격을 잘 나타냅니다."
        )
    },
    "ISTP": {
        "champ": "제드",
        "desc": (
            "ISTP는 침착하고 실용적인 문제 해결사입니다. 제드는 민첩한 암살자로 신속 정확한 공격을 구사합니다. "
            "냉철함과 현실적 판단력이 뛰어난 당신에게 최적의 챔피언입니다. "
            "제드의 은밀하고 빠른 움직임은 ISTP의 분석적이고 현실적인 성향과 잘 맞아떨어집니다."
        )
    },
    "ISFP": {
        "champ": "아리",
        "desc": (
            "ISFP는 감성적이고 예술적인 유형입니다. 아리는 매혹적인 외모와 민첩한 기술로 상대를 교란합니다. "
            "창의력과 섬세함이 뛰어난 당신과 잘 맞는 매력적인 챔피언입니다. "
            "아리의 유연한 전투 스타일과 아름다움은 ISFP의 자유롭고 개성 있는 성격을 반영합니다."
        )
    },
    "ESTP": {
        "champ": "야스오",
        "desc": (
            "ESTP는 용감하고 즉흥적인 활동가입니다. 야스오는 빠른 반응과 뛰어난 기동성으로 전장을 지배합니다. "
            "대담함과 경쟁심이 강한 당신에게 딱 맞는 화려한 전사입니다. "
            "야스오의 역동적인 움직임과 공격성은 ESTP의 대담하고 모험적인 특성과 잘 어울립니다."
        )
    },
    "ESFP": {
        "champ": "사미라",
        "desc": (
            "ESFP는 사교적이고 활기찬 연예인형입니다. 사미라는 화려한 공격과 콤보로 전장을 장악합니다. "
            "긍정적인 에너지와 즐거움을 추구하는 당신과 완벽하게 어울립니다. "
            "사미라의 활발하고 화려한 플레이는 ESFP의 열정적이고 밝은 성격을 잘 보여줍니다."
        )
    },
}

questions = [
    ("새로운 사람들과 어울릴 때 에너지가 넘친다", "E"),
    ("혼자 시간을 보내는 것이 편안하다", "I"),
    ("사람들 앞에서 이야기하는 걸 즐긴다", "E"),
    ("사적인 시간을 혼자 보내는 걸 선호한다", "I"),
    ("사교적인 모임에서 활력이 생긴다", "E"),
    ("혼자서 조용한 시간을 보내는 것을 좋아한다", "I"),
    ("현실적이고 구체적인 정보에 집중하는 편이다", "S"),
    ("상상력과 아이디어를 더 선호한다", "N"),
    ("과거 경험에 기반해 결정을 내린다", "S"),
    ("미래 가능성과 새로운 가능성을 생각하는 걸 좋아한다", "N"),
    ("세부 사항에 주의를 기울이는 편이다", "S"),
    ("큰 그림을 보는 걸 더 즐긴다", "N"),
    ("논리와 객관적인 판단을 우선시한다", "T"),
    ("다른 사람의 감정을 중요하게 생각한다", "F"),
    ("문제를 해결할 때 감정보다 사실에 집중한다", "T"),
    ("사람들의 감정에 공감하는 편이다", "F"),
    ("비판할 때도 감정보다는 논리를 따른다", "T"),
    ("친구의 기분을 살피는 데 신경을 많이 쓴다", "F"),
    ("계획을 세우고 그것을 지키는 편이다", "J"),
    ("즉흥적이고 융통성 있게 행동하는 편이다", "P"),
    ("일정을 미리 짜는 걸 좋아한다", "J"),
    ("변화에 빠르게 적응하는 편이다", "P"),
    ("일을 체계적으로 처리하는 것을 선호한다", "J"),
    ("즉흥적인 선택을 즐긴다", "P"),
]

st.set_page_config(page_title="MBTI 롤 챔피언 추천기", page_icon="🎮", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0f1216;
    color: #f5f3e7;
    font-family: 'Georgia', serif;
}
.main {
    max-width: 720px;
    margin: 40px auto;
    padding: 35px 40px;
    background: linear-gradient(145deg, #1c1f26, #272b35);
    border-radius: 18px;
    box-shadow: 0 0 30px 3px #8e44adcc;
    border: 1.5px solid #6c3483;
}
h1 {
    font-size: 56px;
    color: #bb86fc;
    text-align: center;
    font-weight: 900;
    text-shadow: none;
    margin-bottom: 20px;
}
h2 {
    color: #a678de;
    margin-top: 45px;
    margin-bottom: 20px;
    text-align: center;
    text-shadow: none;
}
.question {
    font-size: 22px;
    margin-top: 25px;
    margin-bottom: 14px;
    font-weight: 700;
    color: #000000;
    text-shadow: none;
}
.stRadio > div {
    color: #dcd6f7 !important;
}
.stRadio > div:hover {
    color: #bb86fc !important;
}
.footer {
    font-size: 13px;
    color: #888888;
    margin-top: 55px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown('<h1>🎯 MBTI 기반 롤 챔피언 추천기</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:18px; color:#ccc;">12개의 질문에 답해서 나와 딱 맞는 챔피언을 만나보세요!</p>', unsafe_allow_html=True)

st.header("📝 성격 질문")

scores = {"E":0,"I":0,"S":0,"N":0,"T":0,"F":0,"J":0,"P":0}

for i in range(0,len(questions),2):
    left_text, left_key = questions[i]
    right_text, right_key = questions[i+1]
    st.markdown(f'<div class="question">{(i//2)+1}. 다음 중 더 당신과 가까운 것은?</div>', unsafe_allow_html=True)
    choice = st.radio("", (left_text,right_text), key=f"q{i}")
    if choice == left_text:
        scores[left_key] += 1
    else:
        scores[right_key] += 1

if st.button("🔍 챔피언 추천받기"):
    ei = "E" if scores["E"] >= scores["I"] else "I"
    sn = "S" if scores["S"] >= scores["N"] else "N"
    tf = "T" if scores["T"] >= scores["F"] else "F"
    jp = "J" if scores["J"] >= scores["P"] else "P"
    mbti = ei + sn + tf + jp

    st.markdown(f'<h2>🧠 당신의 MBTI 유형은: <span style="color:#bb86fc;">{mbti}</span></h2>', unsafe_allow_html=True)

    if mbti in champ_data:
        champ = champ_data[mbti]["champ"]
        desc = champ_data[mbti]["desc"]
        st.markdown(f"### 🎮 추천 챔피언: **{champ}**")
        st.markdown(f'<p style="font-size:17px; line-height:1.6; white-space:pre-line;">{desc}</p>', unsafe_allow_html=True)
    else:
        st.warning("아직 준비 중인 MBTI 유형이에요! 조금만 기다려 주세요.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ❤️ by ChatGPT | League of Legends & MBTI Fusion</div>', unsafe_allow_html=True)
