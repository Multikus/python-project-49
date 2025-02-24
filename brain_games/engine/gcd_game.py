from brain_games.engine.engine_game import get_random_number, text_player_question


def gcd_game():

    b = get_random_number(1, 51)
    a = get_random_number(1, 51)
    min_num = min(a, b)

    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            print('response > ', i)
            player_question = text_player_question(a, b)
            return i, player_question
    player_question = text_player_question(a, b)
    return 1, player_question
