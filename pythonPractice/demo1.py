# a = 10
# b = 3
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)

# total_apples = 10
# people = 3
# print(total_apples % people)
#
# # Concatenate (+)
# text = "Python"
# city = "Chennai"
# name = "John"
# print(text + " is fun!")
# print(city + " is fun!")
# print(city +' '+ name + " is fun!")
#
# # print("Age is " + 25)
#
# print("Age is " + str(25))
#
# a = "Hello"
# b = "Word"
#
# print(a + " " + b)
#
# #Repetation
#
# text = "Hi "
# print(text * 3)

# slicing
# -6  -5  -4  -3  -2  -1    > Negative Index
#  P   Y   T   H   O   N
#  0   1   2   3   4   5     > Positive Index

# # Skipping steps
# text1 = "Python"
# # String[Start : end : step]
# print(text1[1::2])
#
# print(text1[::])
#
# text2 = "Welcome"
# print(text2[:3] + text2[4:])
#
# print(text2[::1])
# #print(text2[2:6:-1])
#
# myName = "Umar Shariff"
# reverseName = myName[::-1]
# print(reverseName)
#
# text = "I love Java"
# print(text)
# print(text.replace('Java','Python'))
#
# spaceWord = "  Hello world   "
# print(spaceWord.strip())
#
#
# #if - else
# age = int(input("Enter you age"))
#
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are an minor")
#

# raining = str(input("Is it Raining...?? "))
#
# if raining == "Yes":
#     print("Take an umbrella")
# else:
#     print("Enjoy sunshine")

# myName = "John"
#
# for i in range(0,len(myName)):
#     print(myName[i])

# import random
# words = ["apple", "banana", "cherry"]
#
# original_word = random.choice(words)
# scrambled_word = ''.join(random.sample(original_word, len(original_word)))
#
# print("world scramble game")
# print(scrambled_word)
#
# while True:
#     guess = input("Enter your guess: ").lower()
#
#     if guess == original_word:
#         print("Correct")
#         break
#     else:
#         print("Wrong")
#
#
#
#  import random
# # words = ["apple", "banana", "cherry"]
# #
# #
# # original_word = random.choice(words)
# # scrambled_word = ''.join(random.sample(original_word, len(original_word)))
# #
# # print("world scramble game")
# # print(scrambled_word)
# #
# # while True:
# #     guess = input("Enter your guess: ").lower()
# #
# #     if guess == original_word:
# #         print("Correct")
# #         break
# #     else:
# #         print("Wrong")
# # text = "Python is easy"
# # result = text.split(" ")
# # print(result)


# familyList = ["Paul", "Amanda", "James", "David", "John", "Russel", "Emily"]
# familyList.sort()
# print(familyList)

# marks = (90, 85, 90, 70)
# for i in range(len(marks)):
#     for j in range(i+1,len(marks)):
#         if marks[i] == marks[j]:
#             print(marks[i], "is duplicate")


movies = ('Inception', 'Avatar', 'Titanic', 'Avatar', 'Interstellar')
unique = []
for i in range(len(movies)):
    count = 0
    unique = movies[i]
    for j in range(i+1,len(movies)):
        if movies[i] == movies[j]:
            print(movies[i], "is duplicate")
            count = count + 1
