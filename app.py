import streamlit as st

st.set_page_config(page_title="Para Ángela María ❤️", page_icon="🥰")

# El símbolo '#' crea un título, y al estar todo en markdown forzamos que sea una sola línea
st.markdown("# Bienvenida mi amor ❤️")

st.write("He creado este pequeño rincón en internet solo para ti. Aquí iré agregando cositas para recordarte lo mucho que te amo y apoyarte cuando lo necesites.")
st.write("👈 Abre el menú lateral para ver lo que he preparado para ti.")

# Creamos 3 columnas (izquierda, centro, derecha)
# Los números [1, 2, 1] hacen que la columna del centro sea un poco más ancha
col1, col2, col3 = st.columns([1, 2, 1])

# Le decimos a Streamlit que ponga la imagen SOLO dentro de la columna del centro (col2)
with col2:
    st.image("foto_portada.jpg", caption="¡Te amo infinito!")
