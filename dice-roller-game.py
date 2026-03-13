import random

#I want to play this game times before I can determine the winner
#The player will agree to play the game, and the computer will also play the game and comparisons will be # made at each point
#At the end of 5 plays, the winner will be determined based on the highest total of rolled dice
# Both the player and computer moves will be random

player_dice = []
computer_dice = []
player_total = 0
computer_total = 0
print("-----ROLL THE DICE-----")
for i in range(5):
  player = input("Would you like to roll the die?(y/n): ").lower()
  if player == "y":
    player = random.randint(1, 6)
    computer = random.randint(1, 6)
    player_dice.append(player)
    computer_dice.append(computer)
    print(f"Player: {player} Computer:{computer}")
  elif player == "n":
    print("Nice game!")
    break
  else:
    print("Try again!")
  
for die in player_dice:
  player_total += die

for die in computer_dice:
  computer_total += die
print(f"Total scores: Player: {player_total} : Computer: {computer_total}")
if player_total > computer_total:
  print("You win!")
else:
  print("You lose!")
print("---------------")
