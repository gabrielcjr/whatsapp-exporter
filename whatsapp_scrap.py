from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, csv
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

class WhatsappScrap ():
    chat_list: list = []
    selected_date: str = ''

    def __init__(self, chat_list: list, selected_date: str) -> None:
        self.chat_list = chat_list
        self.selected_date = selected_date
      
    def get_previous_day (self, date) -> str:

        date_format: str = "%d/%m/%Y"
        date_to_change: datetime = datetime.strptime(date, date_format)
        result_date: datetime = date_to_change - timedelta(days=1)
        result: str = result_date.strftime(date_format)
        return result

    def select_chat_by_name(self, chat_name, wait) -> None:
        x_path_chat: str = '//span[contains(@title, '+ '"' + chat_name + '"'+ ')]'
        x_path_input: str = "//div[@title='Caixa de texto de pesquisa']"
        x_path_arrow: str = "//span[@data-icon='search']"
        
        time.sleep(1)

        text_input_box = wait.until(EC.presence_of_element_located((By.XPATH, x_path_input)))
        text_input_box.click()
        text_input_box.send_keys(chat_name)

        time.sleep(1)

        chat_title = wait.until(EC.presence_of_element_located((By.XPATH, x_path_chat)))
        chat_title.click()

        text_input_box.clear()

        arrow = wait.until(EC.presence_of_element_located((By.XPATH, x_path_arrow)))
        arrow.click()

    def scroll_screen_to_top_and_copy(self, driver, one_day_prior) -> str:

        x_path = "//div[@role='application']"
        element = driver.find_element(By.XPATH, value=x_path)

        driver.execute_script("arguments[0].scrollIntoView(true)", element)

        while True:
            driver.execute_script("arguments[0].scrollIntoView(true)", element)
            time.sleep(2)

            if one_day_prior in driver.page_source:
                text: str = element.get_attribute("outerHTML")
                return text

    def process_web_element(self, element) -> list:
        soup = BeautifulSoup(element, "html.parser")

        elements_with_attribute = soup.select("._1DETJ")

        complete_messages: list = []

        for element in elements_with_attribute:
            phone_data_time: str = element['data-pre-plain-text']
            text_message = element.select(".selectable-text")
            text_message = BeautifulSoup(text_message[0].span.prettify(), "html.parser")
            text_message_cleaned: str = text_message.get_text().replace("\n", "")
            result: str = phone_data_time + text_message_cleaned
            complete_messages.append(result)

        return complete_messages

    def export_to_csv(self, list, selected_date, chat) -> None:
        messages_all_dates: list = []

        for entry in list:
            match = re.search(r'\[(\d{2}:\d{2}), (\d{2}/\d{2}/\d{4})\] (\+\d+ \d+ \d{4,5}-\d{4}): (.*)', entry)
            if match:
                time, date, phone_number, message = match.groups()
                messages_all_dates.append([phone_number, date, time, message])
        
        message_specific_date: list = []

        for item in messages_all_dates:
            if item[1] == selected_date:
                message_specific_date.append(item)

        csv_filename = "output/"+chat+".csv"

        with open(csv_filename, mode='w', newline='', encoding='utf8') as csv_file:
            writer = csv.writer(csv_file)
            
            writer.writerow(["Phone Number", "Date", "Time", "Message"])
            
            writer.writerows(message_specific_date)

        print(f'Data exported to "{csv_filename}"')



