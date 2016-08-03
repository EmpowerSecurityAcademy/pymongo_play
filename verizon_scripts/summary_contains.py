import json
import pymongo
import glob
import sys
sys.path.append('../helpers')
from import_config import load_config
from save_to_csv import export__all_data
from pymongo import MongoClient

#load in config file

config = load_config()

#initialize connection to mongodb

client = MongoClient(config["database"]["connection_url"])

db = client[config['database']['database_name']]
conn = db[config['database']['collection_name']]

data = conn.find({"action.misuse.vector": "LAN access"})

export__all_data(data, "action_vector.csv")