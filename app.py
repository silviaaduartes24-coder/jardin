import streamlit as st
import base64
import time
import os

# 1. Configuración básica de la página
st.set_page_config(
    page_title="Jardín | Una flor para tu nombre",
    layout="centered"
)

# 2. Función para inyectar el fondo y estilos personalizados
def set_styles(image_file):
    encoded_string = ""
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
    
    ext = image_file.split('.')[-1]
    mime_type = f"image/{ext}" if ext != "jpg" else "image/jpeg"

    css = f"""
    <style>
    /* Fondo de la aplicación */
    .stApp {{
        background-image: url("data:{mime_type};base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Tipografía base y color negro global */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3 {{
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
        color: #000000 !important;
    }}

    /* Título principal */
    .titulo-jardin {{
        text-align: center;
        font-size: 4.5rem;
        font-weight: 400; /* Un poco más de peso que el light */
        margin-bottom: 0px;
        letter-spacing: -1px;
    }}

    /* Subtítulo con peso corregido para legibilidad */
    .subtitulo-jardin {{
        text-align: center;
        font-size: 1.4rem;
        font-weight: 400; /* Menos light, mejor legibilidad */
        margin-top: -10px;
        margin-bottom: 30px;
        opacity: 0.8;
    }}

    /* Centrado y tamaño de la caja de texto */
    .stTextInput {{
        width: 350px !important;
        margin: 0 auto;
    }}
    
    /* Estilo del input */
    input {{
        text-align: center;
        border-radius: 20px !important;
        border: 1px solid rgba(0,0,0,0.2) !important;
        color: #000000 !important;
        background-color: rgba(255,255,255,0.4) !important;
    }}

    /* Animación para el resultado */
    @keyframes fadeIn {{
        0% {{ opacity: 0; transform: translateY(10px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .resultado-container {{
        animation: fadeIn 1s ease-out;
        text-align: center;
        margin-top: 30px;
    }}

    /* Ocultar elementos innecesarios de Streamlit */
    #MainMenu, footer, header {{visibility: hidden;}}
    label {{display: none !important;}}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Aplicar estilos y fondo
set_styles("images/fondo.jpg")

# 3. Estructura de la Interfaz (Centrada)
st.markdown('<h1 class="titulo-jardin">Jardín</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo-jardin">Un nombre. Una flor.</p>', unsafe_allow_html=True)

# Contenedor para centrar la caja de texto
col_left, col_mid, col_right = st.columns([1, 2, 1])
with col_mid:
    nombre_input = st.text_input("Nombre", placeholder="Por favor ingresa tu nombre")

# Diccionario de imágenes
imagenes_flores = {
    "Hortensia": "images/hortensia.png",
    "Rosa": "images/rosa.png",
    "Girasol": "images/girasol.png",
    "Clavel": "images/clavel.png",
    "Margarita": "images/margarita.png"
}

# 5. Lógica y Transición
if nombre_input:
    nombre = nombre_input.strip()
    if len(nombre) > 0:
        with st.spinner(''):
            time.sleep(1.2) # Transición fluida

        nombre_lower = nombre.lower()
        vocales = "aeiouáéíóúü"
        cantidad_vocales = sum(1 for letra in nombre_lower if letra in vocales)
        inicia_con_vocal = nombre_lower[0] in vocales
        
        # Lógica de asignación
        if inicia_con_vocal and cantidad_vocales >= 4:
            flor_asignada = "Hortensia"
        elif inicia_con_vocal:
            flor_asignada = "Rosa"
        elif len(nombre_lower) >= 8:
            flor_asignada = "Girasol"
        elif not inicia_con_vocal and len(nombre_lower) <= 5:
            flor_asignada = "Clavel"
        else:
            flor_asignada = "Margarita"

        # Mostrar Resultado
        st.markdown(f"""
            <div class="resultado-container">
                <p style="font-size: 1.8rem; margin-bottom: 10px;">
                    Tu flor es: <b>{flor_asignada}</b>
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Imagen de la flor centrada
        img_path = imagenes_flores.get(flor_asignada)
        if img_path and os.path.exists(img_path):
            c1, c2, c3 = st.columns([1, 1.2, 1])
            with c2:
                st.image(img_path, use_container_width=True)
        else:
            st.error(f"Imagen no encontrada: {img_path}")