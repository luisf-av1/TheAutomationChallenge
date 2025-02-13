import os
import pandas as pd

# Path where challenge.xlsx is located inside the data folder
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "challenge.xlsx")

# Mapping of Excel column names to field names on the webpage
COLUMN_MAPPING = {
    "company_name": "Company Name",
    "company_address": "Address",
    "employer_identification_number": "EIN",
    "sector": "Sector",
    "automation_tool": "Automation Tool",
    "annual_automation_saving": "Annual Saving",
    "date_of_first_project": "Date"
}

def read_challenge_data():
    """Reads the challenge.xlsx file and returns the rows with names matching the form fields."""
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"❌ File not found: {DATA_PATH}")

    df = pd.read_excel(DATA_PATH)

    # Rename columns to match the form field labels
    df = df.rename(columns=COLUMN_MAPPING)

    # Convert the DataFrame into a list of dictionaries (each row = one insertion)
    data_list = df.to_dict(orient="records")

    return data_list[:50]  # Only the first 50 rows
