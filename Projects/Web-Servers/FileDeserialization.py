# import statements
from pathlib import Path
from Lorem_Ipsum import Lorem_Ipsum
import os
import json, ssl
import urllib.request

filePath = Path(__file__).parents[0] # gets the fils path for the json
myFile = os.path.join(filePath, "random_lorem_ipsum.JSON") # finds the json file through the determined path
serializedData = open(myFile) # opens the json file that was previously located
serializedData = json.load(serializedData) # loads the serialized json in the the variable

newLoremIpsum:Lorem_Ipsum = Lorem_Ipsum(**serializedData) # deserializes the info into an object
print(newLoremIpsum) # prints object contained in the variable