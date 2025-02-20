import prompt

from brain_games.engine.engine_game import welcome_user, winner_game, check_result
from brain_games.engine.gcd_game import gcd_game


def brain_gcd(name):
    game_score = 0

    while game_score < 3:
        correct_answer, text_question = gcd_game()
        print(text_question)

        user_response = int(prompt.string('Your answer: ').lower())

        check_num = int(correct_answer)

        result = check_result(user_response, name, check_num)

        if result:
            game_score += 1
        else:
            game_score = 0
    winner_game(name)


def main():
    print('Welcome to the Brain Games!')
    text, name = welcome_user()
    print(text)
    print('Find the greatest common divisor of given numbers.')
    brain_gcd(name)


if __name__ == 'main':
    main()
