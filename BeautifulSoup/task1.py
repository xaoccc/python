import requests
from bs4 import BeautifulSoup
import csv

url = 'https://bnb.bg/Statistics/StInterbankForexMarket/index.htm'
filename = 'interbank_forex_market_data.csv'


response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

def extract_data_rows(soup):
    h2_tag = soup.find('h2')
    if h2_tag:
        table = h2_tag.find_next('table')
        if table:
            rows = table.find_all('tr')
            data_rows = []
            for row in rows[1:]:  # Skipping header row
                cells = row.find_all('td')
                data_rows.append([cell.text.strip() for cell in cells])
            return data_rows


data_rows = extract_data_rows(soup)[1:-1]

for row in data_rows:
    for i in range(1, len(row)):
        if row[i]:
            row[i] = float(row[i].replace(' ', ''))
        else:
            row[i] = 0.1


sorted_data_rows = sorted(data_rows, key=lambda x: x[7], reverse=True)

def write_to_csv(sorted_data_rows, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Bank', 'Currency', 'Volume Sold'])
        writer.writerows(sorted_data_rows)

def compare_and_rewrite_csv(sorted_data_rows, filename):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            existing_data = [row for row in reader]
    except FileNotFoundError:
        existing_data = None

    if sorted_data_rows != existing_data:
        write_to_csv(sorted_data_rows, filename)


def main():

    soup = BeautifulSoup(response.content, 'html.parser')
    if not soup:
        print("Failed to fetch and parse the webpage.")
        return

    compare_and_rewrite_csv(sorted_data_rows, filename)

if __name__ == "__main__":
    main()
