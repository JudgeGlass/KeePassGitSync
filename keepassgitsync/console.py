""" CONSOLE """

# Copyright (c) 2023 Hunter Wilcox
# https://www.judgeglass.net

import logging

from keepassgitsync.backup import init_repo, init_config, start_watchdog

def main():
    print("KeePassGitSync, by Hunter Wilcox. Visit https://judgeglass.net/")
    print("Check 'output.log' to view program log.")
    logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s", filename='output.log', filemode='w', level=logging.INFO)

    args = None

    init_config(args)
    init_repo()
    start_watchdog()