""" CONFIG """

from keepassgitsync import CWD

import json

def load_config(args: {}) -> {}:
    config_data = {}

    with open(f"{CWD}/config.json") as config_json:
        config_data = json.load(config_json)

    if args != None:
        config_data = load_config_cmd_args(config_data, args)

    return config_data
    
def load_config_cmd_args(config: {}, args: {}) -> {}:
    for arg in args:
        config[arg] = args[arg]

    return config
    

