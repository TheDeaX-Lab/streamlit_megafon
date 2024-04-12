import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

@st.cache_data
def get_data():
    df = pd.DataFrame([
        [dt, dt + timedelta(random.randint(1, 1000)), f"Склад {random.randint(1,5)}", random.randint(10**9, 10**18)]
        for dt in [datetime(2023, 1, 1) + timedelta(days=random.randint(1, 400)) for _ in range(10)]
        for _ in range(random.randint(1, 10))
    ], columns=["Дата погрузки", "Дата истечения срока годности", "Место", "№ товара"])
    return df

st.title("Планирование складских операций")
df = get_data()

st.write("Карта оптимальной загрузки склада")
st.image("Screenshot_52.png")
st.write("Инвентаризация")
st.table(df)