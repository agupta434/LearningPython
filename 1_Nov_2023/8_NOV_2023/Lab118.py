# Public - Variable - Don't Mention anything
# Protected - _
# Private - __

# Variable and Function


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        # print("You details", self.__name, self.__age)

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if name == "John":
            print("Don't set the name")
        else:
            self.__name = name

    def print_details(self):
        print("You details", self.__name, self.__age)


person = Person("laddoo", 34) # It will call the  __init__ with name,age
person.print_details()
# person.__init__("promod", 50) # donot call directly __init__
# print(person.__name) # Private ?

# How to change it Get and Set ?
# Fetch - Get
# Set the value  - Constuctor
# name = person.get_name()
# print(name)

person.set_name("John")
person.set_name("ssssamit")

name = person.get_name()
print(name)

person.print_details()



