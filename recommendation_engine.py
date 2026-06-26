from collections import defaultdict


# -----------------------------
# 1. SUBJECT PRIORITY DETECTION
# -----------------------------
def detect_priority_subjects(data):
    """
    Finds which subjects need immediate attention.
    """

    subject_scores = defaultdict(list)
    subject_hours = defaultdict(float)

    for row in data:
        subject = row["Subject"]
        score = float(row["Score"])
        hours = float(row["Time (hrs)"])

        subject_scores[subject].append(score)
        subject_hours[subject] += hours

    priorities = []

    for subject, scores in subject_scores.items():

        avg_score = sum(scores) / len(scores)
        hours = subject_hours[subject]

        # Priority rules (simple but powerful logic)
        priority_score = 0

        if avg_score < 75:
            priority_score += 3

        if hours < 5:
            priority_score += 2

        if max(scores) - min(scores) > 20:
            priority_score += 2

        priorities.append({
            "subject": subject,
            "avg_score": round(avg_score, 2),
            "hours": hours,
            "priority_level": priority_score
        })

    # sort highest priority first
    priorities.sort(key=lambda x: x["priority_level"], reverse=True)

    return priorities


# -----------------------------
# 2. ACTION RECOMMENDATIONS
# -----------------------------
def generate_recommendations(data):
    """
    Generates actionable study advice.
    """

    subject_scores = defaultdict(list)
    concept_scores = defaultdict(list)

    for row in data:
        subject = row["Subject"]
        concept = row["Concept"]
        score = float(row["Score"])

        subject_scores[subject].append(score)
        concept_scores[concept].append(score)

    recommendations = []

    # SUBJECT LEVEL RECOMMENDATIONS
    for subject, scores in subject_scores.items():

        avg = sum(scores) / len(scores)

        if avg < 70:
            recommendations.append(
                f"Focus heavily on {subject} — foundational understanding is weak."
            )
        elif avg < 80:
            recommendations.append(
                f"Improve {subject} through targeted practice sessions."
            )
        else:
            recommendations.append(
                f"Maintain consistency in {subject}."
            )

    # CONCEPT LEVEL RECOMMENDATIONS
    weak_concepts = [
        concept for concept, scores in concept_scores.items()
        if sum(scores) / len(scores) < 75
    ]

    if weak_concepts:
        recommendations.append(
            f"Revise weak concepts: {', '.join(weak_concepts[:3])}"
        )

    return recommendations


# -----------------------------
# 3. MAIN ENGINE FUNCTION
# -----------------------------
def run_recommendation_engine(data):
    return {
        "priority_subjects": detect_priority_subjects(data),
        "recommendations": generate_recommendations(data)
    }
