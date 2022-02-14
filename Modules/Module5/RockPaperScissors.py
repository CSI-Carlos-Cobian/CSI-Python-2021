import random

rps = ["rock", "paper", "scissors"] # Creates an array of RPS options
opponentThrow = random.choice(rps) # Assigns a choice of throw for the opponent randomly
print("Let's play rock paper scissos!\nChoose to throw rock, paper, or scissors!")
userThrow = input("What will you throw? ") # Takes user input
userThrow = userThrow.lower() #Turns user input to lowercase to easily compare with opponent's throw
# Ensures that the input is one of the accepted values of RPS
if not (userThrow == "rock" or userThrow == "paper" or userThrow == "scissors"):
    print("Answer not recognized. Please choose between rock, paper, or scissors.")
    userThrow = input("What is your choice? ")

# Checks if both the user and opponent throw are the same, bypassing the need to add this to every if value for the separate throws.
if userThrow == opponentThrow:
    print(f"You both threw {userThrow}! It's a tie!")

# If value for when the user throws rock. If the opponent threw paper, the player loses. If the user does not throw paper, 
# the user wins. Since the option of the same value (both rock) has already been done prior to the if statement, 
# the player will only win if the enemy throws a scissors
elif userThrow == "rock":
    if opponentThrow == "paper":
        print(f"You threw {userThrow} and your opponent chose {opponentThrow}. The opponent's {opponentThrow} beats your {userThrow}! You lose!")
    else:
        print(f"You threw {userThrow} and your opponent chose {opponentThrow}. Your {userThrow} beats the opponent's {opponentThrow}! You win!")

# Same as the rock logic, but in the case of paper and the values that it loses to and beats.
elif userThrow == "paper":
    if opponentThrow == "scissors":
        print(f"You threw {userThrow} and your opponent chose {opponentThrow}. The opponent's {opponentThrow} beats your {userThrow}! You lose!")
    else:
        print(f"You threw {userThrow} and your opponent chose {opponentThrow}. Your {userThrow} beats the opponent's {opponentThrow}! You win!")

# Same as rock and paper logic, but for other values. Since only "rock", "paper", and "scissors" 
# are accepted, this will only run if the player throws a scissors.
else:
    if opponentThrow == "rock":
        print(f"You threw {userThrow} and your opponent chose {opponentThrow}. The opponent's {opponentThrow} beats your {userThrow}! You lose!")
    else:
        print(f"You threw {userThrow} and your opponent chose {opponentThrow}. Your {userThrow} beats the opponent's {opponentThrow}! You win!")