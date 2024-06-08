import streamlit as st
import time

# Initialize session state
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.question_index = 0
    st.session_state.start_time = 0
    st.session_state.times = {}
    st.session_state.responses = {}
    st.session_state.replays = {}


# Function to update the current question and record time
def next_question():
    current_time = time.time()
    elapsed_time = current_time - st.session_state.start_time
    question_name = QUESTION_TYPES[st.session_state.question_index]
    st.session_state.times[question_name] = elapsed_time
    st.session_state.start_time = current_time
    st.session_state.question_index += 1


# Define the question types
QUESTION_TYPES = ["audio", "video", "image", "text"]


def audio_question():
    st.title("Audio Question")

    audio_file = "material/audio/audio.mp3"  # Replace with the path to your audio file
    st.audio(audio_file)
    questions = [
        "What was Max's favorite treat from the bakery?",
        "Where did the hidden path behind the bakery lead Max?",
        "What did Max find buried under the rose bush in the garden?",
    ]
    answer1 = st.text_input(questions[0])
    answer2 = st.text_input(questions[1])
    answer3 = st.text_input(questions[2])
    response = {questions[0]: answer1, questions[1]: answer2, questions[2]: answer3}

    if st.button("Next"):
        st.session_state.responses["audio"] = response
        next_question()


def video_question():
    st.title("Video Question")

    video_file = "material/video/video.mp4"  # Replace with the path to your video file
    st.video(video_file)

    questions = [
        "Who heard small bird singing?",
        "Why did the big bird said small bird to stop singing?",
        "Who was passing by the jungle",
    ]

    response = {}

    for question in questions:
        answer = st.text_input(question)
        response[question] = answer

    if st.button("Replay Video"):
        if "video_replays" not in st.session_state.replays:
            st.session_state.replays["video_replays"] = 0
        st.session_state.replays["video_replays"] += 1

    if st.button("Next"):
        st.session_state.responses["video"] = response
        next_question()


def image_question():
    st.title("Image Question")

    image_file = "material/image/image.jpg"  # Replace with the path to your image file
    st.image(image_file, caption="Morning Schedule")
    questions = [
        "What activity comes right after Circle Time?",
        "Before Reading time, what do the kids do?",
        "Which activity happens first in the morning schedule?",
    ]
    response = {}

    for question in questions:
        answer = st.text_input(question)
        response[question] = answer

    if st.button("Next"):
        st.session_state.responses["image"] = response
        next_question()


def text_question():
    st.title("Text Story Question")

    text_story = """
    Once upon a time, in a land far away, there was a small village surrounded by mountains. The villagers were known for their hospitality and kindness. 
    One day, a traveler arrived at the village seeking shelter and food. The villagers welcomed him with open arms and offered him a place to stay.
    As the traveler spent more time in the village, he discovered that it was plagued by a mysterious illness. 
    The traveler decided to help the villagers find a cure for the illness.
    """
    st.write(text_story)

    questions = [
        "How did the villagers react when the traveler arrived at the village?",
        "What did the traveler discover about the village after spending some time there?",
        "What did the traveler decide to do to help the villagers?",
    ]

    # Dictionary to store responses
    responses = {}

    # Loop over the questions
    for question in questions:
        response = st.text_input(question)
        responses[question] = response

    if st.button("Next"):
        st.session_state.responses["text"] = responses
        next_question()


# Initial screen with instructions and start button
if not st.session_state.started:
    st.title("Welcome to the Questionnaire")
    st.write("Instructions and Guidance:")
    st.write(
        """
    1. This questionnaire consists of four types of questions: Audio, Video, Image, and Text.
    2. For each question, you will need to perform the required task and then click 'Next' to proceed.
    3. The time taken for each question will be recorded.
    4. Click the 'Start' button to begin the questionnaire.
    """
    )
    if st.button("Start"):
        st.session_state.started = True
        st.session_state.start_time = time.time()
else:
    # Display the current question
    if st.session_state.question_index < len(QUESTION_TYPES):
        question_type = QUESTION_TYPES[st.session_state.question_index]
        if question_type == "audio":
            audio_question()
        elif question_type == "video":
            video_question()
        elif question_type == "image":
            image_question()
        elif question_type == "text":
            text_question()
    else:
        st.title("Questionnaire Completed")
        st.write("Time taken for each question:")
        st.write(st.session_state.times)
        st.write("Responses for each question:")
        st.write(st.session_state.responses)
        st.write("Number of replays for video question:")
        st.write(st.session_state.replays.get("video_replays", 0))
        st.session_state["responses2"] = {
            "responses": st.session_state.responses,
            "times": st.session_state.times,
        }
        st.write(st.session_state["responses1"])
