#Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50, 
        "popcorn": 6.00,
        "fries": 2.50, 
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}


print("------MENU------")
print(menu)
cart = []
total = 0

while True:
  choices = input("Enter your chosen menu items(q to quit): ").lower()
  if choices == "":
    print("Enter your choice again")
  elif choices == "q":
    break
  else:
    if menu.get(choices) == None:
      print(f"{choices} is not in menu option")
    else:
      cart.append(choices)     
print(cart)
for item in cart:
  price = menu.get(item)
  print(f"{price:.2f}")
  total += price
print(f"The total price is: Ksh {total:.2f}")