import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

@st.cache_data
def get_data():
    df = pd.DataFrame([
        [random.randint(10**9, 10**18), random.choice([
            "Нужно помещение с низкой влажностью",
            "Нужно помещение с низкой температурой",
            "Нужно помещение с низкой освещенностью",
        ])]
        for _ in range(random.randint(1, 10))
    ], columns=["Товарное соседство недопустимо (№ товара)", "Советы по расположению"])
    return df

st.title("Карта зонирования")
df = get_data()
st.image("Screenshot_53.png")
st.write("Несовместимое хранение")
st.table(df)