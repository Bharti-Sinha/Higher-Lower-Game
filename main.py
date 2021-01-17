from art import logo, vs
from random import choice
from game_data import data
import os


def clear():
    return os.system('cls')


# select random insta account from game_data.py
def get_random_account():
    """Get data from random account"""
    return choice(data)


# check which insta account has more followers and return the account with highest followers.
def answer(first_account, second_account):
    """ Takes two randomly selected instagram followers
      and returns the insta account with highest followers
   """
    if first_account['follower_count'] > second_account['follower_count']:
        return 'a'
    else:
        return 'b'


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


print(logo)
a_account = get_random_account()


def game(a):
    end_of_game = False
    final_score = 0

    # repeat selecting b until the end of the game
    while not end_of_game:
        b = get_random_account()

        while a == b:
            b = get_random_account()

        print(f"Compare A: {format_data(a)}")
        # print(a["follower_count"])
        print(vs)
        print(f"Against B: {format_data(b)}")
        # print(b["follower_count"])
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)

        # check user's answer
        if user_guess == answer(a, b):
            final_score = final_score + 1
            print(f"You're right! Current score: {final_score}")
            a = b

        else:
            print(f"Sorry, that's wrong. Final score: {final_score}")
            end_of_game = True


game(a_account)
