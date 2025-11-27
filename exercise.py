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