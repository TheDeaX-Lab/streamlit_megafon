import streamlit as st
import time
from statistics import mean

st.set_page_config(
    page_title="Склад",
    page_icon="🏚️",
)

if "inited" not in st.session_state:
    st.session_state.update({
        "inited": True,
        "temperature": [15],
        "vlazhnost": [45],
        "osvesh": [10]
    })

st.write("# Добро пожаловать в Мегасклад")

st.title("Тепловая карта склада")
st.write(f"Средняя температура t = {mean(st.session_state['temperature'][-10:])}°C")
st.write(f"Средняя влажность {mean(st.session_state['vlazhnost'][-10:])}%")
uvlazh = st.checkbox("Управление влажностью")
st.write(f"Средняя освященность {mean(st.session_state['osvesh'][-10:])} лк")
svet = st.checkbox("Управление освещением")
st.image("Rezultativnost-sostavlenija-temperaturnoj-karty.jpg")

while True:
    time.sleep(1)
    st.session_state["temperature"].append(
        max(st.session_state["temperature"][-1] - 1, 15)
        if not svet else
        min(st.session_state["temperature"][-1] + 1, 22)
    )
    st.session_state["vlazhnost"].append(
        max(st.session_state["vlazhnost"][-1] * 0.8, 45)
        if not uvlazh else
        min(st.session_state["vlazhnost"][-1] + 1, 85)
    )
    st.session_state["osvesh"].append(
        10
        if not svet else
        450
    )
    st.rerun()