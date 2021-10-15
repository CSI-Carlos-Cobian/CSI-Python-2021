import math
import json
class ExperimentalData:

    # weaponName = "AK-105"
    # projectileName = "5.45"
    # speed = 905
    # buildingName = "Soleil"
    # height = 88

    def __init__(self,weapon:str, projectile:str, ammunition:str, velocity:float, building:str, altitude:float, gravity:float): # sets up the variables
        self.weaponName = weapon
        self.projectileName = projectile
        self.ammunitionType = ammunition
        self.speed = velocity
        self.buildingName = building
        self.height = altitude
        self.gravity = gravity


    def buildingFireTime(self, height): #Takes height of the building
        time = math.sqrt(height/(9.8/2)) # Uses gravitational acceleration to find the time given a distance
        return time # gives the time value

    def buildingFireDistance(self, time, velocity): #Takes the time to hit the ground and velocity in x axis
        distance = time * velocity # Uses the time and velocity to find distance
        return distance # gives the distance value