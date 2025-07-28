import pandas as pd
import streamlit as st
st.write("Version 0.1")
file = st.file_uploader("Upload a CSV")
file = pd.read_json(file)
st.dataframe(file)