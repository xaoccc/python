import pandas as pd
import requests
from openpyxl import load_workbook
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
# Fetch historical data for Bitcoin (BTC) from CoinGecko
url = "https://pro-api.coinmarketcap.com/v4/dex/spot-pairs/latest"
params = {
    # "timeStart": "1704067200",
    # "timeEnd": "1706745600",
    # "interval": "daily",
    "limit": 100,
    "network_id": "1"
}

# Headers
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": api_key
}

# Make the request
response = requests.get(url, headers=headers, params=params)


data = response.json()

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

list_data = []
for row in data['data']:
    list_data += row['quote']
    del row['quote']
    list_data[-1].update(row)

df = pd.DataFrame(list_data)
print(df)

df.to_excel("crypto.xlsx", sheet_name="15.02.2025", index=False)

with pd.ExcelWriter("crypto.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
    df.to_excel(writer, sheet_name="14.02.2025", index=False, header=False)

