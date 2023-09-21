from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from read_file import turn_file_into_list
import time, csv
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")

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

    text = element.get_attribute("outerHTML")
    return text

html_chat = scroll_screen_to_top_and_copy()

def process_web_element(webelement):
    soup = BeautifulSoup(webelement, "html.parser")

    elements_with_attribute = soup.select("._1DETJ")

    complete_messages = []

    for element in elements_with_attribute:
        single_message = []
        data_pre_plain_text = element['data-pre-plain-text']
        single_message.append(data_pre_plain_text)
        message = element.select(".selectable-text")
        message = BeautifulSoup(message[0].span.prettify(), "html.parser")
        single_message.append(message.get_text())
        complete_messages.append(single_message)

    return complete_messages

messages_list = process_web_element(html_chat)

def export_to_csv(list):
    output_data = []

    for entry in list:
        entry_str = entry[0] + entry[1] 
        match = re.search(r'\[(\d{2}:\d{2}), (\d{2}/\d{2}/\d{4})\] (\+\d+ \d+ \d{4,5}-\d{4}): (.*)', entry_str)
        if match:
            time, date, phone_number, message = match.groups()
            output_data.append([phone_number, date, time, message])

    csv_filename = "output.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(["Phone Number", "Date", "Time", "Message"])
        
        writer.writerows(output_data)

    print(f'Data exported to "{csv_filename}"')

