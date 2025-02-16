from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import even_game


def main():
    print('Welcome to the Brain Games!')
    text, name = welcome_user()
    print(text)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(name)


if __name__ == 'main':
    main()
