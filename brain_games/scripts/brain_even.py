#!/usr/bin/env python
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name_user))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    n = 0
    while i <= 3:
        number = random.randrange(0, 100, 1)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if (number % 2 == 0 and answer == 'yes') or (number % 2 != 0 and answer == 'no'):
            print('Correct!')
        else:
            n = n + 1

        i = i + 1
    if n == 0:
        print('Congratulations, ' + name_user + '!')


if __name__ == '__main__':
    main()
        
