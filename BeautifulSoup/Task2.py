import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

target_table = soup.find('table', {'class': 'wikitable'})

data_rows = []

rows = target_table.find_all('tr')

for row in rows:
    cells = row.find_all(['td', 'th'])
    data_row = [cell.text.strip() for cell in cells]
    data_rows.append(data_row)

country_idx = data_rows[0].index('Country')
pop_idx = data_rows[0].index('Officialfigure')

data_dict = {}
for row in data_rows[2:]:
    data_dict[row[country_idx]] = int(row[pop_idx].replace(',', ''))
total_pop = sum(data_dict.values())

total_data_dict = {}

for key, value in data_dict.items():
    total_data_dict[key] = {'country_population': value, 'country_population_percentage': round(value / total_pop * 100, 1)}

print(total_data_dict)