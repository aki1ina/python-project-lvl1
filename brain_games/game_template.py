import prompt


def template(name_game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name_user))
    print(name_game.rules)
    i = 1
    while i <= 3:
        question, answer = name_game.question_answer()
        print('Question: ' + str(question))
        answer_user = prompt.string('Your answer: ')
        if answer == answer_user:
            print('Correct!')
            i = i + 1
        else:
            i = 10
    if i == 10:
        print(str.capitalize(answer_user) + ' is wrong answer.')
        print('Correct answer was ' + str(answer) + '.')
        print("Let's try again, " + name_user + "!")
    else:
        print('Congratulations, ' + name_user + '!')
