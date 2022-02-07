


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

import os
player_name = os.getenv("PLAYER_NAME", default="Player 1")



# ASK FOR USER INPUT
print("Welcome", player_name, "to Rock Paper Scissors...")
userinput = input("Rock, Paper, Scissors, Shoot!").upper()
print ("USER CHOSE:", userinput)

# VALIDATE INPUTS
if(userinput !="SCISSORS" and userinput !="ROCK" and userinput!="PAPER"): 
    print("INVALID! Please try again!") 
    quit()




# COMPUTER CHOICE
import random

options= ("ROCK", "PAPER", "SCISSORS")

computer_choice = random.choice(options)


print("COMPUTER CHOSE:", computer_choice)


# DETERMINE THE WINNER
if userinput == computer_choice:
    print("Both players played", userinput, "It's a tie! Try again!")
elif userinput == "PAPER":
    if computer_choice == "ROCK":
        print("Paper beats rock. You won! Great job!")
    else:
        print("Scissors beats paper. You lost! Better luck next time!")
elif userinput == "SCISSORS":
    if computer_choice == "PAPER":
        print("Scissors beats paper. You won! Great job!")
    else:
        print("Rock beats scissors. You lost! Better luck next time!")
elif userinput == "ROCK":
    if computer_choice == "SCISSORS":
        print("Rock beats scissors. You won! Great job!")
    else:
        print("Paper beats rock. You lost!")

#FINAL RESULTS