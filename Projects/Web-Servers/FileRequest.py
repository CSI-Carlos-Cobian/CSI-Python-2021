import json, ssl
import urllib.request
from Lorem_Ipsum import Lorem_Ipsum
from pathlib import Path
import os

ssl._create_default_https_context = ssl._create_unverified_context

ipsumURL = "https://random-data-api.com/api/lorem_ipsum/random_lorem_ipsum"
ipsumList:Lorem_Ipsum = []

for i in range(100):
    req = urllib.request.Request(ipsumURL)
    serializedData = json.loads(urllib.request.urlopen(req).read())

    for r in serializedData:
        newIpsum:Lorem_Ipsum = Lorem_Ipsum(**r)
        ipsumList.append(newIpsum)
        print(newIpsum.id)
        
        myOutputPath = Path(__file__).parents[0] # gets the path for the json
        myOutputFilePath = os.path.join(myOutputPath, f'request_{i}.json')
        with open(myOutputFilePath, 'w') as outfile:
            json.dump([ipsum.__dict__ for ipsum in ipsumList], outfile)
            