import math
import json
import ExperimentalData

if __name__ == "__main__":
    experimentalData = ExperimentalData("AK-105", "5.45", 905, "Soleil", 88)
    time = experimentalData.buildingFireTime(experimentalData.height)
    distance = experimentalData.buildingFireDistance(time,experimentalData.speed) # Uses the time from building fire time and speed to find the distance
    print(f"The shot was fired from a {experimentalData.weaponName} gun using a {experimentalData.projectileName} bullet. \nThe shot has an initial velocity of {experimentalData.speed}. \nThe shot was fired from the {experimentalData.buildingName} building, with a height of {experimentalData.height} meters. \nThe shot fired for {round(distance)} meters and took {round(time)} seconds to reach the ground.")
    jsonstring = json.dumps(experimentalData.__dict__)
    print(jsonstring)

    def experiment(experimentData:ExperimentalData):
        print()
