# CUAVs-Coding-Challenge

**Challenge Overview:**
You will be provided with two data files, one in JSON format and the other in CSV format containing geographic coordinates (latitude, longitude) and corresponding signal IDs. These files represent sensor outputs from various locations that record environmental signals. Your task is to correlate these sensor readings based on the coordinates to identify common signals that may have been recorded by multiple sensors.

**Input Data:**
JSON file: Contains a list of sensor readings, where each record consists of an ID, latitude, and longitude. CSV file: Contains a similar set of records but in tabular format. The fields include the ID, latitude, and longitude. (See sample files)

**Goal:** 
Correlate the sensor data from both the JSON and CSV files by matching latitude and longitude values within a 100 meter tolerance threshold (to account for slight variations in reported coordinates). Identify common signals: For each pair of coordinates found within the tolerance range, associate the signal id from each sensor. The output should include a mapping between the sensor IDs from both files that represent the same geographical location.
