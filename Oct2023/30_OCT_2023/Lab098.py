my_dict = {'a': 1, 'c': 2, 'b': 3}
# val = my_dict.pop('a')
# print(val)


# popitem() is used to remove and return an arbitrary key-value pair (as a tuple)
# from the dictionary.
val = type(my_dict.popitem())
print(val)
print(my_dict)

del my_dict

# print(my_dict)