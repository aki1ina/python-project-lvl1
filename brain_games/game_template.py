import prompt


def template(name_game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name_user))
    print(rules)
    i = 1
    while i <= 3:
        print('Question: ' + str(question))
        answer_user = prompt.string('Your answer: ')
        if answer == answer_user:
            print('Correct!')
            i = i + 1
        else:
            i = 10
    if i == 10:
        print(str(answer_user) + ' is wrong answer. Correct answer was ' + str(answer) + '.')
        print("Let's try again, " + name_user + "!")
    else:
        print('Congratulations, ' + name_user + '!')
