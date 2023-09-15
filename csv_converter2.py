import re
import csv

# Specify the path to your input text file and output CSV file
input_file_path = 'input.txt'
output_csv_path = 'output.csv'

# Initialize variables to store message data
messages = []
current_message = ["", "", ""]  # Initialize with empty strings for three fields

# Define the regular expressions for the start and end patterns
start_pattern = re.compile(r'\+\d{2} \d{2} \d{4}-\d{4}')
end_pattern = re.compile(r'^(?:[01]\d|2[0-3]):[0-5]\d$')

# Open the input file for reading
with open(input_file_path, 'r', encoding='latin-1') as input_file:
    for line in input_file:
        line = line.strip()

        # Check if the line matches the start pattern
        if start_pattern.match(line):
            if current_message[0]:
                messages.append(current_message)  # Store the previous message
            current_message = [line, "", ""]  # Start a new message
        elif end_pattern.match(line):
            current_message[1] = line  # Store the second regex in the second field
            messages.append(current_message)  # Store the current message
            current_message = ["", "", ""]  # Reset for the next message
        elif current_message[0]:
            current_message[2] += ' ' + line  # Concatenate lines in between

# Write the extracted messages to a CSV file
with open(output_csv_path, 'w', newline='', encoding='latin-1') as output_csv:
    csv_writer = csv.writer(output_csv)
    csv_writer.writerows(messages)

print("Messages extracted and saved to", output_csv_path)
