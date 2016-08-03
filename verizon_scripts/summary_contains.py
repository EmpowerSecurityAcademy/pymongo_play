import pymongo
import sys
sys.path.append('../helpers')
from import_config import load_config
from save_to_json import json_export
from pymongo import MongoClient

#load in config file

config = load_config()

#initialize connection to mongodb

client = MongoClient(config["database"]["connection_url"])
db = client[config['database']['database_name']]
conn = db[config['database']['collection_name']]

# find all incidents where the word 'patient' exists in the summary field

data = conn.find({"summary": {'$regex':'patient'}})

# export to a json file

json_export(data, "../tmp/summary_contains.json")