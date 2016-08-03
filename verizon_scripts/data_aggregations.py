import pymongo
import sys
sys.path.append('../helpers')
from import_config import load_config
from save_to_json import json_export
from pymongo import MongoClient

# load in config file

config = load_config()

# initialize connection to mongodb

client = MongoClient(config["database"]["connection_url"])
db = client[config['database']['database_name']]
conn = db[config['database']['collection_name']]

# write a query that aggregates the field action.hacking.vector
# and provide a count of the number of each incidents per unique value, export as a list

query = [
	{"$unwind": "$action.hacking.vector"},
	{"$group": {"_id": "$action.hacking.vector", "count": {"$sum": 1}}},
]

data = list(conn.aggregate(query))

# export them to a json file

json_export(data, "../tmp/data_aggregations.json")