import json
import os

FILE_PATH = "data/gradebook.json"

def load_data():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"students": [], "courses": [], "enrollments": []}
    except json.JSONDecodeError:
        print("Error reading JSON file!")
        return {"students": [], "courses": [], "enrollments": []}
    

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)
