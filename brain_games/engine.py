import prompt


numbers_of_rounds = 3


def engine(name_game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name_user))
    print(name_game.rules)
    round_number = 1
    while round_number <= numbers_of_rounds:
        question, answer = name_game.question_answer()
        print('Question: ' + str(question))
        answer_user = prompt.string('Your answer: ')
        if answer == answer_user:
            print('Correct!')
            round_number += 1
        else:
            round_number = 10
    if round_number == 10:
        print(str.capitalize(answer_user) + ' is wrong answer.')
        print('Correct answer was ' + str(answer) + '.')
        print("Let's try again, " + name_user + "!")
    else:
        print('Congratulations, ' + name_user + '!')
