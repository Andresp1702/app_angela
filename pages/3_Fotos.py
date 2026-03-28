import streamlit as st

st.set_page_config(page_title="Nuestra Historia", page_icon="📸")

st.markdown("# Nuestra Historia en Fotos 📸")
st.write("Un pequeño recorrido por nuestros mejores momentos. Cada foto es un instante en el que me di cuenta de lo afortunado que soy de tenerte.")
st.divider()

# --- RECUERDO 1 ---
st.markdown("### 1. El comienzo de todo ✨")
st.caption("Fecha: [Escribe la fecha aquí, ej: 15 de Marzo de 2022]")
# Asegúrate de que "foto1.jpg" sea el nombre exacto de la imagen que subiste
st.image("foto1.jpg", caption="Nuestro primer recuerdo juntos")
st.write("Aquí puedes escribir qué sentiste ese día, por qué fue especial o los nervios que tenías. ¡Cuéntale la historia desde tu perspectiva!")
st.divider()

# --- RECUERDO 2 ---
st.markdown("### 2. Nuestra primera aventura 🌍")
st.caption("Fecha: [Escribe la fecha aquí]")
st.image("foto2.jpg", caption="Descubriendo lugares a tu lado")
st.write("Escribe aquí sobre este viaje, esa salida inolvidable o esa vez que se perdieron pero se divirtieron mucho.")
st.divider()

# --- RECUERDO 3 ---
st.markdown("### 3. Ataques de risa 😂")
st.caption("Fecha: [Escribe la fecha aquí]")
st.image("foto3.jpg", caption="Contigo todo es más divertido")
st.write("Cuenta la historia detrás de esta foto. Recuerda esa anécdota graciosa o esa broma que solo ustedes dos entienden.")
st.divider()

# --- RECUERDO 4 ---
st.markdown("### 4. Un día muy nuestro ❤️")
st.caption("Fecha: [Escribe la fecha aquí]")
st.image("foto4.jpg", caption="Uno de mis días favoritos")
st.write("Escribe por qué este día en particular se quedó grabado en tu corazón. A veces los planes más sencillos son los mejores.")
st.divider()

# --- RECUERDO 5 ---
st.markdown("### 5. Y lo que nos falta... 🥰")
st.caption("Fecha: Hoy y siempre")
st.image("foto5.jpg", caption="Mi persona favorita")
st.write("Cierra esta galería con un mensaje lindo. Recuérdale que esta galería apenas está empezando y que el álbum de su vida juntos tiene muchas páginas en blanco por llenar.")

st.success("Te amo, Ángela María. Gracias por todos estos momentos.")
