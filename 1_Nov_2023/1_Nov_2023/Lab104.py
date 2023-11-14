numbers = (1, -2, -3, -4, 5, 16, -7, 8, -9, 10)

def square(x):
    return x ** 2

squared_numbers = filter(square, numbers)
print(squared_numbers)
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)

for result in squared_numbers_list:
    print(result)


# def is_positive(num):
#     return num > 0
# pos_numbers = filter(is_positive, numbers)
# print(pos_numbers)
# pov_numbers_list = list(pos_numbers)
# print(pov_numbers_list)
