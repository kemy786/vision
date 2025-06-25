import streamlit as st

# --- 챔피언 데이터: 이미지 URL + 상세 설명 포함 ---
champ_data = {
    "INTJ": {
        "champ": "베이가",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Veigar_0.jpg",
        "desc": """🧠 **베이가**는 치밀한 전략가이자 후반을 지배하는 마법사입니다.
- **성격**: 계획적이고 미래지향적인 전략가
- **플레이 스타일**: 강력한 성장형 캐리어, 한타 후반에 팀을 이끕니다.
- **추천 이유**: 냉철한 분석력과 긴 호흡의 플레이가 당신과 닮았죠."""
    },
    "INTP": {
        "champ": "하이머딩거",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Heimerdinger_0.jpg",
        "desc": """🧠 **하이머딩거**는 창의적인 발명가이자 전략가입니다.
- **성격**: 호기심 많고 논리적인 탐구자
- **플레이 스타일**: 변수를 만들어내며, 전장을 지배합니다.
- **추천 이유**: 당신의 독창적인 사고방식과 실험정신이 닮았어요."""
    },
    "ENTJ": {
        "champ": "세트",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sett_0.jpg",
        "desc": """🧠 **세트**는 강력한 리더이자 돌파형 전사입니다.
- **성격**: 카리스마 넘치고 결단력 있는 지도자
- **플레이 스타일**: 전투 선봉에 서서 한타를 지휘합니다.
- **추천 이유**: 강한 주도력과 자신감이 당신의 장점이에요."""
    },
    "ENTP": {
        "champ": "이즈리얼",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ezreal_0.jpg",
        "desc": """🧠 **이즈리얼**은 자유롭고 모험을 즐기는 마법사입니다.
- **성격**: 창의적이고 도전적인 탐험가
- **플레이 스타일**: 기동성 뛰어나며, 스킬 샷으로 적을 농락합니다.
- **추천 이유**: 새로운 도전을 즐기고, 자유분방한 성향이 닮았어요."""
    },
    "INFJ": {
        "champ": "카르마",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Karma_0.jpg",
        "desc": """🧠 **카르마**는 팀을 보호하는 조율자이자 현자입니다.
- **성격**: 깊이 있는 사고와 이상을 지향하는 조력자
- **플레이 스타일**: 보호와 버프를 통해 팀을 지원합니다.
- **추천 이유**: 당신의 배려심과 내면의 힘이 잘 어울려요."""
    },
    "INFP": {
        "champ": "유미",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yuumi_0.jpg",
        "desc": """🧠 **유미**는 따뜻하고 팀을 돕는 지원가입니다.
- **성격**: 감성적이고 이상주의적인 치유자
- **플레이 스타일**: 팀원에게 치유와 버프를 제공하며 함께 싸웁니다.
- **추천 이유**: 당신의 배려와 포용력이 빛나는 챔피언이에요."""
    },
    "ENFJ": {
        "champ": "레오나",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Leona_0.jpg",
        "desc": """🧠 **레오나**는 용맹한 수호자이자 팀의 리더입니다.
- **성격**: 헌신적이고 사교적인 지도자
- **플레이 스타일**: 선봉에서 적을 제압하며 팀을 보호합니다.
- **추천 이유**: 당신의 리더십과 헌신이 닮았어요."""
    },
    "ENFP": {
        "champ": "니달리",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nidalee_0.jpg",
        "desc": """🧠 **니달리**는 모험심 강한 정글러입니다.
- **성격**: 자유롭고 활발한 탐험가
- **플레이 스타일**: 민첩하고 변신을 통해 전장을 지배합니다.
- **추천 이유**: 당신의 활발함과 도전정신이 잘 맞아요."""
    },
    "ISTJ": {
        "champ": "말파이트",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Malphite_0.jpg",
        "desc": """🧠 **말파이트**는 신중하고 강인한 탱커입니다.
- **성격**: 책임감 강하고 신뢰받는 관리자
- **플레이 스타일**: 한타의 중심에서 팀을 지키며 견고합니다.
- **추천 이유**: 묵묵하고 안정적인 성격이 닮았어요."""
    },
    "ISFJ": {
        "champ": "룰루",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lulu_0.jpg",
        "desc": """🧠 **룰루**는 다정하고 헌신적인 지원가입니다.
- **성격**: 따뜻하고 조용한 보호자
- **플레이 스타일**: 아군을 강화하고 적의 공격을 방해합니다.
- **추천 이유**: 당신의 배려심과 섬세함이 딱이에요."""
    },
    "ESTJ": {
        "champ": "오른",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ornn_0.jpg",
        "desc": """🧠 **오른**은 강력한 조직자이자 탱커입니다.
- **성격**: 현실적이고 조직적인 관리자
- **플레이 스타일**: 팀의 힘을 극대화하며 전투를 주도합니다.
- **추천 이유**: 체계적이고 단호한 성격과 잘 어울려요."""
    },
    "ESFJ": {
        "champ": "나미",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nami_0.jpg",
        "desc": """🧠 **나미**는 사교적이고 활발한 지원가입니다.
- **성격**: 친절하고 협력적인 외교관
- **플레이 스타일**: 치유와 군중 제어로 팀을 돕습니다.
- **추천 이유**: 당신의 따뜻한 마음과 사교성이 닮았어요."""
    },
    "ISTP": {
        "champ": "제드",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zed_0.jpg",
        "desc": """🧠 **제드**는 냉철하고 민첩한 암살자입니다.
- **성격**: 독립적이고 현실적인 해결사
- **플레이 스타일**: 빠른 판단으로 적을 암살합니다.
- **추천 이유**: 당신의 침착함과 결단력이 돋보여요."""
    },
    "ISFP": {
        "champ": "아리",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_0.jpg",
        "desc": """🧠 **아리**는 매혹적이고 민첩한 마법사입니다.
- **성격**: 감성적이고 창의적인 예술가
- **플레이 스타일**: 이동성이 뛰어나고 적을 교란합니다.
- **추천 이유**: 당신의 섬세함과 매력이 잘 어울려요."""
    },
    "ESTP": {
        "champ": "야스오",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yasuo_0.jpg",
        "desc": """🧠 **야스오**는 모험심 강하고 공격적인 전사입니다.
- **성격**: 즉흥적이고 용감한 활동가
- **플레이 스타일**: 화려한 기동성과 강력한 한타 능력
- **추천 이유**: 당신의 대담함과 카리스마가 닮았어요."""
    },
    "ESFP": {
        "champ": "사미라",
        "img": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Samira_0.jpg",
        "desc": """🧠 **사미라**는 활기차고 스타일리시한 원거리 딜러입니다.
- **성격**: 사교적이고 즐거움을 추구하는 연예인
- **플레이 스타일**: 공격적이고 화려한 플레이를 선보입니다.
- **추천 이유**: 당신의 에너지와 매력이 빛나는 챔피언이에요."""
    },
}

