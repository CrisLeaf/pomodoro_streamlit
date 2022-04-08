import streamlit as st, time, beepy

st.header("Pomodoro APP de Entrenamiento\n(Para participar en el sorteo)")
series, (col1, col2) = int(st.number_input("Número de Series:", 0, 10)), st.columns(2)
ejercicios = [int(col1.number_input(f"Duración ejercicio {i+1}", min_value=0, step=5)) for i in range(series)]
descansos = [int(col2.number_input(f"Duración descanso {i+1}", min_value=0, step=5)) for i in range(series)]

if st.button("Empezar"):
	for index, (ejercicio, descanso) in enumerate(zip(ejercicios, descansos)):
		with st.empty():
			beep(sound="coin")
			for i in range(ejercicio, 0, -1):
				st.markdown(f"""<p style="color:green;font-size:50px">{i}s</p>""", unsafe_allow_html=True)
				time.sleep(1)
			st.success(f"🔔 Ejercicio n° {index+1} completado! 🔔")
		with st.empty():
			print("\007")
			for i in range(descanso, 0, -1):
				st.markdown(f"""<p style="color:red;font-size:50px">{i}s</p>""", unsafe_allow_html=True)
				time.sleep(1)
			st.error(f"🔔 Descanso n° {index+1} completado! 🔔")
	print("\007")
	st.warning(f"🔔 Serie Completada! 🔔")
