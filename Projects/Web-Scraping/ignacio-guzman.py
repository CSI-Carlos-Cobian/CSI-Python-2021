import bs4 
examplefile = open ("example.htmml")
exampleSou = bs4.BeatifulSoup(examplefile.read(), "html.parser")
elems = exampleSoup..select("#author")
type(elems)
print (len(elems))
type(elems{0})
str(elem{)}
print(elems){0},getText()