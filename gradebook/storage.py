import json
import os
import logging

FILE_PATH = "data/gradebook.json"
LOG_PATH = "logs/app.log"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data():
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            logging.info("Loaded data from gradebook.json")
            return data
    except FileNotFoundError:
        logging.info("gradebook.json not found, returning empty structure")
        return {"students": [], "courses": [], "enrollments": []}
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in gradebook.json")
        return {"students": [], "courses": [], "enrollments": []}


def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=2)
    logging.info("Saved data to gradebook.json")