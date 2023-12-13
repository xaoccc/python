import json
import openpyxl

with open("My_json_data.json", "r") as file:
    text = file.readlines()
all_data = json.loads("".join(text))

workbook = openpyxl.load_workbook('My_file.xlsx')
worksheet = workbook.active

for row in all_data:
    worksheet.append(tuple(row.values()))

workbook.save('My_file.xlsx')
