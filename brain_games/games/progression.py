import random


RULES = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 10
MIN_HIDDEN_NUMBER = 2
MAX_HIDDEN_NUMBER = 9
PROGRESSION_LENGTH = 10


def get_progression(initial_term, difference, length):
    last_term = initial_term + (length * difference)
    progression = (list(range(initial_term, last_term, difference)))
    return progression


def convert_to_string(progression, hidden_term_index):
    progression[hidden_term_index] = '..'
    progression_string = ' '.join(map(str, progression))
    return progression_string


def get_question_and_answer():
    initial_term = random.randint(MIN_NUMBER, MAX_NUMBER)
    difference = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    hidden_term_index = random.randint(MIN_HIDDEN_NUMBER, MAX_HIDDEN_NUMBER)
    progression = get_progression(initial_term, difference, PROGRESSION_LENGTH)
    answer = progression[hidden_term_index]
    question = convert_to_string(progression, hidden_term_index)
    return question, str(answer)
