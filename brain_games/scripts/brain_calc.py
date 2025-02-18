import prompt

from brain_games.engine.engine_game import welcome_user, check_result, winner_game, wrong_game
from brain_games.engine.calc_game import calc


def brain_calc(name):
    game_score = 0

    while game_score < 3:
        correct_answer, text_question = calc()
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
    print('What is the result of the expression?')
    brain_calc(name)


if __name__ == 'main':
    main()
