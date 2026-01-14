import time

time.sleep(3) #our timer will sleep for 3 seconds
print("TIME'S UP!")

#COUNTDOWN TIMER EXAMPLE
print("COUNTDOWN TIMER")
for x in reversed(range(0, 11)): #for x in range(10, 0, -1):
  print(x)
  time.sleep(1)
print("Happy new year!")

for x in range(11, 0, -1):
  print(x)
  time.sleep(1)
print("Happy new year!")

my_time = int(input("Enter the time in seconds: "))

for x in range(0, my_time):
  print(x)
  time.sleep(1)
print("TIME'S UP!")

#COUNTDOWN TIMER
for x in range(my_time, 0, -1):
  seconds = x % 60
  minutes= int(x / 60) % 60 # int is used because division in Python produces a float
  hours = int(x / 3600) # % 24 is not included because we do not have days in our timer
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)
print("TIME'S UP!")
