import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67627/pg67627.txt")
res.raise_for_status()
playFile = open("The Treasure Trail", "wb")
for chunk in res.iter_content(5000):
    playFile.write(chunk)
playFile.close()