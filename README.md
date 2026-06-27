# GED Smart Study Analytics System

## Overview

The GED Smart Study Analytics System is a rule-based analytics and decision-support system designed to support GED students throughout their exam preparation.

This project builds upon an existing Google Sheets study tracker by adding an intelligence layer that interprets study patterns rather than simply recording them. It analyzes exported study log data to generate meaningful insights, including:

* Performance trends
* Diagnostic analysis of learning weaknesses
* Exam readiness scoring
* Cross-subject pattern detection
* Actionable study recommendations

As more study data is collected, the system is able to provide increasingly meaningful and personalized insights.

---

## Problem

Spreadsheet trackers are useful for recording study data but provide limited analytical insight.

While they organize information effectively, they cannot answer questions such as:

* Why is performance improving or declining?
* Are weaknesses isolated to one subject or shared across multiple subjects?
* How prepared is the student for the GED exam?
* What should the student focus on next?

---

## Solution

This project extends spreadsheet-based tracking by adding a structured analytical reasoning layer.

The system transforms raw study logs into educational insights through several independent analytics engines.

### Trend Analysis

Detects whether performance is improving, declining, or remaining stable.

### Diagnostic Analysis

Identifies possible causes of weak performance, including:

* Low average scores
* Inconsistent understanding
* Insufficient study time

### Readiness Scoring

Calculates an explainable readiness score using:

* Subject performance
* Study effort
* Learning consistency
* Recent performance trends

### Cross-Subject Insights

Detects patterns shared across multiple subjects, such as potential reading comprehension weaknesses affecting both RLA and Social Studies.

### Recommendation Engine

Generates prioritized and actionable study recommendations based on the detected learning patterns.

---

## System Architecture

**data_loader.py**

Loads the study log exported from Google Sheets.

**validator.py**

Validates and cleans imported data.

**analytics_engine.py**

Analyzes overall and subject-level performance trends.

**diagnostic_engine.py**

Detects root causes and cross-subject learning patterns.

**readiness_engine.py**

Calculates overall exam readiness.

**recommendation_engine.py**

Generates prioritized study recommendations.

**analytics.py**

Runs the complete analytics pipeline and generates the final report.

---

## Data Source

The system currently uses a single dataset:

`ged_smart_study_tracker_study_log.csv`

This file should be placed in the project's root directory (the same directory as `analytics.py`).

---

## Key Features

* Modular analytics pipeline
* Rule-based decision support system
* Transparent readiness scoring
* Cross-subject reasoning
* Actionable recommendations
* Data validation and quality reporting

---

## Future Improvements

Planned enhancements include:

* Google Sheets API integration
* Interactive web dashboard
* Chat-based study assistant
* Skill graph modelling
* Personalized weekly study planner
* PDF report generation

---

## How to Run

1. Install Python 3.8 or later.
2. Place `ged_smart_study_tracker_study_log.csv` in the project root directory.
3. Run:

```bash
python analytics.py
```

---

## Project Highlights

* Built entirely in Python using the standard library.
* Extends an existing Google Sheets tracker with an analytical reasoning layer.
* Uses modular analytics engines to separate trend analysis, diagnostics, readiness scoring, and recommendations.
* Employs explainable rule-based reasoning instead of black-box machine learning.

---

## Author

**Naychi Phyo**
