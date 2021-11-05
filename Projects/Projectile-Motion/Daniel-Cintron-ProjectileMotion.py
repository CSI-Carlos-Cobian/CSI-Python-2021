import math
from ExperimentalData import ExperimentalData

from pathlib import Path
import json
import os

# gun = "DT MDR"
# cartridge = "5.56x45mm"
# rounds = "HP" 
# velocity_ms = 947

# Building = "Minillas South Tower"
# BuildingHeight = 244

# gravity = 9.81


def ProjectileFunction(experimentalData:ExperimentalData):
    
    time_s =math.sqrt((2 * experimentalData.BuildingHeight) / experimentalData.gravity)

    # distance = experimentationData([velocity_ms] * time_s)
    distance = (experimentalData.velocity_ms * time_s) 

    print(f"The gun chosen was {experimentalData.gun} its cartridge is {experimentalData.cartridge}, its rounds are {experimentalData.rounds} and the bullets velocity was {experimentalData.velocity_ms}.m/s")
    print("Its the product of the US-based company Desert Tech LLC MDR rifle is a modular, multi-caliber weapon with compact bullpup layout. Barrel lengths and calibers can be changed by the end user within minutes with a minimum amount of tools.")
    print(f"The projectile will go to a distance of {distance}, and the time it will take to cover it is {time_s} ")
#Convert your parameters into a single JSON Object.
# experimentationData = {

#  "gun" : "DT MDR",
#  "cartridge" : "5.56x45mm",
#  "rounds" : "HP", 
#  "velocity_ms" : 947,
#  "Building" : "Minillas South Tower",
#  "BuildingHeight" : 244,
#  "gravity" : 9.81

# }


experimentalData = ExperimentalData("DT MDR", "5.56x45mm", "HP", 941, "Minillas South Tower", 244, 9.81)

myDataSet = [
ExperimentalData("DT MDR", "5.56x45mm", "HP", 947, "Minillas South Tower", 244, 9.81),
ExperimentalData("DT MDR", "5.56x45mm", "FMJ", 957, "Minillas South Tower", 244, 9.81),
ExperimentalData("DT MDR", "5.56x45mm", "M855", 922, "Minillas South Tower", 244, 9.81), 
ExperimentalData("DT MDR", "5.56x45mm", "M855A1", 945, "Minillas South Tower", 244, 9.81),   
ExperimentalData("DT MDR", "5.56x45mm", "M856", 874, "Minillas South Tower", 244, 9.81)
]

for data in myDataSet:
    print("\n---------------------------------------\n")
    ProjectileFunction(data)

# Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)
    #json.dump(myDataSet[0].__dict__, outfile)

# ProjectileFunction(experimentalData)