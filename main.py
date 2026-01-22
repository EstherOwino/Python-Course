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
#friends = friends ** 2 #to the power of 2 also called exponent
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
result = name.capitalize() #capitalize the first letter in a name 
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
#in the above, we have covered string indexing


# format specifiers = {value:flags} format a value based on what flags are inserted

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:.2f}") #f after 2 means floating point number, 
#2 = number of decimals to be displayed
# in short .2f rounds a number to 2 decimal places
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

#to allocate space
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

#allocate and zero pad that many spaces(puts 0 where there is space)
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

#left justify = they all start on the same line on the left
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

#right justify = they all end on the same line on the right
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

#center align = all are aligned at the center
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

#use a plus sign to indicate positive value
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

#place sign to leftmost position
#the numbers that will be displayed below, will be aligned evenly
#for + numbers, it will put a space the display the number
#for - numbers, it will put a - sign with no space then display the number
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

#comma separator
#the thousand separator which is a comma
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

#plus sign + thousand separator + decimal precision
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

#while loop = execute some code WHILE some conditions remain true
name = input("Enter you name: ")
while name == "":
  print("You did not enter you name")
  name = input("Enter you name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))
while age < 0:
  print("Age can't be negative")
  age = int(input("Enter your age: "))
print(f"Your are {age} years old!")

food = input("Enter a food you like(q to quit): ") #inorder to escape press q
while not food == "q":
  print(f"You like {food}")
  food = input("Enter another food you like(q to quit): ")
print("bye")

num = int(input("Enter a number between 1 - 10: "))
while num < 1 or num > 10:
  print(f"{num} is not valid")
  num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")

#Python compound interest calculator

#Amount(A) = final amount
#Principle(P) = initial principle balance
#rate(r) = interesr rate
#time(t) = number of time periods elapsed
principle = 0
rate = 0
time = 0 #in years

while principle < 0:
  principle = float(input("Enter the principle amount: "))
  if principle < 0:
    print("Principal can't be less than zero")

while rate < 0:
  rate = float(input("Enter the interest rate: "))
  if rate < 0:
    print("Interest rate can't be less than zero")

while time < 0:
  time = int(input("Enter the time in years: "))
  if time < 0:
    print("Time can't be less than zero")

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate/100) , time)
print(f"Balance after {time} years: Ksh{total:.2f}")
#the above code does not prompt us, rather it just displays 0 at the end

#the below code will prompt us
while True:
  principle = float(input("Enter the principle amount: "))
  if principle < 0:
    print("Principal can't be less than zero")
  else:
    break
    #break helps to stop being in a loop

while True:
  rate = float(input("Enter the interest rate: "))
  if rate < 0:
    print("Interest rate can't be less than zero")
  else:
    break

while True:
  time = int(input("Enter the time in years: "))
  if time < 0:
    print("Time can't be less than zero")
  else:
    break

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate/100) , time)
print(f"Balance after {time} years: Ksh{total:.2f}")

#for loops = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.

#iteration/loop over a range
#(start, end, step)
for x in range(1, 11):
  print(x)
print("HAPPY NEW YEAR!")

for x in reversed(range(1, 11)):
  print(x)
print("Hello")

for x in range(10, 0, -1): #for x in range(10, 0) will output nothing
  print(x)
print("Hola!")

for x in range(1, 11, 2): 
  print(x)
print("Hola! muchachos")

#iteration/loop over a string
credit_card = "1234-5678-9012-3456"
for x in credit_card:
  print(x)

for x in range(1, 21):
  if x == 13: #13 will be skipped
    continue
  else:
    print(x)

for x in range(1, 21):
  if x == 13: #13 will not be printed, the loop will stop at 12
    break
  else:
    print(x)

#iteration through a sequence
rooms = [{"room1"},{"room2"}]
for x in rooms:
  print(x)

rooms = [{"room1"},{"room2"}]
print(rooms[0])

#nested loop = A loop within another loop (outer, inner)
#              outer loop:
#                 inner loop:

for i in range(3): #whatever is inside this loop will be repeated 3 times
  for x in range(1, 10):
    # each print by default ends in end="\n"
    print(x, end="")
  print() #this will print a newline at the end of @loop

#creating a rectangle using nested loops
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for i in range(rows): #similar to for i in range(0,rows):
  for x in range(0,columns): #similar to for x in range(0,columns):
    print(symbol, end="")
  print()

# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicated OK
#   Set = {} unordered and immutable/unchangeable, but Add/Remove OK.No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER than Lists

#List
fruits = ["apple", "orange", "banana", "coconut"] #will be displayed the same way when printed

print(fruits[0:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits: #for every fruit in fruits
  print(fruit)

print(dir(fruits))#dir()lists the different attributes and methods that are available to a collection
#print(help(fruits))#help() provided descriptions of the attributes and methods in dir()
print(len(fruits)) #prints the length/number of the elements

#using in we can check whether our value is within a given collection
#in returns a boolean
print("apple" in fruits)
print("pineapple" in fruits)

fruits[0] = "pineapple"
for fruit in fruits:
  print(fruit)

fruits.append("pineapple")#append() adds to the end of list
fruits.remove("coconut")#remove() removes an element
fruits.insert(0, "apple")
fruits.sort()
fruits.reverse()
#fruits.clear()
print(fruits.index("apple"))
print(fruits.count("pineapple"))
print(fruits)

#Set
fruits = {"apple", "orange", "banana", "coconut"}#will not be displayed the same way when printed
#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)#to check whether elements are in our set
#print(fruits[0]) #we cannot use indexing in a set because they are unordered
fruits.add("pineapple")
fruits.remove("apple")
#fruits.pop()#removes the first element. It is random
#fruits.clear()

print(fruits)

#Tuple
fruits = ("apple", "orange", "banana", "coconut")
#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)
print(fruits.index("apple"))
print(fruits.count("coconut"))
for fruit in fruits:
  print(fruit)

print(fruits)

#2dlist = [list1, list2] #This is a list made up of a list
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
print(groceries[1][2]) #row column

for collection in groceries:
  for food in collection:
    print(food, end=" ")
  print()

#dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals = {"Kenya": "Nairobi",
           "USA": "Washington D.C.",
           "India": "New Delhi", 
           "China": "Beijing",
           "Russia": "Moscow"}
print(dir(capitals))
#print(help(capitals))
print(capitals.get("Kenya"))
print(capitals.get("Japan")) #if a key does not exist, it returns none
if capitals.get("Japan"):
  print("That capital exists")
else:
  print("That capital does not exist")
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroid"})
capitals.pop("China")
capitals.popitem()#removes the latest/last key:value pair
#capitals.clear()
keys = capitals.keys()#to get all of the keys within the dictionary but not the values
print(keys)#This returns a list of keys
for key in keys:
  print(key)

values = capitals.values()#to get all the values within a dictionary
print(values)
for value in values:
  print(value)

items = capitals.items()
print(items) #returns a dictionary object that resembles a 2d list of tuple

for key, value in capitals.items():
  print(f"{key}: {value}")

print(capitals)