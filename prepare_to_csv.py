import csv
import re

data = [
    ['[08:23, 18/09/2023] +55 71 9121-0914: ', '  Aluguel de Consultório de LUXO: '],
    ['[08:42, 18/09/2023] +55 21 97622-3181: ', ' Super Promoção da Ton!  Quer '],
]

output_data = []

# Iterate through the data and extract the phone number, date, time, and message for each entry
for entry in data:
    entry_str = entry[0] + entry[1]  # Combine both elements into a single string
    match = re.search(r'\[(\d{2}:\d{2}), (\d{2}/\d{2}/\d{4})\] (\+\d+ \d+ \d{4,5}-\d{4}): (.*)', entry_str)
    if match:
        time, date, phone_number, message = match.groups()
        output_data.append([phone_number, date, time, message])

csv_filename = "output.csv"

# print(output_data[1])

# Write the extracted data to a CSV file
with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(["Phone Number", "Date", "Time", "Message"])
    
    # Write the extracted data rows
    writer.writerows(output_data)

print(f'Data exported to "{csv_filename}"')
