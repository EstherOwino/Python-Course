import math

#Exercise 1: Calculate the area of a rectangle
length = 10
width = 20
area = length * width
print(f"The area of the rectangle is {area}")

#prompt the user to enter the length and width
#The input in the terminal is always a string and hence it has to be converted to a integer
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area of rectangle is {area} cm2")

#Exercise 2: Create a shopping Cart Program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: Ksh{total}")

#Exercise 3: Calculate the circumference of a circle
#Circumference = PI * D
radius = float(input("Enter your radius: "))
circumference = math.pi * (radius * 2)
print(f"The circumference of the circle is: {round(circumference, 2)}cm")

#Exercise 4: Calculate the area of a circle
#Area = PI * r * r
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm2")

#Exercise 5: Finding the hypotenus of a right triangle
# c = squareroot of (a^2 + b^2)
a = float(input("Enter the value of a: "))
b  = float(input("Enter the value of b: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenus of the triangle is: {c}")