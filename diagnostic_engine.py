from collections import defaultdict


# -----------------------------
# 1. ROOT CAUSE ANALYSIS
# -----------------------------
def detect_root_causes(data):
    """
    Finds WHY performance is weak or strong.
    Focus = interpretation, not numbers.
    """

    subject_scores = defaultdict(list)
    concept_frequency = defaultdict(int)
    study_time = defaultdict(float)

    # Step 1: collect patterns
    for row in data:
        subject = row["Subject"]
        score = float(row["Score"])
        hours = float(row["Time (hrs)"])
        concept = row["Concept"]

        subject_scores[subject].append(score)
        concept_frequency[concept] += 1
        study_time[subject] += hours

    diagnosis = {}

    # Step 2: analyze each subject
    for subject, scores in subject_scores.items():

        avg_score = sum(scores) / len(scores)
        total_hours = study_time[subject]

        reasons = []

        # LOW PERFORMANCE
        if avg_score < 75:
            reasons.append("Low average performance")

        # INCONSISTENCY
        if len(scores) > 1:
            variance = max(scores) - min(scores)
            if variance > 20:
                reasons.append("High score fluctuation (inconsistent understanding)")

        # LOW STUDY TIME
        if total_hours < 5:
            reasons.append("Low study time for subject")

        # FINAL DIAGNOSIS
        if not reasons:
            reasons.append("Stable learning pattern")

        diagnosis[subject] = {
            "average_score": round(avg_score, 2),
            "study_hours": total_hours,
            "root_causes": reasons
        }

    return diagnosis


# -----------------------------
# 2. CONCEPT WEAKNESS DETECTION
# -----------------------------
def detect_weak_concepts(data):
    """
    Finds concepts that appear often in low scores.
    """

    concept_scores = defaultdict(list)

    for row in data:
        concept = row["Concept"]
        score = float(row["Score"])
        concept_scores[concept].append(score)

    weak_concepts = {}

    for concept, scores in concept_scores.items():

        avg = sum(scores) / len(scores)

        if avg < 75:
            weak_concepts[concept] = {
                "average_score": round(avg, 2),
                "status": "Weak concept"
            }

    return weak_concepts


# -----------------------------
# 3. MAIN DIAGNOSTIC ENGINE
# -----------------------------
def run_diagnostic(data):
    return {
        "subject_diagnosis": detect_root_causes(data),
        "weak_concepts": detect_weak_concepts(data)
    }
