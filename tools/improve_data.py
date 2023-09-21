# Specify the path to your input text file and output text file
input_file_path = 'input.txt'
output_file_path = 'output.txt'

# Initialize a variable to store the previous line
prev_line = None

# Open the input file for reading
with open(input_file_path, 'r', encoding='latin-1') as input_file:
    lines = input_file.readlines()

# Filter out empty lines, lines containing 'entrou', and consecutive duplicate lines
filtered_lines = []
for line in lines:
    line = line.strip()
    if line and 'entrou usando' not in line and 'Entrar no grupo' not in line and line != prev_line:
        filtered_lines.append(line)
        prev_line = line

# Open the output file for writing (this will overwrite the existing file)
with open(output_file_path, 'w', encoding='latin-1') as output_file:
    output_file.write('\n'.join(filtered_lines))

print("Empty lines, lines containing 'entrou', and consecutive duplicate lines removed. Output written to", output_file_path)
