# 3. Given a python list [10, 501, 22, 37, 100, 999, 87, 351]
# Find out how many numbers are there in the given python list which are Happy numbers
import math

numberList = [10, 501, 22, 37, 100, 999, 87, 351]
happyNumbers = []

# Iterating the number list
for number in numberList:
    # Storing the number as original
    orginal = number

    # Checking the condition if the sum of number should not make 1 or 4
    # since 1 is the happy number
    # and 4 is an infinite looping which never ends as per happy numbers
    while number != 1 and number != 4:
        # declaring the sum as zero
        sum = 0
        # Iterate until the number is greater than zero
        while number > 0 :
            # Getting the last character of the number
            num = number % 10
            # Multiplying the number itself
            sum += num * num
            # removing the last character which was processed before
            number = number // 10
        # storing the sum of num * num into the number to iterate again
        number = sum
    # If the number becomes 1 then happy
    if number == 1:
        happyNumbers.append(orginal)

print(happyNumbers)