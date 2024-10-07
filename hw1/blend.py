import pandas as pd
from collections import Counter

# List of CSV file names to blend
csv_files = ["output_1.csv", "output_2.csv", "output_3.csv"]  # Add your file names here

# Initialize an empty dictionary to store answers for each id
answers_dict = {}

# Read and process each CSV file
for file in csv_files:
    df = pd.read_csv(file, encoding='utf-8')  # Specify the encoding here
    
    # Iterate through the rows of the CSV
    for _, row in df.iterrows():
        id_val = row["id"]
        answer = row["answer"]
        
        # If the id is already in the dictionary, add the answer to the list
        if id_val in answers_dict:
            answers_dict[id_val].append(answer)
        else:
            # If the id is not in the dictionary, create a new list
            answers_dict[id_val] = [answer]

# Create a list to store the blended answers
blended_answers = []

# Iterate through the dictionary and select the most common answer
for id_val, answers in answers_dict.items():
    counter = Counter(answers)
    most_common_answer, most_common_count = counter.most_common(1)[0]
    
    # Check for ties
    tied_answers = [a for a, c in counter.items() if c == most_common_count]
    
    if len(tied_answers) > 1:
        # If there's a tie, select the shortest answer
        shortest_answer = min(tied_answers, key=len)
        blended_answers.append([id_val, shortest_answer])
    else:
        blended_answers.append([id_val, most_common_answer])

# Create a DataFrame from the blended answers
blended_df = pd.DataFrame(blended_answers, columns=["id", "answer"])

# Save the blended DataFrame to a CSV file with the same encoding
blended_df.to_csv("blend123.csv", index=False, encoding='utf-8')
