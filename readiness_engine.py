from collections import defaultdict


# -----------------------------
# 1. READINESS SCORE CALCULATION
# -----------------------------
def calculate_readiness(data, target_score=180):
    """
    Computes readiness score based on multiple behavioral signals.
    This is a rule-based predictive model (not ML).
    """

    subject_scores = defaultdict(list)
    total_hours = 0

    # Step 1: collect data
    for row in data:
        subject = row["Subject"]
        score = float(row["Score"])
        hours = float(row["Time (hrs)"])

        subject_scores[subject].append(score)
        total_hours += hours

    # Step 2: compute averages per subject
    subject_avgs = []
    all_scores = []

    for scores in subject_scores.values():
        avg = sum(scores) / len(scores)
        subject_avgs.append(avg)
        all_scores.extend(scores)

    overall_avg = sum(all_scores) / len(all_scores)

    # Step 3: consistency (stability signal)
    consistency_penalty = 0
    for scores in subject_scores.values():
        if len(scores) > 1:
            if max(scores) - min(scores) > 20:
                consistency_penalty += 5

    # Step 4: study effort score
    effort_score = min(total_hours / 20 * 100, 100)

    # Step 5: final readiness formula (transparent model)
    readiness_score = (
        (overall_avg * 0.5) +
        (effort_score * 0.3) -
        (consistency_penalty)
    )

    readiness_score = max(0, min(100, readiness_score))

    # Step 6: interpret result
    if readiness_score >= 75:
        status = "Ready 🟢"
    elif readiness_score >= 50:
        status = "At Risk 🟡"
    else:
        status = "Not Ready 🔴"

    # Step 7: estimated probability (simple mapping)
    probability = min(100, max(0, readiness_score - 10))

    return {
        "readiness_score": round(readiness_score, 2),
        "status": status,
        "estimated_success_probability": round(probability, 2),
        "total_study_hours": total_hours,
        "overall_average": round(overall_avg, 2)
    }
