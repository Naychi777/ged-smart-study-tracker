from collections import defaultdict


# -----------------------------
# READINESS ENGINE
# -----------------------------
def calculate_readiness(data):

    subject_scores = defaultdict(list)
    total_hours = 0

    # -----------------------------
    # Collect Data
    # -----------------------------
    for row in data:

        subject = row["Subject"]
        score = float(row["Score"])
        hours = float(row["Time (hrs)"])

        subject_scores[subject].append(score)
        total_hours += hours

    all_scores = []

    consistency_penalty = 0

    for scores in subject_scores.values():

        all_scores.extend(scores)

        if len(scores) > 1:

            if max(scores) - min(scores) > 20:
                consistency_penalty += 5

    overall_average = sum(all_scores) / len(all_scores)

    # -----------------------------
    # COMPONENT 1
    # Subject Performance (40)
    # -----------------------------
    performance_component = min(
        (overall_average / 100) * 40,
        40
    )

    # -----------------------------
    # COMPONENT 2
    # Study Effort (20)
    # -----------------------------
    effort_component = min(
        (total_hours / 20) * 20,
        20
    )

    # -----------------------------
    # COMPONENT 3
    # Consistency (20)
    # -----------------------------
    consistency_component = max(
        20 - consistency_penalty,
        0
    )

    # -----------------------------
    # COMPONENT 4
    # Trend (20)
    # -----------------------------
    first_half = all_scores[:len(all_scores)//2]
    second_half = all_scores[len(all_scores)//2:]

    if len(first_half) > 0:

        trend_change = (
            sum(second_half) / len(second_half)
        ) - (
            sum(first_half) / len(first_half)
        )

    else:
        trend_change = 0

    if trend_change >= 3:
        trend_component = 20

    elif trend_change >= 0:
        trend_component = 15

    elif trend_change >= -3:
        trend_component = 10

    else:
        trend_component = 5

    # -----------------------------
    # FINAL SCORE
    # -----------------------------
    readiness_score = (
        performance_component
        + effort_component
        + consistency_component
        + trend_component
    )

    readiness_score = round(
        min(readiness_score, 100),
        2
    )

    # -----------------------------
    # STATUS
    # -----------------------------
    if readiness_score >= 75:
        status = "Ready"

    elif readiness_score >= 50:
        status = "At Risk"

    else:
        status = "Not Ready"

    probability = round(
        max(0, readiness_score - 10),
        2
    )

    # -----------------------------
    # RETURN
    # -----------------------------
    return {

        "readiness_score": readiness_score,

        "status": status,

        "estimated_success_probability": probability,

        "overall_average": round(overall_average, 2),

        "total_study_hours": round(total_hours, 2),

        # NEW
        "breakdown": {

            "Subject Performance":
                round(performance_component, 2),

            "Study Effort":
                round(effort_component, 2),

            "Consistency":
                round(consistency_component, 2),

            "Recent Trend":
                round(trend_component, 2)

        }

    }
