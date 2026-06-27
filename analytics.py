from data_loader import load_study_log
from validator import validate_data

from analytics_engine import run_engine
from diagnostic_engine import run_diagnostic
from readiness_engine import calculate_readiness
from recommendation_engine import run_recommendation_engine


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():

    raw_data = load_study_log()
    datasets = {"study_log": raw_data}

    clean_data, validation_report = validate_data(datasets)
    study_data = clean_data["study_log"]

    analytics = run_engine(study_data)
    diagnostic = run_diagnostic(study_data)
    readiness = calculate_readiness(study_data)
    recommendations = run_recommendation_engine(study_data)

    print_section("GED SMART STUDY REPORT")

    print("\nOVERALL INSIGHT")
    print(analytics["overall_trend"]["trend"])

    print("\nREADINESS STATUS")
    print(f"Score: {readiness['readiness_score']}")
    print(f"Status: {readiness['status']}")
    print(f"Estimated Success Probability: {readiness['estimated_success_probability']}%")

    print("\nREADINESS BREAKDOWN")

    for k, v in readiness["breakdown"].items():
        print(f"{k:<25} {v}/100")

    print("\nDIAGNOSTIC ANALYSIS")

    for subject, info in diagnostic["subject_diagnosis"].items():

        print(f"\n{subject}")
        print(f"Average Score: {info['average_score']}")
        print(f"Study Hours: {info['study_hours']}")

        print("Evidence:")
        print(f"Sessions: {info['sessions']}")
        print(f"Highest Score: {info['highest_score']}")
        print(f"Lowest Score: {info['lowest_score']}")
        print(f"Score Range: {info['score_range']}")

        print("Root Causes:")
        for cause in info["root_causes"]:
            print(f"- {cause}")

    # -----------------------------
    # NEW SECTION
    # -----------------------------
    print("\nCROSS-SUBJECT INSIGHTS")

    for insight in diagnostic["cross_subject_insights"]:

        print(f"\nPattern: {insight['pattern']}")
        print(f"Evidence: {insight['evidence']}")
        print(f"Interpretation: {insight['interpretation']}")
        print(f"Impact: {insight['impact']}")

    print("\nRECOMMENDATIONS")

    for rec in recommendations["recommendations"]:
        print(f"- {rec['message']}")

    print("\nPRIORITY SUBJECTS")

    for item in recommendations["priority_subjects"]:
        print(f"{item['subject']} (Priority {item['priority_level']})")

        if "reasons" in item:
            for r in item["reasons"]:
                print(f"- {r}")

    print("\nDATA QUALITY")

    print(f"Valid Rows: {validation_report['total_valid_rows']}")
    print(f"Issues Found: {len(validation_report['issues'])}")
    print(f"Data Quality Score: {validation_report['data_quality']}%")


if __name__ == "__main__":
    main()
