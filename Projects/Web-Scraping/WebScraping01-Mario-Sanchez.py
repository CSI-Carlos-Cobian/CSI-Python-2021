import webbrowser
import requests

# webbrowser.open("https://www.sanignacio.pr/")
res = requests.get("https://www.automatetheboringstuff.com/files/rj.txt")
print(len(res.text))
print(res.text[:300])