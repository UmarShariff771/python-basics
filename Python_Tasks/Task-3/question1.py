# 1. Guess the Number
# Concept: The computer randomly selects a number within a range, and the player has to guess it
# Key Elements:
# Variables: Store the random number and the player guess.
# Conditions: Check if the guess is too high, too low or correct.
# Loops: Allow multiple guesses until the correct number is found.

import  random

# Prompt the user to define the range
min_val = int(input("Enter your minimum number "))
max_val = int(input("Enter your maximum number "))

# Function to generate a random number within the specified range
def randomNumber(minVal, maxVal):
    randomNumber = random.randint(minVal, maxVal)
    return randomNumber

# Generate and store the random number
random_Number = randomNumber(min_val, max_val)
print("Generated Random number is " + str(random_Number))

# Loop until the player provides the correct guess
while True:
    guess = int(input("Enter your guess...."))
    if guess == random_Number:
        print("The guessed number is correct " + str(guess))
        break
    else:
        print("The guessed number " + str(guess) + " is wrong, please try again")