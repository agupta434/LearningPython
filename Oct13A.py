# write a program to calculate the area of circle
# import math
# radius = float(input("Enter the radius:\n"))
#
# area = math.pi*(radius**2)
# print(area)

# WRITE PROGRAM TO COMPARE  NUMBER

# num1 = int(input("Enter the int no\n"))
# num2 = int(input("Enter the int no\n"))
# result = "greater than" if num1 > num2 else "less than" if num1 < num2 else "equal to"
# print(f" {num1} is {result} {num2}")

# Find maximum number using ternary operator
numb1 = float(input("Enter the first no\n"))
numb2 = float(input("Enter the second no\n"))
numb3 = float(input("Enter the third no\n"))

max_number = numb1 if (numb1 > numb2 and numb1 > numb3) else (numb2 if numb2>numb3 else numb3)
print(f"The maximum of {numb1}, {numb2} and {numb3} is: {max_number}")