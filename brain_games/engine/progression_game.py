from brain_games.engine.engine_game import get_random_number, text_player_question


def progression_game():
    rnd_step = get_random_number(1, 9)
    print('rnd_step ', rnd_step)
    rnd_len_list = get_random_number(30, 150)

    rnd_list = []

    for i in range(1, rnd_len_list, rnd_step):
        rnd_list.append(i)

    dott = get_random_number(0, len(rnd_list) - 1)
    rnd_list.pop(dott)
    rnd_list.insert(dott, '..')
    rnd_list = ', '.join(map(str, rnd_list))
    player_question = text_player_question(rnd_list)

    return rnd_step, player_question
