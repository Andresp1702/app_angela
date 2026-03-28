import streamlit as st
import random

# Configuración básica de la página
st.set_page_config(page_title="Ruleta de Citas", page_icon="🎡")

st.markdown("# Nuestra Ruleta de Citas 🎡")
st.write("¿No sabes que plan elegir? Esto te ayuda a decidir amor")
st.divider()

# Esta es la lista de planes. ¡Puedes agregar todos los que quieras!
# Solo asegúrate de ponerlos entre comillas y separados por comas.
planes = [
    "Noche de películas y tu comida favorita en casa 🍕🎬",
    "Caminar por un parque nuevo y tomar un helado 🍦🌳",
    "Cocinar juntos una receta que nunca hayamos probado 👩‍🍳👨‍🍳",
    "Tarde de juegos de mesa (el que pierda invita la cena) 🎲🏆",
    "Ir a desayunar a un lugar bonito el fin de semana ☕🥞",
    "Día de spa en casa: mascarillas y masajes 💆‍♀️💆‍♂️",
    "Maratón de nuestra serie favorita con cobijas 🛋️🍿"
]

# Creamos un botón grande
if st.button("🌟 ¡Girar la Ruleta! 🌟", use_container_width=True):
    # random.choice elige un elemento al azar de la lista 'planes'
    plan_elegido = random.choice(planes)
    
    # Lanzamos una animación de globos en la pantalla
    st.balloons()
    
    # Mostramos el resultado con un cuadro verde bonito
    st.success(f"### ¡El plan elegido es: \n ## {plan_elegido}")
    
    st.write("¡Prepárate, mi amor! Va a ser increíble. ❤️")
