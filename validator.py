def validate_data(datasets):
    cleaned = {}
    report = {}

    total_rows = 0
    removed_rows = 0
    issues = []

    for table_name, rows in datasets.items():

        cleaned_rows = []

        for row in rows:
            try:
                # Convert values safely
                score = float(row["Score"])
                hours = float(row["Time (hrs)"])

                # Basic validation rules
                if score < 0 or score > 100:
                    removed_rows += 1
                    issues.append(f"{table_name}: invalid score {score}")
                    continue

                if hours <= 0:
                    removed_rows += 1
                    issues.append(f"{table_name}: invalid hours {hours}")
                    continue

                # Clean row (convert types)
                row["Score"] = score
                row["Time (hrs)"] = hours

                cleaned_rows.append(row)
                total_rows += 1

            except (ValueError, KeyError):
                removed_rows += 1
                issues.append(f"{table_name}: malformed row")
                continue

        cleaned[table_name] = cleaned_rows

    report = {
        "total_valid_rows": total_rows,
        "removed_rows": removed_rows,
        "issues": issues,
        "data_quality": round(
            (total_rows / (total_rows + removed_rows)) * 100, 2
        ) if (total_rows + removed_rows) > 0 else 0
    }

    return cleaned, report
