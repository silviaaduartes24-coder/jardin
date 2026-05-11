import streamlit as st
import base64
import time
import os

# 1. Configuración básica de la página
st.set_page_config(
    page_title="Jardín | Una flor para tu nombre",
    layout="centered"
)

# 2. Función para inyectar el fondo usando base64 (necesario para Streamlit)
def set_background(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        
        # Detectar la extensión para el MIME type
        ext = image_file.split('.')[-1]
        mime_type = f"image/{ext}" if ext != "jpg" else "image/jpeg"

        css = f"""
        <style>
        .stApp {{
            background-image: url("data:{mime_type};base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        /* Tipografía ligera sin serifas para toda la app */
        html, body, [class*="css"] {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
            font-weight: 300;
            color: #000000 !important;
        }}

        /* Estilos para el Título central */
        .titulo-jardin {{
            text-align: center;
            font-size: 4rem;
            font-weight: 300;
            color: #000000;
            margin-bottom: 0px;
            padding-bottom: 0px;
            letter-spacing: 2px;
        }}

        /* Estilos para el Subtítulo */
        .subtitulo-jardin {{
            text-align: center;
            font-size: 1.5rem;
            font-weight: 300;
            color: #000000;
            margin-top: 0px;
            margin-bottom: 40px;
        }}

        /* Animación de entrada fluida para el resultado */
        @keyframes fadeIn {{
            0% {{ opacity: 0; transform: translateY(20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .resultado-animado {{
            animation: fadeIn 1.2s ease-out;
            text-align: center;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

# Aplicar el fondo
set_background("fondo.jpg")

# 3. Encabezados de la interfaz
st.markdown('<h1 class="titulo-jardin">Jardín</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo-jardin">Un nombre. Una flor.</p>', unsafe_allow_html=True)

# 4. Caja de texto para el usuario
# Ocultamos la etiqueta por defecto de Streamlit por estética y usamos el placeholder
st.markdown("<style>label {display: none !important;}</style>", unsafe_allow_html=True)
nombre_input = st.text_input("Ingresa tu nombre", placeholder="Por favor ingresa tu nombre...")

# Diccionario para mapear las flores con sus imágenes
imagenes_flores = {
    "Hortensia": "hortensia.png",
    "Rosa": "rosa.png",
    "Girasol": "girasol.png",
    "Clavel": "clavel.png",
    "Margarita": "margarita.png"
}

# 5. Lógica principal y visualización
if nombre_input:
    # Limpiamos el nombre de espacios extra
    nombre = nombre_input.strip()
    nombre_minusculas = nombre.lower()
    longitud_nombre = len(nombre_minusculas)

    if longitud_nombre > 0:
        # Transición fluida (Simula un tiempo de "pensamiento/carga")
        with st.spinner('Cultivando tu flor...'):
            time.sleep(1.5) # Espera de 1.5 segundos para dar un efecto de transición suave

        # --- LÓGICA DE ASIGNACIÓN (Tu código original) ---
        vocales = "aeiouáéíóúü"
        cantidad_vocales = sum(1 for letra in nombre_minusculas if letra in vocales)
        
        inicia_con_vocal = nombre_minusculas[0] in vocales
        
        flor_asignada = ""
        if inicia_con_vocal and cantidad_vocales >= 4:
            flor_asignada = "Hortensia"
        elif inicia_con_vocal:
            flor_asignada = "Rosa"
        elif longitud_nombre >= 8:
            flor_asignada = "Girasol"
        elif not inicia_con_vocal and longitud_nombre <= 5:
            flor_asignada = "Clavel"
        else:
            flor_asignada = "Margarita"
        # ------------------------------------------------

        # 6. Mostrar el resultado
        st.markdown(f"""
            <div class="resultado-animado">
                <h2 style="color: #000000; font-weight: 300; font-size: 2.2rem;">
                    Tu flor es: <b>{flor_asignada}</b>
                </h2>
            </div>
        """, unsafe_allow_html=True)

        # Mostrar la imagen de la flor centrada
        imagen_path = imagenes_flores.get(flor_asignada)
        
        if imagen_path and os.path.exists(imagen_path):
            # Usamos columnas para centrar la imagen en la pantalla
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                # Mostrar la imagen con un efecto visual limpio
                st.image(imagen_path, use_container_width=True)
        else:
            st.error(f"⚠️ No se encontró la imagen '{imagen_path}' en el repositorio.")