import time
import os
import json
import requests
from colorama import Fore, Style
from tqdm import tqdm
from requests.auth import HTTPBasicAuth

# Function to simulate the execution of a script and return its return code
def simulate_script_execution(description):
    pbar = tqdm(total=100, desc=description, bar_format="{desc}: {percentage:3.0f}%|{bar:10}|")
    time.sleep(3)  # Simulate script execution
    pbar.update(100)  # Mark the progress as 100% after completion
    pbar.close()
    return 0  # Simulate successful execution

# Function to create GeoIP pipeline
def create_geoip():
    description = "Creating GeoIP Pipeline"
    print(f"{Fore.YELLOW}Executing {description}...{Style.RESET_ALL}")
    time.sleep(2)  # Sleep for 2 seconds
    
    try:
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
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}{description} executed successfully{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}{description} failed with status code {response.status_code}{Style.RESET_ALL}")
            return False
    except Exception as e:
        print(f"{Fore.RED}Error executing {description}: {e}{Style.RESET_ALL}")
        return False

# Function to create Elastic Datasource
def create_elastic_datasource():
    description = "Creating Elastic Datasource"
    print(f"{Fore.YELLOW}Executing {description}...{Style.RESET_ALL}")
    time.sleep(2)  # Sleep for 2 seconds
    
    try:
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
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}{description} executed successfully{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}{description} failed with status code {response.status_code}{Style.RESET_ALL}")
            return False
    except Exception as e:
        print(f"{Fore.RED}Error executing {description}: {e}{Style.RESET_ALL}")
        return False

# Function to send JSON to Grafana
def send_json_to_grafana():
    description = "Sending JSON to Grafana"
    print(f"{Fore.YELLOW}Executing {description}...{Style.RESET_ALL}")
    time.sleep(2)  # Sleep for 2 seconds
    
    try:
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
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}{description} executed successfully{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}{description} failed with status code {response.status_code}{Style.RESET_ALL}")
            return False
    except Exception as e:
        print(f"{Fore.RED}Error executing {description}: {e}{Style.RESET_ALL}")
        return False

if __name__ == "__main__":
    create_geoip_success = create_geoip()
    if not create_geoip_success:
        print(f"{Fore.RED}Installation process encountered errors. Stopping the process.{Style.RESET_ALL}")
        exit(1)
    
    create_elastic_datasource_success = create_elastic_datasource()
    if not create_elastic_datasource_success:
        print(f"{Fore.RED}Installation process encountered errors. Stopping the process.{Style.RESET_ALL}")
        exit(1)
    
    send_json_to_grafana_success = send_json_to_grafana()
    if not send_json_to_grafana_success:
        print(f"{Fore.RED}Installation process encountered errors. Stopping the process.{Style.RESET_ALL}")
        exit(1)
    
    print(f"{Fore.GREEN}Installation process completed successfully.{Style.RESET_ALL}")

    print(f"{Fore.GREEN}run main.py and check grafana dashboard at http://localhost:3000/.{Style.RESET_ALL}")
