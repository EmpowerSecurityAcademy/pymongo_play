import json
from bson import json_util
import pandas

def json_export(data, file_name):

	with open(file_name, 'w') as outfile:
		json_docs = []
		for doc in data:
		    json_doc = json.dumps(doc, default=json_util.default)
		    json_docs.append(json_doc)
		json.dump(json_docs, outfile, indent=2)