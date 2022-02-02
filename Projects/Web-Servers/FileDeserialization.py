from pathlib import Path
from Lorem_Ipsum import Lorem_Ipsum
import os
import json, ssl
import urllib.request

filePath = Path(__file__).parents[0]
myFile = os.path.join(filePath, "random_lorem_ipsum.JSON")
serializedData = open(myFile)
serializedData = json.load(serializedData)

newLoremIpsum:Lorem_Ipsum = Lorem_Ipsum(**serializedData)
print(newLoremIpsum)
