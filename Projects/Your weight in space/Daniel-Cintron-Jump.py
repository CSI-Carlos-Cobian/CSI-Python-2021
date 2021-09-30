planets = ["Mercury","Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
rel_gravity = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]

print("Jumping on other planets")

myJump = int(input("What is your jumps length in (inches)? "))
myPlanet = input(f"Select a planet from the list: {planets}")

def  calculateJump(planet, myJump):
    print(f"\nEarth gravity in inches is: {myJump}")

    meters = myJump * 0.0254
    print(f"Length in meters: {meters}")

    

    planet_index = planets.index(planet)

    print(f"Your jump in {planets[planet_index]} is {meters * rel_gravity[planet_index]} m ")

calculateJump(myPlanet, myJump)
