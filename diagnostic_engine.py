from collections import defaultdict


# -----------------------------
# 1. ROOT CAUSE ANALYSIS
# -----------------------------
def detect_root_causes(data):

    subject_scores = defaultdict(list)
    study_time = defaultdict(float)

    for row in data:

        subject = row["Subject"]
        score = float(row["Score"])
        hours = float(row["Time (hrs)"])

        subject_scores[subject].append(score)
        study_time[subject] += hours

    diagnosis = {}

    for subject, scores in subject_scores.items():

        avg_score = round(sum(scores) / len(scores), 2)
        total_hours = round(study_time[subject], 2)

        highest = max(scores)
        lowest = min(scores)
        score_range = highest - lowest

        sessions = len(scores)

        reasons = []

        if avg_score < 75:
            reasons.append("Low average performance")

        if score_range > 20:
            reasons.append("High score fluctuation (inconsistent understanding)")

        if total_hours < 5:
            reasons.append("Low study time for subject")

        if not reasons:
            reasons.append("Stable learning pattern")

        diagnosis[subject] = {
            "average_score": avg_score,
            "study_hours": total_hours,
            "sessions": sessions,
            "highest_score": highest,
            "lowest_score": lowest,
            "score_range": score_range,
            "root_causes": reasons
        }

    return diagnosis


# -----------------------------
# 2. WEAK CONCEPTS
# -----------------------------
def detect_weak_concepts(data):

    concept_scores = defaultdict(list)

    for row in data:

        concept = row["Concept"]
        score = float(row["Score"])

        concept_scores[concept].append(score)

    weak_concepts = {}

    for concept, scores in concept_scores.items():

        avg = round(sum(scores) / len(scores), 2)

        if avg < 75:

            weak_concepts[concept] = {
                "average_score": avg,
                "attempts": len(scores),
                "status": "Weak concept"
            }

    return weak_concepts


# -----------------------------
# 3. CROSS-SUBJECT INSIGHTS (NEW LAYER)
# -----------------------------
def detect_cross_subject_patterns(data):

    subject_scores = defaultdict(list)

    for row in data:

        subject = row["Subject"]
        score = float(row["Score"])

        subject_scores[subject].append(score)

    subject_avg = {
        s: sum(scores) / len(scores)
        for s, scores in subject_scores.items()
    }

    insights = []

    reading_subjects = ["RLA", "Social Studies"]

    reading_scores = [
        subject_avg[s]
        for s in reading_subjects
        if s in subject_avg
    ]

    if len(reading_scores) == 2 and all(s < 80 for s in reading_scores):

        insights.append({
            "pattern": "Reading Comprehension Weakness",
            "evidence": "RLA + Social Studies both below 80",
            "interpretation": "Likely weakness in reading comprehension and interpretation skills",
            "impact": "Affects multiple subjects requiring text understanding"
        })

    if "Math" in subject_avg and subject_avg["Math"] > 80:

        weak_others = [
            s for s in subject_avg
            if s != "Math" and subject_avg[s] < 80
        ]

        if weak_others:

            insights.append({
                "pattern": "Skill Imbalance",
                "evidence": "Math significantly stronger than other subjects",
                "interpretation": "Strong logical ability but weaker verbal/conceptual skills",
                "impact": "Uneven skill development"
            })

    all_scores = [score for scores in subject_scores.values() for score in scores]

    if max(all_scores) - min(all_scores) > 25:

        insights.append({
            "pattern": "Performance Instability",
            "evidence": "Large variation across all subjects",
            "interpretation": "Inconsistent study performance across sessions",
            "impact": "Unstable readiness prediction"
        })

    return insights


# -----------------------------
# 4. MAIN ENTRY
# -----------------------------
def run_diagnostic(data):

    return {
        "subject_diagnosis": detect_root_causes(data),
        "weak_concepts": detect_weak_concepts(data),
        "cross_subject_insights": detect_cross_subject_patterns(data)
    }
