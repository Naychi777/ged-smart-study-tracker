from collections import defaultdict


# -----------------------------
# 1. SUBJECT PRIORITY DETECTION
# -----------------------------
def detect_priority_subjects(data):

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

        score_range = max(scores) - min(scores)

        priority_score = 0
        reasons = []

        # -----------------------------
        # RULE 1: LOW PERFORMANCE
        # -----------------------------
        if avg_score < 70:
            priority_score += 4
            reasons.append("Very low average performance")

        elif avg_score < 80:
            priority_score += 2
            reasons.append("Moderate performance gap")

        # -----------------------------
        # RULE 2: LOW STUDY TIME
        # -----------------------------
        if hours < 5:
            priority_score += 3
            reasons.append("Insufficient study time")

        # -----------------------------
        # RULE 3: INCONSISTENCY
        # -----------------------------
        if score_range > 20:
            priority_score += 2
            reasons.append("High score variability")

        priorities.append({
            "subject": subject,
            "avg_score": round(avg_score, 2),
            "hours": round(hours, 2),
            "priority_level": priority_score,
            "reasons": reasons
        })

    priorities.sort(
        key=lambda x: x["priority_level"],
        reverse=True
    )

    return priorities


# -----------------------------
# 2. ACTION RECOMMENDATIONS
# -----------------------------
def generate_recommendations(data):

    subject_scores = defaultdict(list)
    concept_scores = defaultdict(list)

    for row in data:

        subject = row["Subject"]
        concept = row["Concept"]
        score = float(row["Score"])

        subject_scores[subject].append(score)
        concept_scores[concept].append(score)

    recommendations = []

    # -----------------------------
    # SUBJECT LEVEL ACTIONS
    # -----------------------------
    for subject, scores in subject_scores.items():

        avg = sum(scores) / len(scores)

        if avg < 70:

            recommendations.append(
                {
                    "type": "critical",
                    "message": f"{subject}: rebuild foundational understanding",
                    "action_level": "high"
                }
            )

        elif avg < 80:

            recommendations.append(
                {
                    "type": "improve",
                    "message": f"{subject}: focus on targeted practice",
                    "action_level": "medium"
                }
            )

        else:

            recommendations.append(
                {
                    "type": "maintain",
                    "message": f"{subject}: maintain consistency",
                    "action_level": "low"
                }
            )

    # -----------------------------
    # CONCEPT LEVEL INSIGHT
    # -----------------------------
    weak_concepts = []

    for concept, scores in concept_scores.items():

        avg = sum(scores) / len(scores)

        if avg < 75:

            weak_concepts.append({
                "concept": concept,
                "average_score": round(avg, 2)
            })

    if weak_concepts:

        top_concepts = [
            c["concept"] for c in weak_concepts[:3]
        ]

        recommendations.append(
            {
                "type": "concept_review",
                "message": f"Revise weak concepts: {', '.join(top_concepts)}",
                "action_level": "high"
            }
        )

    return recommendations


# -----------------------------
# 3. MAIN ENGINE
# -----------------------------
def run_recommendation_engine(data):

    return {
        "priority_subjects": detect_priority_subjects(data),
        "recommendations": generate_recommendations(data)
    }
