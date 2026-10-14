
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MBTI로 찾는 나의 단짝 포켓몬",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 공식 Pokémon 사이트의 이미지 주소
IMAGE_BASE = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/"

MBTI_ORDER = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]

POKEMON_DATA = {
    "ISTJ": {
        "ko": "거북왕", "en": "Blastoise", "number": "009",
        "types": "물 타입",
        "traits": "든든하고 책임감 있는 수호자",
        "reasons": [
            "계획을 세우고 차근차근 목표를 이루는 모습이 잘 어울려.",
            "맡은 일을 끝까지 해내는 믿음직한 성격을 표현했어.",
        ],
        "match": "ESFP",
    },
    "ISFJ": {
        "ko": "해피너스", "en": "Blissey", "number": "242",
        "types": "노말 타입",
        "traits": "따뜻하게 친구를 챙기는 힐러",
        "reasons": [
            "주변 사람들을 세심하게 챙기는 다정함이 닮았어.",
            "친구들이 힘들 때 옆에서 든든하게 도와주는 모습이야.",
        ],
        "match": "ESTP",
    },
    "INFJ": {
        "ko": "루카리오", "en": "Lucario", "number": "448",
        "types": "격투 / 강철 타입",
        "traits": "신념과 통찰력을 지닌 전사",
        "reasons": [
            "상대의 마음을 이해하고 깊이 생각하는 모습이 잘 어울려.",
            "자신이 중요하다고 생각하는 가치를 지키는 점도 닮았어.",
        ],
        "match": "ENFP",
    },
    "INTJ": {
        "ko": "메타그로스", "en": "Metagross", "number": "376",
        "types": "강철 / 에스퍼 타입",
        "traits": "논리적으로 전략을 세우는 천재",
        "reasons": [
            "복잡한 문제를 분석하고 효율적인 방법을 찾는 모습이야.",
            "논리와 계획을 중시하는 이미지와 잘 맞아.",
        ],
        "match": "ENFP",
    },
    "ISTP": {
        "ko": "뮤츠", "en": "Mewtwo", "number": "150",
        "types": "에스퍼 타입",
        "traits": "독립적이고 뛰어난 문제 해결사",
        "reasons": [
            "필요한 순간에 침착하게 해결책을 찾는 모습이 닮았어.",
            "혼자서 탐구하고 자신만의 방식으로 움직이는 이미지야.",
        ],
        "match": "ESFJ",
    },
    "ISFP": {
        "ko": "이브이", "en": "Eevee", "number": "133",
        "types": "노말 타입",
        "traits": "자유롭고 개성 넘치는 모험가",
        "reasons": [
            "자신만의 취향과 감성을 소중히 여기는 점이 잘 어울려.",
            "여러 가능성을 가지고 자유롭게 성장하는 모습도 닮았어.",
        ],
        "match": "ESFJ",
    },
    "INFP": {
        "ko": "뮤", "en": "Mew", "number": "151",
        "types": "에스퍼 타입",
        "traits": "상상력이 풍부한 순수한 영혼",
        "reasons": [
            "풍부한 상상력과 호기심으로 새로운 세상을 꿈꾸는 모습이야.",
            "자신만의 가치관과 따뜻한 마음을 소중히 여기는 점이 닮았어.",
        ],
        "match": "ENFJ",
    },
    "INTP": {
        "ko": "폴리곤", "en": "Porygon", "number": "137",
        "types": "노말 타입",
        "traits": "호기심 많은 논리 탐구자",
        "reasons": [
            "새로운 개념과 원리를 파고드는 모습이 잘 어울려.",
            "문제를 다양한 관점에서 분석하는 탐구자 이미지야.",
        ],
        "match": "ENTJ",
    },
    "ESTP": {
        "ko": "리자몽", "en": "Charizard", "number": "006",
        "types": "불꽃 / 비행 타입",
        "traits": "행동력 넘치는 도전가",
        "reasons": [
            "생각에만 머무르지 않고 직접 부딪쳐 보는 모습이 닮았어.",
            "활동적이고 자신감 있게 새로운 경험을 즐기는 이미지야.",
        ],
        "match": "ISFJ",
    },
    "ESFP": {
        "ko": "피카츄", "en": "Pikachu", "number": "025",
        "types": "전기 타입",
        "traits": "주변을 밝히는 에너지 발전소",
        "reasons": [
            "밝은 에너지로 주변 분위기를 즐겁게 만드는 모습이야.",
            "친구들과 함께 순간을 즐기고 활발하게 움직이는 점이 닮았어.",
        ],
        "match": "ISTJ",
    },
    "ENFP": {
        "ko": "파치리스", "en": "Pachirisu", "number": "417",
        "types": "전기 타입",
        "traits": "아이디어가 넘치는 분위기 메이커",
        "reasons": [
            "새로운 생각과 활동에 호기심을 보이는 모습이 잘 어울려.",
            "친구들과 에너지를 나누고 즐거운 일을 만들어 가는 이미지야.",
        ],
        "match": "INFJ",
    },
    "ENTP": {
        "ko": "팬텀", "en": "Gengar", "number": "094",
        "types": "고스트 / 독 타입",
        "traits": "기발한 발상을 즐기는 장난꾸러기",
        "reasons": [
            "남들과 다른 관점에서 문제를 바라보는 모습이 닮았어.",
            "재치 있는 아이디어와 예상 밖의 행동을 즐기는 이미지야.",
        ],
        "match": "INTJ",
    },
    "ESTJ": {
        "ko": "괴력몬", "en": "Machamp", "number": "068",
        "types": "격투 타입",
        "traits": "목표를 향해 나아가는 실행가",
        "reasons": [
            "해야 할 일을 정리하고 바로 실행하는 모습이 잘 어울려.",
            "팀에서 역할을 맡고 목표를 달성하려는 점이 닮았어.",
        ],
        "match": "ISFP",
    },
    "ESFJ": {
        "ko": "푸린", "en": "Jigglypuff", "number": "039",
        "types": "노말 / 페어리 타입",
        "traits": "모두를 하나로 모으는 친구",
        "reasons": [
            "친구들과 잘 어울리고 관계를 소중히 여기는 모습이야.",
            "함께 즐거운 분위기를 만들고 사람들을 챙기는 점이 닮았어.",
        ],
        "match": "ISTP",
    },
    "ENFJ": {
        "ko": "가디안", "en": "Gardevoir", "number": "282",
        "types": "에스퍼 / 페어리 타입",
        "traits": "마음을 이해하고 지켜 주는 리더",
        "reasons": [
            "다른 사람의 감정을 이해하고 응원하는 모습이 잘 어울려.",
            "소중한 사람들을 위해 먼저 나서는 따뜻한 이미지야.",
        ],
        "match": "INFP",
    },
    "ENTJ": {
        "ko": "망나뇽", "en": "Dragonite", "number": "149",
        "types": "드래곤 / 비행 타입",
        "traits": "큰 목표를 향해 이끄는 리더",
        "reasons": [
            "목표를 정하고 자신 있게 앞으로 나아가는 모습이 닮았어.",
            "상황을 빠르게 파악하고 일을 추진하는 이미지와 잘 맞아.",
        ],
        "match": "INTP",
    },
}

