import requests

url = "http://localhost:8000/polls/api/questions/1/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2NTQ3MzgzLCJpYXQiOjE3MjY1NDcwODMsImp0aSI6IjM0Y2Y0MTg1NDI2ODQ4ZTk5MTExMTk3NWE5NjA2Nzg4IiwidXNlcl9pZCI6MX0.XyJ0j4UxCY6MDfGYOSp1WkdYpByh8H1JUlHWZys5Ep0"
}

response = requests.get(url, headers=headers)
print(response.json())
