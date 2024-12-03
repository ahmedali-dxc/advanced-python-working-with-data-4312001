# Python code​​​​​​‌‌​​​​‌‌‌​‌‌‌​​​​​​‌​​​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

from collections import defaultdict
import json


# open the data file and load the JSON
def get_event_classification():
    with open("/tmp/deps/30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)
    
    # categorize each event and count each one
    counters = defaultdict(int)
    for feature in data['features']:
        counters[feature["properties"]["type"]] += 1

    # return the result
    return counters
