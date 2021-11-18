import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json

#"gun" = "GLOCK17"
#"caliber" = "9x19mm"
#"ammunition" = "PBB gzh"
#"velocity"= 560
#"building" = "Caribean Sea View"
#"buildingheight" = 334
#"gravity" = 9.81

#Estan las calculaciones aqui y las listas de los planetas con sus gravedades
def projectilefunction(experimentalData: ExperimentalData):
    planets = ["Neptune", "Urnanus", "Earth", "Saturn", "Jupiter", "Mars", "Venus", "Mercury"]
    gravity = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planets= planets.index(experimentalData.planet)

    time = math.sqrt((2 * experimentalData.buildinheight) / gravity[planets])
    distance = (experimentalData.velocity * time)
    print(f"The gun i choose was the {experimentalData.gun} the ammunition is {experimentalData.ammunition}, the caliber is {experimentalData.caliber}, the velocity is {experimentalData.velocity} it will be at the {distance} at {time} and it will be shot at {experimentalData.building} that has a height of {experimentalData.buildinheight}")
    print(f"The {experimentalData.planet} which has {gravity[planets]} is where this will be taken place.")
experimentalData = ExperimentalData("Glock17", "9x19mm", "PBB", 560, "Carrebean Sea view", 334, "Earth")
#Estamos cogiendo los experimentos en cada planeta que escogi
myDataSet = [
ExperimentalData("Glock17","9x19mm","PBB ", 560, "Caribean Sea  view",334,"Neptune"),
ExperimentalData("Glock17","9x19mm","PBB ", 560, "Caribean Sea  view",334,"Urnanus"),
ExperimentalData("Glock17","9x19mm","PBB ", 560, "Caribean Sea  view",334,"Saturn"),
ExperimentalData("Glock17","9x19mm","PBB ", 560, "Caribean Sea  view",334,"Jupiter"),
ExperimentalData("Glock17","9x19mm","PBB ", 560, "Caribean Sea  view",334,"Mars"),
]


#Aqui estamos pritintiando el data set y llamandolo por seccion
for data in myDataSet:
    print("\n---------------------------------------------------------------------\n")
    projectilefunction(data)
    myOutputPath = Path(__file__).parents[0]
    myOutputFilePath = os.path.join(myOutputPath, "proyectileMotion.json")
    print(myOutputFilePath)
with open(myOutputFilePath, "w") as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)
    deserialize = open(myOutputFilePath)
    experimentJson = json.load(deserialize)
    myOutputPath = Path(__file__).parents[0]
for e in experimentJson:
        print("\n-------------------------------------------------\n")
        projectilefunction(ExperimentalData(**e))