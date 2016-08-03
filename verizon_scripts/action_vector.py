import pymongo
import sys
sys.path.append('../helpers')
from import_config import load_config
from save_to_json import json_export
from pymongo import MongoClient

# load in config file

# config = load_config()

# initialize connection to mongodb

# client = MongoClient(config["database"]["connection_url"])
# db = client[config['database']['database_name']]
# conn = db[config['database']['collection_name']]

# pull all incidents from mongodb that have the field action.misuse.vector set to LAN access

# data = conn.find({"action.misuse.vector": "LAN access"})

# export them to a csv file

# json_export(data, "../tmp/action_vector.json")