import streamlit as st
import random
import json
from nlp_analyzer import analyze_input
from sus_engine import calculate_suspicion
from conversation_memory import store_response
# from question_genrator import generate_followup
from resoning import generate_question

if "score" not in st.session_state:
    st.session_state.score = 0

with open("questions.json") as f:
    questions = json.load(f)["questions"]

st.markdown(
"""
<h1 style='text-align: center; color: #8E1616;font-size: 60px;'>
AI Interrogator
</h1>
""",
unsafe_allow_html=True
)

st.sidebar.title("Suspicion Meter")

score = st.session_state.score
if score < 30:
    st.sidebar.markdown(
        "<b style='color:green;'>Low Stress</b>",
        unsafe_allow_html=True
    )
elif score < 60:
    st.sidebar.markdown(
        "<b style='color:red;'>Moderate Stress </b>",
        unsafe_allow_html=True
    )
else:
    st.sidebar.markdown(
        "<h3 style='color:red; font-weight:bold;'> ⚠⚠ HIGH STRESS ⚠⚠</h3>",
        unsafe_allow_html=True
    )




st.sidebar.progress(score)
st.sidebar.write(f"Suspicion Score: {score}/100")

# st.subheader("Case Summary")

st.info("""
Case Summary :   
A robbery occurred at **9:30 PM**.  
The suspect claims to have been **at home**.  
The AI system will analyze **inconsistencies in statements**.
""")

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "interrogation_started" not in st.session_state:
    st.session_state.interrogation_started = False

if st.button("Start Interrogation"):

    st.session_state.interrogation_started = True

    crimes = [
        "I didn't rob the store.",
        "I didn't murder anyone.",
        "I wasn't involved in the robbery."
    ]

    denial = random.choice(crimes)

    st.session_state.messages = [
        {"role": "user", "content": denial},
        {"role": "assistant", "content": questions[0]}
    ]

    st.session_state.question_index = 0


st.divider()

st.markdown(
"""
<style>

.stApp {
    background-color: #1D1616;
}

</style>
""",
unsafe_allow_html=True
)

st.subheader("Interrogation Chat : ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Your answer...")

if user_input:

    analysis = analyze_input(user_input)

    suspicion = calculate_suspicion(user_input)
    st.session_state.score += suspicion

    store_response(user_input, analysis)
    st.chat_message("user").write(user_input)




    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    analysis = analyze_input(user_input)

    st.write("DEBUG:", analysis)

    # move to next question
    st.session_state.question_index += 1

    if st.session_state.question_index < len(questions):
        ai_response = generate_question()
    else:
        ai_response = "The interrogation is complete."

    st.chat_message("assistant").write(ai_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })


st.markdown("""
<style>

[data-testid="stChatMessage"] {
    border-radius: 10px;
    padding: 8px;
}

</style>
""", unsafe_allow_html=True)

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

