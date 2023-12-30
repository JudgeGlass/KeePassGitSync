""" CONFIG """

from keepassgitsync import CWD

import json
import logging

def load_config(args: {}) -> {}:
    config_data = {}

    config_location = f"{CWD}/config.json"

    if args['config']:
        config_location = args['config']

    logging.info(f"Using config file. ('{config_location}')")

    with open(config_location) as config_json:
        config_data = json.load(config_json)

    if args != None:
        config_data = load_config_cmd_args(config_data, args)

    return config_data
    
def load_config_cmd_args(config: {}, args: {}) -> {}:
    for arg in args:
        if args[arg]:
            config[arg] = args[arg]

    return config
    

