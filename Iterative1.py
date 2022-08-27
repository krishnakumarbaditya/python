# Assignment -3
# 1.write a python script to print first 10 natural numbers.
print("print first 10 natural numbers.")
n = 1
while n <= 10:
    print(n)
    n += 1
print()

# 2.write a python script to print first 10 natural numbers in reverse order.
print("print first 10 natural numbers in reverse order.")
n = 10
while n >= 1:
    print(n)
    n -= 1
print()

# 3.write a python script to print first 10 odd natural numbers.
print("print first 10 odd natural numbers.")
n = 1
while n <= 10:
    print(n*2-1)
    n = n + 1
print()

# 4.write a python script to print first 10 even natural numbers.
print("print first 10 even natural numbers.")
n = 1
while n <= 10:
    print(n*2)
    n = n + 1
print()

# 5.write a python script to print first N natural numbers.Value of N is taken from user.
print("print first N natural numbers.Value of N is taken from user.")
num = int(input("Enter the number "))
i = 1
while i <= num:
    print(i)
    i += 1
print()

# 6.write a python script to print first N natural numbers in reverse order.Value of N is taken from user.
print("print first N natural numbers in reverse order.Value of N is taken from user.")
num = int(input("Enter the number "))
i = 1
while num >= 1:
    print(num)
    num -= 1
print()


# 7.write a python script to calculate sum of first N natural numbers.Value of N is taken from user.
print("calculate sum of first N natural numbers.Value of N is taken from user.")
num = int(input("Enter the number "))
i = 1
sum = 0
while i <= num:
    sum = sum + i
    i += 1
print("sum of first %d natural number is " % num, sum)
print()

# 8.write a python script to calculate sum of first N odd natural numbers.Value of N is taken from user.
print("calculate sum of first N odd natural numbers.Value of N is taken from user.")
num = int(input("Enter the number "))
i = 1
sum = 0
while i <= num:
    sum = sum + i*2-1
    i += 1
print("sum of first %d odd number is " % num, sum)
print()


# 9.write a python script to calculate factorial of a  number.Number is taken from user.
print("calculate factorial of a  number.Number is taken from user.")
num = int(input("Enter the number "))
i = 1
fact = 1
while i <= num:
    fact = fact*i
    i += 1
print("factorial of %d is " % num, fact)
print()

# 10.write a python script to calculate product of first N odd natural numbers.Value of N is taken from user.
print("product of first N odd natural numbers.Value of N is taken from user.")
num = int(input("Enter the number "))
i = 1
product = 1
while i <= num:
    product = product * (i*2-1)
    i += 1
print("Product of first %d odd number is " % num, product)
