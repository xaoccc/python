import plotly.express as px
from country_list import  available_languages
country_codes = [code for code in available_languages() if code == 'en']
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# Using BeautifulSoup, Selenium, plotly and  country_list we can extract and visualise different data from a dataset
# Here the data is show in the website using JS, that is why we need Selenium to extract it

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://www.voronoiapp.com/geopolitics/Top-12-Least-Peaceful-Countries-2020-2024-2762"
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
)
soup = BeautifulSoup(driver.page_source, "html.parser")
table = soup.find("table")  # or use find with id/class
headers = [th.get_text(strip=True) for th in table.find_all("th")]

rows = []
for tr in table.find_all("tr")[1:]:
    cells = [td.get_text(strip=True) for td in tr.find_all("td")]
    if cells:
        rows.append(dict(zip(headers, cells)))

driver.quit()
countries = []
values = []

year = input('choose year:')
while year not in ['2020' , '2021', '2022', '2023', '2024']:
    print('Invalid year input!')
    year = input('choose year:')
for row in rows:
    countries.append(row[year])
    values.append(row['Rank'])

data = {'Country': countries, 'Rank': values}


fig = px.choropleth(data, locations='Country', hover_name="Country", locationmode='country names', color='Rank', title=f'List of the most dangerous countries in {year}')
fig.show()
