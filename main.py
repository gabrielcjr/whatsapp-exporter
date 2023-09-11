from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from read_file import turn_file_into_list
import time, csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com/")

users = turn_file_into_list('r')

wait = WebDriverWait(driver, 600)





driver.get("https://web.whatsapp.com/")

x_arg = '//span[contains(@title, '+ '"' + "Odonto Classificados BA 1" + '"'+ ')]'

person_title = wait.until(EC.presence_of_element_located((
By.XPATH, x_arg)))
print(person_title)
person_title.click()
time.sleep(3)
x_path = "//div[@role='application']"

element = driver.find_element(By.XPATH, value=x_path)

print(element)

# while 'Yesterday' not in element:
#     top = element[0]
#     driver.execute_script("arguments[0].scrollIntoView(true);", top)
#     time.sleep(2)


#     text = driver.find_element(By.XPATH, value=x_path).text

#     file_path = "output.txt"

#     # Open the file in write mode ('w')
#     with open(file_path, 'w') as file:
#         # Write the text to the file
#         file.write(text)

