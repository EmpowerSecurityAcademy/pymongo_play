import unicodecsv


def csv_export(data, file_name):

	file = unicodecsv.writer(open("../tmp/"+file_name, "wb"))
	for row in data:
		file.writerow([
				row["action"]["misuse"]["variety"],
				row["action"]["misuse"]["vector"],
				row["discovery_method"],
				row["incident_id"]
			])