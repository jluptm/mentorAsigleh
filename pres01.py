import streamlit as st
import os
from PIL import Image

def main():
    st.title("Visor de Imágenes")

    # Ruta a la carpeta de imágenes (ajústala a tu necesidad)
    ruta_imagenes = st.text_input("Introduce la ruta a la carpeta de imágenes:", ".")

    try:
        archivos = [f for f in os.listdir(ruta_imagenes) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    except FileNotFoundError:
        st.error(f"La ruta '{ruta_imagenes}' no se encontró.")
        return

    if not archivos:
        st.info("No se encontraron imágenes en la carpeta.")
        return

    # Inicializar el índice de la imagen actual en la sesión
    if 'indice_actual' not in st.session_state:
        st.session_state['indice_actual'] = 0

    def siguiente_imagen():
        st.session_state['indice_actual'] += 1
        if st.session_state['indice_actual'] >= len(archivos):
            st.session_state['indice_actual'] = 0

    def anterior_imagen():
        st.session_state['indice_actual'] -= 1
        if st.session_state['indice_actual'] < 0:
            st.session_state['indice_actual'] = len(archivos) - 1

    col1, col2, _ = st.columns([1, 1, 8]) # Ajustamos las columnas para centrar un poco los botones

    with col1:
        if st.button("Anterior"):
            anterior_imagen()

    with col2:
        if st.button("Siguiente"):
            siguiente_imagen()

    imagen_actual_nombre = archivos[st.session_state['indice_actual']]
    ruta_completa = os.path.join(ruta_imagenes, imagen_actual_nombre)

    try:
        imagen = Image.open(ruta_completa)
        st.image(imagen, caption=imagen_actual_nombre, use_column_width=True)
        st.write(f"Imagen {st.session_state['indice_actual'] + 1} de {len(archivos)}")
    except FileNotFoundError:
        st.error(f"No se pudo encontrar la imagen: {imagen_actual_nombre}")
    except Exception as e:
        st.error(f"Error al abrir la imagen: {e}")

if __name__ == "__main__":
    main()