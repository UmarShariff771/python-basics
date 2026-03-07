# Problem 2: Employee Management
# Create a base class Employee with attributes like name, salary and a method calculate_salary(). Inherit
# from this class to create subclasses RegularEmployee, ContractEmployee, and Manager. Each subclass should
# have specific attributes and calculations for salary.
# Implement Inheritance and polymorphism to calculate the salary of different employee types based on their
# specific attributes and rules.

# Base Employee class
# This class contains common attributes like name and base salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # This method will be overridden by child classes
    def calculate_salary(self):
        pass


# Regular employee class inheriting from Employee
# Regular employees get an additional bonus added to their salary
class Regular_Employee(Employee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    # Calculate total salary including bonus
    def calculate_salary(self):
        total = self.salary + self.bonus
        return total


# Contract employee class inheriting from Employee
# Contractor share will be deducted from the salary
class Contract_Employee(Employee):
    def __init__(self, name, salary, contractor_share):
        super().__init__(name, salary)
        self.contractor_share = contractor_share

    # Calculate salary after deducting contractor share
    def calculate_salary(self):
        deduction = self.salary * (self.contractor_share / 100)
        total = self.salary - deduction
        return total


# Manager class inheriting from Employee
# Managers get an additional allowance
class Manager(Employee):
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance

    # Manager salary includes extra allowance
    def calculate_salary(self):
        total = self.salary + (self.allowance * 2)
        return total


# Create Employees
emp1 = Regular_Employee("John", 50000, 5000)
emp2 = Contract_Employee("Jacob", 40000, 10)
emp3 = Manager("Justin", 70000, 3000)

# Checking salary calculation individually
print(emp1.calculate_salary())
print(emp2.calculate_salary())
print(emp3.calculate_salary())

# Using polymorphism to calculate salary for all employees
employees = [emp1, emp2, emp3]

# looping each employee and their salaries
for emp in employees:
    print(emp.name, "Salary:", emp.calculate_salary())
