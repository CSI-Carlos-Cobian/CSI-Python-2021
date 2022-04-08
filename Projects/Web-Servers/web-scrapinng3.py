import requests
import bs4

res = requests.get("https://sanignacio.pr")
res.raise_for_status()

SanIgnaciopr = bs4.BeautifulSoup(res.text, "html.parser")

elems = SanIgnaciopr.select("title")

print(type(SanIgnaciopr))
print(len(elems))

print(str(elems))

print(elems[0].getText())