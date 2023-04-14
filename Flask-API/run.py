from requests import get, post

response = get("http://localhost:1234/first").json()

print(response["response"])


response = post("http://localhost:1234/numberInspector", json={"value": 14}).json()
print(response)