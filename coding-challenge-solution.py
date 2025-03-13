import json
import csv
import math

# great circle distance formula to calculate distance between two points on Earth [1]
def great_circle_distance(lat1, lon1, lat2, lon2):
    R = 6378000  # radius of Earth in meters [2]
  
    # convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # calculate distance [3]
    d = R * math.acos(math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2) + math.sin(lat1) * math.sin(lat2))

    return d

# load CSV data [4]
csv_data = []
with open('SensorData1.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        csv_data.append(row)

# load JSON data
with open('SensorData2.json', 'r') as json_file:
    json_data = json.load(json_file)

# convert CSV data to floats
for entry in csv_data:
    entry['latitude'] = float(entry['latitude'])
    entry['longitude'] = float(entry['longitude'])

# compare each entry in CSV with each entry in JSON
common_pairs = {}
for csv_entry in csv_data:
    for json_entry in json_data:
        distance = great_circle_distance(csv_entry['latitude'], csv_entry['longitude'], json_entry['latitude'], json_entry['longitude'])
        if distance <= 100:  # 100 meters threshold
            common_pairs[str(csv_entry['id'])] = int(json_entry['id'])

# save output to JSON
with open('output.json', 'w') as output_file:
    json.dump(common_pairs, output_file, indent=4)

'''
Citations:
[1] https://www.geeksforgeeks.org/great-circle-distance-formula/
[2] https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
[3] https://docs.python.org/3/library/math.html
[4] https://docs.python.org/3/library/csv.html
'''