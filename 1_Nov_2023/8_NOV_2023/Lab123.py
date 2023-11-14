# Hierarchical Inheritance:
class Vehicle:
    def info1(self):
        return "This is a vehicle."
    def info(self):
        return "This is a vehicle."


class Car(Vehicle):
    def info(self):
        return "This is a car."


class Bicycle(Vehicle):
    def info(self):
        return "This is a bicycle."


car = Car()
bicycle = Bicycle()
print(car.info())
print(bicycle.info())
print(bicycle.info1())
print(car.info1())
