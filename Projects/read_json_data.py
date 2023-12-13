import json
import openpyxl
from datetime import datetime

with open("CBT4A-outbound-response-new.json", "r") as file:
    text = file.readlines()
all_data = json.loads("".join(text))

workbook = openpyxl.load_workbook('Ford all data.xlsx')
worksheet = workbook.active

row = 0
column = 0

# row_one = tuple(all_data[0].keys())
# worksheet.append(row_one)
for vehicle_data in all_data:
    worksheet.append(tuple(vehicle_data.values())[:-5])

workbook.save('Ford all data.xlsx')
