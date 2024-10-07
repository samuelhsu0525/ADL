import csv
import ast  # Used to parse the text lines as Python dictionaries

# Read data from the text file
with open("output_17.txt", "r") as text_file:
    lines = text_file.readlines()

# Parse the data into a list of dictionaries
predictions = []
for line in lines:
    data = ast.literal_eval(line.strip())
    id = data['id']
    answer = data['prediction_text']
    predictions.append({'id': id, 'answer': answer})

# Define the filename for the CSV file
csv_filename = "output_17.csv"

# Write the data to the CSV file
with open(csv_filename, mode="w", newline='') as csv_file:
    fieldnames = ['id', 'answer']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the header row
    
    for prediction in predictions:
        writer.writerow({'id': prediction['id'], 'answer': prediction['answer']})

print(f"CSV file '{csv_filename}' has been created with the predictions.")
