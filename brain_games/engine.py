import prompt


numbers_of_rounds = 3


def engine(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.rules)
    round_number = 1
    while round_number <= numbers_of_rounds:
        question, answer = game.get_question_and_answer()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
            round_number += 1
        else:
            round_number = 10
    if round_number == 10:
        print(str.capitalize(user_answer) + ' is wrong answer.')
        print('Correct answer was ' + str(answer) + '.')
        print("Let's try again, " + user_name + "!")
    else:
        print('Congratulations, ' + user_name + '!')
