
import streamlit as st

st.set_page_config(
    page_title="CHROMA",
    page_icon="🎨",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #F7F0E8;
}
h1 {
    color: #80634F;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("CHROMA ✨")
st.subheader("Your outfit, your colors")

st.write(
    "Descubrí qué colores de sombras combinan "
    "con tu outfit."
)

foto = st.file_uploader(
    "📸 Subí una foto de tu outfit",
    type=["jpg", "jpeg", "png"]
)

estilo = st.selectbox(
    "💄 Elegí tu estilo de maquillaje",
    ["Natural", "Brillante", "Intenso"]
)

if foto:
    st.image(foto, caption="Tu outfit", use_container_width=True)

    st.success("¡Foto cargada correctamente!")

    st.info(
        f"Tu estilo elegido es: {estilo}. "
        "Próximamente aparecerá tu paleta personalizada."
    )
