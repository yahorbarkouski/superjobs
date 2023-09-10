import json
import os

has_errors = False

def check_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                check_json_file(os.path.join(root, file))

def check_json_file(json_path):
    global has_errors
    try:
        with open(json_path, 'r') as json_file:
            json.load(json_file)
    except ValueError:
        print(f'JSON file {json_path} is not valid. Please fix the syntax.')
        has_errors = True

check_directory('../../superjobs')

if has_errors:
    exit(1)