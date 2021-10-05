import math

#AK-105 5.45
speed = 905
#Soleil
height = 88

def buildingFireTime(height):
    time = math.sqrt(height/(9/8/2))
    return time

def buildingFireDistance(time, velocity):
    distance = time * velocity
    return distance

distance = buildingFireDistance(buildingFireTime(height),speed)
print(f"The building fired for {distance} meters")