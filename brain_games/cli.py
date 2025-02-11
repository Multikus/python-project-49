import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    welcome_text = f'Hello, {name}'

    return welcome_text
