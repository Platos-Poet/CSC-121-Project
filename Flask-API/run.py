from requests import get, post

response = get("http://138.47.139.207:5000/weather/ruston").json()

print(response)