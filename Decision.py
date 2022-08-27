# Assignment-2
import math as m
# 1.Write a python script to check whether a given number is even or odd.
x = int(input("Enter a number "))
if x % 2 != 0:
    print("%d is odd" % x)
else:
    print("%d is even" % x)

# 2.Write a python script to check whether a given number is divisible by 5 or not.
a = int(input("Enter a number "))
if a % 5 == 0:
    print("%d is divisible by 5" % a)
else:
    print("%d is not divisible by 5" % a)

# 3.Write a python script to check whether a given number is positive negative or zero.
b = int(input("Enter a number "))
if b > 0:
    print("%d is positive" % b)
elif b < 0:
    print("%d is negative" % b)
else:
    print("%d is zero" % b)

# 4.Write a python script to find greatest among three numbers.
a = int(input("Enter first number "))
b = int(input("Enter second number "))
c = int(input("Enter third number "))
if a>b:
    if a>c:
        print("%d is greater" % a)
    else:
        print("%d is greater" % c)
elif b>c:
    print("%d is greater" % b)
else:
    print("%d is greater" % c)

# 5.Write a python script to check if a year is Leap year or not.
year = int(input("Enter the year "))
if year % 100 == 0:
    if year % 400 == 0:
        print("%d is Leap Year" % year)
    else:
        print("%d is not a Leap Year" % year)
elif year % 4 == 0:
    print("%d is Leap Year" % year)
else:
    print("%d is not a Leap Year" % year)

# 6.Write a python script to take month value in numeric format and display the number of days in it.
month = int(input("Enter the month number "))
if month == 1:
    print("no of days 31")
elif month == 2:
    print("no of days 28")
elif month == 3:
    print("no of days 31")
elif month == 4:
    print("no of days 30")
elif month == 5:
    print("no of days 31")
elif month == 6:
    print("no of days 30")
elif month == 7:
    print("no of days 31")
elif month == 8:
    print("no of days 31")
elif month == 9:
    print("no of days 30")
elif month == 10:
    print("no of days 31")
elif month == 11:
    print("no of days 30")
else:
    print("no of days 31")

# 7.Write a python script to check nature of roots of a given quadratic equation.
a = int(input("enter the first number "))
b = int(input("enter the second number "))
c = int(input("enter the third number "))
D = (m.pow(b, 2)-4*a*c)
if D > 0:
    print("Real and Distinct Root")
elif D < 0:
    print("Imaginary Root")
else:
    print("Equal Root")

# 8.Write a python script to print a set of three words in Dictionary Order. Words are given by the user.
print("enter three city name")
a, b, c = input(), input(), input()
if a < b < c:
    print(a, b, c)
elif a < c < b:
    print(a, c, b)
elif b < a < c:
    print(b, a, c)
elif b < c < a:
    print(b, c, a)
elif c < a < b:
    print(c, a, b)
else:
    print(c, b, a)

# 9.Write a python script to accept one complex number from user and display the greater number between real part and imaginary part.
print("enter one complex Number ")
a = int(input())
b = int(input())
cn = complex(a, b)
if cn.real > cn.imag:
    print("Real part is bigger")
else:
    print("Imaginary part is bigger")

""" 
10.Write a python script to accept marks of five subjects from user(assuming maximum marks is 100).
Display student's result as Pass or Fail.If student is pass then also display his percentage and division.
"""
Hin = int(input("Hindi marks "))
Eng = int(input("English marks "))
Math = int(input("Math marks "))
Sci = int(input("Science marks "))
His = int(input("History marks "))
Result = (Hin+Eng+Math+Sci+His)/5
if Result > 90:
    print("Percentage is %d and Division is O" % Result)
elif Result > 80 and Result <= 90:
    print("Student is Pass")
    print("Percentage is %d and Division is E" % Result)
elif Result > 70 and Result <= 80:
    print("Student is Pass")
    print("Percentage is %d and Division is A+" % Result)
elif Result > 60 and Result <= 70:
    print("Student is Pass")
    print("Percentage is %d and Division is A" % Result)
elif Result > 50 and Result <= 60:
    print("Student is Pass")
    print("Percentage is %d and Division is B+" % Result)
elif Result > 40 and Result <=50:
    print("Student is Pass")
    print("Percentage is %d and Division is B" % Result)
else:
    print("Student is Fail")
    print("Percentage is %d and Grade is C" % Result)
