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

        if len(scores) < 2:
            trend = "Not enough data"
        else:
            mid = len(scores) // 2

            first_half = sum(scores[:mid]) / len(scores[:mid])
            second_half = sum(scores[mid:]) / len(scores[mid:])

            diff = second_half - first_half

            if diff > 3:
                trend = "Improving 📈"
            elif diff < -3:
                trend = "Declining 📉"
            else:
                trend = "Stable ➖"

        trends[subject] = {
            "trend": trend,
            "average": sum(scores) / len(scores),
            "scores": scores
        }

    return trends


# -----------------------------
# 2. OVERALL TREND ANALYSIS
# -----------------------------
def detect_overall_trend(data):
    scores = [float(row["Score"]) for row in data]

    if len(scores) < 2:
        return "Not enough data"

    mid = len(scores) // 2

    first_half = sum(scores[:mid]) / len(scores[:mid])
    second_half = sum(scores[mid:]) / len(scores[mid:])

    diff = second_half - first_half

    if diff > 3:
        return "Overall Improving 📈"
    elif diff < -3:
        return "Overall Declining 📉"
    else:
        return "Overall Stable ➖"


# -----------------------------
# 3. MAIN ENGINE (ENTRY POINT)
# -----------------------------
def run_engine(data):
    subject_trends = detect_subject_trends(data)
    overall_trend = detect_overall_trend(data)

    return {
        "subject_trends": subject_trends,
        "overall_trend": overall_trend
    }
