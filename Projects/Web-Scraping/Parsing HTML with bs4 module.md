# Parsing HTML
According to Al Sweigart, BeautifulSoup or bs4 is a module for extracting information from an HTML page. To install it, you will need to run(from the commandline):

For Windows:
```python
>>>pip install --user beautifulsoup4 
```
For Mac:
```python
>>>pip3 
>>>pip3 install --user beautifulsoup4 
```

## BeautifulSoup function
The *bs4.BeautifulSoup()* function needs to be called with a string containing the HTML it will parse. The *bs4.BeautifulSoup()* function returns a *BeautifulSoup* 

Open a new terminal and enter the following into the interactive shell:
```python
>>>import requests
>>>import bs4
>>>res = requests.get('https://www.sanignacio.pr')
>>>res.raise_for_status()
>>>SanIgnaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
>>>type(SanIgnaciopr)
```
This code uses *requests.get* to download the main page from the San Ignacio website and then passes the text atrribute of the response to *bs4.BeautifulSoup()*. The BeautifulSoup object that it returns is stored in a variable named SanIgnaciopr. Once yout have a BeautifulSoup Object you can use its methods to find specific parts of an HTML document. 

You can retrieve a web page element from a BeautifulSoup object by calling the *select()* method and passing a string of a CSS selector for the elements you ar looking for. Selectors are like regular expressions: the specify a pattern to look for, in HTML pages instead of general text strings.  The *select* method will return a list of *Tag objects*, which is how BeautifulSoup represents an HTML element. 

Enter the following in the interactive shell:
```python
>>>import requests
>>>import bs4
>>>res = requests.get('https://www.sanignacio.pr')
>>>res.raise_for_status()
>>>SanIgnaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
>>>elems = SanIgnaciopr.select('#author')
>>>type(SanIgnaciopr)
>>>len(elems)
```

### References: 
Sweigart, A. (2020). *Automate the boring stuff with Python*. San Francisco. pages 268-300.
