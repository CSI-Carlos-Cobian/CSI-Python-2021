<div style="text-align:center">
        <img    src="https://sparkyway.com/wp-content/uploads/2017/05/1-ISR0kaBJfjxXoakSF1JiJg.jpeg"
                width="20%" 
                height="20%" />
                
</div>
<br>

# API Calls `(100pts)`
* Your script must be fully documented (`# Inline documentation at every step`).

### Select the API you will be using from [Random Data API](https://random-data-api.com/documentation) `(15pts)`
* Store a sample JSON in the project folder. It must be named after the API you've selected eg. `random_address.json`
* Format the document. Do so by right clicking on VS Code and selecting the `Format Document` option. Alternatively `Alt+Shift+f` will work.
* Commit the file.


### Create a class for the request. `(15pts)`
Recall when we made a class called `ExperimentData` in Projectile-Motion. Create a file in your project folder named `Entities.py`
* Create a class within this file named after your object eg. `class Address:`
* Create a constructor with all variables in the sample json.
* Define the data types in the constructor parameter list.
* Commit the file.

<br>

# Load a file: `(20pts)`
* Create a file named `FileDeserialization.py`
* Load the created JSON file into the Class.
* Print each variable by addressing the class.



```python
import json
import os
from pathlib import Path
from Entities import Address

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_address.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
address:Address = Address(**data)

# Print data from the object
print(f"ID: {address.id}")
print(f"UID: {address.uid}")
print(f"Street Name: {address.street_name}")
print(f"Longitude: {address.longitude}")
print("Others expected...")
```

<br>

# Deserialize a request. `(20pts)`

* Create a file named `RequestDeserialization.py`
* Load the fetched JSON file into the Class.

[How to use urllib](https://docs.python.org/3/howto/urllib2.html)

```python
import json, ssl
import urllib.request
from Entities import Address

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
addressURL = "https://random-data-api.com/api/address/random_address?size=100"

# Create a list to populate with our data
addresses:Address = [] 

# Execute HTTP Request
req = urllib.request.Request(addressURL)
requestData = json.loads(urllib.request.urlopen(req).read())

# Loop over JSON items and Deserialize them into python objects
for r in requestData:  
    # Deserialize 
    address:Address = Address(**r)
    # Add object to list
    addresses.append(address) 

    myOutputFilePath = os.path.join(myOutputPath, f"request{address.id}.json")
    with open(myOutputFilePath, 'w') as outfile:
        json.dump(address, outfile)
```

# Store 10,000 Requests `(30pts)`
* [Programmatically create a folder](https://www.geeksforgeeks.org/create-a-directory-in-python/) within your project directory named `responses`.
* Store 10,000 requests into this folder. Use separate files for each record.
* Do not commit these files. Add `Projects/Web-Servers/responses` to your `.gitignore`.
* You must show the code fetching the records and storing them to your professor in order to gain these points.


## Pseudocode
```
Store path in variable
Join path with folder name
make directory
loop (100)
    HTTP Request
    loop (request items 100)
        Deserialize data
        create unique path filename inside of requests folder
        Save request
```