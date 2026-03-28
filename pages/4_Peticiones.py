import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(page_title="Buzón de Antojos", page_icon="💌")

st.markdown("# Buzón de Antojos 💌")
st.write("¿Tuviste un día pesado? ¿Tienes antojo de algo rico? ¡Haz tu pedido aquí y tu novio exclusivo se encargará del resto!")
st.divider()

# --- FUNCIÓN SECRETA PARA ENVIAR EL CORREO ---
def enviar_correo(categoria, detalles):
    try:
        # Sacamos las llaves de la bóveda
        remitente = st.secrets["correos"]["email_origen"]
        password = st.secrets["correos"]["contrasena"]
        destinatario = st.secrets["correos"]["email_destino"]

        # Armamos el correo
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = "💌 ¡Nuevo pedido de Ángela María!"
        
        cuerpo = f"¡Hola!\n\nTienes un nuevo pedido especial de Ángela desde la app.\n\nAntojo: {categoria}\nDetalles adicionales: {detalles}\n\n¡Es hora de consentirla!"
        msg.attach(MIMEText(cuerpo, 'plain'))

        # Nos conectamos a los servidores de Google para enviarlo
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        return False
# ---------------------------------------------

with st.form("formulario_antojos"):
    st.markdown("### Haz tu pedido especial:")
    
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
    
    detalles = st.text_area("¿Algún detalle extra? (Ej: Quiero pizza de pepperoni, o quiero ver una peli de terror)")
    
    enviado = st.form_submit_button("Enviar pedido a mi novio 🚀")
    
    if enviado:
        if categoria == "Elige una opción...":
            st.warning("¡Oye! Tienes que elegir una opción primero. 😉")
        else:
            with st.spinner("Conectando con el celular de tu novio..."):
                exito = enviar_correo(categoria, detalles)
            
            if exito:
                st.snow() 
                st.success("### ¡Pedido enviado directamente a mi celular! ✅📱")
                st.write(f"**Tu pedido:** {categoria}")
                if detalles:
                    st.write(f"**Notas:** {detalles}")
                st.write("Me acaba de llegar la notificación. ¡Me pongo en marcha de inmediato! Te amo.")
            else:
                st.error("Upps, hubo un problema con la señal del servidor. Pero igual tómale un pantallazo a esto y mándamelo por WhatsApp ❤️")
