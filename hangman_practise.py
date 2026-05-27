#Hangman in Python
import random
words = ("pineapple", "pineapple", "pineapple", "pineapple", "pineapple")

#ideas
#we will guess letters of the word based on how many characters are there
#if the letter exists in the word, replace underscore with the letter
#if it doesn't, do nothing

#if I make a guess that is correct, I need to find it's index in options, then I will replace the _ in #actual_pattern with the guess letter

#problem with duplicate letters, it only takes the index of the first letter
#fix for words that are not in option word

# I now want to work with duplicate letters
# loop through correct word, check if the guessed letter is found there
# replace _ with that letter

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

    wrong_guesses = 0
    #for key in hangman[wrong_guesses]:
    while "_" in actual_pattern: #has to be changed
      if wrong_guesses < 6:
        letter = input("Enter a letter: ").lower()
        your_word.append(letter)
      else:
        break
      
      if letter in option:
        for i in range(len(option)):
          if option[i] == letter:
            actual_pattern[i] = letter
        print(actual_pattern)

      else:
        print("Letter not in guess word!")
        wrong_guesses += 1
        for line in hangman_art[wrong_guesses]:
          print(line)
        print(actual_pattern)

        if wrong_guesses >= 6:
          print("****************************")
          print("You lose game!😔")
          print("****************************")
      if "_" not in actual_pattern:
        print("****************************")
        print("You win game!🎉")
        print("****************************")
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


# number of guesses should not equal the number of words in the word
# we will use hangman and once that has been commpleted, the game shall end