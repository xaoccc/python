import pandas as pd
import requests
from bs4 import BeautifulSoup


response = requests.get("https://dev.bg/digest/top-100-largest-it-companies-in-bulgaria-2024-dc01/?utm_medium=social&utm_source=facebook-page&utm_campaign=top-100-largest-it-companies-in-bulgaria-2024-dc01&utm_content=jb-article&fbclid=IwAR3XVIbmX1k6Nz_AcfOWS3JmoEoPHghTcXZmngH3638Lhv7S9aeS1FOEOeY")
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')


try:
    tables = pd.read_html(str(soup))
    if not tables:
        raise ValueError("No tables found in the HTML file.")
except Exception as e:
    print(f"Error: {e}")

total = 0
employees_num_list = tables[0][2]
for num in employees_num_list:
    if num.isdigit():
        total += int(num)

print(total)