from requests import get, post

response = get("http://192.168.16.95:5000/weather/ruston").json()

print(response)