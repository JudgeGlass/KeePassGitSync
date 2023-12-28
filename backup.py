# Copyright (c) 2023 Hunter Wilcox
# https://www.judgeglass.net

from git import Repo
from os import getcwd, path, remove
from shutil import rmtree
from tkinter import messagebox
from sys import stdin

import platform
import time
import json

IS_TTY: bool = stdin.isatty()

CWD = getcwd()
HOSTNAME = platform.node()

def load_config() -> {}:
    data = {}
    with open(f"{CWD}/config.json") as config_json:
        data = json.load(config_json)
    return data

config = load_config()

def get_config_attrib(key: str) -> str:
    return config[key]

def show_message(title: str, msg: str) -> None:
    if get_config_attrib("showMessages"):
        messagebox.showinfo(title, msg)

def show_error(title: str, msg: str) -> None:
    if get_config_attrib("showMessages"):
        messagebox.showerror(title, msg)

def get_repo_name() -> str:
    REPO_URL = get_config_attrib("repoURL")
    return REPO_URL[REPO_URL.index('/') : len(REPO_URL) - 4]

CWD_REPO: str = f"{get_config_attrib('location')}{get_repo_name()}"

def clone_repo() -> None:
    REPO_URL = get_config_attrib("repoURL")
    print(f"Cloning repo: {REPO_URL}")
    global repo
    repo = Repo.clone_from(REPO_URL, CWD_REPO)

def check_dir_exists(name: str) -> bool:
    return path.exists(name)

def start_watchdog() -> None:
    DATABASE_FILE = get_config_attrib("databaseFile")
    init_filesize: int = path.getsize(f"{CWD_REPO}/{DATABASE_FILE}")
    while True:
        print("Checking for database changes....")
        current_filesize: int = path.getsize(f"{CWD_REPO}/{DATABASE_FILE}")

        if init_filesize != current_filesize and current_filesize > 0:
            print(f"Current size: {current_filesize}\tExpected size: {init_filesize}")
            # Update Github
            print("Updating git...")
            show_message("KeePassGitSync: Updating Database", f"KeePassGitSync has detected that {CWD_REPO} has changed. Syncing with git...")
            repo.index.add([DATABASE_FILE])
            repo.index.commit(f"(KeePassGitSync) {HOSTNAME}")
            repo.remote().push()
            init_filesize = current_filesize
        time.sleep(get_config_attrib("updateFrequency"))


def main() -> None:
    print("KeePassGitSync tool. By Hunter Wilcox")
    try:
        if check_dir_exists(CWD_REPO):
            print("Repo already cloned. Pulling...")
            repo = Repo.init(CWD_REPO)
            repo.remote().pull()
        else:
            print("Cloning repo...")
            clone_repo()
    except Exception as e:
        print("Error cloning repo. Do you have SSH Key set?")
        print(e)
        exit()

    start_watchdog()


if __name__ == "__main__":
    main()
