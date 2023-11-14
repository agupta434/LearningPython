class Car:
    name = "hi" # Class Varaible

    def __init__(self): # Default con
        # self.make = make  #  Instance Vairable
        # self.model = model # Instance Vairable
        print("I will be called first")

    def start_engine(self, make, model):
        self.make = make  # Instance Vairable
        self.model = model  # Instance Vairable
        print("Starting a car", )
    def stopcar(self):
        print("stop a car", self.name, self.make, self.model)


car1 = Car()
car2 = Car()
print(car1.name)
car1.name = "Amit"
car2.name = "Promod"

car1.start_engine("kia", 2003)
car2.start_engine("ford", 2000)
car1.stopcar()
car2.stopcar()
print(id(car1))
print(id(car2))


# Object is created a Special Function is called automatically __int__()
# All the attribute Object you can initilize - add some initial value to them