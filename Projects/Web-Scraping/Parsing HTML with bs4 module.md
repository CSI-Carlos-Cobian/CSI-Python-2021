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

Open a new terminal and enter the following into it:
```python
>>>import requests
>>>import bs4
>>>res = requests.get('https://www.sanignacio.pr')
>>>res.raise_for_status()
>>>SanIgnaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
>>>type(SanIgnaciopr)
```
The code uses *requests.get* to download the main page from the San Ignacio website and then passes the text atrribute of the response to *bs4.BeautifulSoup()*. The BeautifulSoup object that it returns is stored in a variable named SanIgnaciopr.

The request.get()function takes a string of a URL to download. By calling *type()* on *requests.get()*'s return value, you can see that it returns a *Response* object, which contains the response that the web server gave for your request. 

