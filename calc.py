print("CALCULATOR")
print("1. Addition.")
print("2. Subtraction.")
print("3. Multiplication.")
print("4. Division.")
print("5. Modulus.")
number = int(input("Choose the operation you want to perform from the above: "))

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

if number == 1:
  print(f"{num1} + {num2} = {addition}")
elif number == 2:
  print(f"{num1} - {num2} = {subtraction}")
elif number == 3:
  print(f"{num1} * {num2} = {multiplication}")
elif number == 4:
  print(f"{num1} / {num2} = {division}")
elif number == 5:
  print(f"{num1} mod {num2} = {modulus}")
