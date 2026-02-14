# # Single Inheritance
# # one parent > one child
# # father > child
# class Animal:
#     def speak(self):
#         print("Animal Speak")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog bark")
#
# d = Dog()
# d.speak()
# d.bark()

# Multiple Inheritance
# one child > multiple parents
# class Father:
#     def skills(self):
#         print("Gardening")
# class Mother:
#     def talent(self):
#         print("Swimming")
#
# class Child(Father, Mother):
#     pass
#
# c = Child()
# c.skills()
# c.talent()
# Multilevel Inheritance
#
# Grandfather > Father > Son
class Grandparent:
    def property(self):
        print("Land")

class Parent(Grandparent):
    def house(self):
        print("House")

class Child(Parent):
    def car(self):
        print("Car")

c = Child()
c.property()
c.house()
c.car()