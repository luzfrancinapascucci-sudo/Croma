
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
        paletas = {
        "blanco": [("Champagne", "#F3E1A9"),
                   ("Rosa suave", "#E8B9C7"),
                   ("Bronce", "#C58D70"),
                   ("Plateado", "#D8D9E0")],
        "negro": [("Dorado", "#D4AF37"),
                  ("Champagne", "#F3E1A9"),
                  ("Bronce", "#C58D70"),
                  ("Rosa brillante", "#E8B9C7")],
        "gris": [("Plateado", "#D8D9E0"),
                 ("Champagne", "#F3E1A9"),
                 ("Rosa suave", "#E8B9C7"),
                 ("Bronce", "#C58D70")],
        "azul": [("Champagne", "#F3E1A9"),
                 ("Dorado", "#D4AF37"),
                 ("Marrón", "#80583F"),
                 ("Bronce", "#C58D70")],
        "verde": [("Dorado", "#D4AF37"),
                  ("Champagne", "#F3E1A9"),
                  ("Marrón", "#80583F"),
                  ("Bronce", "#C58D70")],
        "beige": [("Marrón", "#80583F"),
                  ("Champagne", "#F3E1A9"),
                  ("Rosa suave", "#E8B9C7"),
                  ("Bronce", "#C58D70")],
        "rosa": [("Champagne", "#F3E1A9"),
                 ("Rosa suave", "#E8B9C7"),
                 ("Dorado", "#D4AF37"),
                 ("Marrón", "#80583F")]
    }

    color = st.selectbox(
        "🎨 ¿Cuál es el color principal de tu ropa?",
        ["blanco", "negro", "gris", "azul", "verde", "beige", "rosa"]
    )

    sombras = paletas[color]

    st.markdown("## ✨ Tu paleta CHROMA")
    st.write(f"Tu estilo elegido es: **{estilo}**")

    columnas = st.columns(4)

    for columna, (nombre, codigo) in zip(columnas, sombras):
        with columna:
            st.markdown(
                f'<div style="background:{codigo}; height:85px; '
                f'border-radius:12px;"></div>',
                unsafe_allow_html=True
            )
            st.caption(nombre)
            st.caption(codigo)
