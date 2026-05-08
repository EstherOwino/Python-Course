#if __name__ == "__main__": (this script can be imported OR run standalone)
#Functions and classes in this module can be reused without the main block of code executing
#Good practice (code is modular
#               helps readability
#               leaves no global variables
#               avoid unintended execution)

#               Ex. library = import library for functionality
#                   When running directly, display a help page

from script1 import *
#print(__name__)
def favourite_drink(drink):
  print(f"Your favourite drink is {drink}")

def main():
  print("This is script2")
  favourite_food("chips")
  favourite_drink("soda")
  print("Goodbye!")

if __name__ == "__main__":
  main()

#print(help("script1"))