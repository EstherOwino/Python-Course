#if __name__ == __main__: (this script can be imported OR run standalone)
#                          Functions and classes in this module can be reused
#                          without the main block of code executing

#def main():
  #Your program goes here

#if __name__ == __main__:
#  main() 

#from script1 import * # * means everything

#print(dir())
#print(__name__)

#if __name__ == "__main__":
  #main()
def favourite_food(food):
  print(f"Your favourite food is {food}")
  
def main():
  print("This is script1")
  favourite_food("chips")
  print("Goodbye!")
  
if __name__ == "__main__":
  #we can check which file is being run directly
  main() #to contain te main body of our program
