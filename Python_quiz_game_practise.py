#Python quiz game
questions = ("1. How many elements are in the periodic table?: ",
             "2. Which animal lays the largest eggs?: ",
             "3. What is the most adundant gas in the Earth's atmosphere?: ",
             "4. How many bones are in the human body?: ",
             "5. Which planet in the solar system is the hottest?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("---------------------")
  print(question)
  for option in options[question_num]:
    print(option)
  your_guess = input("Enter your option: ")
  your_guess = your_guess.upper()
  guesses.append(your_guess)
  if your_guess == answers[question_num]:
    score += 1
  question_num += 1
   

print(f"Your guesses are:        {guesses}")
print(f"The correct answers are: {answers}")
print(f"Your score is: {score}")

