from git import Repo
from os import walk, getcwd, chmod, remove, rmdir, getenv
from os.path import join, exists
from elasticsearch import Elasticsearch
from stat import S_IWUSR
from datetime import datetime
from uuid import uuid4
from argparse import ArgumentParser
from logging import basicConfig, INFO, getLogger

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"


def clone_repo(repo_url: str, dest):
    getLogger(__name__).info(clone_repo.__name__)
    getLogger(__name__).debug(f"repo_url : {repo_url}\ndest: {dest}")
    repo = Repo.clone_from(repo_url, dest)
    return repo


def get_repo_history(repo, days):
    getLogger(__name__).info(loop_on_data.__name__)
    getLogger(__name__).debug(f"repo : {repo}")
    list_commit = repo.iter_commits('main', max_count=days)
    for commit in list_commit:
        getLogger(__name__).info(f"commit ID : {commit} - commit message : {repr(commit.message)} - "
                                 f"commit date : {commit.committed_datetime}")
        if commit.message == "Nightly Auto Update\n":
            repo.git.checkout(commit)
            commit_data = loop_on_data(join(config.local_path, "data"), commit.committed_datetime)
            insert_data(commit_data, Elasticsearch([config.elastic_url], verify_certs=config.elastic_verify),
                        config.elastic_index)


def loop_on_data(path, date=None) -> list:
    getLogger(__name__).info(loop_on_data.__name__)
    getLogger(__name__).debug(f"path : {path}")
    data = []
    if date is None:
        date = datetime.now()
    for root, dirs, files in walk(path):
        for file in files:

            if file != "all.txt":

                for ip in open(join(root, file), "r"):
                    name = file.replace("IPs.txt", "").rstrip()
                    ip = ip.replace("\n", "").replace("\r", "")

                    data.append({"framework": name, "ip": ip, "@timestamp": datetime.strftime(
                        date, "%Y-%m-%dT00:00:00+02:00")})
    return data


def insert_data(data, es, index):
    getLogger(__name__).info(insert_data.__name__)
    getLogger(__name__).debug(f"data : NotPrinted\nes: {es}\nindex : {index}")
    for d in data:
        req = es.create(index=index, id=uuid4().__str__(), document=d, pipeline="geoip")


def rmtree(top):
    getLogger(__name__).info(rmtree.__name__)
    getLogger(__name__).debug(f"top : {top}")
    for root, dirs, files in walk(top, topdown=False):
        for name in files:
            filename = join(root, name)
            chmod(filename, S_IWUSR)
            remove(filename)
        for name in dirs:
            rmdir(join(root, name))
    rmdir(top)


def get_config():
    getLogger(__name__).info(get_config.__name__)
    parser = ArgumentParser(
        prog="C2Live Injector",
        description="Ingest C2 data"
    )
    parser.add_argument("--elastic-url", "-u", type=str, help="elasticsearch url", required=True)
    parser.add_argument("--elastic-index", "-i", type=str.lower, default="C20", help="elasticsearch index")
    parser.add_argument("--elastic-verify", "-ev", type=bool, default=False, help="elasticsearch verify URL")
    parser.add_argument("--data-url", "-d", type=str, default="https://github.com/montysecurity/C2-Tracker.git",
                        help="Data source github repository")
    parser.add_argument("--local-path", "-l", type=str, default=join(getcwd(), "data"), help="Local path")
    parser.add_argument("--log-level", "-ll", type=str, default=None, help="Log Level")
    parser.add_argument("--days", "-n", type=int, default=0, help="Number of history days")

    args = parser.parse_args()
    return args


def init_logging():
    basicConfig(level=INFO, format=f"[{BLUE}%(levelname)s{RESET}] - [{YELLOW}%(asctime)s{RESET}] - [{GREEN}%(name)s{RESET}] - %(message)s")
    return getLogger(__name__)


if __name__ == '__main__':
    init_logging()
    config = get_config()
    if exists(config.local_path):
        rmtree(config.local_path)
    r = clone_repo(config.data_url, config.local_path)

    if config.days > 0:
        get_repo_history(r, config.days)
    elif config.days == 0:
        all_data = loop_on_data(join(config.local_path, "data"))
        insert_data(all_data, Elasticsearch([config.elastic_url], verify_certs=config.elastic_verify), config.elastic_index)
    rmtree(config.local_path)
