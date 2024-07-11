import streamlit as st
print("page reloaded")
st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/monsterball.png"
)
st.markdown("""
<style>
img{
 max-height: 300px;
}
.streamlit-expanderContent div {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)
st.title("포켓몬 도감")

st.subheader("포켓몬을 하나씩 추가해서 도감을 채워보세요")

st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요")

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}



if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle("예시 데이터로 채우기")
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(label="포켓몬 이름",
                             value=example_pokemon["name"] if auto_complete else ""
                             )
    with col2:
        types = st.multiselect(
            label="포켓몬 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else ""
        )
    image_url = st.text_input(label="포켓몬 이미지 URL",
                              value=example_pokemon["image_url"] if auto_complete else ""
                              )
    submit = st.form_submit_button(label="Submit")

    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 1개 이상 선택해주세요")
        else:
            st.success("포켓몬을 추가할 수 있습니다")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })
cols = st.columns(3)
for i in range(len(st.session_state.pokemons)):
    with cols[i % 3]:
        pokemon = st.session_state.pokemons[i]
        with st.expander(label=f"**{i+1}. {pokemon['name']}**", expanded=True):
            st.subheader(pokemon["name"])
            st.image(pokemon["image_url"])

            emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
            st.subheader("/".join(emoji_types))
            delete_button = st.button(label="삭제", key=i, use_container_width=True)
            if delete_button:
                print("delete")
                del st.session_state.pokemons[i]
                st.rerun()