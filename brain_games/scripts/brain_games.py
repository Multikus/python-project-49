from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    text = welcome_user()
    print(text)


if __name__ == 'main':
    main()
