# Assignment - 4
# 1.Write a python script to check weather a given number is prime or not.
# x = int(input("Enter a number "))
# for y in range(2, x):
#     if x % y == 0:
#         break
# if x == y+1:
#     print(x, "is a prime number.")
# else:
#     print(x, "is not a prime number.")

# 2.Write a python script to print next prime number of a given number.
# x = int(input("Enter a number "))
# x = x+1
# while x > x-1:
#     for y in range(2, x):
#         if x % y == 0:
#             break
#     if x == y + 1:
#         break
#     x += 1
# if x == y+1:
#     print("Next prime number is .", x)

# 3.Write a python script to print first N prime number.Value of N is given by user.
# n = int(input("Enter a number : "))
# c = 2
# while n != 0:
#   for i in range(2, c):
#     if c % i == 0:
#       break
#   else:
#     print(c, end=" ")
#     n -= 1
#   c += 1
# 4.Write a python script to print all prime numbers between two given numbers.
# lower_value = int(input("Please, Enter the Lowest Range Value: "))
# upper_value = int(input("Please, Enter the Upper Range Value: "))
#
# print("The Prime Numbers in the range are: ")
# for number in range(lower_value, upper_value):
#     count = 0
#     for i in range(2, number):
#         if number % i == 0:
#             count = count + 1
#             break
#
#     if count == 0 and number != 1:
#         print(" %d" % number, end='  ')

# 5.Write a python script to check weather two given numbers are co-prime or not.
# x = int(input("Enter 1st number"))
# y = int(input("Enter 2nd number"))
# i=0
# m = min(x, y)
# for i in range(2, m):
#     if x % i == 0 and y % i == 0:
#         break
# if i+1 == m:
#     print("coprime")
# else:
#     print("not a coprime")
# 6.Write a python script to print first N odd natural numbers in reverse order using range function in for loop.
# a = int(input("Enter the range "))
# print("first N odd natural numbers in reverse order")
# for i in range(a, 0, -1):
#     odd = i*2-1
#     print(odd)
# 7.Write a python script to print first N even natural numbers in reverse order using range function in for loop.
# a = int(input("Enter the range "))
# print("first N even natural numbers in reverse order")
# for i in range(a, 0, -1):
#     even = i*2
#     print(even)
# 8.Write a python script to print all prime factors of a given number.
# num = int(input("Enter the Number : "))
# for i in range(2, (num+1)):
#     while num % i == 0:
#         print(i)
#         num = num/2

# 9.Write a python script to calculate LCM of two numbers.
# num = int(input("Enter First Number : "))
# num1 = int(input("Enter Second Number : "))
# maximum = max(num, num1)
# while True:
#     if maximum % num == 0 and maximum % num1 == 0:
#         print("Lcm is", maximum)
#         break
#     maximum += 1
# 10.Write a python script to calculate HCF of two numbers.
num = int(input("Enter First Number : "))
num1 = int(input("Enter Second Number : "))
minimum = min(num, num1)
while True:
    if num % minimum == 0 and num1 % minimum == 0:
        print("Hcf is", minimum)
        break
    minimum -= 1
