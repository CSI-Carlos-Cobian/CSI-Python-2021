from pathlib import Path
import os
import math
import json
from ExperimentalData import ExperimentalData

def experiment(experimentData:ExperimentalData):
    time = experimentData.buildingFireTime(experimentData.height) #
    distance = experimentData.buildingFireDistance(time,experimentData.speed) # Uses the time from building fire time and speed to find the distance
    print(f"The shot was fired from a {experimentData.weaponName} gun using a {experimentData.projectileName} {experimentData.ammunitionType} bullet. \nThe shot has an initial velocity of {experimentData.speed}. \nThe shot was fired from the {experimentData.buildingName} building, with a height of {experimentData.height} meters. \nThe shot fired for {round(distance)} meters and took {round(time)} seconds to reach the ground with a gravity of {experimentData.gravity} m/s^2.")

if __name__ == "__main__":
    myDataSet = [
    ExperimentalData("AK-105", "5.45x39mm", "PS gs", 905, "Soleil", 88, 9.8),
    ExperimentalData("M4A1", "5.56x45mm NATO", "55 HP", 947, "Aquablue 1", 85, 9.8),
    ExperimentalData("HK 416A5", "5.56x45mm NATO", "M856A1", 940, "Minillas South Tower", 74, 9.8),
    ExperimentalData("SA-58", "7.62x51mm NATO", "M80", 833, "Nacional Plaza", 73, 9.8),
    ExperimentalData("MP9-N", "9x19mm Parabellum", "PSO gzh", 340, "Oriental Plaza", 64, 9.8)
    ]
    for experimentData in myDataSet:
        experiment(experimentData)
        print()

    myOutputPath = Path(__file__).parents[0]
    myOutputFilePath = os.path.join(myOutputPath, 'ExperimentalData.json')
    with open(myOutputFilePath, 'w') as outfile:
        json.dump(myDataSet.__dict__, outfile)