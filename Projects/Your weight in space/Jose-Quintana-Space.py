# Planets.py
# Calculate your weight in another planet!

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print("Calculate your weight in a different planet of our Solar System!")

# Query the user for a integer mass. Any other data type will result in an error.
myMass = int(input("What is your mass (pounds)? "))

# Convert the planets list into a string. Remove the special characters: ' [ ] 
planetsString = str(planets).replace('\'','').replace('[','').replace(']','')
myPlanet = input(f"Select a planet from the list: {planetsString} ")

def calculateWeight(planet:str,mass):
    print(f"\nEarth mass in pounds is: {mass}")

    # Convert your mass into kilograms.
    m_kg = mass / 2.2046
    print(f"Mass in kg: {round(m_kg , 2)}")

    # Convert the planet input string into a index integer.
    planet = planets.index(planet)

    # Weight in Newtons: Calculate weight by multiplying mass and gravitational acceleration.
    w_n = m_kg * g_ms2[planet]

    # Newtons in a pound constant.
    n_lb = 4.45 

    # Calculate the weight inside of a functional string.
    print(f"Weight in {planets[planet]} is {round( w_n / n_lb,2)} lb. \n")
 
calculateWeight(myPlanet,myMass)