import prompt
from brain_games.engine.engine_game import get_random_number
from brain_games.engine.engine_game import welcome_user
from brain_games.engine.engine_game import wrong_game, winner_game, check_event_or_odd, check_result


def even_game(name):
    game_score = 0
    game_over = False

    while game_score < 3:
        number = get_random_number(1, 51)
        print(f'Question: {number}')

        user_response = prompt.string('Your answer: ').lower()
        check_num = check_event_or_odd(number)
        result = check_result(user_response, name, check_num)

        if result:
            game_score += 1
        else:
            game_score = 0
            game_over = True
            break

    if not game_over:
        winner_game(name)
    else:
        return


def main():
    print('Welcome to the Brain Games!')
    text, name = welcome_user()
    print(text)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(name)


if __name__ == 'main':
    main()
