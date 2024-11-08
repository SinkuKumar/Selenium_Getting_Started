from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

# chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-extensions")  
chrome_options.add_argument("--disable-gpu")

# Provide location where chrome stores profiles
chrome_options.add_argument(r"--user-data-dir=C:\Users\Sinku\AppData\Local\Google\Chrome\User Data")

# {rovide the profile name with which we want to open browser
chrome_options.add_argument(r'--profile-directory=Profile 2')

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
