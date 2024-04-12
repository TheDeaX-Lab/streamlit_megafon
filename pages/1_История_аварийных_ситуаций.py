import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

@st.cache_data
def get_data():
    df = pd.DataFrame([
        [dt, f"Склад {random.randint(1,5)}", random.randint(10**9, 10**18), random.randint(1, 100) * 1000]
        for dt in [datetime(2023, 1, 1) + timedelta(days=random.randint(1, 400)) for _ in range(10)]
        for _ in range(random.randint(1, 10))
    ], columns=["Дата", "Место", "№ товара", "S ущерба"])
    return df

st.title("История аварийных ситуаций")
df = get_data()
flter = st.selectbox("Выберите дату", df["Дата"].unique(), format_func=lambda x: f"{x} (Сумма ущерба {df[df['Дата'] == x]['S ущерба'].sum()})")

st.table(df[df["Дата"] == flter].reset_index(drop=True))