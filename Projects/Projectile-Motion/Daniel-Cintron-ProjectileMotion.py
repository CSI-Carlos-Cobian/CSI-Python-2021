import math

# gun = "DT MDR"
# cartridge = "5.56x45mm"
# rounds = "HP" 
# velocity_ms = 941

# Building = "Minillas South Tower"
# BuildingHeight = 244

# gravity = 9.81


def ProjectileFunction(gun:str, cartridge:str, rounds:str, velocity_ms:int, Building:str, Buildingsweight:str, gravity:str)
time_s = math.sqrt((2 * BuildingHeight) / gravity)

distance = (velocity_ms * time_s)

print(f"The gun chosen was {gun} its cartridge is {cartridge}, its rounds are {rounds} and the bullets velocity was {velocity_ms}.m/s")
print("Its the product of the US-based company Desert Tech LLC MDR rifle is a modular, multi-caliber weapon with compact bullpup layout. Barrel lengths and calibers can be changed by the end user within minutes with a minimum amount of tools.")

ProjectileFunction("DT MDR", "5.56x45mm", "HP", 941, "Minillas South Tower", 244, 9.81)