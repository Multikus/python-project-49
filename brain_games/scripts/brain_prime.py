import prompt
from brain_games.engine.engine_game import welcome_user, winner_game, check_result
from brain_games.engine.prime_game import prime_game


def brain_prime(name):
    prime_game()


def main():
    print('Welcome to the Brain Games!')
    text, name = welcome_user()
    print(text)
    print('What number is missing in the progression?')
    brain_prime(name)


if __name__ == 'main':
    main()

