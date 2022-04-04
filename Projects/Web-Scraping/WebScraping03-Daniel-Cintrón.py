import bs4
exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select("#author")
type(elems)
print(len(elems))
type(elems[0])
str(elems[0])
print(elems[0].getText())
