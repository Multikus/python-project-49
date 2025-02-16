import prompt
from random import randint
from brain_games.cli import welcome_user


def check_event_or_odd(number):

    if number % 2 == 0:
        return 'yes'
    return 'no'


def even_game(name):
    game_score = 0

    while game_score < 3:
        number = randint(1, 50)
        print(f'Question: {number}')

        user_response = prompt.string('Your answer: ').lower()
        check_num = check_event_or_odd(number)
        if user_response == check_num:
            game_score += 1
            print('Correct!')
        else:
            print(f"'{user_response}' is wrong answer ;(. Correct answer was '{check_num}'.\nLet's try again, {name}!")
            game_score = 0
    print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    text, name = welcome_user()
    print(text)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(name)


if __name__ == 'main':
    main()
