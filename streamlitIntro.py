import streamlit as st

name = st.text_input("Your name" , "Nat")
age = st.slider("Your age", 0, 100, 23)

st.write(f"Hola, {name}. Tienes {age} años.")