# --- 질문 리스트: 12문항 (각 지표별 3문항씩) ---
questions = [
    # E/I
    ("새로운 사람들과 어울릴 때 에너지가 넘친다", "E"),
    ("혼자 시간을 보내는 것이 편안하다", "I"),
    ("사람들 앞에서 이야기하는 걸 즐긴다", "E"),
    ("사적인 시간을 혼자 보내는 걸 선호한다", "I"),
    ("사교적인 모임에서 활력이 생긴다", "E"),
    ("혼자서 조용한 시간을 보내는 것을 좋아한다", "I"),

    # S/N
    ("현실적이고 구체적인 정보에 집중하는 편이다", "S"),
    ("상상력과 아이디어를 더 선호한다", "N"),
    ("과거 경험에 기반해 결정을 내린다", "S"),
    ("미래 가능성과 새로운 가능성을 생각하는 걸 좋아한다", "N"),
    ("세부 사항에 주의를 기울이는 편이다", "S"),
    ("큰 그림을 보는 걸 더 즐긴다", "N"),

    # T/F
    ("논리와 객관적인 판단을 우선시한다", "T"),
    ("다른 사람의 감정을 중요하게 생각한다", "F"),
    ("문제를 해결할 때 감정보다 사실에 집중한다", "T"),
    ("사람들의 감정에 공감하는 편이다", "F"),
    ("비판할 때도 감정보다는 논리를 따른다", "T"),
    ("친구의 기분을 살피는 데 신경을 많이 쓴다", "F"),

    # J/P
    ("계획을 세우고 그것을 지키는 편이다", "J"),
    ("즉흥적이고 융통성 있게 행동하는 편이다", "P"),
    ("일정을 미리 짜는 걸 좋아한다", "J"),
    ("변화에 빠르게 적응하는 편이다", "P"),
    ("일을 체계적으로 처리하는 것을 선호한다", "J"),
    ("즉흥적인 선택을 즐긴다", "P"),
]

# --- 페이지 설정 및 디자인 ---
st.set_page_config(page_title="MBTI 롤 챔피언 추천기", page_icon="🎮")

# 배경색과 타이틀 스타일 (CSS 직접 삽입)
st.markdown(
    """
    <style>
    .main {
        background-color: #0B2239;
        color: white;
        padding: 20px;
    }
    h1 {
        font-size: 48px;
        color: #FFD700;
        text-align: center;
        margin-bottom: 10px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 2px 2px 4px #000000;
    }
    h2 {
        color: #FFA500;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-top: 30px;
    }
    .question {
        font-size: 18px;
        margin-top: 15px;
        margin-bottom: 10px;
        font-weight: 600;
    }
    .footer {
        font-size: 12px;
        color: #888888;
        margin-top: 40px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1>🎯 MBTI 기반 롤 챔피언 추천기</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">12개의 질문에 답해서 나와 딱 맞는 챔피언을 만나보세요!</p>', unsafe_allow_html=True)

st.header("📝 성격 질문")

# 점수 초기화
scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

# 질문 12개 중 두 개씩 묶어 라디오 버튼 제공 (둘 중 하나 선택)
for i in range(0, len(questions), 2):
    left_text, left_key = questions[i]
    right_text, right_key = questions[i+1]

    st.markdown(f'<div class="question">{(i//2)+1}. 다음 중 더 당신과 가까운 것은?</div>', unsafe_allow_html=True)
    choice = st.radio(
        "",
        (left_text, right_text),
        key=f"q{i}"
    )
    if choice == left_text:
        scores[left_key] += 1
    else:
        scores[right_key] += 1

# 결과 버튼
if st.button("🔍 챔피언 추천받기"):
    # 점수 비교로 MBTI 유형 완성
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

# 하단 푸터
st.markdown('<div class="footer">Made with ❤️ by ChatGPT | League of Legends & MBTI Fusion</div>', unsafe_allow_html=True)
