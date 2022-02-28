import random
import string

EASY_DIFF_LIVES = 20
MEDIUM_DIFF_LIVES = 10
HARD_DIFF_LIVES = 5

# Function to check letter
def check_letter(turns, letter, lives):
    if turns > letter:
        print("Cold")
        return lives - 1
    elif turns < letter:
        print("Hot")
        return lives - 1
    else:
        print(f"You hit the spot! The letter was {letter}.")

# Function to set difficulty of game.
def game_diff():
    difficulty = input("Pick a difficulty for the game. Type 'easy', 'medium', or 'hard': ")

    if difficulty == "easy":
        return EASY_DIFF_LIVES
    elif difficulty == "medium":
        return MEDIUM_DIFF_LIVES
    else:
        return HARD_DIFF_LIVES

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