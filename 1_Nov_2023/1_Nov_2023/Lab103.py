numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]

# num%2==0
# even_numbers = [2, 4, 6, 8, 10]


# def greet(z):
#     print("hello",10)
#     return "Hello", 10
# greet(2)
# op=greet(2)
# print(type(op))
#
# def minimum(first, second):
#     if (first < second):
#         return first
#     return second
# op1=minimum(25,6)
# print(op1)




# filter -> Number element can be less or equal the list

def is_even(num):
    return num % 2 == 0

op1= is_even(10)
print(op1)


# Mod
# 2| 10 | 5
#    10
#    ---
#    0

even_numbers = filter(is_even, numbers)
even_numbers1 = map(is_even, numbers)
print(even_numbers)
print(even_numbers1)
even_numbers_list = list(even_numbers)
even_numbers_list1 = list(even_numbers1)
print(even_numbers_list)
print(even_numbers_list1)