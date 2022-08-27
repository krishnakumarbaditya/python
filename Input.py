# Assignment - 1
import math as m
# 1. write a python script to add two number(integers) taken from user through the keyboard.
x = int(input("Enter first number "))
y = int(input("Enter second number "))
z = x + y
print("Sum of two number is ", z)

# 2. write a python script to calculate area of circle,radius taken from user.
radius = int(input("Enter radius "))
area = m.pi*m.pow(radius, 2)
print("Area of the circle is ", area)

# 3. write a python script to calculate volume of a cuboid,dimensions(float value) taken from the user.
length = float(input("Enter length "))
width = float(input("Enter width "))
height = float(input("Enter height "))
vol = (length*width*height)
print("volume of cuboid is ", vol)

# 4. write a python script to calculate simple interest,data required should be taken from user.
principle = float(input("Enter the principle amount "))
rate = float(input("Enter the rate "))
time = float(input("Enter the time "))
SI = (principle*rate*time)/100
print("Simple Interest is ", SI)

# 5. write a python script to calculate square of a given number(number taken from user).
n = int(input("Enter a number "))
sq = m.pow(n, 2)
print("Square of a %d is " % n, sq)

# 6. write a python script to calculate area of triangle. Length of side are given by user.
base = float(input("Enter base "))
height = float(input("Enter height "))
area = (base * height)/2
print("Area of triangle is ", area)
