import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from selenium.webdriver.firefox.service import Service
import os


myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/geckodriver.exe"
s = Service(driverPath)

myOptions = Options()
myOptions.headless = True

driver = webdriver.Firefox(service = s)
driver.maximize_window()
driver.get("https://www.amazon.com/")
search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("chainsaw man manga")
search.send_keys(Keys.ENTER)
link = driver.find_element_by_class_name("a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
link = link.get_attribute("href")
print(link)

