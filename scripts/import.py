import json
import pymongo
import glob
import sys
sys.path.append('../')
from import_config import load_config
from pymongo import MongoClient

#load in config file

config = load_config()

print config

#initialize connection to mongodb

client = MongoClient(config["database"]["connection_url"])

db = client[config['database']['database_name']]
conn = db[config['database']['collection_name']]


#read in all files in the directory


for file_name in glob.glob("../data_json/*.json"):

#	load json objects 


	with open(file_name) as data_file:
		data = json.load(data_file)
		print data

#		insert one by one into mongodb

		conn.insert_one(data)
