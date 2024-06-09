from models.AnalyzingModel import chat_session
import json
import streamlit as st

responses = {
    "age": st.session_state["age"],
    "Main Questions": st.session_state["responses2"],
    "Sub Questions": st.session_state["responses1"],
}

response = chat_session.send_message(str(responses))
data = json.loads(response.text)
print(data)
print(type(data))


# Unpack the results dictionary
character = data["character"]
name = st.session_state["name"]
title = data["title"]
description = data["description"]
strengths = data["strengths"]
areas_for_improvement = data["areas_for_improvement"]
learning_style_scale = data["learning_style_scale"]

# Display the results
st.title("Learning Style 📊")
st.header(f"{name} - The {character}")
st.header(f"Title: {title}")
st.subheader(f"Description:")
st.write(f"{description}")
st.subheader(f"Strengths:")
for strength in strengths:
    st.write(strength)
st.subheader(f"Areas for Improvement:")
for area in areas_for_improvement:
    st.write(area)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Visual", learning_style_scale["visual"])
col2.metric("Auditory", learning_style_scale["auditory"])
col3.metric("Reading", learning_style_scale["reading"])
col4.metric("Kinesthetic", learning_style_scale["kinesthetic"])
