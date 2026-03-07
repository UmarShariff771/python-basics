from abc import ABC, abstractmethod
from pydoc import pager


#
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#
# class Car(Vehicle):
#     def start(self):
#         print("Car starts with key")
#
# c = Car()
# c.start()
#
#
# class Bike(Vehicle):
#     pass
# b= Bike()
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
# class CreditCard(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using credit card")
# class Upi(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Upi")
#
# p1 = CreditCard()
# p1.pay(100)
#
# p2 = Upi()
# p2.pay(100)


class MathUtils:
    def add(self, a, b, c=0):
        return a + b + c

m1 = MathUtils()
print(m1.add(1, 2))


class MathUtils:
    def add(a, b, c=0):
        return a + b + c


m1 = MathUtils()
print(m1.add(1, 2))


print(1+1)
print("1"+"1")