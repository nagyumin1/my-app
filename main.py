import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="🎮",
    layout="centered"
)

pokemon_data = {
    "INTJ": ("뮤츠", "전략적이고 독립적인 천재형 🧠"),
    "INTP": ("후딘", "분석적이고 호기심이 많은 탐구자 🔬"),
    "ENTJ": ("리자몽", "강한 리더십을 가진 지휘관 🔥"),
    "ENTP": ("팬텀", "창의적이고 장난기 많은 혁신가 😈"),
    "INFJ": ("루기아", "신비롭고 통찰력이 뛰어난 조언자 🌊"),
    "INFP": ("이브이", "상상력이 풍부한 몽상가 🌈"),
    "ENFJ": ("피카츄", "사람들을 이끄는 따뜻한 리더 ⚡"),
    "ENFP": ("뮤", "자유롭고 호기심 많은 모험가 ✨"),
    "ISTJ": ("거북왕", "책임감 있고 믿음직한 수호자 🛡️"),
    "ISFJ": ("해피너스", "배려심 깊고 따뜻한 힐러 💖"),
    "ESTJ": ("보스로라", "체계적이고 강인한 관리자 ⚙️"),
    "ESFJ": ("푸린", "친화력이 뛰어난 인기인 🎤"),
    "ISTP": ("루카리오", "침착하고 실용적인 해결사 👊"),
    "ISFP": ("나인테일", "감성적이고 예술적인 영혼 🌸"),
    "ESTP": ("고우스트", "스릴을 즐기는 행동파 ⚡"),
    "ESFP": ("꼬부기", "즐거움을 전파하는 엔터테이너 😎")
}

st.markdown(
    """
    <h1 style='text-align:center;'>🎮 MBTI 포켓몬 추천기 🎮</h1>
    <p style='text-align:center; font-size:18px;'>
    당신의 MBTI와 가장 잘 어울리는 포켓몬은 누구일까요? 🤔
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

mbti = st.text_input(
    "📝 MBTI를 입력하세요 (예: INFP)",
    max_chars=4
).upper()

if st.button("🔍 포켓몬 추천받기", use_container_width=True):

    if mbti in pokemon_data:
        pokemon, desc = pokemon_data[mbti]

        st.balloons()

        st.success("추천 결과가 나왔어요! 🎉")

        st.markdown(
            f"""
            ## 🌟 당신에게 어울리는 포켓몬

            # 🎯 {pokemon}

            ### 💡 성향
            **{desc}**

            ### 🎮 한 줄 평가
            "{pokemon}처럼 자신만의 매력을 가진 특별한 사람이에요!"
            """
        )

        st.info(
            f"📊 {mbti} 유형은 자신만의 강점을 살려 주변 사람들에게 독특한 인상을 남기는 경우가 많아요!"
        )

    else:
        st.error("❌ 올바른 MBTI를 입력해주세요! (예: INTJ, ENFP)")
        st.caption("가능한 값: INTJ, INTP, ENTJ, ENTP, INFJ, INFP, ENFJ, ENFP, ISTJ, ISFJ, ESTJ, ESFJ, ISTP, ISFP, ESTP, ESFP")

st.divider()

st.caption("✨ Made by 규민이의 웹사이트")
