from cgi import print_directory
import requests
res = requests.get(https://www.gutenberg.org/ebooks/67637)
type(res)
res.status_code == requests.code.ok
len(res.text)
print