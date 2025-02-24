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


def get_random_number(num1, num2):
    number = randint(num1, num2)
    return number


def get_random_operation():
    operation_selection = ['+', '-', '*']
    operation = choice(operation_selection)

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


def check_result(user_resp, name, corr_response):

    correct_response = corr_response
    if user_resp == correct_response:
        print('Correct!')
        return True
    else:
        wrong_game(user_resp, correct_response, name)
        return False


def text_player_question_calc_game(num1, rnd_operation, num2):
    question_text = f'Question: {num1} {rnd_operation} {num2}'
    return question_text


def text_player_question(num1, num2=None):
    if num2 is None:
        question_text = f'Question: {num1}'
    else:
        question_text = f'Question: {num1} {num2}'
    return question_text
