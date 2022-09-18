import random


RULES = 'What is the result of the expression?'
MIN_NUMBER = 0
MAX_NUMBER = 150


def get_question_and_answer():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    action = random.choice([' + ', ' - ', ' * '])
    if action == ' + ':
        answer = str(number1 + number2)
    elif action == ' - ':
        answer = str(number1 - number2)
    elif action == ' * ':
        answer = str(number1 * number2)
    question = str(number1) + action + str(number2)
    return question, answer
