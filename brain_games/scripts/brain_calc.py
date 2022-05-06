#!/usr/bin/env python
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name_user))
    print('What is the result of the expression?')
    i = 1
    while i <= 3:
        number1 = random.randint(0, 150)
        number2 = random.randint(0, 150)
        action = random.choice([' + ', ' - ', ' * '])
        if action == ' + ':
            answer = number1 + number2
        elif action == ' - ':
            answer = number1 - number2
        elif action == ' * ':
            answer = number1 * number2
        print('Question: ' + str(number1) + action + str(number2))
        answer_user = prompt.string('Your answer: ')
        if int(answer_user) == answer:
            print('Correct!')
            i = i + 1
        else:
            i = 10
    if i == 10:
        print(str(answer_user) + ' is wrong answer . Correct answer was ' + str(answer) + '.')
        print("Let's try again, " + name_user + "!")
    else:
        print('Congratulations, ' + name_user + '!')

if __name__ == '__main__':
    main()
