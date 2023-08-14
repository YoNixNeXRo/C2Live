import os
import requests
import json
from requests.auth import HTTPBasicAuth


# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the dashboard configuration file
config_file_path = os.path.join(script_dir, "dashboard.json")

# Load the dashboard configuration from the JSON file
with open(config_file_path, "r") as config_file:
    dashboard_json = json.load(config_file)

# Grafana API details
grafana_url = "http://localhost:3000/api/dashboards/db"
username = "admin"
password = "admin"

headers = {
    "Content-Type": "application/json"
}

auth = HTTPBasicAuth(username, password)

response = requests.post(grafana_url, headers=headers, auth=auth, json=dashboard_json)

print(response.status_code)
print(response.json())

