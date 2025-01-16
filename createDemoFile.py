import random

# negative and positive file
file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_file_path = '1000.txt'

# Define the total number of lines needed in the new file
total_lines = 1000

# Function to read lines from a file
def read_lines(file_path):
    with open(file_path, 'r') as file:
        # Strip the newline character while reading the lines
        lines = [line.strip() for line in file.readlines()]
    return lines

# Function to randomly select lines from a list
def select_random_lines(lines, num_lines):
    return random.sample(lines, num_lines)


def create_combined_file(file1_path, file2_path, output_file_path, total_lines):
    # Read lines from both files
    file1_lines = read_lines(file1_path)
    file2_lines = read_lines(file2_path)

    # Calculate the number of lines to select from each file
    lines_from_file1 = total_lines // 2
    lines_from_file2 = total_lines - lines_from_file1  # To ensure total_lines is fully used

    # Randomly select lines from each file
    selected_file1_lines = select_random_lines(file1_lines, lines_from_file1)
    selected_file2_lines = select_random_lines(file2_lines, lines_from_file2)

    # Combine the selected lines
    combined_lines = selected_file1_lines + selected_file2_lines

    # Shuffle the combined lines to mix the selections from both files
    random.shuffle(combined_lines)

    # Write the combined lines to the output file
    with open(output_file_path, 'w') as output_file:
        # Write each line followed by a newline character
        for line in combined_lines:
            output_file.write(line + '\n')

    
create_combined_file(file1_path, file2_path, output_file_path, total_lines)

