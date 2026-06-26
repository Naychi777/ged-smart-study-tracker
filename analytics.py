from data_loader import load_study_log
from validator import validate_data

from analytics_engine import run_engine
from diagnostic_engine import run_diagnostic
from readiness_engine import calculate_readiness
from recommendation_engine import run_recommendation_engine


def main():

    # -----------------------------
    # 1. LOAD DATA
    # -----------------------------
    raw_data = load_study_log()

    datasets = {"study_log": raw_data}

    # -----------------------------
    # 2. VALIDATE DATA
    # -----------------------------
    clean_data, report = validate_data(datasets)

    study_data = clean_data["study_log"]

    # -----------------------------
    # 3. ANALYTICS ENGINE (WHAT)
    # -----------------------------
    analytics_result = run_engine(study_data)

    # -----------------------------
    # 4. DIAGNOSTIC ENGINE (WHY)
    # -----------------------------
    diagnostic_result = run_diagnostic(study_data)

    # -----------------------------
    # 5. READINESS ENGINE (HOW READY)
    # -----------------------------
    readiness_result = calculate_readiness(study_data)

    # -----------------------------
    # 6. RECOMMENDATION ENGINE (WHAT TO DO)
    # -----------------------------
    recommendation_result = run_recommendation_engine(study_data)

    # -----------------------------
    # 7. FINAL REPORT OUTPUT
    # -----------------------------
    print("\n==============================")
    print("📊 GED SMART STUDY REPORT")
    print("==============================")

    print("\n🧠 OVERALL INSIGHT")
    print(analytics_result["overall_trend"])

    print("\n📈 READINESS STATUS")
    print(f"Score: {readiness_result['readiness_score']}")
    print(f"Status: {readiness_result['status']}")
    print(f"Success Probability: {readiness_result['estimated_success_probability']}%")

    print("\n🧠 DIAGNOSTIC INSIGHT")

    for subject, info in diagnostic_result["subject_diagnosis"].items():
        print(f"\n{subject}:")
        print(f"  Avg Score: {info['average_score']}")
        print(f"  Study Hours: {info['study_hours']}")
        print(f"  Root Causes:")
        for cause in info["root_causes"]:
            print(f"   - {cause}")

    print("\n🎯 RECOMMENDATIONS")

    for rec in recommendation_result["recommendations"]:
        print(f"- {rec}")

    print("\n📌 PRIORITY SUBJECTS")

    for item in recommendation_result["priority_subjects"]:
        print(f"{item['subject']} → Priority {item['priority_level']}")

    print("\n==============================")


if __name__ == "__main__":
    main()
