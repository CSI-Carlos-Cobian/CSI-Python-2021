import random

print("Welcome to the totally legal and not a scam magic 8 ball business")
Name=input("WHAT IS YOUR NAME?")
print(f"Hi:{Name}")
Question=input("What is your question?")
print(f"{Question}")

 
random_number = random.randint(1,12)
if random_number == 1:
    print("Yes - definitely so.")
elif random_number == 2:
    print("It is decidedly so.")
elif random_number == 3:
    print("Without a doubt.")
elif random_number == 4:
    print("Reply hazy, tray again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not to tell you now.")
elif random_number == 7:
    print("My sources say NO")
elif random_number == 8:
    print("Outlook not so good.")
elif random_number == 9:
    print("Very doubtful.")
elif random_number == 10:
    print("0%")
elif random_number == 11:
    print("50%/50%")
elif random_number == 12:
    print("100%")        
else:
    print ("error")    