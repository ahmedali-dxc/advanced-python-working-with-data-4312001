# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
def getdate(quake):
    return quake["properties"]["time"]

def getsig(quake):
    sig = quake["properties"]["sig"]
    return 0 if sig is None else sig

mostsignificants = sorted(data["features"], key=getsig, reverse=True)
mostsignificants = mostsignificants[:40]
# mostsignificants.sort(key=getdate, reverse=True)
mostsignificants.sort(key=lambda quake: quake["properties"]["time"], reverse=True)

# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map link"]
rows = []

for significant in mostsignificants:
    thedate = datetime.date.fromtimestamp(int(significant["properties"]["time"] / 1000))
    longitude, latitude, _ = significant["geometry"]["coordinates"]
    felt = significant["properties"]["felt"]
    rows.append([
        significant["properties"]["mag"],
        significant["properties"]["place"],
        0 if felt is None else felt,
        thedate,
        f"https://maps.google.com/maps/search/?api=1&query={latitude},{longitude}"
    ])

with open("mostsignificants.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
