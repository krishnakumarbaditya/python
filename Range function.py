# 1.write a python script to print a table of 5.
# num = 5
# for i in range(1, 11):
#     num1 = num * i
#     print("%d * %d = %d" % (num, i, num1))
# 2.write a python script to print a table of user's choice.
# num = int(input("Enter the number by user "))
# for i in range(1, 11):
#     num1 = num * i
#     print("%d * %d = %d" % (num, i, num1))

# 3.write a python script to print all armstrong numbers under 1000.
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))
# for num in range(lower, upper + 1):
#     # order of number
#     order = len(str(num))
#     # initialize sum
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#     if num == sum:
#         print(num)

# 4.write a python script to print squares of numbers from a to b.Values of a and b are given by user.
# import math
#
# a = int(input("Enter the lower range "))
# b = int(input("Enter the upper range "))
# for num in range(a, b+1):
#     print(math.pow(num, 2))
"""5.write a python script to print a sequence of with given step size and boundary value.For example
boundary values are 10 and 30,step is 2 then your output should be 10,12,14,16,18,20,22,24,26,28,30."""
print("sequence of with given step size and boundary value.")
print("boundary values are 10 and 30,step is 2")
for num in range(10, 30+1, 2):
    print(num, end=" ")
