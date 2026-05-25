#Hangman in Python
import random
words = ("mango", "orange", "peach", "lemon", "melon")

#ideas
#we will guess letters of the word based on how many characters are there
#if the letter exists in the word, replace underscore with the letter
#if it doesn't, do nothing

#if I make a guess that is correct, I need to find it's index in options, then I will replace the _ in #actual_pattern with the guess letter

#problem with duplicate letters, it only takes the index of the first letter
#fix for words that are not in option word

print("****************************")
print("        HANGMAN GAME        ")
print("****************************")
print()
print("        INSTRUCTIONS        ")
print("        ------------        ")
print("1. This is a guessing game.")
print("2. A random word will be selected.")
print("3. You will be required to guess the letters in the word.")
print()
print("****************************")
print("         START GAME         ")
print("****************************")

def play_game():
  while True: 
    option = random.choice(words)
    #print(option)
    option = list(option)
    #print(option)

    print(f"The word is a {len(option)} letter word.")
    actual_pattern = []
    your_word = []

    for y in range(len(option)):
      actual_pattern.append("_")

    for x in range(len(option)):
      letter = input("Enter a letter: ").lower()
      your_word.append(letter)
      
      if letter in option:
        index = option.index(letter)
        #print(f"Index: {index}")
        actual_pattern[index] = letter
        print(actual_pattern)
      else:
        print("Letter not in guess word!")
        print(actual_pattern)
    print()
    print(f"The actual word is {option}")
    print()
    break
play_game()

play_again = input("Would you like to play the game again? (Y/N): ").upper()

if play_again == 'Y':
  play_game()
else:
  print("**********************************")
  print("Thanks for playing! Welcome again!")
  print("**********************************")