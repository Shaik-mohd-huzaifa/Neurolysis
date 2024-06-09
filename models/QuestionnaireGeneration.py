import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMENI_API_KEY"))
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
    system_instruction="I am building a application to analyze the learning style of a Kid. There are some set of questions and parameter which you need to consider and generate question from different topics.\n\n* The Question will be generated also by considering the age of the kid.\n\n* You will be given some data like age of the kid.\n\nGenerate one question for each topic and also with options like the options can range from 2 - 4 max\nThe questions should be more of like understand the thinking ability of the kid rather than the right answer. \nEx: Assume your friend knows cricket. what would you learn ? 1. learn same sport, 2. learn other sport, 3. do not learn anything.\n \n\nTopics :\n1. Intelligence Quotient \n2. Emotional Quotient\n3. Social or Scenario Based Questions\n4. Priority Based questions\n5. Self Esteem\n6. Self Confidence\n7. Problem Solving\n8. Growth Mindset\n\n\nGenerate response in a JSON\n\n ",
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "Age: 5",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Here are some questions for a 5-year-old, designed to understand their thinking and learning style:\n\n**1. Intelligence Quotient (IQ)**\n\n* **Question:**  You have 3 cookies, and your friend has 2 cookies. Who has more cookies? \n    * **Options:**  a) You  b) Your friend  c) You both have the same\n\n**2. Emotional Quotient (EQ)**\n\n* **Question:** Your friend is feeling sad because they lost their favorite toy. How can you make them feel better?\n    * **Options:** a) Give them a hug  b) Play a game with them  c)  Let them cry  \n\n**3. Social or Scenario Based Questions**\n\n* **Question:** You are at the park with your family. You see a little bird that has fallen out of its nest. What do you do?\n    * **Options:** a) Leave it alone  b) Try to put it back in the nest  c) Take it home with you\n\n**4. Priority Based Questions**\n\n* **Question:** You want to go to the playground, but your mom says you have to clean up your toys first. What do you do?\n    * **Options:**  a) Go to the playground first  b) Clean up your toys first  c) Ask your mom to clean them up\n\n**5. Self Esteem**\n\n* **Question:** What is something you are really good at?\n    * **Options:**  a) Drawing  b) Singing  c) Running  d) Playing with toys \n\n**6. Self Confidence**\n\n* **Question:** You have a new puzzle that looks really hard. Do you think you can solve it?\n    * **Options:** a) Yes, I can try  b) No, it's too hard  c) I'll ask for help\n\n**7. Problem Solving**\n\n* **Question:** You want to build a tower with blocks, but the blocks keep falling down. What could you do to make the tower stay up?\n    * **Options:**  a) Use more blocks  b) Stack them carefully  c) Ask for help\n\n**8. Growth Mindset**\n\n* **Question:** You tried to learn how to ride a bike, but you fell down a few times. Will you keep trying?\n    * **Options:** a) Yes, I'll keep trying  b) No, it's too hard  c) I'll ask for help\n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "Age 10\n",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Here are some questions for a 10-year-old, designed to explore their thinking and learning style:\n\n**1. Intelligence Quotient (IQ)**\n\n* **Question:** You have 10 candies, and you want to share them equally with your two friends. How many candies would each person get?\n    * **Options:** a) 3  b) 4  c) 5 \n\n**2. Emotional Quotient (EQ)**\n\n* **Question:**  Your best friend is upset because they didn't get the part they wanted in the school play. How would you support them?\n    * **Options:**  a) Tell them it's okay, and that they'll get a different role next time  b) Encourage them to try out for something else  c)  Let them know you're there for them and listen to them\n\n**3. Social or Scenario Based Questions**\n\n* **Question:** You are at a friend's house, and they offer you a snack that you know you're allergic to. What do you do?\n    * **Options:** a) Politely decline the snack and explain why  b) Take the snack anyway, hoping it won't bother you  c) Tell your friend's parent about the allergy \n\n**4. Priority Based Questions**\n\n* **Question:** You have a big test tomorrow, but your friend wants you to go to the movies tonight. What do you do? \n    * **Options:** a) Go to the movies anyway  b) Study for the test  c) See if you can go to the movies another day\n\n**5. Self Esteem**\n\n* **Question:** What are you proud of accomplishing recently?\n    * **Options:** (Open ended - let them tell you) \n\n**6. Self Confidence**\n\n* **Question:** You are trying out for the school soccer team. How would you feel if you didn't make the team?\n    * **Options:**  a) Discouraged but I'd try out again next year  b)  I wouldn't try out again  c) I would be disappointed, but I'd focus on other things I enjoy\n\n**7. Problem Solving**\n\n* **Question:** You are planning a birthday party for your friend. You need to figure out a fun activity, but you're on a tight budget. What could you do?\n    * **Options:** (Open ended - encourage them to come up with creative solutions)\n\n**8. Growth Mindset**\n\n* **Question:**  You're learning to play a new instrument. It's really hard at first, and you're not very good. Will you keep practicing?\n    * **Options:** a) Yes, I know I'll get better with practice  b) No, it's too hard  c) I'll try, but I might give up if I don't improve quickly\n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "12",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Here are some questions for a 12-year-old, designed to assess their thinking and learning style:\n\n**1. Intelligence Quotient (IQ)**\n\n* **Question:**  You're trying to solve a puzzle.  You've tried a few different approaches, but nothing seems to work. What do you do next? \n    * **Options:** a)  Give up and try a different puzzle  b)  Take a break and come back to it later  c)  Try a new approach, or look for hints online \n\n**2. Emotional Quotient (EQ)**\n\n* **Question:**  You're having a disagreement with a friend.  What's the most important thing to do to try to resolve it?\n    * **Options:** a)  Tell them they're wrong  b)  Listen to their perspective  c)  Walk away and avoid talking to them\n\n**3. Social or Scenario Based Questions**\n\n* **Question:** You see someone being bullied at school.  What do you do?\n    * **Options:** a)  Ignore it and pretend you didn't see it  b)  Step in and try to help the person being bullied  c)  Tell a teacher or another trusted adult\n\n**4. Priority Based Questions**\n\n* **Question:**  You have a school project due next week, and your friend wants you to go to a concert with them the night before. What do you do? \n    * **Options:** a) Go to the concert and work on the project later  b)  Finish the project first and go to the concert  c)  Ask your friend to postpone the concert \n\n**5. Self Esteem**\n\n* **Question:**  What are some of your strengths and talents?\n    * **Options:** (Open ended - let them tell you)\n\n**6. Self Confidence**\n\n* **Question:**  You're trying out for the school play. How would you feel if you didn't get a part?\n    * **Options:** a)  Discouraged, but I'd try out again next year  b) I wouldn't try out again  c) I'd be disappointed, but I'd focus on other things I enjoy\n\n**7. Problem Solving**\n\n* **Question:** You're trying to plan a trip with your family, but everyone has different ideas about where to go. How would you approach finding a solution that everyone agrees on?\n    * **Options:** (Open ended - encourage them to brainstorm solutions)\n\n**8. Growth Mindset**\n\n* **Question:** You're learning a new skill, like playing an instrument or coding.  You're not very good at it yet.  How do you stay motivated to keep learning and practicing?\n    * **Options:**  a)  Focus on how much you've already learned  b)  Compare yourself to others  c)  Remember that everyone starts somewhere \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "3",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Here are some questions for a 3-year-old, designed to understand their thinking and learning style: \n\n**1. Intelligence Quotient (IQ)**\n\n* **Question:**  You have two apples, and I give you one more.  How many apples do you have now?\n    * **Options:** a) One  b) Two  c) Three\n\n**2. Emotional Quotient (EQ)**\n\n* **Question:**  Your friend is crying because they fell down.  What do you do? \n    * **Options:** a)  Cry with them  b)  Give them a hug  c)  Tell them it's okay\n\n**3. Social or Scenario Based Questions**\n\n* **Question:**  You are at the park, and you see a little dog.  What do you do?\n    * **Options:** a)  Run away  b)  Say hello to the dog  c)  Pet the dog \n\n**4. Priority Based Questions**\n\n* **Question:**  You want to play with your toys, but it's time for dinner. What do you do? \n    * **Options:** a)  Play with your toys first  b)  Eat dinner first  c)  Ask for more time to play\n\n**5. Self Esteem**\n\n* **Question:** What is something you like to do?\n    * **Options:** (Open ended - let them tell you)\n\n**6. Self Confidence**\n\n* **Question:** You are going to try a new toy.  Are you excited to try it?\n    * **Options:** a) Yes  b) No  c) Maybe\n\n**7. Problem Solving**\n\n* **Question:**  You want to build a tower with blocks, but the blocks keep falling down.  What could you do?\n    * **Options:**  a) Give up  b)  Ask for help  c)  Try to stack them differently\n\n**8. Growth Mindset**\n\n* **Question:**  You tried to put on your shoes, but you can't do it by yourself.  Will you keep trying?\n    * **Options:** a) Yes  b) No  c) Maybe \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "Generate in JSON format but as a string\n",
            ],
        },
        {
            "role": "model",
            "parts": [
                '```json\n{\n  "questions": [\n    {\n      "topic": "Intelligence Quotient (IQ)",\n      "question": "You have two apples, and I give you one more.  How many apples do you have now?",\n      "options": ["One", "Two", "Three"]\n    },\n    {\n      "topic": "Emotional Quotient (EQ)",\n      "question": "Your friend is crying because they fell down.  What do you do?",\n      "options": ["Cry with them", "Give them a hug", "Tell them it\'s okay"]\n    },\n    {\n      "topic": "Social or Scenario Based Questions",\n      "question": "You are at the park, and you see a little dog.  What do you do?",\n      "options": ["Run away", "Say hello to the dog", "Pet the dog"]\n    },\n    {\n      "topic": "Priority Based Questions",\n      "question": "You want to play with your toys, but it\'s time for dinner. What do you do?",\n      "options": ["Play with your toys first", "Eat dinner first", "Ask for more time to play"]\n    },\n    {\n      "topic": "Self Esteem",\n      "question": "What is something you like to do?",\n      "options": ["Open ended - let them tell you"] \n    },\n    {\n      "topic": "Self Confidence",\n      "question": "You are going to try a new toy.  Are you excited to try it?",\n      "options": ["Yes", "No", "Maybe"]\n    },\n    {\n      "topic": "Problem Solving",\n      "question": "You want to build a tower with blocks, but the blocks keep falling down.  What could you do?",\n      "options": ["Give up", "Ask for help", "Try to stack them differently"]\n    },\n    {\n      "topic": "Growth Mindset",\n      "question": "You tried to put on your shoes, but you can\'t do it by yourself.  Will you keep trying?",\n      "options": ["Yes", "No", "Maybe"]\n    }\n  ]\n}\n``` \n',
            ],
        },
        {
            "role": "user",
            "parts": [
                "gnenerate response in text but in json format",
            ],
        },
    ]
)

# response = chat_session.send_message("Age: 5")

# print(json.dumps(json.loads(response.text), indent=4))
# print(response.text)
