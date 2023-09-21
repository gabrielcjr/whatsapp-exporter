from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from read_file import turn_file_into_list
import time, csv
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")

# users = turn_file_into_list('r')

wait = WebDriverWait(driver, 600)

driver.get("https://web.whatsapp.com/")

chat_name = "Odonto Classificados BA 1"

def select_chat_by_name(chat_name):
    x_arg = '//span[contains(@title, '+ '"' + chat_name + '"'+ ')]'
    person_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
    person_title.click()
    time.sleep(3)

select_chat_by_name(chat_name)

def scroll_screen_to_top_and_copy():

    x_path = "//div[@role='application']"
    element = driver.find_element(By.XPATH, value=x_path)

    driver.execute_script("arguments[0].scrollIntoView(true)", element)
    time.sleep(30)
    driver.execute_script("arguments[0].scrollIntoView(true)", element)
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true)", element)
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true)", element)
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true)", element)
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true)", element)
    time.sleep(2)
    
    # text = driver.find_element(By.XPATH, value=x_path)

    text = driver.find_elements(By.CLASS_NAME, "_1DETJ copyable-text")

    

    all_chats = []

    for item in text:
        soup = BeautifulSoup(item)
        soup.
        data_path = "//div[@role='application']"
        date_and_phone = 


    return text

result = scroll_screen_to_top_and_copy()

def process_web_element(webelement):



file_path = "output.txt"

# Open the file in write mode ('w')
with open(file_path, 'w', encoding="utf_8") as file:
    # Write the text to the file
    file.write(result)