# 크림색과 노란색 테마
st.markdown(
    """
    <style>
    :root {
      --cream: #fff9e9;
      --yellow: #ffda70;
      --yellow-dark: #f0bd42;
      --brown: #4b382b;
      --muted: #8b7968;
      --border: #f0e2c4;
      --pale: #fff0bd;
    }

    .stApp {
      background: linear-gradient(
        180deg, #fff9e9 0%, #fffdf7 72%, #fff6dc 100%
      );
      color: var(--brown);
    }

    [data-testid="stHeader"] {
      background: rgba(255, 249, 233, 0.75);
    }

    [data-testid="stAppViewContainer"] .main .block-container {
      max-width: 1000px;
      padding-top: 2.2rem;
      padding-bottom: 3rem;
    }

    h1, h2, h3, p, label {
      color: var(--brown);
    }

    .hero {
      text-align: center;
      padding: 0.8rem 0 1.3rem;
    }

    .hero-icon {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 76px;
      height: 76px;
      border-radius: 24px;
      background: var(--yellow);
      font-size: 42px;
      transform: rotate(-5deg);
      margin-bottom: 12px;
      box-shadow: 0 6px 0 rgba(116, 85, 38, 0.07);
    }

    .hero-tag {
      display: inline-block;
      background: var(--pale);
      color: #78551c;
      border-radius: 999px;
      padding: 5px 13px;
      font-size: 0.85rem;
      font-weight: 800;
      letter-spacing: 0.06em;
    }

    .hero h1 {
      font-size: clamp(2rem, 5vw, 3.15rem);
      font-weight: 900;
      letter-spacing: -0.06em;
      line-height: 1.2;
      margin: 14px 0 8px;
    }

    .hero p {
      color: var(--muted);
      font-size: 1.08rem;
      margin: 0;
    }

    .section-heading {
      font-size: 1.45rem;
      font-weight: 900;
      margin: 0 0 5px;
    }

    .section-help {
      color: var(--muted);
      margin: 0 0 18px;
      font-size: 0.98rem;
    }

    div[data-testid="stButton"] button {
      min-height: 3.2rem;
      border-radius: 15px;
      border: 2px solid var(--border);
      background: #fffdf7;
      color: var(--brown);
      font-weight: 800;
      font-size: 1.05rem;
      transition: transform 0.15s ease, border-color 0.15s ease,
                  background 0.15s ease;
    }

    div[data-testid="stButton"] button:hover {
      border-color: var(--yellow-dark);
      background: var(--pale);
      color: var(--brown);
      transform: translateY(-2px);
    }

    div[data-testid="stButton"] button[kind="primary"] {
      background: var(--yellow);
      border-color: var(--yellow-dark);
      color: var(--brown);
    }

    .result-top {
      text-align: center;
      margin: 1.2rem 0 1rem;
    }

    .result-pill {
      display: inline-block;
      border-radius: 999px;
      background: var(--pale);
      padding: 6px 15px;
      font-size: 0.95rem;
      font-weight: 900;
    }

    .result-title {
      font-size: clamp(1.7rem, 4vw, 2.2rem);
      font-weight: 900;
      margin: 10px 0 0;
    }

    .pokemon-name {
      font-size: clamp(1.8rem, 4vw, 2.3rem);
      font-weight: 900;
      line-height: 1.2;
      margin: 0 0 8px;
    }

    .pokemon-en {
      color: var(--muted);
      font-weight: 650;
      font-size: 1.05rem;
    }

    .type-pill {
      display: inline-block;
      margin: 3px 5px 8px 0;
      padding: 5px 11px;
      background: #fff0bd;
      border: 1px solid #f2dda0;
      border-radius: 999px;
      color: #74521e;
      font-weight: 800;
      font-size: 0.93rem;
    }

    .trait {
      font-size: 1.05rem;
      font-weight: 800;
      color: #6c5037;
      margin: 5px 0 12px;
    }

    .reason-card {
      background: rgba(255,255,255,0.88);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 18px 20px;
      margin-top: 12px;
    }

    .reason-card h3 {
      font-size: 1.12rem;
      margin: 0 0 8px;
    }

    .reason-line {
      margin: 7px 0;
      color: #665342;
      line-height: 1.75;
    }

    .reason-line span {
      color: #d5a222;
      font-weight: 900;
      margin-right: 7px;
    }

    .match-card {
      background: #fff3ca;
      border: 1px solid #f2dda0;
      border-radius: 18px;
      padding: 17px 20px;
      margin-top: 14px;
      text-align: center;
    }

    .match-title {
      font-size: 1rem;
      font-weight: 800;
      margin-bottom: 3px;
    }

    .match-type {
      font-size: 1.65rem;
      font-weight: 900;
    }

    .match-note {
      font-size: 0.92rem;
      color: #786449;
    }

    .footer-note {
      text-align: center;
      margin-top: 25px;
      color: #a08e7b;
      font-size: 0.85rem;
    }

    [data-testid="stImage"] img {
      border-radius: 22px;
    }

    @media (max-width: 600px) {
      [data-testid="stAppViewContainer"] .main .block-container {
        padding-top: 1.2rem;
      }

      div[data-testid="stButton"] button {
        min-height: 2.8rem;
        font-size: 0.95rem;
      }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 선택 결과가 나올 때 실행되는 색종이 애니메이션
CONFETTI_HTML = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 150px;
    overflow: hidden;
    background: transparent;
  }
  canvas {
    display: block;
    width: 100%;
    height: 150px;
  }
</style>
</head>
<body>
<canvas id="confetti"></canvas>
<script>
(() => {
  const canvas = document.getElementById('confetti');
  const ctx = canvas.getContext('2d');
  const colors = [
    '#ffca3a', '#ff7b54', '#f7aef8',
    '#80d8c3', '#82b1ff', '#fff0bd'
  ];
  let width = 0;
  let height = 150;
  let particles = [];

  function resize() {
    const dpr = window.devicePixelRatio || 1;
    width = window.innerWidth;
    canvas.width = Math.max(1, Math.floor(width * dpr));
    canvas.height = Math.floor(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function makeParticle() {
    return {
      x: Math.random() * Math.max(width, 1),
      y: -Math.random() * 200,
      w: 5 + Math.random() * 7,
      h: 7 + Math.random() * 10,
      speed: 1.8 + Math.random() * 3.4,
      drift: -1.1 + Math.random() * 2.2,
      angle: Math.random() * Math.PI,
      spin: -0.12 + Math.random() * 0.24,
      color: colors[Math.floor(Math.random() * colors.length)]
    };
  }

  function start() {
    resize();
    particles = Array.from({length: 115}, makeParticle);
    const started = performance.now();

    function draw(now) {
      ctx.clearRect(0, 0, width, height);

      particles.forEach((p) => {
        p.y += p.speed;
        p.x += p.drift + Math.sin(p.y / 20) * 0.7;
        p.angle += p.spin;

        if (p.y > height + 20) {
          p.y = -10 - Math.random() * 90;
          p.x = Math.random() * Math.max(width, 1);
        }

        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate(p.angle);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
        ctx.restore();
      });

      if (now - started < 4200) {
        requestAnimationFrame(draw);
      } else {
        ctx.clearRect(0, 0, width, height);
      }
    }

    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize);
  start();
})();
</script>
</body>
</html>
"""

# ------------------------------------------------------------
# 앱 화면
# ------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
      <div class="hero-icon">⚡</div><br>
      <span class="hero-tag">POKÉMON × MBTI</span>
      <h1>MBTI로 찾는 나의 단짝 포켓몬</h1>
      <p>내 성격과 닮은 포켓몬을 만나 보자!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-heading">🎯 내 MBTI를 골라 봐!</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-help">16가지 유형 중 하나를 선택하면 단짝 포켓몬을 찾아줄게.</div>',
    unsafe_allow_html=True,
)

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

