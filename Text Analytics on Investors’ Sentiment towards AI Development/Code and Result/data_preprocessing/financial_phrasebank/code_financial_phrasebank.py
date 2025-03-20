import os
import sys

# Read Sentences_AllAgree.txt text file
file_Sentences_AllAgree = open("Sentences_AllAgree.txt", "r", encoding="latin-1")

copied_sentences = []

for line in file_Sentences_AllAgree.readlines():
        copied_sentences.append(line)

sentiment_mapping = {
    '@positive\n': 2,
    '@neutral\n': 1,
    '@negative\n': 0
}

split_sentences = []

for sentence in copied_sentences:
    for sentiment_label, sentiment_value in sentiment_mapping.items():
        if sentiment_label in sentence:
            split_sentence = sentence.split(sentiment_label)
            split_sentence = [part.strip() for part in split_sentence if part.strip()] # To remove the empty strings from the resulting parts, the list comprehension uses the if part.strip() condition. The strip() method removes leading and trailing whitespace from each part. In this case, part.strip() would evaluate to '' for the empty strings in the list. Since an empty string is considered a falsy value in Python, the if part.strip() condition filters out those empty strings, ensuring that only non-empty parts are added to the split_sentence list.

            split_sentence.append(sentiment_value)
            split_sentences.append(split_sentence)
            break

################################################################
result = split_sentences                       # final result  #
print(result)                                  # print(result) #
################################################################

file_Sentences_AllAgree.close()

################################################################
# Export: result_financial_phrasebank.txt                      #
################################################################

file_path = 'result_financial_phrasebank.txt'   # Specify the file path and name

with open(file_path, 'w') as file:              # Open the file in write mode
    for item in result:
        file.write(str(item) + '\n')            # Convert the item to a string



