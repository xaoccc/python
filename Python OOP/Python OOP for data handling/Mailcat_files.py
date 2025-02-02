import pickle
import csv
import pandas as pd
from openpyxl import Workbook 
from Mailcat import Mailcat_object, Mailcat_collection, create_catalog

# 1. Open a raw python object
database = open('db.obj', 'rb')
Mail_c = pickle.load(database)
database.close()
print(Mail_c.serialize_Mailcat_objects())

# 1.1. Save serialized data(lists in a list) into a variable
Mail_c_serialized = Mail_c.serialize_Mailcat_objects()  

# 2. Write data into a CSV file
with open('mailcat_db.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Mail_c_serialized)

# 2.1. Read from a CSV file
csv_temp = []
with open('mailcat_db.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_temp.append(row)

# 3. Write data into an Excel sheet
workbook = Workbook()
sheet = workbook.active
for row in csv_temp:
    sheet.append(row)
workbook.save('mailcat_db.xlsx')

# 3.1. Read from the Excel sheet
for row in sheet.iter_rows():
    row_list =[]
    for cell in row:
        row_list.append(str(cell.value) + " ")
    print(row_list)

# 4. Convert CSV into pandas dataframe
# More info here https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
Mailcat_df = pd.read_csv('mailcat_db.csv', delimiter=',')
print(Mailcat_df)
    