if "celebrated_mbti" not in st.session_state:
    st.session_state.celebrated_mbti = None

# 16개 버튼을 4열로 표시
for row_start in range(0, len(MBTI_ORDER), 4):
    columns = st.columns(4, gap="small")

    for column, mbti in zip(
        columns, MBTI_ORDER[row_start:row_start + 4]
    ):
        with column:
            is_selected = st.session_state.selected_mbti == mbti

            if st.button(
                mbti,
                key=f"mbti_button_{mbti}",
                type="primary" if is_selected else "secondary",
                use_container_width=True,
            ):
                st.session_state.selected_mbti = mbti
                st.rerun()

selected = st.session_state.selected_mbti

if selected:
    data = POKEMON_DATA[selected]
    is_new_result = st.session_state.celebrated_mbti != selected

    # 새 MBTI 결과가 표시될 때만 축하 효과 실행
    if is_new_result:
        st.session_state.celebrated_mbti = selected
        st.balloons()
        components.html(
            CONFETTI_HTML,
            height=150,
            scrolling=False,
        )

    st.markdown(
        f"""
        <div class="result-top">
          <span class="result-pill">✨ 나의 MBTI · {selected}</span>
          <div class="result-title">🎉 너의 단짝 포켓몬을 찾았어!</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    image_url = f"{IMAGE_BASE}{data['number']}.png"

    left, right = st.columns(
        [1, 1.15],
        gap="large",
        vertical_alignment="center",
    )

    with left:
        st.image(
            image_url,
            caption=f"{data['ko']} 공식 도감 이미지",
            width=300,
        )

        st.markdown(
            f"""
            <div class="match-card">
              <div class="match-title">🤝 잘 맞는 MBTI</div>
              <div class="match-type">{data['match']}</div>
              <div class="match-note">
                서로 다른 매력을 나눌 수 있는 유형!
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            f"""
            <div class="pokemon-name">
              {data['ko']}<br>
              <span class="pokemon-en">({data['en']})</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <span class="type-pill">
              타입 · {data['types']}
            </span>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<div class='trait'>💛 {data['traits']}</div>",
            unsafe_allow_html=True,
        )

        reasons_html = "".join(
            f"<div class='reason-line'><span>✦</span>{reason}</div>"
            for reason in data["reasons"]
        )

        st.markdown(
            f"""
            <div class="reason-card">
              <h3>왜 너와 잘 어울릴까?</h3>
              {reasons_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="footer-note">
          포켓몬과 MBTI의 조합은 재미를 위한 설정이야.
          실제 성격을 정확히 판단하는 검사는 아니야! 🌟
        </div>
        """,
        unsafe_allow_html=True,
    )

else:
    st.markdown(
        """
        <div class="reason-card">
          <h3>🌼 어떻게 사용하나요?</h3>
          <div class="reason-line">
            <span>1</span> 위에서 내 MBTI 버튼을 눌러 줘.
          </div>
          <div class="reason-line">
            <span>2</span> 포켓몬의 이미지와 타입을 확인해 봐.
          </div>
          <div class="reason-line">
            <span>3</span> 잘 맞는 MBTI와 포켓몬의 특징도 알아봐!
          </div>
        </div>
        <div class="footer-note">
          포켓몬 이미지를 불러오려면 인터넷 연결이 필요해.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="footer-note">
      이미지 출처:
      <a href="https://www.pokemon.com/" target="_blank">
        공식 Pokémon 웹사이트
      </a>
    </div>
    """,
    unsafe_allow_html=True,
)
