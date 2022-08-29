# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if computer_choice == "r" and user_choice == "p":
    print("You win")
if computer_choice == "r" and user_choice == "s":
    print("You lose")
if computer_choice == "r" and user_choice == "r":
    print("You tied")
if computer_choice == "p" and user_choice == "p":
    print("You tied")
if computer_choice == "p" and user_choice == "r":
    print("You lose")
if computer_choice == "p" and user_choice == "s":
    print("you win")
if computer_choice == "s" and user_choice == "r":
    print("You win")
if computer_choice == "s" and user_choice == "s":
    print("You tied")
if computer_choice == "s" and user_choice == "p":
    print("You lose")
print("computer choice " + computer_choice)