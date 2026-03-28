import streamlit as st
import random

# 1. Configuración básica de la página
st.set_page_config(page_title="Para Ángela María ❤️", page_icon="🥰")

# 2. Inicializar la "memoria" de la app para que no se repitan los mensajes
if 'mensajes' not in st.session_state:
    st.session_state.mensajes = {
        "Felicidad": [
            "No sabes cuánto amo verte reír", "Amo tu sonrisa", "Verte feliz me llena el corazón",
            "Me encantas", "Iluminas mis días con tu alegría", "Eres mi sol", "Tu felicidad es mi felicidad",
            "Gracias por compartir tu alegría", "Contigo todo es más bonito", "Adoro cuando te ríes a carcajadas",
            "Tu energía positiva me inspira", "Eres una fuente de luz", "Cada día contigo es un regalo",
            "Tu risa cura mis penas", "No cambies nunca quién eres", "Eres perfecta tal como eres",
            "Me encanta verte brillar", "Tu entusiasmo me motiva", "Eres mi razón de sonreír", "Comodín: Te regalo un helado mi amor",
            "Gracias por ser tú", "Me encanta tu forma de amarme y me siento muy amado", "Hoy y siempre te celebro",
            "Me haces muy feliz", "Tu felicidad es contagiosa", "Te adoro en tu mejor versión", "Estoy muy enamorado de ti, mi sol"
        ],
        "Enojo": [
            "Respira, recuerda que te amo", "No tomes decisiones apresuradas", "No te dejes llevar por la ira",
            "Piensa en Mailo", "Está bien estar enojada", "Sé consciente de tus emociones", "Te amo, toma tu tiempo",
            "Comodín: Te compro lo que quieras mi amor", "Recuerda que te puedes desahogar conmigo", "Estoy contigo en esto",
            "Permítete calmarte antes de hablar", "Tu paz es más importante",
            "No te castigues por sentir rabia", "Te amo con todas tus emociones", "Tu bienestar es mi prioridad",
            "Tu enojo es válido, pero no te destruyas", "Soy tu apoyo incondicional mi amor", "Te mando un abrazo, mi sol",
            "Eres fuerte y puedes manejarlo", "Todo pasa, y esto también pasará", "Respira profundo y suelta",
            "No necesitas tener razón para ser feliz", "Cuida tu corazón y no te lastimes más",
            "Te entiendo y te apoyo", "Estoy aquí para ti, siempre", "El amor que siento por ti es muy grande, mi princesa"
        ],
        "Estrés": [
            "Confía en ti", "Eres capaz de lograrlo", "Tu talento es real", "Has superado cosas antes",
            "Cree en tu proceso", "Cada paso cuenta", "No te subestimes", "Tienes fuerza interior",
            "Eres más valiosa de lo que crees", "Puedes con esto y más", "Tu voz importa",
            "Aprendes y creces a cada momento", "Estás en el camino correcto", "Tienes todo lo necesario",
            "No temas equivocarte", "El fracaso no te define", "Levántate con más ganas",
            "Eres resiliente", "Tu intuición es sabia", "Yo confío en ti",
            "Mereces reconocerte", "Hazlo por ti", "Confía en tu juicio", "Tu seguridad se construye",
            "Eres fuerte, mi amor, y puedes con esto", "Comodín: Te regalo un masaje relajante mi amor", "Eres una guerrera", "Estoy orgulloso de ti, mi princesa"
        ],
        "Tristeza": [
            "Llora si necesitas", "Estoy aquí para ti", "No estás sola", "Puedes desahogarte cuando quieras",
            "Te acompaño en tu tristeza", "Permítete sentir", "No te apresures a estar bien",
            "Te abrazo en la distancia", "Es válido que te sientas así", "Tus emociones importan",
            "Eres valiente por permitirte estar triste", "Tómate el tiempo que necesites", "Te sostengo con amor",
            "No escondas lo que sientes", "Puedo escucharte sin juzgar, cuando quieras", "Eres humana y está bien",
            "Cuidaré tu corazón", "Puedes apoyarte en mí", "No te reclames por sentir dolor", "Comodín: Te invito a ver tu película favorita mi amor",
            "Todo pasa, respira", "La tristeza no es eterna", "Permitámonos sanar juntos", "Comodín: Una chocolatina, el chocolate siempre ayuda mi amor",
            "Tu sensibilidad es un don", "Estoy a tu lado", "Eres valiosa aun en la tristeza", "Recuerda que estoy aquí para ti, siempre"
        ],
        "Amor": [
            "Eres amada", "Tu corazón merece amor", "Eres querida profundamente", "Tienes un lugar especial en mi vida",
            "Merezco tu cuidado y lo valdrá", "El amor te rodea", "Eres hermosa dentro y fuera", "Tu ternura me conmueve",
            "Te admiro con todo mi ser", "Te aprecio sin condiciones", "Estoy enamorado de ti",
            "Tu esencia es maravillosa", "Contigo mi alma sonríe", "Eres mi paz", "Eres mi impulso",
            "Gracias por compartir tu amor", "Tu corazón merece lo mejor", "Me encanta quererte", "Comodín: Invita a comer lo que quieras mi amor",
            "Eres afecto puro", "De ti brota cariño", "Eres mi refugio", "Tu amor me transforma",
            "Siempre buscaré cuidarte", "Eres un tesoro", "Eres inolvidable", "¿Te había dicho que me encantas?"
        ]
    }

# 3. Encabezado de la aplicación
st.title("Hola, Ángela María ❤️")
st.write("Esta pequeña app está diseñada para apoyarte en tus momentos malos, resaltar tu alegría, y demostrarte un poco de tooodo el amor que tengo por ti.")
st.write("De tu novio, Andrés Felipe, te amo <3")

st.divider() # Una línea decorativa

st.subheader("¿Qué sientes hoy?")

# 4. Crear columnas para mostrar los botones uno al lado del otro
col1, col2, col3, col4, col5 = st.columns(5)

emocion_seleccionada = None

# Distribuimos los botones en las columnas
with col1:
    if st.button("💛 Felicidad"):
        emocion_seleccionada = "Felicidad"
with col2:
    if st.button("❤️ Enojo"):
        emocion_seleccionada = "Enojo"
with col3:
    if st.button("💚 Estrés"):
        emocion_seleccionada = "Estrés"
with col4:
    if st.button("💙 Tristeza"):
        emocion_seleccionada = "Tristeza"
with col5:
    if st.button("💖 Amor"):
        emocion_seleccionada = "Amor"

# 5. Lógica para mostrar y borrar el mensaje
if emocion_seleccionada:
    lista_actual = st.session_state.mensajes[emocion_seleccionada]
    
    # Comprobamos si todavía hay mensajes en la lista
    if len(lista_actual) > 0:
        # Elegir mensaje aleatorio
        mensaje_elegido = random.choice(lista_actual)
        
        # Eliminar el mensaje de la lista almacenada en session_state
        st.session_state.mensajes[emocion_seleccionada].remove(mensaje_elegido)
        
        # Mostrar el mensaje con un estilo bonito
        st.success(f"### {mensaje_elegido}")
    else:
        # Qué pasa si ya se acabaron los mensajes de esa categoría
        st.info(f"Ya leíste todos los mensajitos de {emocion_seleccionada}. ¡Te amo infinito! 🥰")
