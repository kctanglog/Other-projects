import os
import sys

import csv

# Create an empty list to store the selected columns
selected_columns = []

# Open the CSV file
with open('full-corpus.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the "TweetText" and "Sentiment" columns
        tweet_text = row['TweetText']
        sentiment = row['Sentiment']

        # Filter out rows with "irrelevant" sentiment
        if sentiment != 'irrelevant':
            # Map sentiment to numerical values
            if sentiment == 'positive':
                sentiment = 2
            elif sentiment == 'neutral':
                sentiment = 1
            elif sentiment == 'negative':
                sentiment = 0

            # Append the selected row to the list
            selected_columns.append([tweet_text, sentiment])

################################################
result = selected_columns             # Result #
print(result)                                  #
################################################


# Export to 'result_sanders.txt'
# Define the output file path
output_file = 'result_sanders.txt'

# Export the selected columns to a new text file
with open(output_file, 'w') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the selected columns to the file
    for row in result:
       # Convert each row to a string with square brackets and write to the file
        file.write(f"[{', '.join(map(str, row))}]\n")

file.close()
