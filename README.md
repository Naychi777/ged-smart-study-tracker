# GED Smart Study Tracker + Analytics System

## Overview

This project is an adaptive learning analytics system designed to help GED students track study performance and understand their learning progress using structured data analysis.

It converts study logs into insights such as performance trends, weak areas, readiness level, and study recommendations.

## System Context

This project extends a Google Sheets-based study tracking system by adding a Python-based intelligence layer.

While Google Sheets is used for structured data entry and basic analysis, the Python engine enhances the system by identifying patterns, generating diagnostic insights, and producing adaptive recommendations.

As more data is collected, the system becomes more accurate in detecting learning patterns, weaknesses, and study behavior trends.

---

## Problem

Students often study without structured feedback. They may not know:

- which subjects are weak
- whether performance is improving
- if they are ready for the exam

This leads to inefficient study planning.

---

## Solution

This system processes study data and generates structured insights through:

- performance analysis
- diagnostic reasoning
- readiness scoring
- recommendation generation

It acts as a decision-support system for self-directed learning.

---

## System Structure

Data Loader → Data Validator → Analytics Engine → Diagnostic Engine → Readiness Engine → Recommendation Engine

---

## Key Features

- Load study data from Google Sheets (CSV export)
- Validate and clean data
- Analyze performance trends
- Identify weak subjects and concepts
- Generate readiness score
- Provide study recommendations

---

## Example Output

Readiness Score: 54.77
Status: At Risk
Success Probability: 44.77%

Recommendations:
- Improve Social Studies through targeted practice
- Focus on weak concepts
- Maintain consistency in Math

---

## Tech Stack

- Python
- CSV data processing
- Rule-based analytics

---

## Future Improvements

- Google Sheets API integration for real-time data
- AI-based chat assistant for study advice
- Automated study planner
- Visualization dashboard for progress tracking

---

## Author

Naychi Phyo
