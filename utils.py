import random
from exercises import EXERCISES

def get_random_question(subject):
    return random.choice(EXERCISES.get(subject, []))

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()