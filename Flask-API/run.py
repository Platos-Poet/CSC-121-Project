from requests import get, post

response = get("http://138.47.138.189:5000/weather/ruston").json()

print(response)