import os

# Define the paths to the folders and files
base_path = "../data_preprocessing/"
folders = ["financial_phrasebank", "sanders", "taborda"]
files = ["result_financial_phrasebank.txt", "result_sanders.txt", "result_taborda.txt"]

# Create a list to store the extracted text
combined_text = []

# Iterate over the folders and files
for folder, file_name in zip(folders, files):
    file_path = os.path.join(base_path, folder, file_name)

    # Read the contents of the file
    with open(file_path, "r") as file:
        text = file.read().strip()  # Strip any leading/trailing whitespace
        
    # Append the text to the combined_text list
    combined_text.append(text)

# Combine the extracted text with a newline separator
combined_text = "\n".join(combined_text)

# Write the combined text to the new file
output_file_path = os.path.join(base_path, "combined_result.txt")
with open(output_file_path, "w") as output_file:
    output_file.write(combined_text)

print("Text extraction and combination completed. The combined result is saved in 'combined_result.txt'.")