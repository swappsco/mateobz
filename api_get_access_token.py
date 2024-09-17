import requests

url = "http://localhost:8000/api/token/"
data = {"username": "mateo", "password": "mateo321"}

response = requests.post(url, data=data)
print(response.json())
