import random


rules = 'What number is missing in the progression?'

def question_answer():
    number = random.randint(1, 100)
    question = str(number)
    step = random.randint(1, 10)
    hidden = random.randint(2, 10)
    answer = str(number + step * hidden)
    i = 1
    while i < 10:
        if i == hidden:
            question += ' ..'
        else:
            question += ' ' + str(number + step * i)
        i += 1
    return question, answer
