import random


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    check = 0
    divider = 2
    if question < 2:
        return False
    else:
        while divider <= question // 2:
            if question % divider == 0:
                check += 1
                divider = question
            divider += 1
        if check != 0:
            return False
    return True


def get_question_and_answer():
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
