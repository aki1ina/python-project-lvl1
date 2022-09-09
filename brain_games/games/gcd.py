import random


rules = 'Find the greatest common divisor of given numbers.'


def get_answer(number1, number2):
    while number2 != 0:
        if number1 > number2:
            number1, number2 = number2, number1
        number2 = number2 % number1
    return str(number1)


def get_question_and_answer():
    number1 = random.randint(0, 150)
    number2 = random.randint(0, 150)
    question = f'{number1} {number2}'
    answer = get_answer(number1, number2)
    return question, answer
