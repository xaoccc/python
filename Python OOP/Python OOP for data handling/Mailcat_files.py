import pickle
import csv
import pandas as pd
from openpyxl import Workbook 
from Mailcat import Mailcat_object, Mailcat_collection, create_catalog

database = open('db.obj', 'rb')
Mail_c = pickle.load(database)
database.close()
Mail_c.list_Mailcat_objects()
print(Mail_c.serialize_Mailcat_objects())

Mail_c_serialized = Mail_c.serialize_Mailcat_objects()  

with open('mailcat_db.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Mail_c_serialized)

csv_temp = []
with open('mailcat_db.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_temp.append(row)

workbook = Workbook()