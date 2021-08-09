import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

server_host_url = 'https://aternos.org/go/'
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def start_mc_server():
  driver.get(server_host_url)
  time.sleep(60)
  test = driver.get_element_by_xpath('/html/body/div[3]/div/div/div[1]').text
  return test