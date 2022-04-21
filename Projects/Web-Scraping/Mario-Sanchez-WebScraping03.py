import requests
import bs4
# res = requests.get("https://www.sanignacio.pr/")
# SanIgnacioPR = bs4.BeautifulSoup(res.content, "html.parser")
# elems = SanIgnacioPR.select("title")
# print(len(elems))
# print(str(elems))
# print(elems[0].getText)
site = requests.get("https://www.sanignacio.pr/sobre-csi/historia-del-colegio")
data = bs4.BeautifulSoup(site.content, "html.parser")
elems = data.select("p")
print(len(elems))
print(elems[2].getText())
print(elems[3].getText())