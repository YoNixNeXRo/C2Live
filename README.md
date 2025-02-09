# C2Live


C2Live is an open-source project aimed at providing a comprehensive and interactive platform for tracking C2 servers, tools, and botnets malicious IP addresses over time. This project focuses on categorizing and visualizing these IPs based on the framework they are associated with and the country they originate from. The goal is to help security professionals, researchers, and organizations gain insights into the evolving landscape of cyber threats. This project is based on [C2Tracker](https://github.com/montysecurity/C2-Tracker) from [@_montysecurity](https://twitter.com/_montysecurity).


Provided by [@Y_NeXRo](https://twitter.com/Y_NeXRo) and [ikuroNoriiwa](https://github.com/ikuroNoriiwa)  


![alt text](https://github.com/YoNixNeXRo/C2Live/blob/main/preview.jpg?raw=true)

The website version at [c2tracker.com](https://c2tracker.com))

## To run the project:
### Install requirements.txt
`pip3 install -r requirements.txt`
### lunch the docker compose
> Note: Make sure to have docker compose installed :)


`docker-compose -f elastic-grafana-docker-compose.yaml up`
### lunch the connectors.py 
`python3 connectors.py`  
It will create geoip pipeline,elastic connector to grafana and import a default dashboard.
### lunch main.py
#### Todays datas
`python3 main.py -u http://localhost:9200/  `  
It will ingest todays data so you will only have 1 day of data. 
#### Past datas
You can also ingest past datas  
`python3 main.py -u http://localhost:9200/ -n <number_of_history_commits>`  
> Note: number of history commits is normally equivalent of 1 day. So ingesting 10 history commits will ingest past 10 days datas.

 
You can enjoy grafana dashboard on `http://localhost:3000/ `  
creds are admin:admin

### main.py Usage 
```
usage: C2Live Injector [-h] --elastic-url ELASTIC_URL [--elastic-index ELASTIC_INDEX] [--elastic-verify ELASTIC_VERIFY] [--data-url DATA_URL] [--local-path LOCAL_PATH] [--log-level LOG_LEVEL] [--days DAYS]

Ingest C2 data

optional arguments:
  -h, --help            show this help message and exit
  --elastic-url ELASTIC_URL, -u ELASTIC_URL
                        elasticsearch url
  --elastic-index ELASTIC_INDEX, -i ELASTIC_INDEX
                        elasticsearch index
  --elastic-verify ELASTIC_VERIFY, -ev ELASTIC_VERIFY
                        elasticsearch verify URL
  --data-url DATA_URL, -d DATA_URL
                        Data source github repository
  --local-path LOCAL_PATH, -l LOCAL_PATH
                        Local path
  --log-level LOG_LEVEL, -ll LOG_LEVEL
                        Log Level
  --days DAYS, -n DAYS  Number of history commits from source url 

```
### make a cron with main.py to ingest data daily


