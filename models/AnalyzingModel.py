import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))
# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction='I am developing a app where we analyze the learning style of the a kid. \n\nYou will be given data which will be questions given to the kid, answers by kid, reason for choosing that answer and response time taken.\n\nYou have to analyze the data given by considering the answering approach, time taken for that particular question and generate a report that displays the qualities of a kid, what kid lacks and area of improvements.\n\nBelow are some characters which you should put a kid into and response with the character, title, description.\n\n* Characters:  \n\n- Visual Learner: "Vibrant Visionary"\n\nCharacter: A character who loves colors, diagrams, and visual representations. They often draw pictures, create mind maps, and use visual aids to learn and remember information.\nDescription: Vibrant Visionaries prefer to see and visualize information to understand and remember it better.\n\n- Auditory Learner: "Acoustic Ace"\n\nCharacter: A character who excels in listening to lectures, discussions, and audio materials. They might enjoy reading aloud, participating in discussions, and using mnemonics or songs to memorize facts.\nDescription: Acoustic Aces thrive on hearing information. They learn best through listening and speaking.\n\n- Kinesthetic Learner: "Dynamic Doer"\n\nCharacter: A character who learns best by doing and experiencing things firsthand. They enjoy hands-on activities, experiments, and physical movement while learning.\nDescription: Dynamic Doers need to physically engage with their learning materials. They understand and remember information through movement and touch.\n- Reading/Writing Learner: "Literary Luminary"\n\nCharacter: A character who loves to read and write. They prefer using lists, notes, and written explanations. They learn best through reading textbooks, writing essays, and making lists.\nDescription: Literary Luminaries excel with written words. They prefer to interact with text and often find it easier to process and retain information this way.\n\n- Logical/Mathematical Learner: "Logical Luminary"\n\nCharacter: A character who enjoys logical reasoning and problem-solving. They excel in mathematics and science and prefer structured, step-by-step learning methods.\nDescription: Logical Luminaries thrive on logic and order. They excel at reasoning and problem-solving tasks.\n\n- Social Learner: "Social Savvy"\n\nCharacter: A character who learns best in group settings. They enjoy working with others, discussing ideas, and collaborating on projects.\nDescription: Social Savvies learn through interaction with others. They benefit from group discussions and collaborative activities.\n\n* If a kid is good at answering and understand the visual questions faster then consider him. You can suggest combination of multiple characters.\n\n\nGive Response in a json format',
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                'Time taken for each question:\n\n{\n"audio":3.6729929447174072\n"video":0.6724557876586914\n"image":4.040899038314819\n"text":3.4273178577423096\n}\nResponses for each question:\n\n{\n"audio":{\n"What was Max\'s favorite treat from the bakery?":""\n"Where did the hidden path behind the bakery lead Max?":""\n"What did Max find buried under the rose bush in the garden?":""\n}\n"video":{\n"Who heard small bird singing?":""\n"Why did the big bird said small bird to stop singing?":""\n"Who was passing by the jungle":""\n}\n"image":{\n"What activity comes right after Circle Time?":""\n"Before Reading time, what do the kids do?":""\n"Which activity happens first in the morning schedule?":""\n}\n"text":""\n}\nNumber of replays for video question:\n\n0\n\n\n{"Intelligence Quotient (IQ)": {\n        "question": "You have 3 cookies, and your friend has 2 cookies. Who has more cookies?",\n        "answer": "You",\n        "reason": "3 cookies are more than 2 cookies.",\n        "options": [\n            "You",\n            "Your friend",\n            "You both have the same"\n        ]\n    },\n    "Emotional Quotient (EQ)": {\n        "question": "Your friend is feeling sad because they lost their favorite toy. How can you make them feel better?",\n        "answer": "Give them a hug",\n        "reason": "A hug can provide comfort and show that you care about their feelings.",\n        "options": [\n            "Give them a hug",\n            "Play a game with them",\n            "Let them cry"\n        ]\n    },\n    "Social or Scenario Based Questions": {\n        "question": "You are at the park with your family. You see a little bird that has fallen out of its nest. What do you do?",\n        "answer": "Leave it alone",\n        "reason": "The bird\'s parents are likely nearby and will take care of it.",\n        "options": [\n            "Leave it alone",\n            "Try to put it back in the nest",\n            "Take it home with you"\n        ]\n    },\n    "Priority Based Questions": {\n        "question": "You want to go to the playground, but your mom says you have to clean up your toys first. What do you do?",\n        "answer": "Clean up your toys first",\n        "reason": "It\'s important to listen to your mom and take responsibility for cleaning up.",\n        "options": [\n            "Go to the playground first",\n            "Clean up your toys first",\n            "Ask your mom to clean them up"\n        ]\n    },\n    "Self Esteem": {\n        "question": "What is something you are really good at?",\n        "answer": "Drawing",\n        "reason": "I have been practicing drawing a lot and enjoy creating art.",\n        "options": [\n            "Drawing",\n            "Singing",\n            "Running",\n            "Playing with toys"\n        ]\n    },\n    "Self Confidence": {\n        "question": "You have a new puzzle that looks really hard. Do you think you can solve it?",\n        "answer": "Yes, I can try",\n        "reason": "I believe in my ability to solve challenging puzzles if I take my time.",\n        "options": [\n            "Yes, I can try",\n            "No, it\'s too hard",\n            "I\'ll ask for help"\n        ]\n    },\n    "Problem Solving": {\n        "question": "You want to build a tower with blocks, but the blocks keep falling down. What could you do to make the tower stay up?",\n        "answer": "Stack them carefully",\n        "reason": "By carefully stacking the blocks, the tower will be more stable.",\n        "options": [\n            "Use more blocks",\n            "Stack them carefully",\n            "Ask for help"\n        ]\n    },\n    "Growth Mindset": {\n        "question": "You tried to learn how to ride a bike, but you fell down a few times. Will you keep trying?",\n        "answer": "Yes, I\'ll keep trying",\n        "reason": "I know that practice will help me improve and eventually succeed.",\n        "options": [\n            "Yes, I\'ll keep trying",\n            "No, it\'s too hard",\n            "I\'ll ask for help"\n        ]\n    }',
            ],
        },
        {
            "role": "model",
            "parts": [
                '```json\n{\n  "character": "Vibrant Visionary",\n  "title": "Visual Learner",\n  "description": "This kid excels in understanding and remembering information presented visually. They are drawn to colors, diagrams, and visual representations, and learn best through visual aids like pictures, mind maps, and videos. They are a natural at absorbing information quickly through visual stimuli."\n}\n```',
            ],
        },
        {
            "role": "user",
            "parts": [
                "what about other fields like strenghts, etc",
            ],
        },
        {
            "role": "model",
            "parts": [
                '```json\n{\n  "character": "Vibrant Visionary",\n  "title": "Visual Learner",\n  "description": "This kid excels in understanding and remembering information presented visually. They are drawn to colors, diagrams, and visual representations, and learn best through visual aids like pictures, mind maps, and videos. They are a natural at absorbing information quickly through visual stimuli.",\n  "strengths": [\n    "Visual Memory:  Excellent at remembering what they see.",\n    "Spatial Reasoning:  Strong ability to understand and manipulate spatial relationships.",\n    "Creativity:  Thrives on visual expression,  enjoys drawing, art, and design.",\n    "Attention to Detail:  Notices small details in images and visual information."\n  ],\n  "areas_for_improvement": [\n    "Auditory Processing: May struggle to process and remember information presented verbally.",\n    "Kinesthetic Learning: Might benefit from incorporating more hands-on activities to solidify understanding." \n  ]\n}\n``` \n',
            ],
        },
        {
            "role": "user",
            "parts": [
                "Also show like scale from 1 to 100 for these for learning types visual, auditory, reading, kinesthetics of a kid  ",
            ],
        },
        {
            "role": "model",
            "parts": [
                '```json\n{\n  "character": "Vibrant Visionary",\n  "title": "Visual Learner",\n  "description": "This kid excels in understanding and remembering information presented visually. They are drawn to colors, diagrams, and visual representations, and learn best through visual aids like pictures, mind maps, and videos. They are a natural at absorbing information quickly through visual stimuli.",\n  "strengths": [\n    "Visual Memory:  Excellent at remembering what they see.",\n    "Spatial Reasoning:  Strong ability to understand and manipulate spatial relationships.",\n    "Creativity:  Thrives on visual expression,  enjoys drawing, art, and design.",\n    "Attention to Detail:  Notices small details in images and visual information."\n  ],\n  "areas_for_improvement": [\n    "Auditory Processing: May struggle to process and remember information presented verbally.",\n    "Kinesthetic Learning: Might benefit from incorporating more hands-on activities to solidify understanding." \n  ],\n  "learning_style_scale": {\n    "visual": 90,\n    "auditory": 50,\n    "reading": 60, \n    "kinesthetic": 40 \n  }\n}\n```\n\n**Explanation of the Scale:**\n\n* **Visual (90):**  The kid demonstrates a very strong preference for visual learning, scoring high on this scale.\n* **Auditory (50):**  While not as strong as visual, the kid still has some ability to learn through auditory means, but it might require more effort.\n* **Reading (60):** The kid has moderate preference for learning through reading, indicating that they are comfortable with text-based learning but might not be as engaged as with visual methods.\n* **Kinesthetic (40):** The kid scores lower on kinesthetic learning, suggesting that they might benefit from incorporating more hands-on activities to supplement their learning. \n\n**Note:** These scores are estimations based on the provided data.  To get a more accurate and detailed assessment, a more comprehensive evaluation using various learning style assessments is recommended. \n',
            ],
        },
    ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
print(chat_session.history)
