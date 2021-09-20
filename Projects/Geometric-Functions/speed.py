# speed.py

# Calculate speed by using the distance 
def speed(distance:float, time:float):
        return ( distance / time )

# Format a value using 2 decimal places and scientific notation. 
# Print a verbal representation with units.
def printSpeedScientific(speed:float, unit:str):
        print(f"The speed in scientific notation is: {speed:.2e} {unit}.")

# Format a value to 2 decimal places. Print a verbal representation with units.
def printSpeedSimple(speed:float, unit:str):
        print(f"The speed is { round(speed, 2) } {unit}.")

# Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating various speeds: \n")

printSpeedScientific(speed(100, 60.0), "m/s")
printSpeedScientific(speed(55.5, 1), "m/s")
printSpeedScientific(speed(1.27E4, 290), "m/s")
printSpeedScientific(speed(1.27E-8, 0.001), "m/s")

# I am adding a space in between each example to separate them.
print()

printSpeedSimple(speed(100, 60.0), "m/s")
printSpeedSimple(speed(55.5, 1), "m/s")
printSpeedSimple(speed(1.27E4, 290), "m/s")
printSpeedSimple(speed(1.27E-8, 0.001), "m/s")