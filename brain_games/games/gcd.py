import random


RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    while number2 != 0:
        if number1 > number2:
            number1, number2 = number2, number1
        number2 = number2 % number1
    return str(number1)


def get_question_and_answer():
    MIN_NUMBER = 0
    MAX_NUMBER = 150
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number1} {number2}'
    answer = get_gcd(number1, number2)
    return question, answer
