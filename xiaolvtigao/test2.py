import requests

url = 'https://www.5jcd.com/play/138775-2-1.html'

resp = requests.get(url)

print(resp.text)