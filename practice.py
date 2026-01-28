import random

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