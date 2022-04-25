import requests
import bs4
site = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.3149&lon=-65.2887#.Yma5xufMJyw")
data = bs4.BeautifulSoup(site.content, "html.parser")
elems = data.select("p")
for i in range(4):
    print(elems[i+12].getText())