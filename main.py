import math
import random
import time

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
for x in range(1, 11): #range only works with integers
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
fruits.pop() #removes the last element
print(fruits)

#Set
#sets cannot be reversed
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

#How to generate random numbers in Python


#print(dir(random)) #for a comprehensive list

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6","7","8","9","10","J", "Q", "K", "A"]
number = random.randint(low, high) #for a random whole integer, within the brackets, give a range
number = random.random()#for a random floating number,it gives a range between 0 and 1 by default
option = random.choice(options)#you can pick a random choice from a sequence
random.shuffle(cards)

print(cards)

#function = a block of reusable code
#           place () after the funtion name to invoke/call it 

#to define a function use keyword def then the function_name
def happy_birthday(name, age): #the data inside () is called parameter
  print(f"Happy birthday {name}!")
  print(f"You are {age} years old!")
  print("Happy birthday to you!")
  print()
happy_birthday("Esther Owino", 20) #the data inside () is called argument

def display_invoice(username, amount, due_date):
  print(f"Hello {username}")
  print(f"Your bill of ${amount:.2f} is due: {due_date}")
display_invoice("Esther Owino", 42.50, "01/01")

#return = statement used to end a function
#          and send a result back to the caller
def add(x, y):
  z=x+y
  return z

def subtract(x, y):
  z=x-y
  return z

def multiply(x, y):
  z=x*y
  return z

def divide(x, y):
  z=x/y
  return z
print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
  first = first.capitalize()
  last = last.capitalize()
  return first + " " + last
full_name = create_name("esther", "owino")
print(full_name)

full_name = create_name("spongebob", "squarepants")
print(full_name)

#default arguments = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces #(number) of arguments
#                    1. positional(already covered in last topic), 2. DEFAULT(today), 3. keyword, 4. #                    arbitrary

def net_price(list_price, discount = 0, tax = 0.05):
  return list_price * (1 - discount) * (1 + tax)
print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

#creating a count-up timer
def count(end, start=0):
  for x in range(start, end+1):
    print(x)
    time.sleep(1)
  print("DONE!")
count(30,15)

#keyword arguments = an argument preceded by an identifier
#                    helps with readability
#                    order of arguments doesn't matter
#                    1. positional 2. default 3. KEYWORD 4. arbitrary
def hello(greeting, title, first, last):
  print(f"{greeting} {title} {first.capitalize()} {last.capitalize()}")
#positional arguments should always come before keyword arguments
hello("Hello", title = "Madam",last= "owino", first="esther")
hello("Hello", "Mr", "spongebob", "squarepants")

for x in range(1, 11):
  #end is a keyword statement found within the print function
  print(x, end= " ")
print()

print("1","2","3","4","5", sep="-")

#function to generate phone number
def get_phone(country, area, first, last):
  return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=789)
print(phone_num)

#arbitrary arguments = varying amount of arguments, we don't know how many 
#                      arguments a user will pass in when invoking a function
# To accept a varying number of variables, developers can use args and kwargs
# *args(arguments)            = allows you to pass multiple non-key arguments
# **kwargs(keyword arguments) = allows you to pass multiple keyword-arguments
#                             * = unpacking operator
#                             1. positional 2. default 3. KEYWORD 4. arbitrary
# invoking a function with *args will be packed into tuples
# invoking a function with *kwargs will be packed into a dictionary

# other variable names apart from args can also be used 
def add(*args):
  total = 0
  for arg in args:
    total += arg
  return total

print(add(1,2,3))

def display_name(*args):
  #print(type(args))
  for arg in args:
    print(arg, end=" ")
  print()
display_name("Esther", "Achieng'", "Owino")

def print_address(**kwargs):
  print(type(kwargs))
  print(kwargs)
  for key, value in kwargs.items():
    print(f"{key}: {value}")
print_address(street="123 Fake St", apt="100", city="Detroit", state="MI", zip="54321")

def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()

  if "apt" in kwargs:
    #use single quotes for street as Python gets confused t0 where the quotes end if there are double quotes
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
  elif "pobox" in kwargs:
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('pobox')}")
  else:
    print(f"{kwargs.get('street')}")
  print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St", pobox="PO box #1001", city="Detroit", state="MI", zip="54321")

#iterables = an object/collection that can return its elements one at a time,
#            allowing it to be iterated over in a loop

#an example of a dictionary iterable
my_dictionary = {"A":1, "B":2, "C":3}
for key, value in my_dictionary.items():
  print(f"{key} = {value}")

# Membership operators = used to test whether a value or a variable is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                         1. in
#                         2. not in
word = "APPLE"
letter = input("Guess a letter in the secret word: ")
if letter not in word:
  print(f"{letter} was not found")
else:
  print(f"There is a {letter}")

# Example game
print("-----Guess the words game-----")
word = "APPLE"
print(f"The word contains {len(word)} characters")
guess_letters = []
for character in range(len(word)):
  letter = input("Guess a letter in the secret word: ").upper()
  guess_letters.append(letter)
print(f"Your guesses are: {guess_letters}")
print(f"The word is: {word}")

#membership operators with sets
students = {"Spongebob", "Patrick", "Sandy"}
student = input("Enter a name of a student: ").capitalize()
if student in students:
  print(f"{student} is a student")
else:
  print(f"{student} was not found")

#membership operators with dictionaries
grades = {"Sandy": "A", 
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}
student = input("Enter the name of a student: ")
if student in grades: 
  print(f"{student}'s grade is {grades[student]}")
  #print(f"{student}'s grade is {grades.get(student)}")
else:
  print(f"{student} was not found")

