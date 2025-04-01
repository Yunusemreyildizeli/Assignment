# settings.py

import csv
import os

# Path to the settings CSV file used for storing budget limits by category
SETTINGS_FILE = "data/settings.csv"

def load_limits():
    """
    Loads category-wise spending limits from the settings CSV file.

    Returns:
        dict: A dictionary where the key is the category name (str)
              and the value is the spending limit (float).
    """
    limits = {}

    # Check if the settings file exists before reading
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    # Convert the second column (limit) to float
                    limits[row[0]] = float(row[1])

    return limits