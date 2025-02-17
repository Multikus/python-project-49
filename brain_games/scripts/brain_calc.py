import prompt

from brain_games.engine.engine_game import welcome_user, check_result, winner_game
from brain_games.engine.calc_game import calc


def brain_calc(name):
    game_score = 0

    while game_score < 3:
        correct_answer, text_question = calc()
        print(text_question)
        user_response = prompt.string('Your answer: ').lower()

        check_num = correct_answer
        check_result(game_score, user_response, name, check_num)

    winner_game(name)


def main():
    print('Welcome to the Brain Games!')
    text, name = welcome_user()
    print(text)
    print('What is the result of the expression?')
    brain_calc(name)


if __name__ == 'main':
    main()
