from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, csv
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

driver.get("https://web.whatsapp.com/")

chat_list = ["Odonto Classificados BA 1", "Odonto Classificados SP 6"]

selected_date = "20/10/2023"

def get_day_before (date):
    date_format = "%d/%m/%Y"

    date_to_change = datetime.strptime(date, date_format)

    result_date = date_to_change - timedelta(days=1)

    result = result_date.strftime(date_format)

    return result

one_day_prior = get_day_before(selected_date)

for chat in chat_list:

    def select_chat_by_name(chat):
        x_arg = '//span[contains(@title, '+ '"' + chat + '"'+ ')]'
        person_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
        person_title.click()
        time.sleep(3)

    select_chat_by_name(chat)

    def scroll_screen_to_top_and_copy():

        x_path = "//div[@role='application']"
        element = driver.find_element(By.XPATH, value=x_path)

        driver.execute_script("arguments[0].scrollIntoView(true)", element)
        # Time to allow Whatsapp Web to complete loading all data
        time.sleep(30)

        while True:
            driver.execute_script("arguments[0].scrollIntoView(true)", element)
            time.sleep(2)

            if one_day_prior in driver.page_source:
                text = element.get_attribute("outerHTML")
                return text

    html_chat = scroll_screen_to_top_and_copy()

    def process_web_element(element):
        soup = BeautifulSoup(element, "html.parser")

        elements_with_attribute = soup.select("._1DETJ")

        complete_messages = []

        for element in elements_with_attribute:
            phone_data_time = element['data-pre-plain-text']
            text_message = element.select(".selectable-text")
            text_message = BeautifulSoup(text_message[0].span.prettify(), "html.parser")
            text_message_cleaned = text_message.get_text().replace("\n", "")
            result = phone_data_time + text_message_cleaned
            complete_messages.append(result)

        return complete_messages

    messages_list = process_web_element(html_chat)

    def export_to_csv(list):
        messages_all_dates = []

        for entry in list:
            match = re.search(r'\[(\d{2}:\d{2}), (\d{2}/\d{2}/\d{4})\] (\+\d+ \d+ \d{4,5}-\d{4}): (.*)', entry)
            if match:
                time, date, phone_number, message = match.groups()
                messages_all_dates.append([phone_number, date, time, message])
        
        message_specific_date = []

        for item in messages_all_dates:
            if item[1] == selected_date:
                message_specific_date.append(item)

        csv_filename = chat+".csv"

        with open(csv_filename, mode='w', newline='', encoding='utf8') as csv_file:
            writer = csv.writer(csv_file)
            
            writer.writerow(["Phone Number", "Date", "Time", "Message"])
            
            writer.writerows(message_specific_date)

        print(f'Data exported to "{csv_filename}"')

    export_to_csv(messages_list)