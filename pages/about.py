import streamlit as st


def run():
    st.write("Welcome to the about page!")
    st.write("This is a simple example of a multi-page Streamlit app.")
    st.write("Click the button below to go to the home page.")
    if st.button("Go to the home page"):
        st.session_state["current_page"] = "home"
