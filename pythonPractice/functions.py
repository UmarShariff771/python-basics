# Closure function

# def outer():
#     greet = "Good Morning"
#     def inner():
#         print(greet)
#     return inner()
#
# func = outer()
#
# print(type(func))
###################################################
# closure function with parameters
# def multiplier(x):
#     def multiply(y):
#         return x * y
#     return multiply
#
# double = multiplier(2)
# triple = multiplier(3)
#
# print(double(3))
# print(triple(3))
#
# print(type(double))


# Base price = 500, 300
# different discount rate = 0.1

# def discount(percent):
#     def applyDiscount(price):
#         price = price - (price * percent / 100)
#         return price
#     return applyDiscount
#
# diwaliDiscount = discount(30)
# newyearDiscount = discount(20)
#
# print("The diwali discount of 30 % is ", diwaliDiscount(1000))
# print("The christmas discount of 20 % is ", newyearDiscount(1000))

# loan = 500000
# interest = 8
# month = 18
#
# def interestRate(duration, rate):
#     def applyInterest(amount):
#         # annual interest
#         annualRate = rate / 100
#         monthlyInterest = annualRate / 12
#
#         interestAmount = (amount * duration * monthlyInterest / 100)
#         totalAmountPerMonth = amount + interestAmount
#         return totalAmountPerMonth
#     return applyInterest
#
# homeLoan = interestRate(month, interest)
# personalLoan = interestRate(12, 11)
#
# print("The emi for a loan amount of ", loan, " is ", homeLoan(loan), " with rate ", interest, "% for ", month, " months.")
# print("The emi for a personal load of 200000 is fixed is ", personalLoan(200000), " with 11% rate for 12 months fixed.")

################################################

# call back function

# def greet(name):
#     print("Hello, " + name + "!")
#
# def processUser(call):
#     call("John")
#
# processUser(greet)

def success():
    print("Payment is successful")

def fail():
    print("Payment failed")

def payment(status, successCB, failCB):
    if status:
        return successCB()
    else:
        return failCB()

payment(True, success, fail)

