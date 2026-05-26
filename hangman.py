#Hangman in Python
import random
from wordslist import words
#dictionary of key:() ...key will represent incorrect number of guesses
hangman_art = {0: ("   ",
                   "   ", 
                   "   "),
               1: (" o ", 
                   "   ", 
                   "   "), 
               2: (" o ", 
                   " | ", 
                   "   "), 
               3: (" o ", 
                   "/| ", 
                   "   "), 
               4: (" o ", 
                   "/|\\", 
                   "   "), 
               #Two \\ have to be used to print \, as \ is used as an escape sequence within a string 
               5: (" o ", 
                   "/|\\", 
                   "/  "), 
               6: (" o ", 
                   "/|\\", 
                   "/ \\")}

#for line in hangman_art.get(6):
#  print(line, end="\n")

def display_man(wrong_guesses):
  print("*****************************")
  for line in hangman_art[wrong_guesses]:# or for line in hangman_art.get(wrong_guesses):
    print(line)
  print("*****************************")


def display_hint(hint):
  #this will display a list of _ and for every correct letter guessed, the _ will be swapped 
  #with that letter
  print(" ".join(hint)) #for each character in our string, join it with an empty space
  #join() takes every string inside the list and combines them into one single string, 
  #separated by " " (a space

def display_answer(answer):
  print(" ".join(answer))

def main():
  answer = random.choice(words)
  #print(answer)
  hint = ["_"] * len(answer)
  #print(hint)
  wrong_guesses = 0
  guessed_letters = set() #to create a set we cannot only use (), we need the set function set()
  is_running = True

  while is_running:
    display_man(wrong_guesses)
    display_hint(hint)
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input")
      continue

    if guess in guessed_letters:
      print(f"{guess} already guessed")
      continue

    guessed_letters.add(guess)

    if guess in answer:
      for i in range(len(answer)):
        if answer[i] == guess:
          hint[i] = guess
    else:
      wrong_guesses += 1

    if "_" not in hint:
      display_man(wrong_guesses)
      display_answer(answer)
      print("YOU WIN!")
      is_running = False
    elif wrong_guesses >= len(hangman_art) - 1: #len(hangman_art) == 7
      display_man(wrong_guesses)
      display_answer(answer)
      print("YOU LOSE!")
      is_running = False


if __name__ == "__main__":
  main()


