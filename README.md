GED Smart Study Analytics System
=================================

Overview
--------
This project is a rule-based analytics and decision-support system for GED students.

It processes study log data exported from Google Sheets and converts it into structured insights such as:

- Performance trends
- Diagnostic analysis of weaknesses
- Exam readiness scoring
- Cross-subject pattern detection
- Actionable study recommendations

It is designed as an intelligence layer on top of a simple spreadsheet tracker.

---

Problem
-------
Spreadsheet trackers (e.g., Google Sheets) only display raw study data.

They do not explain:
- Why performance is changing
- Whether weaknesses are skill-based or subject-based
- How ready the student is for the exam
- What actions should be taken next

---

Solution
--------
This system enhances traditional tracking by adding an analytical reasoning layer.

It transforms raw study logs into:

1. Trend Analysis
   Detects improvement, decline, or stability.

2. Diagnostic Analysis
   Identifies root causes such as:
   - Low performance
   - Inconsistent understanding
   - Insufficient study time

3. Readiness Scoring
   Computes a transparent readiness score based on:
   - Performance
   - Study effort
   - Consistency
   - Recent trends

4. Cross-Subject Insights
   Detects shared weaknesses across subjects (e.g., reading comprehension issues).

5. Recommendation Engine
   Produces prioritized, actionable study guidance.

---

System Architecture
-------------------

data_loader.py
→ Loads study log CSV file

validator.py
→ Cleans and validates raw data

analytics_engine.py
→ Detects trends in performance (WHAT is happening)

diagnostic_engine.py
→ Identifies root causes and cross-subject patterns (WHY it is happening)

readiness_engine.py
→ Calculates exam readiness score (HOW ready the student is)

recommendation_engine.py
→ Generates prioritized study actions (WHAT to do next)

analytics.py
→ Main entry point that generates the final report

---

Data Source
------------
The system uses a single dataset:

- ged_smart_study_tracker_study_log.csv (Google Sheets export)

Important:
The CSV file must be placed in the root directory of the project (same folder as analytics.py).

---

Key Features
------------
- End-to-end study analytics pipeline
- Rule-based intelligence system (no machine learning required)
- Transparent scoring model
- Cross-subject reasoning
- Actionable recommendations
- Data validation and quality tracking

---

Future Improvements
-------------------
Planned enhancements:

- Automatic Google Sheets API integration
- Interactive dashboard (web-based UI)
- Chat-based study assistant
- Skill graph modeling (concept-to-skill mapping)
- Personalized weekly study planner
- PDF report export system

---

How to Run
-----------

1. Install Python 3.8+
2. Place the CSV file in the project root directory
3. Run the system:

```bash
python analytics.py

## Author

Naychi Phyo
