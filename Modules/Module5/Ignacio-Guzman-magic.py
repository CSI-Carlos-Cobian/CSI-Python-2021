import random
print("Welcome to the Magic 8-Ball Game")
Player_name = input("What is your name?")
print(f"Hello {Player_name} ! Welcome to the Magic 8-Ball Game")
Player_question =  input ("What do you want to ask me?")
print(f"{Player_name} ask {Player_question}")
random_number = random.randint(1,12)
if random_number == 1 :
    print("Yes - definitely")
elif random_number == 2:
    print("It is decidebly so.")
elif random_number == 3:
    print("Without a doubt")
elif random_number == 4:
    print("Reply hazy, tray again.")
elif random_number == 5:
    print("Ask Again Later")
elif random_number == 6:
    print("Better not tell you now.")
elif random_number == 7:
    print("My sources say NO.")
elif random_number == 8:
    print("Outlook not so good.")
elif random_number == 9:
    print("Very doubtful.")
elif random_number == 10:
    print("Not Today")
elif random_number == 11:
    print("I think so")
elif random_number == 12:
    print("Tomorrow")
else:
    print("There was an error")