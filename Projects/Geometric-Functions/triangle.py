from pathlib import Path
exec(open(Path(__file__).parents[2].joinpath("images/Logo.py")).read())
# triangle.py

# Returns the area of a triangle using the 
# 1/2 * base * height equation as a float. Not rounded.
def triArea(height:float, base:float):
    return 0.5 * base * height

# Prints a sentence with the area of a triangle in scientific  notation 
# (rounded to two decimal places) followed by the unit of measurement.
def printTriangleAreaScientific(area:float, unit:str):
    print(f"The area of the triangle is {area: .2e} {unit}.")

# Prints a sentence with the area of a triangle rounded 
# to two places followed by the unit of measurement.
def printTriangleAreaSimple(area:float, unit:str):
    print(f"The area of the triangle is { round(area, 2)} {unit}.")

# Creates a 2d array containing values for 4 triangles, 
# height, base, and unit of measurement, using user input 
# through a for loop. The other 3 functions are then used 
# for each of these 4 triangles in a second for loop, 
# which runs through each 1d array within the 2d array once.
def triangleValues():
    triangleValues = [[None, None, None], [None, None, None], [None, None, None], [None, None, None]]
    for i in range(4):
        height = input(f"What is the height of triangle #{i+1}? \n")
        height = float(height)
        triangleValues[i][0] = height
        base = input(f"What is the length of the base of triangle #{i+1}? \n")
        base = float(base)
        triangleValues[i][1] = base
        unit = input(f"What unit of measurement will you be using for triangle #{i+1}? \n")
        unit = str(unit)
        triangleValues[i][2] = unit
    for i in range(4):
        print(f"The following is the information for triangle #{i+1}")
        area = triArea(triangleValues[i][0], triangleValues[i][1])
        printTriangleAreaScientific(area, triangleValues[i][2])
        printTriangleAreaSimple(area, triangleValues[i][2])
        print("")

triangleValues()
