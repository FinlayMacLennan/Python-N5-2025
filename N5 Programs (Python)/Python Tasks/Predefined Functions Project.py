# PROJECT

#From the code starter provided above, create a word guessing game that gives the user five turns to guess the secret word. 
#Their score is then displayed.

import random

words = ["python", "function", "random", "length", "computer", "program", "variable"]

secret_word = random.choice(words)

guess = input("Guess the word")

if guess == secret_word:
    print("Well Done you have guesses the word")
    socre == len(secret_word)

elif guess != secret_word:
    print("try again that is not the right word")