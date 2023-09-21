import re
import csv

# Define a regular expression pattern to match dates, phone numbers, messages, and time
pattern = r'(\w+\s*-\s*\w+|\+\d{2}\s\d{2}\s\d{4,5}(-\d{4})?|\d{2}:\d{2}|.+?(?=\d{2}:\d{2}|$))'

# Read the input text from the file
with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Split the text using the regular expression pattern
data_list = re.findall(pattern, data)

# Initialize variables to store the extracted information
date = ""
phone_number = ""
time = ""
message = ""

# Initialize a list to store the extracted data
csv_data = []

# Iterate through the extracted data
for item in data_list:
    if isinstance(item, tuple):
        # Handle tuples (groups) by joining them into a single string
        item = ' '.join(item)
    if re.match(r'\w+\s*-\s*\w+', item):
        date = item.strip()
    elif re.match(r'\+\d{2}\s\d{2}\s\d{4,5}(-\d{4})?', item):
        phone_number = item.strip()
    elif re.match(r'\d{2}:\d{2}', item):
        time = item.strip()
    else:
        message = item.strip()
        # Append the extracted data to the CSV data list
        csv_data.append([date, phone_number, time, message])

# Define the CSV file name
csv_filename = "chat_data.csv"

# Write the extracted data to a CSV file
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row
    csv_writer.writerow(["Date", "Phone Number", "Time", "Message"])
    # Write the extracted data
    csv_writer.writerows(csv_data)

print(f"CSV file '{csv_filename}' created successfully.")
