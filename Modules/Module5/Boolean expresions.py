import random
print("Welcome to rock paper scissors game")
RPS = ["rock", "paper", "scissors"]

playerChoice = input("Lets play . Choose one: rock, paper, scissors")

computerChoice = random.choice(RPS)
print(f"Computer selected: {computerChoice}")
print(f"Player selected: {playerChoice}")

if(playerChoice == computerChoice):
    print("You tied")

elif(playerChoice == "rock" and computerChoice == "scissors"):
        print("rock crushes scissor. You Win!")

elif(playerChoice == "rock" and computerChoice == "paper"):
    print("You Lost")

elif(playerChoice == "paper" and computerChoice == "rock"):
    print("You Won")

elif(playerChoice == "scissors" and computerChoice == "paper"):
    print("You Won")

elif(playerChoice == "scissors" and computerChoice == "rock"):
    print("You Lost")

elif(playerChoice == "paper" and computerChoice == "scissors"):
    print("You Lost")

else:
    print("something isnt right, maybe try again")


