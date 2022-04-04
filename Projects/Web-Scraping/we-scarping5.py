
import requests
import bs4

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=18.3808&lon=-65.9574#.Yks0w27MJQI")
forecast = bs4.BeautifulSoup(website.content , "html.parser")
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]
# period = tonight.find(class_="period-name").get_text()
# print(period)
print(tonight.prettify())
 print (tonight,prettify())
R11
period - tonight. find(class_-"period-namelD-get_text()
12
print (period)
13
14
short desc = tonight. find(class_-"short-desc"').get text()
print (short desc)
25
temp = tonight. find(class_-"low low-temp").get_text()
16
print (temp)
