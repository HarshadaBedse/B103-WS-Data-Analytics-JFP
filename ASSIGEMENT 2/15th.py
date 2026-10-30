import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number (1-10): "))

        if guess == number:
            print("Correct Guess!")
            break
        else:
            print("Wrong Guess! Try again.")

guessing_game()


""" Guess a number (1-10): 3
Wrong Guess! Try again."""