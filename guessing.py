#Fernando Guzman

##Guessing program that based off the user's input tells them
##"guess higher", "guess lower", or "well done, you guessed it."

import random

while True:
    random_int = random.randint(1,10)
    user_guess = int(input("Guess a number between 1-10: "))

    while user_guess != random_int:
        if user_guess < random_int:
            user_guess = int(input("Incorrect, guess higher."))
        elif user_guess > random_int:
            user_guess = input(input("Incorrect, guess lower."))
    
    print("Well done, you guessed it.")
    repeat = str(input("Would you like to guess a new number (Y/N)?"))
    if repeat != "Y":
        break
