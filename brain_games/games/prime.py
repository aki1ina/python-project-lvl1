import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question < 2:
        return False
    for i in range(2, question):
        if question % i == 0:
            return False
        return True


def get_question_and_answer():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
