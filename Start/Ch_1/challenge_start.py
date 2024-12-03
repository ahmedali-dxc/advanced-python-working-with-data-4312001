# Python code​​​​​​‌‌​​​​‌‌‌​​‌‌​‌​‌​‌​‌​‌​​ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = False

import json


TotalEvents = 0
TotalFelt = 0
MostFeltEvent = ""
MostFeltCount = 0

def calc_summary():
    global TotalEvents, TotalFelt, MostFeltEvent, MostFeltCount
    # open the data file and load the JSON
    with open("/tmp/deps/30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)

    # YOUR CODE GOES HERE
    # Calculate the values

    # How many quakes are there in total?
    TotalEvents = len(data["features"])
    # How many quakes were felt by at least 100 people?
    TotalFelt = sum(
        quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100 
            for quake in data["features"]
    )
    # What is the name of the place whose quake was felt by the most people
    maxFeltQuake = max(data["features"], key=getfelt)
    MostFeltEvent = maxFeltQuake["properties"]["title"]
    # How many reports were given for the MostFeltEvent?
    MostFeltCount = maxFeltQuake["properties"]["felt"]


def getfelt(quake):
    felt = quake["properties"]["felt"]
    if (felt is None):
        felt = 0
    return felt