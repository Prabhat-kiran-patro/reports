import json
import csv

def fetch_json(file_path):
    with open(file_path) as file:
        return json.load(file)

def write_to_csv(file_path, data):
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def read_file(file_path):
    with open(file_path) as file:
        return file.read()