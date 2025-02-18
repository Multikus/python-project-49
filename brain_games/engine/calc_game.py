from brain_games.engine.engine_game import get_random_operation, get_random_number, text_player_question


def calc():
    a = get_random_number()
    b = get_random_number()
    math_operator, operation = get_random_operation()
    correct_answer = math_operator(a, b)

    player_question = text_player_question(a, operation, b)

    return correct_answer, player_question
