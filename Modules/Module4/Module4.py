def greetStudent(name):
    print(f"Hello, {name}!")
name = 'Mario Sanchez'
greetStudent(name)

var:str = "regular string"
myNumber:float = 3.5

myFunctionalString = f"Combine an existing {var} with a number such as: {myNumber} or execute something like {round(3.4 * 1.1)}"

print(myFunctionalString)

print(f"Or use the print directly {myNumber}")

breakfast = None
lunch = None
dinner = None
meal = ["", "", ""]

def updateMeal():
    breakfast = input("What did you have for breakfast? " )
    meal[0] = breakfast
    lunch = input("What was your Lunch? ")
    meal[1] = lunch
    dinner = input("What did you eat for dinner? ")
    meal[2] = dinner
    print(f"Your breakfast was: {meal[0]}")
    print(f"Your lunch was: {meal[1]}")
    print(f"Your dinner was: {meal[2]}")

updateMeal()
input()
