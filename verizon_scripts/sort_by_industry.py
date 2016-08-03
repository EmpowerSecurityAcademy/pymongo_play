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

# pull all incidents from mongodb and sort DESCENDING by victim.industry

# data = conn.find().sort("victim.industry", pymongo.DESCENDING)

# export them to a json file

# json_export(data, "../tmp/sort_by_industry.json")