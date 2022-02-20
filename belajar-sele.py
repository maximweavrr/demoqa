from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

chrome_options = Options()
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")

#buka browser
driver = webdriver.Chrome(options=chrome_options)

#maximize window
driver.maximize_window()

driver.get("https://www.google.com")

assert 'Google' in driver.title
driver.implicitly_wait(10)

# Element Selector
search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium")
search_button.click()

driver.implicitly_wait(10)
assert "Selenium - Penelusuran Google" == driver.title

#SELECT ARTICLE THAT REDIRECTS USER TO SELENIUM.DEV
time.sleep(2)
# first_article = driver.find_element(By.CSS_SELECTOR,"div.yuRUbf > a[href*='selenium.dev']")
first_article = driver.find_element(By.XPATH,"//div[@class='yuRUbf']/a[contains(@href, 'selenium.dev')]")
first_article.click()

time.sleep(2)

#SELECT ELEMENT THAT WILL REDIRECT TO TWITTER.COM USING CONTENTS
# driver.find_element(By.CSS_SELECTOR,"p.card-text > a[href*='AutomatedTester']").click()
driver.find_element(By.XPATH,"//p[@class='card-text']/ a[contains(text(), 'AutomatedTester')]").click()
time.sleep(2)

driver.back()
driver.back()

time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("herokuapp.com login" + Keys.RETURN)

driver.find_element(By.XPATH, "//div[@class='yuRUbf']/a[contains(@href, 'https://the-internet.herokuapp.com/login')]").click()

# driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.XPATH,"//div[@class='large-4 large-centered columns']//a[contains(text(), 'Elemental Selenium')]").click()
time.sleep(1)

driver.switch_to.window(driver.window_handles[1])
# time.sleep(3)

# driver.quit()