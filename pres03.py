import streamlit as st
import os
from PIL import Image

def main():
    st.title("Mentoreo Pastoral Asigleh")

    # Ruta base donde se encuentran las carpetas de imágenes
    ruta_base = "."  # La misma carpeta del script por defecto
    carpetas_imagenes = ["pres01", "pres02", "pres03"]

    # Selector de carpetas
    carpeta_seleccionada = st.selectbox("Selecciona la carpeta de imágenes:", carpetas_imagenes)
    ruta_imagenes = os.path.join(ruta_base, carpeta_seleccionada)

    try:
        archivos = [f for f in os.listdir(ruta_imagenes) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        archivos.sort()  # Opcional: ordenar los archivos alfabéticamente
    except FileNotFoundError:
        st.error(f"La carpeta '{carpeta_seleccionada}' no se encontró.")
        return

    if not archivos:
        st.info(f"No se encontraron imágenes en la carpeta '{carpeta_seleccionada}'.")
        return

    # Inicializar el índice de la imagen actual en la sesión
    if 'indice_actual' not in st.session_state:
        st.session_state['indice_actual'] = 0
    if 'carpeta_actual' not in st.session_state or st.session_state['carpeta_actual'] != carpeta_seleccionada:
        st.session_state['carpeta_actual'] = carpeta_seleccionada
        st.session_state['indice_actual'] = 0  # Resetear el índice al cambiar de carpeta

    def siguiente_imagen():
        st.session_state['indice_actual'] += 1
        if st.session_state['indice_actual'] >= len(archivos):
            st.session_state['indice_actual'] = 0

    def anterior_imagen():
        st.session_state['indice_actual'] -= 1
        if st.session_state['indice_actual'] < 0:
            st.session_state['indice_actual'] = len(archivos) - 1



    imagen_actual_nombre = archivos[st.session_state['indice_actual']]
    ruta_completa = os.path.join(ruta_imagenes, imagen_actual_nombre)

    try:
        imagen = Image.open(ruta_completa)
        st.image(imagen, use_container_width=True)
        #st.write(f"Imagen {st.session_state['indice_actual'] + 1} de {len(archivos)} en '{carpeta_seleccionada}'")
    except FileNotFoundError:
        st.error(f"No se pudo encontrar la imagen: {imagen_actual_nombre}")
    except Exception as e:
        st.error(f"Error al abrir la imagen: {e}")
    
    options = ["Atras", "Siguiente"]
    selection = st.pills("Directions", options, selection_mode="single", label_visibility="collapsed")
    if selection == "Atras":
        anterior_imagen()
    elif selection == "Siguiente":
        siguiente_imagen()
    st.divider()



    
    # col1, col2, _ = st.columns([1, 1, 8])

    # with col1:
    #     if st.button("Anterior"):
    #         anterior_imagen()

    # with col2:
    #     if st.button("Siguiente"):
    #         siguiente_imagen()

if __name__ == "__main__":
    main()
