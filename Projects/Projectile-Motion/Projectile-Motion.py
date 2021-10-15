import math
import json
from ExperimentalData import ExperimentalData

def experiment(experimentData:ExperimentalData):
    time = experimentData.buildingFireTime(experimentData.height) #
    distance = experimentData.buildingFireDistance(time,experimentData.speed) # Uses the time from building fire time and speed to find the distance
    print(f"The shot was fired from a {experimentData.weaponName} gun using a {experimentData.projectileName} {experimentData.ammunitionType} bullet. \nThe shot has an initial velocity of {experimentData.speed}. \nThe shot was fired from the {experimentData.buildingName} building, with a height of {experimentData.height} meters. \nThe shot fired for {round(distance)} meters and took {round(time)} seconds to reach the ground with a gravity of {experimentData.gravity} m/s^2.")


if __name__ == "__main__":
    experiment(ExperimentalData("AK-105", "5.45", "PS gs", 905, "Soleil", 88, 9.8))