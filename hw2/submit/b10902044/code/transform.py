import json
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python transfer.py [jsonl_file_name]")
    sys.exit(1)

# Get the JSONL input file name from the command-line argument
jsonl_file_path = sys.argv[1]

# Set the output JSON file name to "test.json"
json_file_path = "test.json"

# Open the JSONL input file and read its lines
try:
    with open(jsonl_file_path, 'r') as jsonl_file:
        lines = jsonl_file.readlines()
except FileNotFoundError:
    print(f"Error: The file '{jsonl_file_path}' not found.")
    sys.exit(1)

# Initialize an empty list to store the JSON objects
json_objects = []

# Iterate through the lines, parse each line as JSON, remove "title" if present, and add an empty "title"
for line in lines:
    json_object = json.loads(line)
    # Check if "title" field is present and remove it
    if "title" in json_object:
        json_object.pop("title")
    # Add an empty "title" field to the JSON object
    json_object["title"] = ""
    json_objects.append(json_object)

# Open the JSON output file and write the JSON objects as an array
with open(json_file_path, 'w') as json_file:
    json.dump(json_objects, json_file, indent=2)

print(f"Converted {len(json_objects)} JSONL objects from '{jsonl_file_path}' to '{json_file_path}'")
