import prompt


def greeting_user():
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name_user))