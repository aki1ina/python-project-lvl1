import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    if question % 2 != 0:
        return False
    return True


def get_question_and_answer():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    question = random.randrange(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
