# 4. Write a python program to find the sum of the first and last digit of an integer

# Getting the number from the user input
givenNumber = int(input("Enter the number to find the sum of first and last digit..."))

# Adding the first and last numbers of the given number in a function
def sumDigits(number):
    # Converted the number as string
    numberAsString = str(number)
    # Getting the first and last char of the string as number
    firstDigit = numberAsString[0]
    lastDigit = numberAsString[-1]
    # returning the sum of two numbers as int
    return int(firstDigit) + int(lastDigit)

print(sumDigits(givenNumber))