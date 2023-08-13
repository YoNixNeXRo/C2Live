from git import Repo
from os import walk, getcwd, chmod, remove, rmdir
from os.path import join, exists
from elasticsearch import Elasticsearch
from stat import S_IWUSR
from datetime import datetime
from uuid import uuid4


def clone_repo(repo_url: str):
    Repo.clone_from(repo_url, "data", )


def loop_on_data() -> list:
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
        req = es.create(index="c6", id=uuid4().__str__(), document=d, pipeline="geoip")


def rmtree(top):
    for root, dirs, files in walk(top, topdown=False):
        for name in files:
            filename = join(root, name)
            chmod(filename, S_IWUSR)
            remove(filename)
        for name in dirs:
            rmdir(join(root, name))
    rmdir(top)


if __name__ == '__main__':
    if exists(join(getcwd(), "data")):
        rmtree(join(getcwd(), "data"))
    clone_repo("https://github.com/montysecurity/C2-Tracker")
    all_data = loop_on_data()
    insert_data(all_data, Elasticsearch(["http://localhost:9200"], verify_certs=False))
    rmtree(join(getcwd(), "data"))
