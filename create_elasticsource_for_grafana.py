import requests
from requests.auth import HTTPBasicAuth

grafana_url = "http://localhost:3000/api/datasources"
username = "admin"
password = "admin"

headers = {
    "Content-Type": "application/json"
}

auth = HTTPBasicAuth(username, password)

data = {
    "name": "elasticsearch",
    "type": "elasticsearch",
    "url": "http://elasticsearch:9200",
    "access": "proxy",
    "jsonData": {
        "esVersion": 7,
        "index": "c20",
        "timeField": "@timestamp",
        "interval": "Daily"
    },
    "secureJsonFields": {},
    "version": 1,
    "editable": True,
    "uid": "e4994ccf-a285-445f-be54-8c393490c47f"
}

response = requests.post(grafana_url, headers=headers, auth=auth, json=data)

print(response.status_code)
print(response.json())

