# import statements
import json, ssl
import urllib.request
from Lorem_Ipsum import Lorem_Ipsum
from pathlib import Path
import os

ssl._create_default_https_context = ssl._create_unverified_context # setting up secure connection for when looking up the api

ipsumURL = "https://random-data-api.com/api/lorem_ipsum/random_lorem_ipsum?size=100" #url calling 100 json objects
ipsumList:Lorem_Ipsum = [] # empty list created

myPath = Path(__file__).parents[0] # gets the path for the json
myFolderPath = os.path.join(myPath, "requests") # info for file directory
os.mkdir(myFolderPath) # creates file directory

for i in range(100): # 100x for loop, will ensure 10k json objects
    req = urllib.request.Request(ipsumURL) # requests from the url that gets 100 json objects
    serializedData = json.loads(urllib.request.urlopen(req).read()) # loads and reads the request, creates serialized json info

    for r in serializedData: # for loop to look through the serialized jsons
        newIpsum:Lorem_Ipsum = Lorem_Ipsum(**r) # deserializes the next random ipsum
        ipsumList.append(newIpsum) # adds the newly created ipsum in the Lorem_Ipsum class to the list of ipsums
        print(newIpsum.uid) # prints the unique id
    
        newFilePath = os.path.join(myFolderPath, f"request{newIpsum.uid}.json") # creates a unique file name for the ipsum

        with open(newFilePath, 'w') as outfile: # opens up the new json file
            json.dump(newIpsum.__dict__, outfile) # dumps the new ipsum into the json file

