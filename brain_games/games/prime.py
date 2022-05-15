import random


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_answer():
    question = random.randint(1, 100)
    check = 0
    divider = 2
    if question < 2:
        answer = 'no'
    else:
        while divider <= question // 2:
            if question % divider == 0:
                check += 1
                divider = question
            divider += 1
        if check == 0:
            answer = 'yes'
        else:
            answer = 'no'
    return question, answer
