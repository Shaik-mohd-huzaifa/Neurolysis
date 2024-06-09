import streamlit as st

st.set_page_config(page_title="Neurolisys", page_icon="🐢")


st.title("Neurolisys 🐢")
st.write(
    "Welcome to Neurolisys! This is a platform that uses AI to analyze your learning style and personality."
)

if st.button("Check your kids Learning Style"):
    st.switch_page("pages/1 - Info.py")
