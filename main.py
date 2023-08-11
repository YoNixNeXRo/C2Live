from git import Repo
from os import walk
from os.path import join

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
                    # print(f"{name} - {ip}")
                    data.append({"name": name, "ip": ip})
    print(data)


if __name__ == '__main__':
    clone_repo("https://github.com/montysecurity/C2-Tracker")
    loop_on_data()