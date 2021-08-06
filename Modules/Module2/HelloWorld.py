from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

name = input("Hello there! What is your name? ")
studentId = input("What is your student id? ")

print(f"Hello {name}! ")
print(f"Your Student id is: {studentId} ")
print(f"Currently, the time is: {current_time} ")