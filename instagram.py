from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

link = input("Enter Instagram Image URL: ")

options = Options()
options.add_argument("--disable-notifications")

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


driver.get(link)
time.sleep(5)   # wait for page to load

soup = BeautifulSoup(driver.page_source, 'lxml')
img = soup.find("img")

if img:
    img_url = img["src"]
    r = requests.get(img_url)

    with open(f"instagram_{int(time.time())}.jpg", "wb") as f:
        f.write(r.content)

    print("Image downloaded successfully ✅")
else:
    print("Image not found ❌")

driver.quit()
