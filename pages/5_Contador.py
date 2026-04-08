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

# --- BONO: Cuentas regresivas ---
st.markdown("### Próximos destinos:")

# 1. Lógica para el próximo CUMPLEMÉS (Los 22 de cada mes)
if ahora.day < fecha_inicio.day:
    # Si aún no es 22, el próximo cumplemés es este mismo mes
    mes_proximo = ahora.month
    ano_proximo = ahora.year
else:
    # Si ya pasamos del 22, el próximo cumplemés es el mes siguiente
    if ahora.month == 12:
        # Si estamos en diciembre, saltamos a enero del otro año
        mes_proximo = 1
        ano_proximo = ahora.year + 1
    else:
        mes_proximo = ahora.month + 1
        ano_proximo = ahora.year

proximo_mesversario = datetime(ano_proximo, mes_proximo, fecha_inicio.day)
faltan_meses = proximo_mesversario - ahora

# 2. Lógica para el próximo ANIVERSARIO
si_ya_paso_este_ano = (ahora.month > fecha_inicio.month) or (ahora.month == fecha_inicio.month and ahora.day >= fecha_inicio.day)
ano_proximo_aniversario = ahora.year + 1 if si_ya_paso_este_ano else ahora.year

proximo_aniversario = datetime(ano_proximo_aniversario, fecha_inicio.month, fecha_inicio.day)
faltan_anios = proximo_aniversario - ahora

# Mostramos los resultados en dos tarjetas de colores diferentes para que se vea hermoso
st.info(f"🗓️ Faltan exactamente **{faltan_meses.days} días** para nuestro próximo **cumplemés** (el 22). ¡A celebrar!")
st.success(f"🎉 Y faltan **{faltan_anios.days} días** para nuestro próximo **aniversario**. ¡Y los que nos faltan!")
