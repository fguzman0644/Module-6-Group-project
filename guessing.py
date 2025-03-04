#Fernando Guzman, Michael Calderon, Medina Kubanychbekova, Ariben Ballesteros

##Guessing program that based off the user's input tells them
##"guess higher", "guess lower", or "well done, you guessed it."

#import Module
import random

#Defining While Loop Variable
playAgain = True

#Introduce program to user and give directions.
print('''
    In this game you will have to try and guess the number randomly 
    by the program. If you guess wrong the program will give you a 
    hint. Your hint will be try to lower or higher depending on your guess.
    
''')

#While variable is true, program will keep running
while playAgain == True:
    #generate random number to be guessed
    random_int = random.randint(1,10)
    #Users guess
    user_guess = int(input("Guess a number between 1-10: "))
#while user hasnt guessed the right number it will give a hint and ask to try again
    while user_guess != random_int:
        if user_guess < random_int:
            user_guess = int(input("Incorrect, guess higher: "))
        elif user_guess > random_int:
            user_guess = int(input("Incorrect, guess lower: "))
    
    print("Well done, you guessed it.")
#ask user if to try again. 
    repeat = input("Would you like to guess a new number (Y/N)?").lower()
    if repeat != "y":
        playAgain = False
    elif repeat == "y":
        input("Press Any Key To Start Over...")
