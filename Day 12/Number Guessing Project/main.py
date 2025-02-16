import random

import art


def check_guess(u_guess, c_guess):
    if u_guess > c_guess:
        print("Too High.")
    elif u_guess < c_guess:
        print("Too Low.")
    elif u_guess == c_guess:
        print(f"You got it! The answer was {u_guess}")

def check_difficulty_level(level):
    if level.lower() == 'hard':
        return 5
    elif level.lower() == 'easy':
        return 10

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty_level = input("Choose the difficulty level. Type 'easy' or 'hard': ")
    random_number = random.randint(1,100)
    attempts = check_difficulty_level(difficulty_level)
    guess_number = -1
    while guess_number != random_number:
        print(f"You have {attempts} remaining to guess the number. ")
        guess_number = int(input("Make a guess: "))
        check_guess(guess_number,random_number)
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            print(f"The correct answer is {random_number}")
            return
        elif guess_number != random_number:
            print("Guess again.")


game()