import requests

url = "http://localhost:9200/_ingest/pipeline/geoip"

headers = {
    "Content-Type": "application/json"
}

data = {
    "description": "Add geoip info",
    "processors": [
        {
            "geoip": {
                "field": "ip"
            }
        }
    ]
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

