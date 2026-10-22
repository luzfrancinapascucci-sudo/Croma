
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
h2, h3 {
    color: #80634F;
}
.stButton > button {
    background-color: #C5A46D;
    color: white;
    border-radius: 10px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.title("CHROMA ✨")
st.subheader("Your outfit, your colors")

st.write(
    "Descubrí qué colores de sombras combinan "
    "con tu outfit y tu estilo."
)

st.markdown("---")

foto = st.file_uploader(
    "📸 Subí una foto de tu outfit",
    type=["jpg", "jpeg", "png"]
)

estilo = st.selectbox(
    "💄 Elegí tu estilo de maquillaje",
    ["Natural", "Brillante", "Intenso"]
)

paletas = {
    "Blanco": [
        ("Champagne", "#F3E1A9"),
        ("Rosa suave", "#E8B9C7"),
        ("Bronce", "#C58D70"),
        ("Plateado", "#D8D9E0")
    ],
    "Negro": [
        ("Dorado", "#D4AF37"),
        ("Champagne", "#F3E1A9"),
        ("Bronce", "#C58D70"),
        ("Rosa brillante", "#E8B9C7")
    ],
    "Gris": [
        ("Plateado", "#D8D9E0"),
        ("Champagne", "#F3E1A9"),
        ("Rosa suave", "#E8B9C7"),
        ("Bronce", "#C58D70")
    ],
    "Azul": [
        ("Champagne", "#F3E1A9"),
        ("Dorado", "#D4AF37"),
        ("Marrón", "#80583F"),
        ("Bronce", "#C58D70")
    ],
    "Verde": [
        ("Dorado", "#D4AF37"),
        ("Champagne", "#F3E1A9"),
        ("Marrón", "#80583F"),
        ("Bronce", "#C58D70")
    ],
    "Beige": [
        ("Marrón", "#80583F"),
        ("Champagne", "#F3E1A9"),
        ("Rosa suave", "#E8B9C7"),
        ("Bronce", "#C58D70")
    ],
    "Rosa": [
        ("Champagne", "#F3E1A9"),
        ("Rosa suave", "#E8B9C7"),
        ("Dorado", "#D4AF37"),
        ("Marrón", "#80583F")
    ]
}

if foto is not None:
    st.image(
        foto,
        caption="Tu outfit",
        use_container_width=True
    )

    color = st.selectbox(
        "🎨 ¿Cuál es el color principal de tu ropa?",
        list(paletas.keys())
    )

    st.markdown("## ✨ Tu paleta CHROMA")
    st.write(f"**Estilo elegido:** {estilo}")

    columnas = st.columns(4)

    for columna, (nombre, codigo) in zip(
        columnas, paletas[color]
    ):
        with columna:
            st.markdown(
                f"""
                <div style="
                    background-color: {codigo};
                    height: 85px;
                    border-radius: 12px;
                    border: 1px solid #D8C7B2;
                "></div>
                """,
                unsafe_allow_html=True
            )
            st.caption(nombre)
            st.caption(codigo)

    if estilo == "Natural":
        st.info(
            "Consejo: probá tonos suaves para un resultado natural."
        )
    elif estilo == "Brillante":
        st.info(
            "Consejo: usá champagne y dorado para dar luminosidad."
        )
    else:
        st.info(
            "Consejo: combiná bronce y marrón para un look intenso."
        )
else:
    st.info(
        "Para comenzar, subí una foto de tu outfit "
        "y elegí tu estilo de maquillaje."
    )

st.markdown("---")
st.caption("CHROMA · Your outfit, your colors ✨")
