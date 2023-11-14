# List is Mutable, Its content can be changed!
my_list = [1, 2, 3, 4, 5, 5]
my_list1 = list([9])
print(my_list1)
print(type(my_list1))
print(my_list)
my_list[1] = 20
print(my_list)
print(type(my_list))

# Tuple - It is immutable in nature. - No modification
car = ("Ford GT", "Raptor", "Lambo", "Lambo")
car1 = (True,)
car2 = ("Ford GT", True, "Lambo")

print("------------------")

car3= list(car)
print(car3)
print(type(car3))
print("------------------------------")
print(type(car1))
car3[1]= "maruti"
print(car3)
car4= tuple(car3)
print("car4", car4)
print(type(car4))
print(car)
print(type(car))
# car[1] = "XUV 500"

print(len(car))

# Tuple (), Its content can't be changed, List [] and it content can be changed!

# List can be converted

list1 = [1, 2, 3, 4, 5, 6]
print(tuple(list1))



