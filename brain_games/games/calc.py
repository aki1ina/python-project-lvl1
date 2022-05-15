import random


rules = 'What is the result of the expression?'


def question_answer():
    number1 = random.randint(0, 150)
    number2 = random.randint(0, 150)
    action = random.choice([' + ', ' - ', ' * '])
    if action == ' + ':
        answer = str(number1 + number2)
    elif action == ' - ':
        answer = str(number1 - number2)
    elif action == ' * ':
        answer = str(number1 * number2)
    question = str(number1) + action + str(number2)
    return question, answer
    