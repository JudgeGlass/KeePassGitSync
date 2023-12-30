""" CONSOLE """

# Copyright (c) 2023 Hunter Wilcox
# https://www.judgeglass.net

import logging
import argparse
import sys
import importlib.metadata

from keepassgitsync import CWD
from keepassgitsync.backup import init_repo, init_config, start_watchdog

def arg_handler() -> {}:
    parser = argparse.ArgumentParser(prog='KeePassGitSync', description='A tool that sync your KeePass database to a git repository')
    parser.add_argument('-V', '--verison', action='version', version="%(prog)s {version}".format(version=importlib.metadata.version('keepassgitsync')))
    parser.add_argument('-c', '--config', type=str, help="The JSON config file")

    parser.add_argument('-r', '--repoURL', type=str, help="SSH URL/Address to git repository", required="--config" not in sys.argv)
    parser.add_argument('-d', '--databaseFile', type=str, help="The name of the KeePass database file in the repository", required="--config" not in sys.argv)
    parser.add_argument('-l', '--location', type=str, help="The directory you want to keep the KeePass database repository", required="--config" not in sys.argv)

    return vars(parser.parse_args())

def exception_handler(exception: Exception):
    print(f"ERROR: {exception}")
    logging.exception(exception)

def main():
    args = arg_handler()

    print("KeePassGitSync, by Hunter Wilcox. Visit https://judgeglass.net/")
    print(f"\nLogging to {CWD}/output.log\n")

    logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s", filename='output.log', filemode='w', level=logging.INFO)

    try:
        init_config(args)
        init_repo()
        start_watchdog()
    except Exception as e:
        exception_handler(e)
    finally:
        print("\nExiting....")
        print(f"Log saved to {CWD}/output.log\n\n")