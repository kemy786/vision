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
        "desc": """🧠 **사미라**는 활기차고 스타일리시한 원
