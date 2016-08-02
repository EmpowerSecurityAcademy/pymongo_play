import unicodecsv


def export__all_data(data, file_name):

	file = unicodecsv.writer(open("../tmp/"+file_name, "wb"))
	for row in data:
		file.writerow(
				row["action"]["misuse"]["variety"],
				row["action"]["misuse"]["vector"],
				row["discovery_method"],
				row["incident_id"],
				row["timeline"]["incident"]["day"],
				row["timeline"]["incident"]["month"],
				row["timeline"]["incident"]["year"],
				row["summary"],
				row["state"],
				row["victim_id"],
			)