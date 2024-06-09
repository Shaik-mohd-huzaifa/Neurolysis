import streamlit as st


st.title("Childs Information 🐇")
st.write("Please fill out the following information about your child.")
name = st.text_input("Name")
age = st.text_input("Age")
grade = st.text_input("Grade")
medical_conditions = st.text_area("Medical Conditions")
if st.button("Submit"):
    if name:
        # Store the information in session state
        st.session_state["name"] = name
        st.session_state["age"] = age
        st.session_state["grade"] = grade
        st.session_state["medical_conditions"] = medical_conditions

        # Switch to a new page
        st.switch_page("pages/2 - questionnaries.py")
    else:
        st.error("Please fill out the name field.")
