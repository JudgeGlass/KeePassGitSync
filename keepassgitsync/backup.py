import time
import logging

from keepassgitsync.config import load_config
from keepassgitsync.git import clone_repo, push_commit, init_existing_repo, get_repo_name

from os import path

repo = None
config = None


def check_dir_exists(name: str) -> bool:
    return path.exists(name)

def start_watchdog() -> None:
    DATABASE_FILE = config["databaseFile"]
    init_filesize: int = path.getsize(f"{config['CWD_REPO']}/{DATABASE_FILE}")

    logging.info("Waiting for database changes...")
    while True:
        current_filesize: int = path.getsize(f"{config['CWD_REPO']}/{DATABASE_FILE}")

        if init_filesize != current_filesize and current_filesize > 0:
            logging.info(f"'{DATABASE_FILE}' has changed!")
            
            push_commit([DATABASE_FILE], repo)
            init_filesize = current_filesize

            logging.info("Waiting for database changes...")

        time.sleep(config["updateFrequency"])

def init_config(args: {}):
    global config
    config = load_config(args)
    config["CWD_REPO"] = f"{config['location']}{get_repo_name(config)}"

def init_repo() -> None:    
    global repo

    if check_dir_exists(config["CWD_REPO"]):
        repo = init_existing_repo(config)
    else:
        repo = clone_repo(config)
