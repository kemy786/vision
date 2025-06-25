import streamlit as st

# --- 챔피언 데이터: 이미지 URL + 100자 이상 상세 설명 포함 ---
champ_data = {
    "INTJ": {
        "champ": "베이가",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Veigar_0.jpg",
        "desc": """
INTJ 유형은 미래를 내다보고 치밀하게 계획하는 전략가입니다. 베이가는 작은 체구지만 강력한 어둠의 마법을 다루며, 
긴 호흡으로 전장을 지배합니다. 냉철한 사고와 높은 집중력으로 한타의 흐름을 바꾸고, 체계적인 플레이를 좋아하는 당신과 완벽히 어울립니다. 
베이가는 특히 시간이 지날수록 강해지는 성장형 캐리어로, 당신의 전략적이고 계획적인 성향을 잘 반영합니다.
"""
    },
    "INTP": {
        "champ": "하이머딩거",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Heimerdinger_0.jpg",
        "desc": """
INTP 유형은 깊은 호기심과 독창적인 사고를 가진 탐구자입니다. 하이머딩거는 다양한 발명품과 기계장치를 활용해 전장을 통제하며, 
복잡한 문제 해결을 즐깁니다. 창의적인 전략을 실험하는 당신과 닮아 있으며, 변칙적인 전술과 기발한 아이디어로 상대를 압도하는 그의 플레이 스타일은 당신의 개성과도 잘 맞습니다.
"""
    },
    "ENTJ": {
        "champ": "세트",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sett_0.jpg",
        "desc": """
ENTJ 유형은 강력한 리더십과 추진력을 가진 전사형 지도자입니다. 세트는 전투의 선봉에서 팀을 이끌며, 돌진과 제압에 뛰어납니다. 
결단력 있고 목표지향적인 당신은 세트처럼 한타를 지휘하며 적진을 붕괴시키는 역할에 어울립니다. 그의 공격적이고 강한 존재감은 당신의 카리스마를 잘 반영합니다.
"""
    },
    "ENTP": {
        "champ": "이즈리얼",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ezreal_0.jpg",
        "desc": """
ENTP 유형은 모험을 즐기고 창의적인 도전을 멈추지 않는 탐험가입니다. 이즈리얼은 뛰어난 기동성과 정교한 스킬샷으로 전장을 누비며, 
자유분방하고 변화무쌍한 플레이를 선호합니다. 즉흥적이고 도전적인 당신과 딱 맞는 챔피언으로, 항상 새로운 전략을 시도하는 그의 모습에서 많은 영감을 받을 수 있습니다.
"""
    },
    "INFJ": {
        "champ": "카르마",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Karma_0.jpg",
        "desc": """
INFJ 유형은 내면의 신념이 강하고 타인을 돕는 이상주의자입니다. 카르마는 팀을 조율하고 보호하는 능력이 뛰어나며, 
조용하지만 강력한 힘으로 팀을 승리로 이끕니다. 당신의 배려심과 깊은 통찰력은 카르마의 플레이 스타일과 잘 맞으며, 
팀워크를 중시하는 당신에게 최적화된 챔피언입니다.
"""
    },
    "INFP": {
        "champ": "유미",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yuumi_0.jpg",
        "desc": """
INFP 유형은 감성적이고 이상을 추구하는 치유자입니다. 유미는 팀원에게 붙어 치유와 보호를 제공하며, 
전장에서 따뜻한 존재감으로 팀에 긍정적인 영향을 미칩니다. 당신의 섬세한 마음과 타인을 위한 배려는 유미의 헌신적인 서포트와 완벽하게 어울립니다.
"""
    },
    "ENFJ": {
        "champ": "레오나",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Leona_0.jpg",
        "desc": """
ENFJ 유형은 사교적이고 헌신적인 리더입니다. 레오나는 적진에서 팀을 보호하며, 돌진과 강력한 군중 제어로 팀 전투를 이끌죠. 
당신의 따뜻한 리더십과 강인함은 레오나의 플레이 스타일과 잘 맞으며, 팀원들을 위해 앞장서는 모습에서 당신의 성향이 드러납니다.
"""
    },
    "ENFP": {
        "champ": "니달리",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nidalee_0.jpg",
        "desc": """
ENFP 유형은 활기차고 자유로운 탐험가입니다. 니달리는 민첩하고 변화무쌍한 정글러로, 다양한 상황에 빠르게 적응하며 적을 기습합니다. 
당신의 열정과 호기심은 니달리의 유연한 전투 스타일과 잘 어울리며, 언제나 새로운 도전을 즐기는 당신에게 완벽한 선택입니다.
"""
    },
    "ISTJ": {
        "champ": "말파이트",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Malphite_0.jpg",
        "desc": """
ISTJ 유형은 책임감 있고 신중한 관리자입니다. 말파이트는 견고한 탱커로 팀의 앞에서 적을 막아내며 신뢰받는 존재입니다. 
체계적이고 묵묵한 당신과 닮았으며, 전투에서 믿음직한 버팀목 역할을 합니다. 꾸준함과 성실함이 돋보이는 플레이 스타일이 특징입니다.
"""
    },
    "ISFJ": {
        "champ": "룰루",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lulu_0.jpg",
        "desc": """
ISFJ 유형은 다정하고 세심한 보호자입니다. 룰루는 아군을 보호하고 변신시키는 독특한 스킬로 팀을 돕습니다. 
당신의 꼼꼼하고 헌신적인 성격이 룰루의 플레이 스타일과 잘 맞으며, 팀을 위해 기꺼이 희생하는 모습이 닮았습니다.
"""
    },
    "ESTJ": {
        "champ": "오른",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ornn_0.jpg",
        "desc": """
ESTJ 유형은 현실적이고 조직적인 지도자입니다. 오른은 튼튼한 탱커이자 조력자로서, 팀의 전투력을 극대화합니다. 
당신의 체계적이고 효율적인 성향과 맞아떨어지며, 계획을 실행하고 결과를 책임지는 모습을 보여줍니다.
"""
    },
    "ESFJ": {
        "champ": "나미",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nami_0.jpg",
        "desc": """
ESFJ 유형은 친절하고 사교적인 외교관입니다. 나미는 치유와 군중 제어 스킬로 팀을 지원하며, 협력을 중요시합니다. 
당신의 따뜻한 마음과 타인을 돕는 성향이 나미의 플레이와 조화를 이루며, 팀워크에서 빛나는 역할을 맡게 됩니다.
"""
    },
    "ISTP": {
        "champ": "제드",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zed_0.jpg",
        "desc": """
ISTP 유형은 침착하고 실용적인 문제 해결사입니다. 제드는 민첩한 암살자로, 신속하고 정확한 공격으로 적을 제압합니다. 
당신의 현실적인 태도와 냉철함이 제드의 플레이 스타일과 매우 잘 맞으며, 언제나 기민하게 상황을 컨트롤합니다.
"""
    },
    "ISFP": {
        "champ": "아리",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_0.jpg",
        "desc": """
ISFP 유형은 감성적이고 예술적인 성향을 가진 사람입니다. 아리는 매혹적인 외모와 민첩한 기술로 적을 교란합니다. 
당신의 창의력과 섬세함이 아리의 우아한 플레이 스타일과 잘 어우러지며, 상대를 압도하는 매력을 발산합니다.
"""
    },
    "ESTP": {
        "champ": "야스오",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yasuo_0.jpg",
        "desc": """
ESTP 유형은 용감하고 즉흥적인 활동가입니다. 야스오는 빠른 반응과 뛰어난 기동성으로 전장을 휘젓는 전사입니다. 
당신의 대담함과 경쟁심이 야스오의 공격적이고 화려한 플레이 스타일과 완벽히 맞아떨어집니다. 항상 전투의 중심에 서는 역할을 즐깁니다.
"""
    },
    "ESFP": {
        "champ": "사미라",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Samira_0.jpg",
        "desc": """
ESFP 유형은 사교적이고 활기찬 연예인형입니다. 사미라는 화려한 콤보와 공격으로 전장을 장악하는 원거리 딜러입니다. 
당신의 긍정적인 에너지와 즐거움을 추구하는 성격이 사미라의 플레이 스타일과 완벽히 맞으며, 전투를 즐기며 팀의 중심이 됩니다.
"""
    },
}

