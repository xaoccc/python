from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()

driver.get("....")

wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

html_content = driver.page_source

print(html_content)

try:
    tables = pd.read_html(str(html_content))
    if not tables:
        raise ValueError("No tables found in the HTML file.")
except Exception as e:
    print(f"Error: {e}")

print(tables)

driver.quit()