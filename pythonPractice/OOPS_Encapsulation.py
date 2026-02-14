# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old")
#
# s1 = Student("Ketki",25)
# s2 = Student("Rahul", 19)
#
# s1.introduce()
# s2.introduce()

# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def showDetails(self):
#         print(f"The phone: {self.brand} has a price of {self.price}")
#
# mob1 = Mobile("Samsung", "45000")
# mob2 = Mobile("Apple", "95000")
#
# mob1.showDetails()
# mob2.showDetails()


# Static Method
# @staticmethod
# from operator import add
#
#
# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# result = MathUtils.add(5,3)
# print(result)

# Class method
# class Student:
#     school_name = "ABC School"
#     @classmethod
#     def change_school(cls, new_school):
#         cls.school_name = new_school
#
# s1 = Student()
# s2 = Student()
# print(s1.school_name)
# print(s2.school_name)
#
# Student.change_school("XYZ School")
# print(s1.school_name)
# print(s2.school_name)


# Instance method
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show_salary(self):
#         print(f"{self.name} earns {self.salary}")
#
# emp1 = Employee("Ketki", 5000)
# # # emp1.show_salary()

# instance : 1
# Class : Bank accout
# constructor : account holder , balance
# instance method : deposit amount > add money

class Bank_Account:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount

holder1 = Bank_Account("Raj", 1000)
holder1.deposit(5000)
print(f"The account holder {holder1.accountHolder} has balance of {holder1.balance}")
holder1.deposit(-2000)
print(f"The account holder {holder1.accountHolder} has balance of {holder1.balance}")

# 2nd :
# class variable Department Name : HR
# change the department
#
# Static method: (dont create object, call them directly by class name)
# class calclator
#     add
#     substract
#     multiply

class Organisation:

    Department = "HR"

    @classmethod
    def changeDepartment(self, newDepartment):
        self.Department = newDepartment
        print(f"The department changed to {self.Department}")

Organisation.changeDepartment("IT")