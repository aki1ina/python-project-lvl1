import random
import math


rules = 'Find the greatest common divisor of given numbers.'


def question_answer():
    number1 = random.randint(0, 150)
    number2 = random.randint(0, 150)
    question = str(number1) + ' ' + str(number2)
    answer = str(math.gcd(number1, number2))
    return question, answer
