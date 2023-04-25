from requests import get, post

response = get("http://localhost:5000/weather/London").json()

print(response)