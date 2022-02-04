import json, ssl
import urllib.request
from pathlib import Path
import os

while(True):
    req = urllib.request.Request("http://192.168.0.101/")
    print(urllib.request.urlopen(req).read())