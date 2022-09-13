import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    return question % 2 = 0


def get_question_and_answer():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    question = random.randrange(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
