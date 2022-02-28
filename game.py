import random
import string

EASY_DIFF_LIVES = 20
MEDIUM_DIFF_LIVES = 10
HARD_DIFF_LIVES = 5

def main():
    # Introduction of game
    # Choose random letter (a-z)
    player = input("To begin the game, please enter your name: ")
    print("Hi " + player + ", " + "Welcome to Guess The Letter!")

    print("In order to win, guess the letter I'm thinking between a and z.")

    # letter = chr(random.randint(ord('a'), ord('z')))
    lower_letter = string.ascii_lowercase
    letter = random.choice(lower_letter)

    print(f"Answer is {letter}")

    lives = game_diff()