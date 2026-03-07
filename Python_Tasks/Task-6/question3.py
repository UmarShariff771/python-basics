# Problem 3 : Vehicle Rental
# Create a base class Vehicle with attributes like model, rental_rate, and a method calculate_rental().
# Inherit from this class to create subclasses Car, Bike, and Truck. Each subclass should have specific
# attributes and calculations for rental rates. Implement polymorphism to calculate the rental cost of
# different vehicles based on their type and rental duration.

# Base class for all vehicles
# It stores common details like model name and rental rate
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    # This method will be different for each vehicle type
    # so it will be overridden in the subclasses
    def calculate_rental(self, days):
        pass


# Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, model, rental_rate, seats):
        super().__init__(model, rental_rate)
        self.seats = seats

    # rental calculation for car
    # cost depends on number of days and a small charge based on seats
    def calculate_rental(self, days):
        rental = days * self.rental_rate + (self.seats * 2)
        return rental


# Bike class inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, model, rental_rate, engine_cc):
        super().__init__(model, rental_rate)
        self.engine_cc = engine_cc

    # rental calculation for bike
    # engine size slightly affects the rental cost
    def calculate_rental(self, days):
        rental = days * (self.rental_rate + self.engine_cc * 0.5)
        return rental


# Truck class inherits from Vehicle
class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity

    # rental calculation for truck
    # larger trucks cost more because of higher load capacity
    def calculate_rental(self, days):
        rental = days * self.rental_rate + (self.load_capacity * 0.5)
        return rental


# Creating objects for each type of vehicle
vehicle_1 = Car("Ford Dodge Charger", 5000, 4)
vehicle_2 = Bike("Triumph Thruxton 400", 2000, 400)
vehicle_3 = Truck("Ashok Leyland truck", 10000, 3000)

# storing all vehicles in a list
vehicles = [
    vehicle_1,
    vehicle_2,
    vehicle_3
]

# looping each vehicle and calculate rental cost for 3 days
for v in vehicles:
    print(v.model, "Rental cost:", v.calculate_rental(3))
