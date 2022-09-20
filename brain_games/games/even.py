import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = random.randrange(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
