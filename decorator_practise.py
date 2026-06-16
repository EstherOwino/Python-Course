print("*************************************")
print("Hello, welcome to this icecream shop!")
print("*************************************")
print("You can make you icecream order now!")
flavour = input("What flavour would you like on your icecream? ")
input_sprinkles = input("Would you like sprinkles on your icecream?(Y/N): ").upper()
input_fudge = input("Would you like fudge on your icecream?(Y/N): ").upper()

def add_sprinkles(func):
  def wrapper(*args, **kwargs):
    print("*You add sprinkles 🎊*")
    func(*args, **kwargs)
  return wrapper

def add_fudge(func):
  def wrapper(*args, **kwargs):
    print("*You add fudge 🍫*")
    func(*args, **kwargs)
  return wrapper

if input_sprinkles == "Y" and input_fudge == "Y":
  @add_sprinkles
  @add_fudge
  def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream 🍦")

elif input_sprinkles == "Y" and input_fudge == "N":
  @add_sprinkles
  def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream 🍦")

elif input_sprinkles == "N" and input_fudge == "Y":
  @add_fudge
  def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream 🍦")

elif input_fudge == "N" and input_sprinkles == "N":
  def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream 🍦")

elif input_sprinkles != "N" or input_sprinkles !="Y" and input_fudge != "N" or input_fudge !="Y":
  print("Invalid input!")
  def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream 🍦")

get_ice_cream(flavour)

print("*************************************")
print("Thankyou for shopping with us 🎉🎉🎉")
print("*************************************")