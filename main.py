#This is my first Python program
print('I love chips!')
print("It's really good!")

#a variable is a container for a value

#strings
first_name = 'Esther'
food="chips"
email='essyachieng005@gmail.com'

print(first_name)
# f means format
print(f"Hello {first_name}")
print(f"You love {food}")
print(f"{first_name} your email is {email}")
print(f"Your email is {email}")

#integers
age = 20
quantity = 3
num_of_students = 91
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#floats
price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is Ksh {price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")

#Boolean
is_student = True
for_sale = True
is_online = True
print(f"Are you a student? {is_student}")

if is_student:
  print("You are a student")
else:
  print("You are NOT a student")

if for_sale:
  print("That item is for sale")
else:
  print("That item is not available for sale")

if is_online:
  print("You are online")
else:
  print("You are offline")

user_name = "Esther Achieng'"
year = 2025
pi = 3.14
is_admin = True

print(f"{user_name}")
print(f"{year}")
print(f"{pi}")
print(f"{is_admin}")

# Typecasting = the process of converting a variable from one data type to another
# Typecast functions include str(), int(), float() and bool()

name = "Esther Achieng' Owino"
age = 20
gpa = 10.9
is_still_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_still_student))

gpa = int(gpa)
print(gpa)

is_still_student = int(is_still_student)
print(is_still_student)

name = bool(name)
print(name)

if name:
  print("Correct! Name has been entered correctly")
else:
  print("Error! Please enter your name again please!")

age = float(age)
print(age)

age = str(age)
print(age)
print(type(age))

age += "1"
print(age)

#input() = A function that prompts the user to enter data. Returns the entered data as a string
name = input("What is your name?: ")
#The input in the terminal is always a string and hence it has to be converted to a integer
age = int(input("How old are you?: "))

#age = int(age)
age += 1

print(f"Hello {name}")
print("HAPPY BIRTHDAY")
print(f"You are {age} years old!")
