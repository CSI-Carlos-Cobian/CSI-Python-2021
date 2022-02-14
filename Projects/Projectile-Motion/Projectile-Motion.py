from pathlib import Path
import os
import math
import json
from ExperimentalData import ExperimentalData

def experiment(experimentData:ExperimentalData):
    time = experimentData.buildingFireTime(experimentData.height) # finds the time it's fired for
    distance = experimentData.buildingFireDistance(time,experimentData.speed) # Uses the time from building fire time and speed to find the distance
    print(f"The shot was fired from a {experimentData.weaponName} gun using a {experimentData.projectileName} {experimentData.ammunitionType} bullet. The shot has an initial velocity of {experimentData.speed}. The shot was fired from the {experimentData.buildingName} building, with a height of {experimentData.height} meters. The shot fired for {round(distance)} meters and took {round(time)} seconds to reach the ground with the gravity of the planet {experimentData.planetName} and a gravity of {round(experimentData.getGravity(experimentData.planetName, experimentData.height) * 1000)/1000}.")

if __name__ == "__main__":
    myDataSet = [ #this section defines the variables that go into the json. used for testing purposes.
        ExperimentalData("AK-105", "5.45x39mm", "PS gs", 905, "Soleil", 88, "Mercury"),
        ExperimentalData("M4A1", "5.56x45mm NATO", "55 HP", 947, "Aquablue 1", 85, "Venus"),
        ExperimentalData("HK 416A5", "5.56x45mm NATO", "M856A1", 940, "Minillas South Tower", 74, "Earth"),
        ExperimentalData("SA-58", "7.62x51mm NATO", "M80", 833, "Nacional Plaza", 73, "Mars"),
        ExperimentalData("MP9-N", "9x19mm Parabellum", "PSO gzh", 340, "Oriental Plaza", 64, "Jupiter")
    ]
    for experimentData in myDataSet: # used for testing purposes before the json
        experiment(experimentData)
        print()

    myOutputPath = Path(__file__).parents[0] # gets the path for the json
    myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')
    with open(myOutputFilePath, 'w') as outfile:
        json.dump([data.__dict__ for data in myDataSet], outfile)
    
    deserialize = open(myOutputFilePath) # puts the elements that will be deserialized

    experimentJson = json.load(deserialize) # elements are deserialized

    for e in experimentJson: # objects in the json are put into experiment data classes and run through the experiment process
        experiment(ExperimentalData(**e))
        print("--------------")