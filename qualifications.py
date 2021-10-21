# Get qualifications timing for F1 drivers
import requests as re
import pandas as pd
import json

print("-"*10, "List of 2021 Formula 1 Drivers", "-"*10)
response_d = re.get("https://ergast.com/api/f1/2021/drivers.json")
json_d = response_d.json()

drivers = []
for item in json_d['MRData']['DriverTable']['Drivers']:
    drivers.append(item['driverId'])

print(drivers)
print("-"*10)

input = input("Insert driver's name:")
url = "https://ergast.com/api/f1/2021/drivers/" + input + "/qualifying.json"
print("Query url:", url)

response_q = re.get(url)
json_q = response_q.json()

rounds = []
race_name = []
position = []
q1_time = []

for item in json_q['MRData']['RaceTable']['Races']:
    rounds.append(item['round'])
    race_name.append(item['raceName'])
    position.append(item['QualifyingResults'][0]['position'])
    q1_time.append(item['QualifyingResults'][0]['Q1'])

df = pd.DataFrame({'rounds': rounds, 'race_name': race_name, 'position': position, 'q1_time': q1_time})
print(df)
