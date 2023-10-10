# Develop a program. Take input 5 times including 1-2 duplicate and print it.
c = []

for i in range(1,6):
    a=input("Enter your number:\t")
    c.append(a)

d=set(c)
e=list(c)
print(d)
print(e)


#option 2
n = input("enter first no\t")
n1 = input("enter second no\t")
n2 = input("enter third no\t")
n3 = input("enter fourth no\t")
n4 = input("enter fifth no\t")

set={n, n1, n2, n3, n4}

print(set)