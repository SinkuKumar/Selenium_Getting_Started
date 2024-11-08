from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

# chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-extensions")  
chrome_options.add_argument("--disable-gpu")

chrome_service = Service(r"..\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
