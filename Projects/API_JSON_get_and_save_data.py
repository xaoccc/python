# NOTE! The real data for this project is confidential. Here are shown the principles.
import requests
import json
import openpyxl

# Define the parameters of the post method
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'parameter_1': 'value_1',
        'parameter_2': 'value_2',
        'parameter_3': 'value_3',
        }

# Initiate post request
API_post = requests.post('https://some.web.address.for.the.post.request', headers=headers, data=data)

# Get the authorization data
for key, value in API_post.__dict__.items():
    if key == "_content":
        password = json.loads(value.decode('utf-8'))['authorization']

# Enter get request parameters and authorization data
headers = {'Content-Type': 'Application/json',
           'Authorization': password,
           'parameter_2': 'value_2',
           'parameter_3': 'value_3'}
params = {'parameter_1': 'value_1', 'parameter_2': 'value_2'}

# Initiate get request
API_get = requests.get('https://some.web.address.for.the.get.request', headers=headers, params=params)

# Since we receive the data in json format(string), we need to convert it to dictionary
# Here we do two things: get the data from the request and convert it to dictionary
all_data = json.loads("".join(API_get.text))

# Verify if the status of the request is OK
if API_get.status_code != 200:
    print(f"Error! Code {API_get.status_code}")
else:
    # Open the workbook to store the info from the get request
    workbook = openpyxl.load_workbook('My data.xlsx')
    worksheet = workbook.active

    # The keys from the data are the first row in the Excel table. We need it just the first time we fill our workbook
    # row_one = tuple(all_data[0].keys())
    # worksheet.append(row_one)

    # Here we insert the data into our workbook
    for row in all_data:
        worksheet.append(tuple(row.values()))

    # Save the file, and we're ready to go :)
    workbook.save('My data.xlsx')
