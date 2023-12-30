import logging

from keepassgitsync import HOSTNAME
from git import Repo

def clone_repo(config: {}) -> Repo:
    REPO_URL = config["repoURL"]
    logging.info(f"Cloning repo: {REPO_URL}")
    REPO_URL = config["repoURL"]
    return Repo.clone_from(REPO_URL, config['CWD_REPO'])

def init_existing_repo(config: {}) -> Repo:
    logging.info(f"Repo already cloned! Using: {config['CWD_REPO']}")
    repo = Repo.init(config["CWD_REPO"])
    repo.remote().pull()
    return repo

def push_commit(files: [], repo: Repo):
    logging.info("Pushing commit...")
    repo.index.add(files)
    repo.index.commit(f"(KeePassGitSync) {HOSTNAME}")
    repo.remote().push()

def get_repo_name(config: {}) -> str:
    REPO_URL = config["repoURL"]
    return REPO_URL[REPO_URL.index('/') + 1: len(REPO_URL) - 4]