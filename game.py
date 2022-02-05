


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#




# ASK FOR USER INPUT
userinput = input("Please choose one of : 'rock', 'paper', 'scissors':")

print ("USER CHOSE:", userinput)

# VALIDATE INPUTS




# COMPUTER CHOICE
import random

options= ("rock", "paper", "scissors")

computer_choice = random.choice(options)


print("COMPUTER CHOSE:", computer_choice)


# DETERMINE THE WINNER
if userinput == computer_choice:
    print("Both players played", userinput, "It's a tie! Try again!")
elif userinput == "paper":
    if computer_choice == "rock":
        print("Paper beats rock. You won! Great job!")
    else:
        print("Scissors beats paper. You lost! Better luck next time!")
elif userinput == "scissors":
    if computer_choice == "paper":
        print("Scissors beats paper. You won! Great job!")
    else:
        print("Rock beats scissors. You lost! Better luck next time!")
elif userinput == "rock":
    if computer_choice == "scissors":
        print("Rock beats scissors. You won! Great job!")
    else:
        print("Paper beats rock. You lost!")

#FINAL RESULTS