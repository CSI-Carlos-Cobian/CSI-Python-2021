import random
print("Welcome to Rock, Paper, Scissors Game!!!")
RPS = ("rock", "paper", "scissors")

playerChoice = input("Lets play. Choose one: rock, paper, scissors\n")

computerChoice = random.choice(RPS)
print(f"Computer selected: {computerChoice}")
print(f"Player selected: {playerChoice}")

if(playerChoice == computerChoice) :
    print("You tied :-/")

elif(playerChoice == "rock" and computerChoice == "scissors") :
    print("Rock crushes Scissor. You won! :)")
     
elif(playerChoice == "rock" and computerChoice == "paper") :
    print("Rock gets suffocated Paper. You lost! :)")

elif(playerChoice == "paper" and computerChoice == "rock") :
    print("Paper suffucates Rock . You won! :)")   

elif(playerChoice == "paper" and computerChoice == "scissors") :
    print("Paper gets decapitated by Scissors. You lost! :)")

elif(playerChoice == "scissors" and computerChoice == "rock") :
    print("Scissor gets crushed by Rock. You lost! :)")

elif(playerChoice == "scissors" and computerChoice == "paper") :
    print("Scissor cuts Paper. You won! :)")
  
else:
    print("Something isn't right, maybe try again")