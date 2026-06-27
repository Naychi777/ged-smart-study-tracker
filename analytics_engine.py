from collections import defaultdict


# -----------------------------
# 1. SUBJECT TREND ANALYSIS
# -----------------------------
def detect_subject_trends(data):
    subjects = defaultdict(list)

    for row in data:
        subject = row["Subject"]
        score = float(row["Score"])
        subjects[subject].append(score)

    trends = {}

    for subject, scores in subjects.items():

        average = round(sum(scores) / len(scores), 2)

        highest = max(scores)
        lowest = min(scores)

        if len(scores) < 2:
            trend = "Not enough data"
            change = 0

        else:
            mid = len(scores) // 2

            first_half = sum(scores[:mid]) / len(scores[:mid])
            second_half = sum(scores[mid:]) / len(scores[mid:])

            change = round(second_half - first_half, 2)

            if change > 3:
                trend = "Improving 📈"
            elif change < -3:
                trend = "Declining 📉"
            else:
                trend = "Stable ➖"

        trends[subject] = {
            "trend": trend,
            "average": average,
            "highest": highest,
            "lowest": lowest,
            "sessions": len(scores),
            "score_change": change,
            "scores": scores
        }

    return trends


# -----------------------------
# 2. OVERALL TREND ANALYSIS
# -----------------------------
def detect_overall_trend(data):

    scores = [float(row["Score"]) for row in data]

    average = round(sum(scores) / len(scores), 2)

    highest = max(scores)
    lowest = min(scores)

    if len(scores) < 2:

        return {
            "trend": "Not enough data",
            "average": average,
            "highest": highest,
            "lowest": lowest,
            "change": 0
        }

    mid = len(scores) // 2

    first_half = sum(scores[:mid]) / len(scores[:mid])
    second_half = sum(scores[mid:]) / len(scores[mid:])

    change = round(second_half - first_half, 2)

    if change > 3:
        trend = "Overall Improving 📈"

    elif change < -3:
        trend = "Overall Declining 📉"

    else:
        trend = "Overall Stable ➖"

    return {
        "trend": trend,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "change": change
    }


# -----------------------------
# 3. MAIN ENGINE
# -----------------------------
def run_engine(data):

    return {
        "subject_trends": detect_subject_trends(data),
        "overall_trend": detect_overall_trend(data)
    }
