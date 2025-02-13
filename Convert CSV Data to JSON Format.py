import csv
import json


def csv_to_json(csv_filepath, json_filepath):
    data = []
    # Read CSV file and convert each row into a dictionary
    with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Write the list of dictionaries to a JSON file
    with open(json_filepath, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print(f"Data has been successfully converted from {csv_filepath} to {json_filepath}")


# Example usage:
csv_to_json("data.csv", "data.json")


# Why? This snippet converts CSV data into JSON format using Python's built-in csv and json modules. It's incredibly
# useful for data migration, preprocessing, and integrating CSV data with web APIs or other JSON-based systems.
