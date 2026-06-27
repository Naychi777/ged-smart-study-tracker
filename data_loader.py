import csv


def load_study_log():
    """
    Loads the study log exported from Google Sheets.
    This is the primary data source for the analytics system.
    """

    filename = "ged_smart_study_tracker_study_log.csv"

    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
