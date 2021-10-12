import math
import json
class ExperimentalData:

    # weaponName = "AK-105"
    # projectileName = "5.45"
    # speed = 905
    # buildingName = "Soleil"
    # height = 88

    def __init__(self,weapon:str, projectile:str, velocity:float, building:str, altitude:float):
        self.weaponName = weapon
        self.projectileName = projectile
        self.speed = velocity
        self.buildingName = building
        self.height = altitude


    def buildingFireTime(self, height): #Takes height of the building
        time = math.sqrt(height/(9.8/2)) # Uses gravitational acceleration to find the time given a distance
        return time

    def buildingFireDistance(self, time, velocity): #Takes the time to hit the ground and velocity in x axis
        distance = time * velocity # Uses the time and velocity to find distance
        return distance