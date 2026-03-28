import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Nuestro Tiempo", page_icon="⏳")

st.markdown("# El Contador Eterno ⏳❤️")
st.write("Desde el primer momento en que decidimos estar juntos, el tiempo se ha convertido en mi medida favorita. Cada segundo cuenta.")
st.divider()

# --- AQUÍ PONES LA FECHA DE SU ANIVERSARIO ---
# Formato: datetime(Año, Mes, Día)
fecha_inicio = datetime(2026, 2, 22) 

# Obtenemos la fecha y hora de este exacto momento
ahora = datetime.now()

# Matemáticas del tiempo
diferencia = ahora - fecha_inicio
dias_totales = diferencia.days
segundos_totales = diferencia.seconds

# Calculamos años, meses y días (Aproximación estándar)
anos = dias_totales // 365
meses = (dias_totales % 365) // 30
dias = (dias_totales % 365) % 30

# Calculamos horas, minutos y segundos
horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60

st.markdown("### Tiempo exacto sumando historias juntos:")

# st.metric crea cuadros de números grandes y bonitos
col1, col2, col3 = st.columns(3)
col1.metric("Años", anos)
col2.metric("Meses", meses)
col3.metric("Días", dias)

col4, col5, col6 = st.columns(3)
col4.metric("Horas", horas)
col5.metric("Minutos", minutos)
col6.metric("Segundos", segundos)

st.caption("*(Actualiza la página en cualquier momento para ver cómo los segundos siguen subiendo)*")
st.divider()

# --- BONO: Cuenta regresiva para el próximo aniversario ---
# Lógica para saber si el aniversario de este año ya pasó o apenas viene
si_ya_paso_este_ano = (ahora.month > fecha_inicio.month) or (ahora.month == fecha_inicio.month and ahora.day >= fecha_inicio.day)
ano_proximo_aniversario = ahora.year + 1 if si_ya_paso_este_ano else ahora.year

proximo_aniversario = datetime(ano_proximo_aniversario, fecha_inicio.month, fecha_inicio.day)
faltan = proximo_aniversario - ahora

st.markdown("### Próximo destino:")
st.info(f"Faltan exactamente **{faltan.days} días** para nuestro próximo aniversario. ¡Y los que nos faltan! 🎉")
