import requests

url = "http://127.0.0.1:5000/test"
response = requests.get(url)
print(response.text)
