import requests

url = "http://localhost:5000/generate"
data = {"prompt": "Who developed you?, Write a short poem about the sea."}

response = requests.post(url, json=data)

print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"Text: {response.text}")

try:
    print("JSON:", response.json())
except Exception as e:
    print("JSON decode error:", e)