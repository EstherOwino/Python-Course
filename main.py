import math


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


#arithmetic operators
friends = 5
#friends = friends + 1
friends += 1
#friends = friends -2
friends -= 2
#friends = friends * 3
friends *= 3
#friends = friends / 2
friends /=2
#friends = friends ** 2 #to the power of 2 aslo called exponent
friends **= 2
remainder = friends % 3

print(friends)
print(remainder)


#built in math related functions
x = 3.14
y = -4
z = 5
result = round(x)
print(result)
result = abs(y) #abs mean absolute value, it is the distance away from 0 as a whole number
print(result)
result = pow(z, 2) #power function, we will need a base and an exponent or power
print(result)

result = max(x,y,z)
print(result)
result = min(x,y,z)
print(result)

print(math.pi)
print(math.e)

x = 9
result = math.sqrt(x) #square root of a number
print(result)
result = math.pow(x, 2)
print(result)
result = math.ceil(4.4)
print(result)
result = math.floor(4.6)
print(result)


#if statements
#if = do some code only IF some condition is True Else do something else
age = int(input("Enter your age: "))
if age >= 100:
  print("You are too old to sign up")
elif age >= 18:
  print("You are now signed up!")
elif age < 0:
  print("You haven't been born yet!")
else:
  print("You must be 18+ to sign up")

response = input("Would you like food? (Y/N): ")
# == is the comparison operator
# = is the assignment operator
if response == "Y": 
  print("Have some food!")
else:
  print("No food for you!")

name = input("Enter your name: ")
if name == "":
  print("You did not type in your name!")
else:
  print(f"Hello {name}")

for_sale = True
if for_sale:
  print("This item is for sale")
else:
  print("This item is NOT for sale")

online = False
if online:
  print("The user is online")
else:
  print("The user is offline")

#logical operators = evaluate multiple conditions(or, and, not)
#                   or = at least one condition must be true 
#                   and = both conditions must be True
#                   not = inverts the condition(not False, not True)

#or
temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
  print("The outdoor event is cancelled")
else:
  print("The outdoor event is still scheduled")

temp = 0
is_sunny = False

#and
if temp >= 28 and is_sunny:
  print("It is HOT outside")
  print("It is SUNNY")
elif temp <= 0 and is_sunny:
  print("It is COLD outside")
  print("It is SUNNY")
elif temp < 28 and temp > 0 and is_sunny:
  print("It is WARM outside")
  print("It is SUNNY")

#not
elif temp >= 28 and not is_sunny:
  print("It is HOT outside")
  print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
  print("It is COLD outside")
  print("It is CLOUDY")
elif temp < 28 and temp > 0 and not is_sunny:
  print("It is WARM outside")
  print("It is CLOUDY")

#conditional expression = A one-line shortcut for the if-else statement(ternary operator)
#                         Print or assign one or two values based on a condition
#                         X if condition else Y
num = 5

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 6
b = 7
# if a > b return a else return b 
max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

age = 25
status = "Adult" if age >= 18 else "Child"
print(status)

temperature = 20
weather = "HOT" if temperature > 20 else "COLD"
print(weather)

user_role = "guest"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)

name = input("Enter your full name: ")
result = len(name)
result = name.find("o") #This gives the first occurrence of something eg space, always begins with index 0
result = name.rfind("o") #This finds the last occurence, r=reverse
#If Python is not able to locate a given character, it will return -1
result = name.capitalize() #capitalize the first letter in a 
result = name.upper()#upper takes all the characters in the string then make then all uppercase
result = name.lower()
result = name.isdigit()#returns True or False if a string contains only digits
#.isdigit() only returns True if what is typed ONLY contains digits
result = name.isalpha()#returns True or False if a string contains alphabetical characters
#.isalpha() only returns True if what is typed ONLY contains alphabets
#in .isdigit and .isalpha(), even a space results in False
print(result)

phone_number = input("Enter your phone number: ")
result = phone_number.count("-") #counts the number of something, this method returns an integer
result = phone_number.replace("-", "") #replaces something with another thing
print(result)

#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"
print(credit_number[4])
print(credit_number[:4]) #is the same as the one below
#                         Python assumes you need everything from the start of the string
print(credit_number[0:4]) #the starting index is inclusive and the ending index is exclusive
print(credit_number[5:9])
print(credit_number[15:]) #Python assumes you need everything till te end of the string
#                          Does the same thing as the code below
print(credit_number[15:19])
print(credit_number[4:])
print(credit_number[-1]) #if you want the LAST character in a string
print(credit_number[-2]) #if you want the second LAST character in a string and so on
print(credit_number[::2])#Python assumes its from the first to the last
#                         prints every 2nd character of our string, the 1st number is inclusive
print(credit_number[::3])

last_digits = credit_number[15:]
last_digits = credit_number[-1:-5]
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#let's reverse the characters in the string
credit_number = credit_number[::-1]#-1 reverses the string
print(credit_number)
#in te above, we have covered string indexing
