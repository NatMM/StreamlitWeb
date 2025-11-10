import streamlit as st
import pandas as pd
import numpy as np

st.title("Dashboard title")
st.header("Section Header")
st.subheader("Subsection")
st.write("Markdown, numbers, dataframes, floats, strs")
st.markdown("**NAT** _nat_ ´code´")

name = st.text("Mode name")
options = st.selectbox("Choose a model", ["CNN", "RNN", "YOLO", "Diffusion"])
threshold = st.slider("Confidence threshold", 0.0, 1.0, 1.5)
run_button = st.button("Run inference")

df = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.dataframe(df)
st.line_chart(df)