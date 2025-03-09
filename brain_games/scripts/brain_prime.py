import prompt
from brain_games.engine.engine_game import welcome_user, winner_game, check_result
from brain_games.engine.prime_game import prime_game


def brain_prime(name):
    game_score = 0
    game_over = False

    while game_score < 3:
        correct_answer, text_question = prime_game()
        print(text_question)

        user_response = prompt.string('Your answer: ').lower()

        check_num = correct_answer

        result = check_result(user_response, name, check_num)

        if result:
            game_score += 1
        else:
            game_over = True
            break
    winner_game(name)


def main():
    print('Welcome to the Brain Games!')
    text, name = welcome_user()
    print(text)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    brain_prime(name)


if __name__ == 'main':
    main()