# --- 질문 리스트 ---
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

# --- 페이지 설정 및 디자인 ---
st.set_page_config(page_title="MBTI 롤 챔피언 추천기", page_icon="🎮", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0A1E3F;
    color: #F0E68C;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.main {
    max-width: 700px;
    margin: auto;
    padding: 30px;
    background: linear-gradient(135deg, #1E2A47, #112B4E);
    border-radius: 15px;
    box-shadow: 0 0 20px #FFD700;
}
h1 {
    font-size: 52px;
    color: #FFD700;
    text-align: center;
    font-weight: 900;
    text-shadow: 3px 3px 8px #000000;
}
h2 {
    color: #FFA500;
    margin-top: 40px;
    margin-bottom: 15px;
    text-align: center;
    text-shadow: 2px 2px 5px #000000;
}
.question {
    font-size: 20px;
    margin-top: 20px;
    margin-bottom: 10px;
    font-weight: 700;
    color: #FFFACD;
}
.stRadio > div {
    color: #FFFACD;
}
.footer {
    font-size: 12px;
    color: #888888;
    margin-top: 40px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown('<h1>🎯 MBTI 기반 롤 챔피언 추천기</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">12개의 질문에 답해서 나와 딱 맞는 챔피언을 만나보세요!</p>', unsafe_allow_html=True)

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

    st.markdown(f'<h2>🧠 당신의 MBTI 유형은: <span style="color:#FFD700;">{mbti}</span></h2>', unsafe_allow_html=True)

    if mbti in champ_data:
        champ = champ_data[mbti]["champ"]
        img_url = champ_data[mbti]["img"]
        desc = champ_data[mbti]["desc"]
        st.markdown(f"### 🎮 추천 챔피언: **{champ}**")
        st.image(img_url, use_container_width=True)
        st.markdown(desc)
    else:
        st.warning("아직 준비 중인 MBTI 유형이에요!")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ❤️ by ChatGPT | League of Legends & MBTI Fusion</div>', unsafe_allow_html=True)
