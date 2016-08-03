import json
from bson import json_util
import pandas

def json_export(data, file_name):

	with open(file_name, 'w') as outfile:
		json_docs = []
		for doc in data:
		    json_doc = json.dumps(doc, default=json_util.default)
		    modified = json.loads(json_doc)
		    json_docs.append(modified)
		json.dump(json_docs, outfile, indent=2)