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

driver.get("https://demoqa.com/")
assert "ToolsQA" in driver.title

time.sleep(1)

# NAVIGATE TO Element
driver.find_element(By.XPATH,"//div[@class='card mt-4 top-card']//h5[contains(text(), 'Elements')]").click()

# SELECT Text Box
driver.find_element(By.ID,"item-0").click()

time.sleep(1)
# Fill Full Name
driver.find_element(By.ID,"userName").send_keys("Lutfianda Kunanta")
driver.find_element(By.ID,"userName").clear()
driver.find_element(By.ID,"userName").send_keys("Lutfianda Kunanta")
# Fill Email
driver.find_element(By.ID,"userEmail").send_keys("lutfiandakunanta@rocketmail.con")
driver.find_element(By.ID,"userEmail").clear()
driver.find_element(By.ID,"userEmail").send_keys("lutfiandakunanta@rocketmail.con")
# Fill Current Address
driver.find_element(By.ID,"currentAddress").send_keys("Ngloram, Blora")
driver.find_element(By.ID,"currentAddress").clear()
driver.find_element(By.ID,"currentAddress").send_keys("Ngloram, Blora")
# Fill Perm Address
driver.find_element(By.ID,"permanentAddress").send_keys("Ngloram, Blora")
driver.find_element(By.ID,"permanentAddress").clear()
driver.find_element(By.ID,"permanentAddress").send_keys("Ngloram, Blora")
# SELECT Submit Button
driver.find_element(By.ID,"submit").click()

#CHECKPOINTS OF OUTPUT
output1 = driver.find_element(By.XPATH,"//div[@id='output']//p[@id='name']")
output2 = driver.find_element(By.XPATH,"//div[@id='output']//p[@id='email']")
output3 = driver.find_element(By.XPATH,"//div[@id='output']//p[@id='currentAddress']")
output4 = driver.find_element(By.XPATH,"//div[@id='output']//p[@id='permanentAddress']")

assert "Lutfianda Kunanta" in output1.text
assert "lutfiandakunanta@rocketmail.con" in output2.text
assert "Blora" in output3.text
assert "Ngloram" in output4.text

driver.quit()
