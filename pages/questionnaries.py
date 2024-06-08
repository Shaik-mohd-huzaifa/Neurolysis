import streamlit as st
import json
from models.QuestionnaireGeneration import chat_session

st.title("Questionnaire 🏄‍♂️")
st.session_state["responses1"] = {}
response = chat_session.send_message(
    "Age:"
    + str(st.session_state["age"])
    + ","
    + "Medical Conditions:"
    + str(st.session_state["medical_conditions"])
    + ","
    + "Grade:"
    + str(st.session_state["grade"])
)
# data = response.json()
data = json.loads(response.text)

# Create an empty dictionary to store the answers
answers = {}
reasons = {}
responses = {}


for question in data["questions"]:
    st.subheader(question["topic"])
    st.write(question["question"])

    # Radio buttons for answer selection
    selected_answer = st.radio(
        "Choose an answer:", question["options"], key=question["question"]
    )

    # Text area for reason
    reason_text = st.text_area(
        f"Reason for choosing '{selected_answer}':",
        key=f"reason_{question['question']}",
    )

    # Store answer and reason
    answers[question["question"]] = selected_answer
    reasons[question["question"]] = reason_text
    responses[question["topic"]] = {
        "question": question["question"],
        "answer": selected_answer,
        "reason": reason_text,
        "options": question["options"],
    }
# Submit button to process answers
if st.button("Submit Answers"):
    st.session_state["responses1"] = responses
    st.success("Form submitted successfully!")
    st.switch_page("pages/quiz.py")
