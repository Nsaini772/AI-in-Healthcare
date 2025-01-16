import os

# Positive and negative folder
folder1 = '/users/nsaini/projectOne/negative'
folder2 = '/users/nsaini/projectOne/positive'

# Combined one file of all positive and negative files
output_file_folder1 = '/users/nsaini/projectOne/file1.txt'
output_file_folder2 = '/users/nsaini/projectOne/file2.txt'

# Function to combine files from a folder into one
def combineFiles(folder, output_file):
    # List all files in the folder
    files = os.listdir(folder)
    
    # Open the output file in write mode (overwrite if file exists)
    with open(output_file, 'w') as outfile:
        for filename in files:
            file_path = os.path.join(folder, filename)
            # Check if it is a file (not a directory)
            if os.path.isfile(file_path):
                print(f"Combining {filename} into {output_file}...")
                with open(file_path, 'r') as infile:
                    # Write the contents of the file to the output file
                    outfile.write(infile.read())
                    # Optionally, add a newline to separate file contents
                    outfile.write("\n")

# Combine files from both folders into separate files
combineFiles(folder1, output_file_folder1)
combineFiles(folder2, output_file_folder2)
