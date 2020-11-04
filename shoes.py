import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

email="*****@gmail.com"
password='*******'
ccv="***"

link = "https://www.nike.com/launch/t/air-force-1-gtx-boot-medium-olive"


def click(path): # wait for element to load then click
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
        driver.find_element_by_xpath(path).click()
    except TimeoutException:
        print("Failed to load", path)

def type(path, text): # wait for element to load then type
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
        driver.find_element_by_xpath(path).send_keys(text)
    except TimeoutException:
        print("Failed to load", path)

options = Options()
# options.add_argument("--headless") # makes chrome window not show
driver = webdriver.Chrome(options=options)
driver.get(link)
click('/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/ul/li[11]/button') #click size
print('chose size')

click('/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section/div[2]/aside/div/div[2]/div/div[2]/div/button')  #click add to cart
print('added to cart')

driver.get('https://www.nike.com/us/en/cart') # go to cart
click('/html/body/div[2]/div/div[1]/main/div[2]/div[2]/aside/div[7]/div/button[1]')
print('checking out')

if driver.current_url == "https://www.nike.com/checkout/tunnel":
    print('logging in')
    type('/html/body/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div/div[1]/form/div[2]/input', email) #type in email
    type('/html/body/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div/div[1]/form/div[3]/input', password) #type in password
    click('/html/body/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div/div[1]/form/div[7]/input') # click login
    print('logged in')

try: #handle error if it shows up
    click('/html/body/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/button')
    click('/html/body/div/div/div[3]/div/div[2]/div/div/main/section[2]/div/div[3]/div/button')
    print('handled error')
except (RuntimeError, TypeError, NameError):
    pass

type('/html/body/form/div/input', ccv) # type in ccv
print('typed in ccv')

click('/html/body/div[1]/div/div[3]/div/div[2]/div/div/main/section[3]/div/div[1]/div[2]/div[5]/button') #click submit
print('submitted')

