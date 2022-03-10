# Web-Scraping (15 points)
*Web scrapping* is the term for using a program to download and process content from the web. In this lesson you will learnn several modules that make it easy to scrape web pages in Python.  This modules are:
- **webbrowser** - opens a browser to a specific page.
- **requests** - downloads files and web pages from the internet.
- **bs4** - parses HTML
- **selenium** - launces and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in the browser. 

## Open a specific URL
The *webbrowser* module's open() function can launch a new browser to a specified URL. Open a terminal and enter the following:
```python
>>>import webbrowser
>>>webbrowser.open("https://...")
```
## Downloading files from the Web with the requests Module
The *requests* module lets you download files from the web without having to worry about network or connection errors. You will have to install this module.  Fro the command line, run **pip install --user requests**. If possible that you will have to restart your PC. 

Open a new terminal and enter the following into it:
```python
>>>import requests
```
If no error messages shows up, then the module has benn installed correctly. 

### References: 
Sweigart, A. (2020). *Automate the boring stuff with Python*. San Francisco. pages 268-300

