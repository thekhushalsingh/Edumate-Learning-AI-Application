import streamlit as st
from database import init_db, add_user, log_progress, get_progress
from exercises import EXERCISES, RESOURCES
from ai_agent import explain_concept, generate_hint
from utils import get_random_question, check_answer

# Initialize DB
init_db()

st.title("🎓 EduMate - Your AI Learning Companion (Powered by SambaNova)")

# User setup
if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.header("Welcome! Let's set up your learning profile.")
    name = st.text_input("Your Name")
    goals = st.text_input("Learning Goals")
    style = st.selectbox("Preferred Learning Style", ["Visual", "Textual", "Interactive"])
    
    if st.button("Start Learning"):
        add_user(name, goals, style)
        st.session_state.user = name
        st.success(f"Profile created! Welcome, {name}")

# Main interface
if st.session_state.user:
    st.header(f"Hello {st.session_state.user}, what do you want to learn today?")
    subject = st.selectbox("Choose a subject", ["Math", "Science", "Coding", "English"])

    # Show example exercise
    question_data = get_random_question(subject)
    st.subheader("Try this question:")
    st.write(question_data["question"])
    user_answer = st.text_input("Your Answer:")

    if st.button("Submit Answer"):
        if check_answer(user_answer, question_data["answer"]):
            st.success("✅ Correct! Great job.")
            log_progress(1, subject, 1)  # user_id=1 for simplicity
        else:
            st.error("❌ Incorrect. Here's a hint:")
            st.info(generate_hint(question_data["question"]))

    # Explain concepts
    st.subheader("Need an explanation?")
    concept = st.text_input("Enter a concept to explain")
    style = st.selectbox("Choose explanation style", ["simple", "technical", "analogy"])
    
    if st.button("Explain"):
        explanation = explain_concept(concept, style)
        st.write(explanation)

    # Resource suggestions
    st.subheader("Recommended Resources")
    for res in RESOURCES.get(subject, []):
        st.write(f"- {res}")

    # Show progress
    st.subheader("Your Progress")
    progress_data = get_progress(1)
    st.write(progress_data)