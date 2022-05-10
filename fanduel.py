from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')

url = 'https://sportsbook.fanduel.com/navigation/mlb'
path = '/Users/tenzinchoezin/Desktop/chromedriver'

driver = webdriver.Chrome(path, options=options)
driver.get(url)


odds = driver.find_elements_by_xpath('//span[@class="iq ir fo fh ja jb dz"]')
for odd in odds:
    print(odd.text)
driver.quit()