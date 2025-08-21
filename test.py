# app.py
# ---------------------------------------------
# 🎓 나의 학습 알고리즘 찾기 (Streamlit)
# 목적: 학생의 학습 스타일을 '알고리즘' 메타포로 진단하고,
#       결과에 따른 맞춤 공부 전략 + 하루 계획표를 제안한다.
# 평가 기준 반영:
# 1) 주제/목적 명확 + 현실 적용(실천 팁/계획표)
# 2) 창의적 컨셉(알고리즘 유형)
# 3) 직관적 UI(사이드바 진행률, 탭, 알림, 깔끔한 그래프)
# 4) 코드 모듈화/주석/타입별 상수 분리
# 5) 다양한 위젯/시각화/인터랙션(다운로드)
# 6) 예외 처리/검증/빠른 렌더링
# ---------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import altair as alt
import matplotlib.pyplot as plt
from math import pi
from datetime import datetime, timedelta

# ----------------------
# 기본 설정 & 테마 톤
# ----------------------
st.set_page_config(page_title="나의 학습 알고리즘 찾기", page_icon="🧠", layout="centered")
st.markdown(
    """
    <style>
    .small-muted { color:#666; font-size:0.9rem; }
    .pill { display:inline-block; padding:2px 10px; border-radius:999px; background:#F4F6FA; margin-right:6px; }
    .accent { color:#c2185b; font-weight:600; }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# 상수/유형 정의
# ----------------------
ALGO_TYPES = [
    "정렬형 📑",      # 계획·정돈·순차
    "깊이우선형 🔍",  # 난이도 높은 문제 파고듦
    "동적계획형 🔄",  # 기초 반복/누적 복습
    "탐색형 🔎",      # 정보 탐색/자료 수집
    "창의휴리스틱형 🎨", # 직관/아이디어/마인드맵
    "실습형 ✍️",      # 손으로/프로젝트/코딩
]

ALGO_COLORS = {
    "정렬형 📑": "#7E57C2",
    "깊이우선형 🔍": "#039BE5",
    "동적계획형 🔄": "#43A047",
    "탐색형 🔎": "#FFB300",
    "창의휴리스틱형 🎨": "#E53935",
    "실습형 ✍️": "#8D6E63",
}

# 레이더 차트의 4차원 축 (설명력 높이기 위함)
DIMENSIONS = ["계획성(Planning)", "탐색성(Exploration)", "심층성(Depth)", "반복성(Repetition)"]

# 유형별 설명 (약 200자, 발표용 복붙 가능)
ALGO_DESCRIPTIONS = {
    "정렬형 📑": "계획과 질서를 중시하는 순차 학습러. 공부 전 체크리스트를 만들고, 과목별 시간 배분을 정갈하게 유지해 효율을 끌어올립니다. 오답노트와 색인표로 지식을 정리하며 마감 관리에 강합니다. 단, 계획 과몰입으로 실행이 늦어질 수 있어 유연한 조정이 보완 포인트예요.",
    "깊이우선형 🔍": "가장 어려운 문제부터 파고드는 탐구형. 낯선 개념을 만나면 끝을 보려는 집중력이 돋보입니다. 한 주제에서 깊은 통찰을 얻고 장기 기억에 강점이 있습니다. 다만 과몰입으로 범위 관리가 흔들릴 수 있어, ‘깊이 7:범위 3’ 같은 가드레일을 두면 더 탄탄해져요.",
    "동적계획형 🔄": "기초를 쌓아올리는 누적 학습러. 개념→유형→응용 순으로 작은 성공을 반복하며 탄탄히 성장합니다. 오답 재활용과 스페이싱 복습에 특히 강합니다. 속도가 느린 편일 수 있으므로 데드라인 중심의 마일스톤과 주간 점검표를 함께 쓰면 완성도가 폭발합니다.",
    "탐색형 🔎": "자료 수집과 비교를 즐기는 정보 헌터. 교과서, 강의, 블로그를 가로지르며 핵심을 뽑아냅니다. 빠르게 전반을 훑고 전략을 세우는 데 능합니다. 정보 과잉에 빠지지 않도록 ‘참고 자료 슬롯 3개’처럼 제한을 두고, 요약 카드로 실행을 붙이면 성과가 커져요.",
    "창의휴리스틱형 🎨": "아이디어와 연결을 즐기는 시각형 학습러. 마인드맵, 그림, 스토리텔링으로 개념을 엮어 이해합니다. 문제를 새 관점에서 재해석하고 융합 과제에서 강점을 보입니다. 루틴이 흐트러질 수 있어 ‘짧고 굵은 스프린트’와 체크리스트를 곁들이면 안정적이에요.",
    "실습형 ✍️": "손으로 부딪히며 배우는 실전파. 예제 코딩, 실험, 프로젝트를 통해 개념을 체화합니다. ‘알겠다’ 보다는 ‘되겠다’가 목표라 적용력이 뛰어납니다. 이론 보완이 필요할 수 있으니, 실습 전후로 정리 카드 3장을 적어 개념 틀을 확실히 잡아주면 완벽합니다.",
}

# 유형별 맞춤 전략(현실 적용)
ALGO_TIPS = {
    "정렬형 📑": ["하루 시작 10분 계획, 끝 5분 회고", "오답노트: ‘틀린 이유/교정 전략/유사문제’ 3칸"],
    "깊이우선형 🔍": ["어려운 문제 25분 집중 + 5분 범위 스캔", "깊이:범위 = 7:3 비율 유지"],
    "동적계획형 🔄": ["스페이싱 복습(1-3-7일)", "개념→유형→응용 체크리스트"],
    "탐색형 🔎": ["참고 자료 슬롯 3개 제한", "자료 요약 5줄 → 바로 적용 2문제"],
    "창의휴리스틱형 🎨": ["마인드맵 1장/과목", "포모도로 25분 스프린트 x 3 세트"],
    "실습형 ✍️": ["예제→변형→확장 3단 실습", "실습 전후 개념 카드 3장"],
}

# ----------------------
# 유틸 함수
# ----------------------
def init_state():
    if "responses" not in st.session_state:
        st.session_state.responses = {}
    if "meta" not in st.session_state:
        st.session_state.meta = {}
    if "scored" not in st.session_state:
        st.session_state.scored = False

def pct_complete(total_q: int) -> float:
    answered = sum(1 for k in st.session_state.responses if st.session_state.responses[k] is not None)
    return answered / total_q if total_q else 0.0

def questions_spec() -> List[Dict]:
    """질문/선택지/점수 매핑 정의(모듈화). 각 선택지는 여러 유형 가중치."""
    return [
        {
            "key": "q1",
            "text": "문제집을 풀 때 나는…",
            "options": {
                "순서대로 차근차근": {"정렬형 📑": 2, "동적계획형 🔄": 1},
                "섞어 풀다가 어려운 것에 오래": {"깊이우선형 🔍": 2, "창의휴리스틱형 🎨": 1},
                "쉬운 것부터 빠르게 훑기": {"탐색형 🔎": 2, "정렬형 📑": 1},
                "예제 만들어 직접 변형": {"실습형 ✍️": 2, "동적계획형 🔄": 1},
            },
        },
        {
            "key": "q2",
            "text": "모르는 개념이 나오면 우선…",
            "options": {
                "교과서/노트 다시 정리": {"동적계획형 🔄": 2, "정렬형 📑": 1},
                "영상/블로그 등 자료 탐색": {"탐색형 🔎": 2, "창의휴리스틱형 🎨": 1},
                "가장 어려운 응용문제 먼저": {"깊이우선형 🔍": 2},
                "직접 예제 만들어 실습": {"실습형 ✍️": 2},
            },
        },
        {
            "key": "q3",
            "text": "시험 7일 전 학습 계획은…",
            "options": {
                "시간표를 만들어 그대로 실행": {"정렬형 📑": 2, "동적계획형 🔄": 1},
                "그날 관심 가는 과목 위주": {"창의휴리스틱형 🎨": 2},
                "범위 전체를 얕게 훑기": {"탐색형 🔎": 2},
                "취약 단원 깊게 파기": {"깊이우선형 🔍": 2},
            },
        },
        {
            "key": "q4",
            "text": "복습 스타일은…",
            "options": {
                "스페이싱 복습표로 주기적 반복": {"동적계획형 🔄": 2, "정렬형 📑": 1},
                "오답만 모아 집중 공략": {"깊이우선형 🔍": 2},
                "요약 카드로 핵심만 정리": {"탐색형 🔎": 1, "정렬형 📑": 1, "창의휴리스틱형 🎨": 1},
                "같은 유형 새로 만들어 풀기": {"실습형 ✍️": 2},
            },
        },
        {
            "key": "q5",
            "text": "협업/스터디에 대한 생각은…",
            "options": {
                "역할 나눠 계획대로 진행": {"정렬형 📑": 2},
                "어려운 파트 맡아 깊게 연구": {"깊이우선형 🔍": 2},
                "자료 조사/정리 담당": {"탐색형 🔎": 2},
                "프로토타입/실험 담당": {"실습형 ✍️": 2},
            },
        },
    ]

def extra_inputs() -> Dict:
    """보조 신호(슬라이더/멀티셀렉트 등)를 유형 점수에 가볍게 가중치로 반영."""
    st.subheader("추가 설정 (선택)")
    col1, col2 = st.columns(2)
    with col1:
        daily_hours = st.slider("평균 일일 공부 시간(시간)", 0, 10, 3)
        prefer_hands_on = st.checkbox("손으로 해봐야 이해됨(실습 선호)")
        group_study = st.checkbox("스터디/토론이 동기부여가 됨")
    with col2:
        tools = st.multiselect(
            "주요 학습 도구(복수 선택)",
            ["마인드맵", "요약카드", "플래너/갠트차트", "영상강의", "예제코딩/실험", "백과사전/검색"],
            default=[]
        )
        goal = st.text_input("이번 달 학습 목표(선택): 예) 수1 고난도 80% 정복")

    # 가벼운 가점 정책
    bonus = {k: 0 for k in ALGO_TYPES}
    if daily_hours >= 5:
        bonus["깊이우선형 🔍"] += 1
        bonus["동적계획형 🔄"] += 1
    if prefer_hands_on:
        bonus["실습형 ✍️"] += 2
    if group_study:
        bonus["탐색형 🔎"] += 1
        bonus["창의휴리스틱형 🎨"] += 1
    if "마인드맵" in tools:
        bonus["창의휴리스틱형 🎨"] += 1
    if "요약카드" in tools:
        bonus["정렬형 📑"] += 1
        bonus["탐색형 🔎"] += 1
    if "플래너/갠트차트" in tools:
        bonus["정렬형 📑"] += 2
    if "영상강의" in tools:
        bonus["탐색형 🔎"] += 1
    if "예제코딩/실험" in tools:
        bonus["실습형 ✍️"] += 2
    if "백과사전/검색" in tools:
        bonus["탐색형 🔎"] += 1

    meta = {
        "daily_hours": daily_hours,
        "prefer_hands_on": prefer_hands_on,
        "group_study": group_study,
        "tools": tools,
        "goal": goal,
    }
    return bonus, meta

def score_responses(responses: Dict[str, str], bonus: Dict[str, int]) -> Dict[str, int]:
    """질문 응답과 보너스를 종합해 유형 점수 계산."""
    scores = {k: 0 for k in ALGO_TYPES}
    # 질문 점수
    for spec in questions_spec():
        key = spec["key"]
        if key in responses and responses[key] is not None:
            choice = responses[key]
            for algo, w in spec["options"][choice].items():
                scores[algo] += w
    # 보너스 반영
    for algo, b in bonus.items():
        scores[algo] += b
    return scores

def to_dimensions(scores: Dict[str, int]) -> Dict[str, float]:
    """
    유형 점수를 4차원 지표로 투영(시각화/설명력 강화).
    간단 가중 매핑: (정렬=계획, 탐색=탐색, 깊이=심층, 동적=반복, 창의/실습은 보조 반영)
    """
    P = scores["정렬형 📑"] * 1.0 + scores["동적계획형 🔄"] * 0.5
    E = scores["탐색형 🔎"] * 1.0 + scores["창의휴리스틱형 🎨"] * 0.5
    D = scores["깊이우선형 🔍"] * 1.0 + scores["실습형 ✍️"] * 0.3
    R = scores["동적계획형 🔄"] * 1.0 + scores["정렬형 📑"] * 0.3
    return {
        "계획성(Planning)": P,
        "탐색성(Exploration)": E,
        "심층성(Depth)": D,
        "반복성(Repetition)": R,
    }

def best_type(scores: Dict[str, int]) -> Tuple[str, int]:
    """최고 점수 유형 반환(동점 시 알파벳/이모지 포함 이름 정렬로 안정성)."""
    max_val = max(scores.values())
    cands = [k for k, v in scores.items() if v == max_val]
    cands.sort()
    return cands[0], max_val

def bar_chart(scores: Dict[str, int]):
    """Altair 막대 그래프(깔끔/경량/빠름)."""
    df = pd.DataFrame({
        "유형": list(scores.keys()),
        "점수": list(scores.values()),
        "색": [ALGO_COLORS[k] for k in scores.keys()]
    })
    chart = (
        alt.Chart(df)
        .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
        .encode(
            x=alt.X("유형:N", sort="-y", axis=alt.Axis(labelAngle=-20)),
            y=alt.Y("점수:Q"),
            color=alt.Color("색:N", scale=None, legend=None),
            tooltip=["유형", "점수"]
        )
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)

def radar_chart(dim_scores: Dict[str, float], title: str = "학습 성향 레이더"):
    """Matplotlib 레이더 차트(안정적)."""
    labels = list(dim_scores.keys())
    stats = list(dim_scores.values())
    # 정규화(0~1)
    maxv = max(stats) if max(stats) > 0 else 1
    stats_norm = [s / maxv for s in stats]
    stats_norm += stats_norm[:1]
    angles = [n / float(len(labels)) * 2 * pi for n in range(len(labels))]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids([a * 180 / pi for a in angles[:-1]], labels, fontsize=10)
    ax.plot(angles, stats_norm, linewidth=2, linestyle='-', color="#c2185b")
    ax.fill(angles, stats_norm, alpha=0.15, color="#c2185b")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=12)
    ax.set_yticklabels([])
    st.pyplot(fig, use_container_width=True)

def make_dayplan(final_algo: str, daily_hours: int) -> pd.DataFrame:
    """유형별 권장 블록으로 하루 학습 계획표 생성(현실 적용)."""
    blocks = []
    start = datetime(2000,1,1,18,0)  # 방과후 18:00 가정
    def add_block(name, h):
        nonlocal start
        end = start + timedelta(hours=h)
        blocks.append([start.strftime("%H:%M"), end.strftime("%H:%M"), name, h])
        start = end

    # 유형별 핵심 루틴
    if final_algo == "정렬형 📑":
        seq = [("플래너 체크/우선순위", 0.5), ("개념복습", 1.0), ("유형문제", 1.0), ("오답정리", 0.5)]
    elif final_algo == "깊이우선형 🔍":
        seq = [("취약단원 심층공략", 1.5), ("핵심개념 보강", 0.5), ("고난도 문제", 1.0)]
    elif final_algo == "동적계획형 🔄":
        seq = [("개념→유형 누적복습", 1.0), ("오답 재도전", 0.5), ("응용 문제", 1.0)]
    elif final_algo == "탐색형 🔎":
        seq = [("개요 훑기/요약카드", 0.8), ("자료탐색/요약정리", 0.8), ("핵심문제 적용", 0.8)]
    elif final_algo == "창의휴리스틱형 🎨":
        seq = [("마인드맵/연결고리", 0.8), ("핵심개념 재구성", 0.7), ("응용·융합 문제", 0.8)]
    else:  # 실습형 ✍️
        seq = [("예제실습", 1.0), ("변형·확장 과제", 1.0), ("개념정리 카드", 0.5)]

    total_seq = sum(h for _, h in seq)
    if daily_hours <= 0:
        daily_hours = 2
    scale = min(daily_hours / total_seq, 1.5)  # 과도하게 늘리지 않게 클램프
    for name, h in seq:
        add_block(name, round(h * scale, 1))

    df = pd.DataFrame(blocks, columns=["시작", "끝", "활동", "시간(h)"])
    return df

def download_df_button(df: pd.DataFrame, filename: str, label: str):
    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(label=label, data=csv, file_name=filename, mime="text/csv")

# ----------------------
# 앱 본문
# ----------------------
init_state()

st.title("🧠 나의 학습 알고리즘 찾기")
st.caption("공대 감성으로 내 공부 습관을 ‘알고리즘’으로 분석하고, 내게 맞는 전략과 계획표를 받아보자!")

with st.sidebar:
    st.header("진행 상황")
    total_q = len(questions_spec())
    prog = pct_complete(total_q)
    st.progress(prog, text=f"{int(prog*100)}% 완료")
    st.markdown("<span class='small-muted'>모든 질문은 결과 정확도를 위해 필요해요.</span>", unsafe_allow_html=True)

tabs = st.tabs(["테스트", "결과", "정보"])

# ----------------------
# 탭 1: 테스트
# ----------------------
with tabs[0]:
    st.subheader("질문에 답해주세요")
    st.markdown("<span class='pill'>라디오 선택</span> <span class='pill'>보조 신호</span>", unsafe_allow_html=True)

    # 질문 폼(제출 단일 액션)
    with st.form("qa_form", clear_on_submit=False):
        for spec in questions_spec():
            st.radio(
                label=f"• {spec['text']}",
                options=list(spec["options"].keys()),
                key=f"resp_{spec['key']}",
                horizontal=False
            )
            # 상태 저장
            st.session_state.responses[spec["key"]] = st.session_state.get(f"resp_{spec['key']}", None)

        bonus, meta = extra_inputs()
        submitted = st.form_submit_button("결과 계산하기 ✨")

        if submitted:
            # 검증: 미응답 체크
            missing = [q["text"] for q in questions_spec() if st.session_state.responses.get(q["key"]) is None]
            if missing:
                st.error("모든 질문에 답해주세요. 미응답: " + " / ".join(missing))
            else:
                st.session_state.meta = meta
                st.session_state.scores = score_responses(st.session_state.responses, bonus)
                st.session_state.dim_scores = to_dimensions(st.session_state.scores)
                st.session_state.final_type, st.session_state.final_score = best_type(st.session_state.scores)
                st.session_state.scored = True
                st.success("계산 완료! 상단의 ‘결과’ 탭을 확인하세요 😉")

# ----------------------
# 탭 2: 결과
# ----------------------
with tabs[1]:
    st.subheader("진단 결과")
    if not st.session_state.get("scored", False):
        st.info("먼저 ‘테스트’ 탭에서 질문에 답하고 계산을 완료하세요.")
    else:
        final_algo = st.session_state.final_type
        daily_hours = st.session_state.meta.get("daily_hours", 3)

        st.markdown(f"### 🎯 당신의 학습 알고리즘: <span class='accent'>{final_algo}</span>", unsafe_allow_html=True)
        st.write(ALGO_DESCRIPTIONS[final_algo])

        # 시각화: 유형 점수 막대
        st.markdown("#### 📊 알고리즘 유형 점수")
        bar_chart(st.session_state.scores)

        # 시각화: 레이더(4차원 지표)
        st.markdown("#### 🕸️ 학습 성향 레이더")
        radar_chart(st.session_state.dim_scores, title="Planning / Exploration / Depth / Repetition")

        # 맞춤 전략
        st.markdown("#### 🧩 맞춤 전략")
        tips = ALGO_TIPS[final_algo]
        st.markdown("\n".join([f"- {t}" for t in tips]))

        # 하루 계획표
        st.markdown("#### 🗓️ 추천 하루 계획표 (방과 후 기준)")
        plan_df = make_dayplan(final_algo, daily_hours)
        st.dataframe(plan_df, use_container_width=True)
        download_df_button(plan_df, "study_dayplan.csv", "계획표 CSV 다운로드")

# ----------------------
# 탭 3: 정보/방법론
# ----------------------
with tabs[2]:
    st.subheader("방법론 & 해석 가이드")
    st.markdown(
        """
        - **알고리즘 메타포**: 정렬/탐색/동적계획/깊이우선/휴리스틱/실습형 패턴으로 학습 습관을 모델링했습니다.  
        - **4차원 지표**: 계획성·탐색성·심층성·반복성으로 결과를 시각화해 강/약점을 한눈에 보입니다.  
        - **현실 적용**: 유형별 전략 + 하루 계획표로 바로 실행 가능한 액션을 제공합니다.  
        - **주의**: 재미와 자기 성찰 도구이며, 절대적 진단이 아닙니다. 상황에 따라 유연하게 조정하세요.
        """
    )
    with st.expander("유형별 한 줄 요약"):
        for k in ALGO_TYPES:
            st.markdown(f"- **{k}**: {ALGO_DESCRIPTIONS[k][:42]}…")

    st.caption("© 2025 학습 알고리즘 랩 — Streamlit 데모. 발표/프로젝트에 자유롭게 활용하세요.")
