# C2Live: Tracking C2 Malicious IPs Over Time


C2Live is an open-source project aimed at providing a comprehensive and interactive platform for tracking Command and Control (C2) malicious IP addresses over time. This project focuses on categorizing and visualizing these IPs based on the framework they are associated with and the country they originate from. The goal is to help security professionals, researchers, and organizations gain insights into the evolving landscape of cyber threats. This project is based on [C2Tracker](https://github.com/montysecurity/C2-Tracker) from [@_montysecurity](https://twitter.com/_montysecurity).


Provided by [@Y_NeXRo](https://twitter.com/Y_NeXRo) and [@ikuroNoriiwa](https://twitter.com/ikuroNoriiwa)  


![alt text](https://github.com/YoNixNeXRo/C2Live/blob/main/preview.jpg?raw=true)


### To run the project:
#### Install requirements.txt
`pip install -r requirements.txt`
#### lunch the docker compose
> Note: Make sure to have docker compose installed :)


`docker-compose -f elastic-grafana-docker-compose.yaml up`
#### lunch the connectors.py 
`python3 connectors.py`
It will create geoip pipeline,elastic connector to grafana and import a default dashboard.
#### lunch main.py
`python3 main.py -u http://localhost:9200/  `  
It will ingest todays data so you will only have 1 day of data.  
You can enjoy grafana dashboard on `http://localhost:3000/ `  
creds are admin:admin
#### make a cron with main.py to ingest data daily
