
import streamlit as st

st.set_page_config(
    page_title="CHROMA",
    page_icon="🎨",
    layout="centered"
)

# DISEÑO: BEIGE, DORADO Y LETRAS NEGRAS
st.markdown("""
<style>
.stApp {
    background-color: #F7F0E8;
    color: #000000;
}

.stApp p,
.stApp label,
.stApp span,
.stApp li,
.stApp small,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stWidgetLabel"] p,
[data-testid="stCaptionContainer"] {
    color: #000000 !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #000000 !important;
}

.stButton > button {
    background-color: #C5A46D;
    color: #000000 !important;
    border-radius: 10px;
    border: 1px solid #80634F;
}

[data-testid="stAlert"] p {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

# ENCABEZADO
st.title("CHROMA ✨")
st.subheader("Tus colores, tu estilo")

st.write(
    "Descubrí qué colores de sombras combinan "
    "con tu ropa y tu estilo de maquillaje."
)

st.markdown("---")

# CARGA DE FOTO
foto = st.file_uploader(
    "📸 Subí una foto de tu conjunto de ropa",
    type=["jpg", "jpeg", "png"]
)

# ELECCIÓN DEL ESTILO
estilo = st.selectbox(
    "💄 Elegí tu estilo de maquillaje",
    ["Natural", "Brillante", "Intenso"]
)

# PALETAS DE SOMBRAS
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

# RESULTADOS
if foto is not None:
    st.image(
        foto,
        caption="Tu conjunto de ropa",
        use_container_width=True
    )

    st.markdown("### 🎨 Personalizá tu paleta")

    color = st.selectbox(
        "¿Cuál es el color principal de tu ropa?",
        list(paletas.keys())
    )

    st.markdown("## ✨ Tu paleta de sombras CHROMA")
    st.write(f"**Estilo elegido:** {estilo}")
    st.write(f"**Color de tu ropa:** {color}")

    sombras = paletas[color]
    columnas = st.columns(4)

    for columna, (nombre, codigo) in zip(columnas, sombras):
        with columna:
            st.markdown(
                f"""
                <div style="
                    background-color: {codigo};
                    height: 85px;
                    border-radius: 12px;
                    border: 1px solid #BDA989;
                "></div>
                """,
                unsafe_allow_html=True
            )
            st.caption(nombre)
            st.caption(codigo)

    st.markdown("### 💡 Consejo de maquillaje")

    if estilo == "Natural":
        st.info(
            "Elegí tonos suaves para conseguir "
            "un maquillaje delicado y natural."
        )
    elif estilo == "Brillante":
        st.info(
            "Probá los tonos champagne y dorado "
            "para lograr un maquillaje luminoso."
        )
    else:
        st.info(
            "Combiná los tonos bronce y marrón "
            "para conseguir un maquillaje intenso."
        )

else:
    st.info(
        "Para comenzar, subí una foto de tu ropa "
        "y elegí tu estilo de maquillaje."
    )

st.markdown("---")
st.caption("CHROMA · Encontrá los colores que van con vos ✨")
