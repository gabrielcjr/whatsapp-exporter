import os, json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from whatsapp_scrap import WhatsappScrap
from dotenv import load_dotenv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

load_dotenv()

chat_list: list = json.loads(os.getenv("CHAT_LIST"))

selected_date: str = os.getenv("DATE")

ws = WhatsappScrap(chat_list, selected_date)

previous_day: str = ws.get_previous_day(selected_date)

for chat in chat_list:

    ws.select_chat_by_name(chat, wait)

    html_chat: str = ws.scroll_screen_to_top_and_copy(driver, previous_day)

    messages_list: list = ws.process_web_element(html_chat)

    ws.export_to_csv(messages_list, selected_date, chat)