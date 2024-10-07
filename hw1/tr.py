import json

# Read the original JSON file
with open('train.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a dictionary to store the transformed data
transformed_data = []

# Load the context data from context.json
with open('context.json', 'r', encoding='utf-8') as context_file:
    context_data = json.load(context_file)

# Function to map paragraph indices to corresponding context strings
def get_context(index):
    if 0 <= index < len(context_data):
        return context_data[index]
    else:
        return ""

# Loop through the original data and perform transformations
for item in data:
    # Get the index of the "relevant" number in "paragraphs" list
    label = item["paragraphs"].index(item["relevant"])
    
    transformed_item = {
        "fold-ind": item["id"],
        "sent1": item["question"],
        "sent2": "",
        "ending0": get_context(item["paragraphs"][0]),
        "ending1": get_context(item["paragraphs"][1]),
        "ending2": get_context(item["paragraphs"][2]),
        "ending3": get_context(item["paragraphs"][3]),
        "label": label
    }
    transformed_data.append(transformed_item)

# Write the transformed data to a new JSON file
with open('transformed_train.json', 'w', encoding='utf-8') as output_file:
    json.dump(transformed_data, output_file, ensure_ascii=False, indent=2)
