from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# #buka browser
# driver = websetup.Chrome(options=chrome_options)
# #maximize window
# setup.maximize_window()

@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    #buka browser
    driver = webdriver.Chrome(options=chrome_options)
    #maximize window
    driver.maximize_window()
    #Open Demo QA Web
    driver.get("https://demoqa.com/")
    assert "ToolsQA" in driver.title
    #Selecting Elements
    elements = driver.find_element(By.XPATH,"//div[@class='card mt-4 top-card']//h5[contains(text(), 'Elements')]")
    elements.click()
    # Selecting TextBox
    driver.find_element(By.ID,"item-0").click()
    yield driver
    driver.quit() 

# Fill Full Name
input_username = [("Lutfiando Kunanta"), ("Lutfianda Kunanta")]
@pytest.mark.parametrize("username", input_username)
def test_fillUserName(setup,username):
    setup.find_element(By.ID,"userName").send_keys(username)
    assert username == setup.find_element(By.ID,"userName").get_attribute("value")
    #CONSOLE ASSERT
    #IF
    if username == "Lutfiando Kunanta":
        setup.find_element(By.ID,"userName").clear()
        print,"\n clear success.\n"
    else:
        setup.find_element(By.ID,"submit").click()
        output1 = setup.find_element(By.XPATH,"//div[@id='output']//p[@id='name']")
        assert username in output1.text

input_username = range(5)
@pytest.mark.parametrize("i", input_username)
def test_fillUserName(setup,i):
    setup.find_element(By.ID,"userName").send_keys(i)
    assert str(i) == setup.find_element(By.ID,"userName").get_attribute("value")
    # #IF
    # if username == "Lutfiando Kunanta":
    #     setup.find_element(By.ID,"userName").clear()
    # else:
    #     setup.find_element(By.ID,"submit").click()
    #     output1 = setup.find_element(By.XPATH,"//div[@id='output']//p[@id='name']")
    #     assert username in output1.text



# # Fill Email
# input_email = [("lutfiandakunatna@rocketmail.con"), ("lutfiandakunanta@rocketmail.com")]
# @pytest.mark.parametrize("email", input_email)
# def test_fillEmail(setup, email):
#     setup.find_element(By.ID,"userEmail").send_keys(email)
#     assert email == setup.find_element(By.ID,"userEmail").get_attribute("value")
#     if email == "lutfiandakunatna@rocketmail.con":
#         setup.find_element(By.ID,"userEmail").clear()

# # Fill Current Address
# input_currentAddress = [("Ngloram1"), ("Ngloram2")]
# @pytest.mark.parametrize("currentaddress", input_currentAddress)
# def test_fillCurrentAddress(setup, currentaddress):
#     setup.find_element(By.ID,"currentAddress").send_keys(currentaddress)
#     assert currentaddress == setup.find_element(By.ID,"currentAddress").get_attribute("value")
#     if currentaddress == "Ngloram1":
#         setup.find_element(By.ID,"currentAddress").clear()

# # Fill Perm Address
# input_permanentAddress = [("Blora1"), ("Blora2")]
# @pytest.mark.parametrize("permanentsaddress", input_permanentAddress)
# def test_fillPermanentAddress(setup, permanentsaddress):
#     setup.find_element(By.ID,"permanentAddress").send_keys(permanentsaddress)
#     assert permanentsaddress == setup.find_element(By.ID,"permanentAddress").get_attribute("value")
#     #CONSOLE
#     if permanentsaddress == setup.find_element(By.ID,"permanentAddress").get_attribute("value"):
#         print("same value")
#     else:
#         print("permanent value != input")
#     #CLEAR
#     if permanentsaddress == "Blora1":
#         setup.find_element(By.ID,"permanentAddress").clear()
    
# # SELECT Submit Button
# def test_selectSubmit(setup):
    

# #CHECKPOINTS OF OUTPUT
# def test_Output():
#     #LOCATING VALUE IN TEXTBOX
#     username = setup.find_element(By.ID,"userName").get_attribute("value")
#     email = setup.find_element(By.ID,"userEmail").get_attribute("value")
#     currentaddress = setup.find_element(By.ID,"currentAddress").get_attribute("value")
#     permanentsaddress = setup.find_element(By.ID,"permanentAddress").get_attribute("value")

#     #LOCATING OUTPUT
#     output1 = setup.find_element(By.XPATH,"//div[@id='output']//p[@id='name']")
#     output2 = setup.find_element(By.XPATH,"//div[@id='output']//p[@id='email']")
#     output3 = setup.find_element(By.XPATH,"//div[@id='output']//p[@id='currentAddress']")
#     output4 = setup.find_element(By.XPATH,"//div[@id='output']//p[@id='permanentAddress']")
    
#     #ASSERTIONS
#     assert username in output1.text
#     assert email in output2.text
#     assert currentaddress in output3.text
#     assert permanentsaddress in output4.text
#     setup.get_screenshot_as_file("output.png")

# def test_tearDown():
#     setup.quit()
