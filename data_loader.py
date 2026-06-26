import csv
import os


def load_study_log(folder="data"):
    """
    Loads ONLY the study log CSV from Google Sheets export.
    This is the core dataset used for analytics and intelligence engine.
    """

    filename = "ged_smart_study_tracker_study_log.csv"
    path = os.path.join(folder, filename)

    try:
        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        return data

    except FileNotFoundError:
        print(f"Error: {filename} not found in {folder}/")
        return []
