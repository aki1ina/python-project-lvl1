import prompt


NUMBERS_OF_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.RULES)
    for i in range(NUMBERS_OF_ROUNDS):
        question, answer = game.get_question_and_answer()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print('Correct!')
        else:
            print(str.capitalize(user_answer) + ' is wrong answer.')
            print('Correct answer was ' + str(answer) + '.')
            print("Let's try again, " + user_name + "!")
            return
    print('Congratulations, ' + user_name + '!')
