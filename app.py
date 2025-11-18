import streamlit as st
from google import genai

# Configuración de la página
st.set_page_config(
    page_title="Gemini AI Chat",
    page_icon="🤖",
    layout="wide"
)

# CSS Personalizado
st.markdown("""
    <style>
    /* Fondo general */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Estilo del título */
    .title {
        text-align: center;
        color: white;
        font-size: 3em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        color: #e0e0e0;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    
    /* Contenedor principal */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Estilo de los text areas y inputs */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        border: 2px solid #667eea;
        padding: 10px;
        font-size: 16px;
        color: #000000 !important;
    }
    
    .stTextArea > div > div > textarea {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        border: 2px solid #667eea;
        padding: 10px;
        font-size: 16px;
        color: #000000 !important;
    }
    
    /* Placeholder text (texto de ejemplo) */
    .stTextArea > div > div > textarea::placeholder {
        color: #666666 !important;
        opacity: 0.7;
    }
    
    /* Cursor/caret (línea indicadora) */
    .stTextArea > div > div > textarea {
        caret-color: #000000 !important;
    }
    
    .stTextInput > div > div > input {
        caret-color: #000000 !important;
    }
    
    /* Estilo del botón */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 15px 40px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    /* Cajas de respuesta */
    .response-box {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        margin-top: 20px;
        border-left: 5px solid #667eea;
        color: #000000 !important;
    }
    
    /* Spinner personalizado */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<p class="title">🤖 Gemini AI Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Powered by Google Gemini & Streamlit</p>', unsafe_allow_html=True)

# Sidebar para configuración
with st.sidebar:
    st.header("⚙️ Configuración")
    
    # Intentar obtener API Key de secrets primero
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
        st.success("✅ API Key cargada desde secrets")
    else:
        api_key = st.text_input("API Key de Gemini:", type="password", help="Ingresa tu API Key de Google AI Studio")
    
    st.markdown("---")
    st.markdown("### 📖 Instrucciones:")
    st.markdown("""
    1. Ingresa tu API Key de Gemini
    2. Escribe tu prompt
    3. Haz clic en 'Generar Respuesta'
    4. ¡Disfruta de la IA!
    """)
    
    st.markdown("---")
    st.markdown("### 🔗 Enlaces útiles:")
    st.markdown("[Obtener API Key](https://aistudio.google.com/app/apikey)")
    st.markdown("[Documentación Gemini](https://ai.google.dev/)")

# Contenedor principal
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    # Campo de entrada de texto
    st.markdown("### ✍️ Escribe tu prompt:")
    user_prompt = st.text_area(
        label="Prompt",
        placeholder="Ejemplo: Escríbeme un poema sobre el mar...",
        height=150,
        label_visibility="collapsed"
    )
    
    # Botón de envío
    generate_button = st.button("🚀 Generar Respuesta")
    
    # Procesamiento cuando se presiona el botón
    if generate_button:
        if not api_key:
            st.error("⚠️ Por favor ingresa tu API Key en la barra lateral")
        elif not user_prompt:
            st.warning("⚠️ Por favor escribe un prompt")
        else:
            try:
                # Configurar cliente de Gemini con el nuevo SDK
                client = genai.Client(api_key=api_key)
                
                # Mostrar spinner mientras se genera
                with st.spinner('🤔 Gemini está pensando...'):
                    # Generar respuesta con el nuevo SDK
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=user_prompt
                    )
                    
                    # Mostrar respuesta
                    st.markdown("### 💬 Respuesta de Gemini:")
                    st.markdown(f'<div class="response-box">{response.text}</div>', unsafe_allow_html=True)
                    
                    # Mostrar éxito
                    st.success("✅ Respuesta generada exitosamente!")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Verifica que tu API Key sea correcta y que tengas conexión a internet")

# Footer
st.markdown("---")
col_a, col_b, col_c = st.columns([2, 3, 2])
with col_b:
    st.markdown(
        '<p style="text-align: center; color: white; opacity: 0.7;">Desarrollado con ❤️ usando Streamlit y Gemini</p>',
        unsafe_allow_html=True
    )
