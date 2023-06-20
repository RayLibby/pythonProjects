rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

# Storing values in a list
choices = ["rock", "paper", "scissors"]
# Asking user for selection
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Random int 0-2
random_int = random.randint(0, 2)
# Getting random selection
computerChoice = choices[random_int]

# Converting computers word selection to a numbers
if computerChoice == "rock":
    computerToNumber = 0
elif computerChoice == "paper":
    computerToNumber = 1
else:
    computerToNumber = 2

# Print the user's selection
if userChoice == 0:
    print(rock)
elif userChoice == 1:
    print(paper)
else:
    print(scissors)

# Print the computer's selection
print("Computer chose:\n")

# Random number to word
if computerToNumber == 0:
    print(rock)
elif computerToNumber == 1:
    print(paper)
else:
    print(scissors)

# Logic to figure out the winner/loser:

# If Draw
if userChoice == computerToNumber:
    print("Draw")

# rock vs paper
elif userChoice == 0 and computerToNumber == 1:
    print("You Lose")
elif userChoice == 1 and computerToNumber == 0:
    print("You Win")

# paper vs scissors
elif userChoice == 1 and computerToNumber == 2:
    print("You Lose")
elif userChoice == 2 and computerToNumber == 1:
    print("You Win")

# scissors vs rock
elif userChoice == 2 and computerToNumber == 0:
    print("You Lose")
elif userChoice == 0 and computerToNumber == 2:
    print("You Win")

else:
    print("NA")





