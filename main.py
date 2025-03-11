import streamlit as st 
import random
import time
st.title("Quiz Application")
questions=[
    {
        "question":"What is the capital of Pakistan?",
        "options":["Karachi","Islamabad","Lahore","Quetta"],
        "answer":"Islamabad"
    },
    {
        "question":"who is the founder of Pakistan?",
        "options":["Allama Iqbal","Quaid-e-Azam","Liaquat Ali Khan","Sir Syed Ahmed Khan"],
        "answer":"Quaid-e-Azam"
    },
    {
        "question":"What is the national game of Pakistan?",
        "options":["Hockey","Cricket","Football","Kabaddi"],
        "answer":"Hockey"
    },
    {
        "question":"What is the national bird of Pakistan?",
        "options":["Chakor","Parrot","Eagle","Sparrow"],
        "answer":"Chakor"
    },
    {
        "question":"What is the national flower of Pakistan?",
        "options":["Rose","Jasmine","Lily","Sunflower"],
        "answer":"Jasmine"
    },
    {
        "question":"What is the national animal of Pakistan?",
        "options":["Lion","Deer","Markhor","Elephant"],
        "answer":"Markhor"
    },
    {
        "question":"What is the national language of Pakistan?",
        "options":["Urdu","Sindhi","Punjabi","Balochi"],
        "answer":"Urdu"
    },
   
    {
        "question":"What is the national tree of Pakistan?",
        "options":["Neem","Banyan","Pine","Deodar"],
        "answer":"Deodar"
    },
    {
        "question":"what is the currency of Pakistan?",
        "options":["Dollar","Rupee","Dinar","Euro"],
        "answer":"Rupee"
    },
    {
         "question":"What is the national dress of Pakistan?",
        "options":["Shalwar Kameez","Pant Shirt","Jeans","Shorts"],
        "answer":"Shalwar Kameez"
    },
    {
        "question":"which is the largest province of Pakistan by area?",
        "options":["Punjab","Sindh","KPK","Balochistan"],
        "answer":"Balochistan"  
    },
    {
        "question":"Which is the largest province of Pakistan by population?",
        "options":["Punjab","Sindh","KPK","Balochistan"],       
        "answer":"Punjab"
    },
    {
        "question":"Which is the smallest province of Pakistan by area?",
        "options":["Punjab","Sindh","KPK","Balochistan"],
        "answer":"KPK"
    },
    {
        "question":"which city is known as city of lights in Pakistan?",
        "options":["Karachi","Lahore","Islamabad","Quetta"],
        "answer":"Karachi"  
    },
   
]
if "current_question" not in st.session_state:
    st.session_state.current_question=random.choice(questions)
question=st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Choose your answer:", question["options"], key="answer")
if st.button("Submit Answer"):
    if selected_option==question["answer"]:
        st.success("Correct Answer!")
        st.balloons()
    else:
        st.error("Incorrect Answer! the correct answer is"+ question["answer"])
    
time.sleep(3)
st.session_state.current_question=random.choice(questions)
st.rerun()
