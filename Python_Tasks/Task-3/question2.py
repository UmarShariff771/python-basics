# 2. Word Scramble
#Concept: The player has to unscramble a jumbled word  from the words given in a list format as:-

# Key Elements
# String Manipulations: Scramble and Unscramble words.
# Conditions: Check if the player's guess matches the original word.
# Loops: Allow multiple attempts to guess the words.

import random

words = ["python", "javascript", "java", "automation", "pytest", "guvi", "selenium"]

# Get a random word
randomWord = random.choice(words)
# Convert the string into a list of characters and scramble it
scrambledArray = random.sample(randomWord, len(randomWord))
# Join the scrambled characters to String
scrambledWord = "".join(scrambledArray)
print(scrambledWord)

# Guess the word until its correct
while True:
    guessedWord = str(input("Guess the scrambled word....")).lower()
    if(guessedWord == randomWord):
        print("You guessed the scrambled word! " + str(guessedWord))
        break
    else:
        print("The guessed word " + str(guessedWord) + " is wrong, try again")