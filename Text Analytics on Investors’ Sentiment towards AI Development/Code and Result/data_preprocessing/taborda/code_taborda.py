import csv

# Create an empty list to store the selected columns
selected_columns = []

# Open the CSV file
with open('tweets_labelled_09042020_16072020.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file, delimiter=';')

    # Skip the header row
    next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the "text" and "sentiment" columns
        text = row[2]  # "text" is the third column (index 2)
        sentiment = row[3]  # "sentiment" is the fourth column (index 3)

        if sentiment:  # Check if sentiment is not empty
            # Map sentiment to numerical values
            if sentiment == 'positive':
                sentiment = '2'
            elif sentiment == 'neutral':
                sentiment = '1'
            elif sentiment == 'negative':
                sentiment = '0'

            # Append the selected row to the list
            selected_columns.append([text, sentiment])

# Print the selected columns
for row in selected_columns:
    print(row)

# Define the output file path
output_file = 'result_taborda.txt'

# Export the selected columns to a new text file
with open(output_file, 'w') as file:
    # Write the selected columns to the file
    for i, row in enumerate(selected_columns):
        if i != len(selected_columns) - 1:
            file.write(f"[{row[0]}, {row[1]}]\n")
        else:
            file.write(f"[{row[0]}, {row[1]}]")