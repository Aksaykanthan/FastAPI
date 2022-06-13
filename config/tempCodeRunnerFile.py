import requests

x = requests.get('http://192.168.1.11:5000/users')

print(x.text)