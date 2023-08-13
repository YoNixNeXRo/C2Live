from git import Repo
from os import walk
from os.path import join
from elasticsearch import Elasticsearch
from datetime import datetime
from requests import Session
from uuid import uuid4

## cloen repo
## loop sur les data sauf all

## load into elastic db

def clone_repo(repo_url:str):
    Repo.clone_from(repo_url, "data")

def loop_on_data():
    data = []
    for root, dirs, files in walk("data/data"):
        for file in files:

            if file != "all.txt":
                for ip in open(join(root, file), "r"):
                    name = file.replace("IPs.txt", "")
                    ip = ip.replace("\n", "").replace("\r", "")

                    data.append({"framework": name, "ip": ip, "@timestamp": datetime.strftime(datetime.now(), "%Y-%m-%dT00:00:00+02:00")})
    return data


def insert_data(data, es):
    for d in data:
        print(d)
        req = es.create(index="c6", id=uuid4().__str__(), document=d, pipeline="geoip")
        print(req)


if __name__ == '__main__':
    clone_repo("https://github.com/montysecurity/C2-Tracker")
    data = loop_on_data()
    insert_data(data, Elasticsearch(["http://localhost:9200"], verify_certs=False))