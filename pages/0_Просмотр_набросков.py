import os
import streamlit as st

folder = "photosui"
for file in os.listdir(folder):
    st.image(os.path.join(folder, file))
