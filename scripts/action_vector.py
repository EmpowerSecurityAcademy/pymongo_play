import json
import pymongo
import glob
import sys
sys.path.append('../')
sys.path.append('../helpers')
from import_config import load_config
from pymongo import MongoClient

#load in config file

config = load_config()

#initialize connection to mongodb

client = MongoClient(config["database"]["connection_url"])

db = client[config['database']['database_name']]
conn = db[config['database']['collection_name']]

data = conn.find({"action.misuse.vector": "LAN access"})

for element in data:
	print(element)