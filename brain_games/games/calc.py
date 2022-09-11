import random


rules = 'What is the result of the expression?'


def get_question_and_answer():
    MIN_NUMBER = 0
    MAX_NUMBER = 150
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
