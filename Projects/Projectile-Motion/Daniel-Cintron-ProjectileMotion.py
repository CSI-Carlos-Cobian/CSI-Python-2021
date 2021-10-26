gun = "DT MDR"
cartridge = "5.56x45mm"
rounds = "Full-Auto" 
velocity_ms = 650

Building = "Minillas South Tower"
BuildingHeight = 244

gravity = 9.81

import math

time_s = math.sqrt((2 * BuildingHeight) / gravity)

distance = (velocity_ms * time_s)

print(f"The gun chosen was {gun} its cartridge is {cartridge}, its rounds are {rounds} and the bullets velocity was {velocity_ms}.m/s")
print("Its the product of the US-based company Desert Tech LLC MDR rifle is a modular, multi-caliber weapon with compact bullpup layout. Barrel lengths and calibers can be changed by the end user within minutes with a minimum amount of tools.")