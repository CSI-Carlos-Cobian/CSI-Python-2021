import random

foo = ['Rock', 'Paper', 'Scissors']

computerChoice = random.choice(foo)
playerChoice = input("Rock, Paper or  Scissors? ")

print(f"Computer selected: {computerChoice}")
print(f"Player selected: {playerChoice}")

if(computerChoice == "Rock" and playerChoice == "Rock"):
    print("tied")
elif(computerChoice == "Rock" and playerChoice == "Paper"):
    print("You Win!") 
elif(computerChoice == "Rock" and playerChoice == "Scissors"):
    print("Computer Wins") 


elif(computerChoice == "Paper" and playerChoice == "Paper"): 
    print("Tied!")
elif(computerChoice == "Paper" and playerChoice == "Scissors"): 
    print("You win!") 
elif(computerChoice == "Paper" and playerChoice == "Rock"): 
    print("You Lose") 


elif(computerChoice == "Scissors" and playerChoice == "Scissors"): 
    print("Tied!") 
elif(computerChoice == "Scissors" and playerChoice == "Rock"): 
    print("You Win") 
elif(computerChoice == "Scissors" and playerChoice == "Paper"): 
    print("You Lose")
else:
    print("Something went wrong")

# ## Conditions of Rock,Paper and Scissors
# if player == computer:
#     print("Tie!")
# elif player == "Rock":
#     if computer == "Paper":
#         print("You lose!", computer, "covers", player)
# print("You win!", player, "smashes", computer) 

# if player == "Paper":
#     print("You Lose!")
# if computer == "Scissors":
#  print("You lose!")