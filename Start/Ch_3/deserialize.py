# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []

# open the CSV file for reading
with open("largequakes.csv") as csvfile:
    reader = csv.reader(csvfile)
    
    # to detect header
    sniffer = csv.Sniffer()
    sample = csvfile.read(1024)
    # seek back to the begining after detection
    csvfile.seek(0)
    if (sniffer.has_header(sample)):
        # skip header (1st row)
        next(reader)

    for row in reader:
        # print(row)
        result.append({
            "place": row[0],
            "magnitude": row[1],
            "date": row[3],
            "link": row[2]
        })

pprint.pp(result)
