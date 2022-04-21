import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67893/pg67893.txt")
res.raise_for_status()
playFile = open("Projects/Web-Scraping/The Rover Boys Shipwrecked.txt", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
