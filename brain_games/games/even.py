import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer():
    question = random.randrange(0, 100, 1)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
