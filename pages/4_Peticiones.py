import streamlit as st

st.set_page_config(page_title="Buzón de Antojos", page_icon="💌")

st.markdown("# Buzón de Antojos 💌")
st.write("¿Tuviste un día pesado? ¿Tienes antojo de algo rico? ¡Haz tu pedido aquí y tu novio exclusivo se encargará del resto!")
st.divider()

# Creamos el formulario. Todo lo que esté indentado (hacia la derecha) pertenece a él
with st.form("formulario_antojos"):
    st.markdown("### Haz tu pedido especial:")
    
    # st.selectbox crea un menú desplegable
    categoria = st.selectbox(
        "¿Qué necesitas hoy, mi amor?",
        ["Elige una opción...", 
         "🍕 Antojo de comida chatarra", 
         "💆‍♀️ Vale por un masajito", 
         "🍦 Salida por un helado", 
         "🎬 Tarde de películas y arrunchis", 
         "👂 Alguien que me escuche quejarme de mi día",
         "🫂 Solo un abrazo muy fuerte"]
    )
    
    # st.text_area crea un cuadro de texto grande
    detalles = st.text_area("¿Algún detalle extra? (Ej: Quiero pizza de pepperoni, o quiero ver una peli de terror)")
    
    # El botón que envía el formulario
    enviado = st.form_submit_button("Enviar pedido a mi novio 🚀")
    
    # Esta es la lógica: ¿Qué pasa cuando presiona el botón?
    if enviado:
        if categoria == "Elige una opción...":
            # Si no eligió nada, le damos un pequeño aviso
            st.warning("¡Oye! Tienes que elegir una opción primero. 😉")
        else:
            # Si eligió algo, lanzamos un efecto de nieve (diferente a los globos) y un mensaje
            st.snow() 
            st.success("### ¡Pedido recibido con éxito! ✅")
            st.write(f"**Tu pedido:** {categoria}")
            
            # Si escribió detalles, también se los mostramos
            if detalles:
                st.write(f"**Notas adicionales:** {detalles}")
                
            st.write("Tu solicitud ha sido procesada. Me pondré en marcha lo más pronto posible. ¡Te amo!")
