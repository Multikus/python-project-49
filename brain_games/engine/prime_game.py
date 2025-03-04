from brain_games.engine.engine_game import get_random_number, text_player_question


def prime_game():
    n = get_random_number(1, 51)
    player_question = text_player_question(n)

    negative_response = 'no'
    positive_response = 'yes'

    if n < 2:
        return negative_response, player_question

    for i in range(2, n):
        if n % i == 0:
            return negative_response, player_question

    return positive_response, player_question
