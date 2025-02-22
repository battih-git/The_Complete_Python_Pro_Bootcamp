

from art import logo, vs
import random
from game_data import data

def format_data(record):
    """Prints the record from the dictionary in correct format"""
    name = record['name']
    description = record['description']
    country = record['country']
    return f"{name}, a {description}, from {country}"

def check_answer(case_1, case_2, user_input):
    """Returns bool whether user gave the correct answer"""
    if case_1['follower_count'] > case_2['follower_count']:
        return user_input == 'a'
    else:
        return user_input == 'b'


print(logo)

game_continue = True
case_b = random.choice(data)
score = 0
while game_continue:
    case_a = case_b
    case_b = random.choice(data)
    while case_a == case_b:
        case_b = random.choice(data)
    print(f"Compare A: {format_data(case_a)}")
    print(vs)
    print(f"Against B: {format_data(case_b)}")
    user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    user_won = check_answer(case_a,case_b,user_ans)
    if user_won:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
