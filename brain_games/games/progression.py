import random


rules = 'What number is missing in the progression?'


def get_progression(initial_term, difference, length):
    last_term = initial_term + (length * difference)
    progression = list(range(initial_term, last_term, difference))
    return progression


def convert_to_string(progression):
    progression_string = ' '.join(map(str, progression))
    return progression_string


def get_question_and_answer():
    initial_term = random.randint(1, 100)
    difference = random.randint(1, 10)
    hidden = random.randint(2, 10)
    length = 10
    progression = get_progression(initial_term, difference, length)
    answer, progression[hidden] = progression[hidden], '..'
    question = convert_to_string(progression)
    return question, str(answer)
