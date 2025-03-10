from brain_games.engine.engine_game import get_random_operation, get_random_number, text_player_question_calc_game


def calc():
    a = get_random_number(1, 20)
    b = get_random_number(1, 20)
    math_operator, operation = get_random_operation()
    correct_answer = math_operator(a, b)

    player_question = text_player_question_calc_game(a, operation, b)

    return correct_answer, player_question
