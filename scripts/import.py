import json
import pymongo
import os
sys.path.append('../')
from import_config import load_config
from pymongo import MongoClient

#load in config file

config = load_config()

#initialize connection to mongodb

client = MongoClient(config["database"]["connection_url"])

db = client[config['database']['database_name']]
conn = db[config['database']['collection_name']]


#read in all files in the directory


for filename in os.listdir(os.getcwd()):


#load json objects 



#insert one by one into mongodb


