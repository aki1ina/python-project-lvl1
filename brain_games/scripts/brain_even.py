#!/usr/bin/env python
import random
import prompt
from brain_games.scripts.greeting import greeting_user, name_user

def main():
    greeting_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        question = random.randrange(0, 100, 1)
        print('Question: ' + str(question))
        answer_user = prompt.string('Your answer: ')
        if question % 2 == 0: 
            answer = 'yes'
        else:
            answer = 'no'
        if answer == answer_user:
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
        
