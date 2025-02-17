import prompt
import operator
from random import randint, choice


def welcome_user():
    name = prompt.string('May I have your name? ')
    welcome_text = f'Hello, {name}'

    return welcome_text, name


def wrong_game(user_response, correct_answer, user_name):
    print(f"'{user_response}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")


def winner_game(name):
    print(f'Congratulations, {name}!')


def get_random_number():
    number = randint(1, 50)
    return number


def get_random_operation():
    operation_selection = ['+', '-', '*']
    operation = choice(operation_selection)
    print(operation)

    if operation == '+':
        math_operator = operator.add
        return math_operator, operation
    elif operation == '-':
        math_operator = operator.sub
        return math_operator, operation
    elif operation == '*':
        math_operator = operator.mul
        return math_operator, operation


def check_event_or_odd(number):

    if number % 2 == 0:
        return 'yes'
    return 'no'


def check_result(score, user_resp, name, corr_response):

    correct_response = corr_response
    if user_resp == correct_response:
        score += 1
        print('Correct!')
    else:
        wrong_game(user_resp, correct_response, name)
        score = 0


def text_player_question(num1, rnd_operation, num2):
    question_text = f'Question: {num1} {rnd_operation} {num2}'
    return question_text
