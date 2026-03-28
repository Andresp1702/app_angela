import streamlit as st
import random

# Configuración básica de la página
st.set_page_config(page_title="Ruleta de Citas", page_icon="🎡")

st.markdown("# Nuestra Ruleta de Citas 🎡")
st.write("Esto te ayudará a decidir sobre nuestros planes")
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
if st.button("Presiona aquí para elegir", use_container_width=True):
    # random.choice elige un elemento al azar de la lista 'planes'
    plan_elegido = random.choice(planes)
    
    # Lanzamos una animación de globos en la pantalla
    st.balloons()
    
    # Mostramos el resultado con un cuadro verde bonito
    st.success(f"### El plan elegido essss: \n ## {plan_elegido}")
    
    st.write("Tenemos plan vida. ❤️")
    
    # 1. Creamos un "espacio vacío" en la pantalla que podemos actualizar
    espacio_ruleta = st.empty()
    
    # 2. Hacemos el efecto de "girar" cambiando el texto rápidamente 20 veces
    for i in range(20):
        plan_temporal = random.choice(planes)
        # Mostramos el texto en gris simulando que está pasando rápido
        espacio_ruleta.markdown(f"<h3 style='text-align: center; color: gray;'>🔄 {plan_temporal} 🔄</h3>", unsafe_allow_html=True)
        time.sleep(0.1) # Una pausa diminuta entre cada cambio
        
    # 3. Elegimos el ganador definitivo
    plan_ganador = random.choice(planes)
    
    # 4. Mostramos el ganador en grande, centrado y con color rojo
    espacio_ruleta.markdown(f"<h2 style='text-align: center; color: #ff4b4b;'>✨ {plan_ganador} ✨</h2>", unsafe_allow_html=True)
    
    st.balloons()
    st.success("Tenemos plan vida. ❤️")

# Creamos un botón grande
if st.button("🌟 ¡Girar la Ruleta! 🌟", use_container_width=True):
    # random.choice elige un elemento al azar de la lista 'planes'
    plan_elegido = random.choice(planes)
    
    # Lanzamos una animación de globos en la pantalla
    st.balloons()
    
    # Mostramos el resultado con un cuadro verde bonito
    st.success(f"### ¡El plan elegido es: \n ## {plan_elegido}")
    
    st.write("¡Prepárate, mi amor! Va a ser increíble. ❤️")
