from brain_games.engine.engine_game import welcome_user


def brain_gcd(name):

    print('Hello brain_gcd')


def main():
    print('Welcome to the Brain Games!')
    text, name = welcome_user()
    print(text)
    print('What is the result of the expression?')
    brain_gcd(name)


if __name__ == 'main':
    main()