#Membership operators with strings
email = "spongebobsquarepants010@gmail.com"
if "@" and "." in email:
  print("Valid email")
else:
  print("Invalid email")

#List comprehension = A concise way to create lists in Python
#                     Compact and easier to read thar traditional loops
#                     [expression for value in iterable if condition]

doubles = [] #traditional loop
for x in range(1,11):
  doubles.append(x*2)
print(doubles)

doubles = [x*2 for x in range(1,11)]#list comprehension, condition is optional
print(doubles)

triples = [y*3 for y in range(1,11)]#condition is optional
print(triples)

squares = [math.pow(z,2) for z in range(1,11)]#condition is optional
print(squares)

fruits = ["apple","orange","banana","coconut"]
for fruit in fruits:
  print(fruit.upper(), end=" ")
print()

fruits = [fruit.upper() for fruit in ["apple","orange","banana","coconut"]]
print(fruits)

#take the first letter and put it in a new list
first_letter = []
for fruit in fruits:
  first_letter.append(fruit[0])
print(first_letter)

fruits = [fruit[0] for fruit in fruits]
print(fruits)

numbers = [abs(x) for x in [1, -2, 3, -4, 5, -6]]
print(numbers)

#using conditions
numbers = [1, -2, 3, -4, 5, -6, -7, 8]
positive_nums = [num for num in numbers if num>=0]
print(positive_nums)

negative_nums = [num for num in numbers if num<0]
print(negative_nums)

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

odd_nums = [num for num in numbers if not num % 2 == 0]
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

#Match-case statement (switch): An alternative to using many 'elif' statements
#                               Execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable
def day_of_week(day):
  if day == 1:
    return "It is Sunday"
  elif day == 2:
    return "It is Monday"
  elif day == 3:
    return "It is Tuesday"
  elif day == 4:
    return "It is Wednesday"
  elif day == 5:
    return "It is Thursday"
  elif day == 6:
    return "It is Friday"
  elif day == 7:
    return "It is Saturday"
  else:
    return "Not a valid day"
  
print(day_of_week(7))

#case = value we are examining eg.day
def day_of_week(day):
  match day:
    case 1:
      return "It is Sunday"
    case 2:
      return "It is Monday"
    case 3:
      return "It is Tuesday"
    case 4:
      return "It is Wednesday"
    case 5:
      return "It is Thursday"
    case 6:
      return "It is Friday"
    case 7:
      return "It is Saturday"
    case _:#for else
      return "Not a valid day"
  
print(day_of_week("pizza"))

def is_weekend(day):
  match day:
    case "Sunday":
      return True
    case "Monday":
      return False
    case "Tuesday":
      return False
    case "Wednesday":
      return False
    case "Thursday":
      return False
    case "Friday":
      return False
    case "Saturday":
      return True
    case _:#for else
      return False
print(is_weekend("chips"))

def is_weekend(day):
  match day:
    case "Sunday" | "Saturday":
      return True
    case "Monday" | "Tuesday" | "Wenesday" | "Thursday" | "Friday":
      return False
    case _:#for else
      return False
  
print(is_weekend("Tuesday"))

def grading():
  marks = int(input("Enter your marks: "))
  marks = int(marks/10)
  match marks:
    case 10 | 9 | 8 | 7:
      return "You have an A!"
    case 6:
      return "You have a B!"
    case 5:
      return "You have a C!"
    case 4:
      return "You have a D!"
    case 3 | 2 | 1 | 0:
      return "You have failed!"
    case _:
      return "Invalid marks!"
print(grading())

#module = a file containing code you want to include in your program
#         use 'import' to include a module {built-in or your own}
#         useful to break up a large program reusable separate files
print(help("modules"))#for a list of all modules found within the standard Python library
#to list all the different variables and functions found in a module, you can 
#place the name of the module within the help function
print(help("math"))

#3 ways to import
#import math
#import math as m #renaming an in-built module
from math import pi #can however cause naming conficts when created again in current file

print(pi)

#import math
import example

#in python, if you want aceess something from another file, import the filename without .py
#this automatically makes everything in that file an export
result = example.pi
print(result)
print(example.area(10))
print(example.square(13))
print(f"{example.circumference(3):.2f}")

#variable scope = where a variable is visible and accessible
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in (LEGB gives the order of operations)

#Local
def func1():
  a = 1
  print(a)

def func2():
  b = 2
  print(b)

func1()
func2()

#Enclosed(an example is having a function declared within another function)
#example1
def func1():
  x = 1
  def func2():
    x = 2 #if this x exists which is local it will be printed
    print(x)
  func2()

func1()

#example2
def func1():
  x = 1
  def func2():
    #if a new x is not declared here, the first/enclosed x will be used 
    print(x)
  func2()

func1()

#Global
name = "Esther"
def func1():
  print(name)

def func2():
  print(name)

func1()
func2()
#NB: if local / enclosed variables existed, they would be used instead of the global variable

#Built-in
from math import e
def func1():
 print(e)
# e = 3 #NB: This e is global and it would be printed in the above function if used 
func1()

#if __name__ == __main__: (this script can be imported OR run standalone)
#                          Functions and classes in this module can be reused
#                          without the main block of code executing

#def main():
  #Your program goes here

#if __name__ == __main__:
#  main()

#Codes to be found in script1.py and script2.py 


#cypher encryption and decryption
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

#print(chars)
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

#strings are iterable
for letter in plain_text:
  index = chars.index(letter)
  cipher_text += key[index]
print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

#strings are iterable
for letter in cipher_text:
  index = key.index(letter)
  plain_text += chars[index]
print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")