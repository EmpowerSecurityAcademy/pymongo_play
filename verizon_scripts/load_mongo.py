import pymongo
import sys
sys.path.append('../helpers')
from import_config import load_config
from pymongo import MongoClient

#load in config file



#initialize connection to mongodb




#read in all files in the directory

for file_name in glob.glob("../verizon_data_json/*.json"):

#	load json objects 





#		insert one by one into mongodb


