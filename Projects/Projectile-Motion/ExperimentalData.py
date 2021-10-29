import math
import json
class ExperimentalData:

    # weaponName = "AK-105"
    # projectileName = "5.45"
    # speed = 905
    # buildingName = "Soleil"
    # height = 88
    
    def gravitation(height:float, planetName:str):
        planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
        planetRadius = [2439700, 6051800, 6371000, 3389500, 69911000, 58232000, 25362000, 24622000]
        planetMass = [3.285 * math.pow(10, 23), 4.867 * math.pow(10, 24), 5.972 * math.pow(10, 24), 6.39 * math.pow(10, 23), 1.898 * math.pow(10, 27), 5.683 * math.pow(10, 26), 8.681 * math.pow(10, 25), 1.024 * math.pow(10, 26)]
        planetName = planetName.lower()
        index = planets.index(planetName)
        radius = planetRadius[index] + height
        gravity = planetMass[index] * 6.67408 * math.pow(10, -11) / math.pow(radius, 2)

    def __init__(self,weaponName:str, projectileName:str, ammunitionType:str, speed:float, buildingName:str, height:float, planetName:str): # sets up the variables
        self.weaponName = weaponName
        self.projectileName = projectileName
        self.ammunitionType = ammunitionType
        self.speed = speed
        self.buildingName = buildingName
        self.height = height
        self.planetName = planetName

    def getGravity(self, planetName, height): # calculates gravity using Newton's grvity equations
        G = 6.67408 * math.pow(10, -11)
        planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
        planetRadius = [2439700, 6051800, 6371000, 3389500, 69911000, 58232000, 25362000, 24622000]
        planetMass = [3.285 * math.pow(10, 23), 4.867 * math.pow(10, 24), 5.972 * math.pow(10, 24), 6.39 * math.pow(10, 23), 1.898 * math.pow(10, 27), 5.683 * math.pow(10, 26), 8.681 * math.pow(10, 25), 1.024 * math.pow(10, 26)]
        name = planetName.lower()
        index = planets.index(name)
        radius = planetRadius[index] + height
        gravity = (planetMass[index] * G) / math.pow(radius, 2)
        return gravity

    def buildingFireTime(self, height): #Takes height of the building
        time = math.sqrt(height/(9.8/2)) # Uses gravitational acceleration to find the time given a distance
        return time # gives the time value

    def buildingFireDistance(self, time, velocity): #Takes the time to hit the ground and velocity in x axis
        distance = time * velocity # Uses the time and velocity to find distance
        return distance # gives the distance value