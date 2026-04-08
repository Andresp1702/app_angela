import streamlit as st
import random

# Configuración básica de la página
st.set_page_config(page_title="Elegir Cita", page_icon="🎡")

st.markdown("# Cajita de Citas 🎡")
st.write("Esto nos ayudará a decidir que hacer hoy mi amor")
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
    "Hacer una caminata que termine con un rio o cascada",
    "Ir a pasear perritos",
    "Ir a pintar figuras de porcelana",
    "Hacer cita como si fueramos desconocidos",
    "Resolver casos de policia con vinito",
    "Tomarnos una smirnoff de tamarindo solossss",
    "Ir a misa",
    "Aprendernos una canción y cantarla juntos",
    "Maratón de nuestra serie favorita con cobijas 🛋️🍿",
    "Cata de postres en casa: comprar varios postres diferentes y darles puntuación 🍰🤤",
    "Armar un fuerte con cobijas y almohadas para hablar y comer snacks ⛺🏰",
    "Noche de comprar mecato para el otro pero en sorpresa jeje",
    "Noche de cócteles inventados por nosotros 🍹🍸",
    "Hacer un picnic en la casa, en el piso y con musiquita suave 🧺🍓",
    "Cita de lectura: cada uno lee su libro juntos y con un buen café",
    "Recrear nuestra primera cita paso a paso ⏪❤️",
    "Noche de karaoke a grito herido en la casa 🎤🎶",
    "Ir a las maquinitas y apostar quién saca más 🕹️👾",
    "Comprar un lienzo grande, poner música y pintarlo juntos 🎨🖌️",
    "Ir a una librería, separarnos por 10 minutos y elegir un libro para el otro 📚🏃‍♂️",
    "Armar un rompecabezas grande mientras escuchamos un podcast o un disco nuevo 🧩🎧",
    "Ir a un mirador a ver el atardecer y comer algo",
    "Visitar un pueblito cercano a comer algo rico 🚙🏘️",
    "Ir a un vivero a elegir una 'planta hija' y plantarla juntos en casa 🪴🌻",
    "Cita fotográfica: salir a caminar por la ciudad solo para tomarnos fotos bonitas 📸🚶‍♀️",
    "Ir a una cafetería bonita exclusivamente a escribirnos cartas el uno al otro ☕💌"
]

# Creamos un botón grande
if st.button("🌟 Presiona aquí! 🌟", use_container_width=True):
    # random.choice elige un elemento al azar de la lista 'planes'
    plan_elegido = random.choice(planes)
    
    # Lanzamos una animación de globos en la pantalla
    st.balloons()
    
    # Mostramos el resultado con un cuadro verde bonito
    st.success(f"### El plan elegido essss: \n ## {plan_elegido}")
    
    st.write("Eso va mi amorrrr. ❤️")
