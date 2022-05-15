import random


rules = 'What number is missing in the progression?'

def question_answer():
    number = random.randint(1, 100)
    question = ''
    step = random.randint(1, 10)
    hidden = random.randint(2, 10)
    i = 1
    while i <= 10:
        if i == hidden:
            question += '.. '
            answer = str(number)
        else:
            question += str(number) + ' '
        i += 1
        number += step
    return question, answer
