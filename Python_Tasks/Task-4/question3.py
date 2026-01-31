# 3. Given a python list [10, 501, 22, 37, 100, 999, 87, 351]
# Find out how many numbers are there in the given python list which are Happy numbers
import math

numberList = [10, 501, 22, 37, 100, 999, 87, 351]
happyNumbers = []

for number in numberList:
    orginal = number

    while number != 1 and number != 4:
        sum = 0
        while number > 0 :
            num = number % 10
            sum += num * num
            number = number // 10

        number = sum

    if number == 1:
        happyNumbers.append(orginal)

print(happyNumbers)