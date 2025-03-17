# PROJECT

#From the code starter provided above, create a word guessing game that gives the user five turns to guess the secret word. 
#Their score is then displayed.
#The score for guessing correctly is the number of letters in the secret word divided by the number of turns taken to guess it, 
#rounded to 1 decimal place. They score 0 if they run out of turns.

import random

words = ["python", "function", "random", "length", "computer", "program", "variable"]

secret_word = random.choice(words)
