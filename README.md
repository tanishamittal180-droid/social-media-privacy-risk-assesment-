# Social Media Privacy Risk Assessment Framework

## Overview

A defensive, privacy-first educational application that assesses social-media privacy practices using a self-reported questionnaire and synthetic data.

The application does **not** scrape social-media platforms, access private accounts, enumerate users, track people, or request passwords/real contact details.

## Problem Statement

Social-media profiles can expose unnecessary personal information, location context, workplace/education details, historical posts, connection patterns, and account-security weaknesses. Users often know individual privacy settings but lack a repeatable way to assess their overall exposure.

This project provides a transparent risk-assessment and security-awareness workflow.

## Objectives

- Assess privacy exposure through 40+ questions.
- Convert responses into category risk scores from 0–100.
- Produce an overall risk score.
- Classify risk as LOW, MODERATE, HIGH, or CRITICAL.
- Generate prioritized recommendations.
- Simulate privacy improvements.
- Provide an awareness dashboard and printable report.
- Demonstrate privacy-by-design and data minimization.
- Generate 1,000 synthetic assessment records for analytics.

## Cybersecurity Relevance

The project demonstrates privacy risk assessment, security awareness, GRC concepts, digital-footprint analysis, account-security hygiene, data minimization, risk scoring, Python/Flask development, SQLite, testing, and reporting.

## Privacy vs Security

Privacy focuses on how personal information is exposed, shared, and used. Security focuses on protecting accounts, systems, and information from unauthorized access or misuse.

A user can have MFA and a strong password while still publicly exposing a phone number or real-time location.

## Features

- 40+ question assessment
- 10 risk categories
- Explainable rule-based scoring
- Personalized findings
- Prioritized remediation
- Improvement simulator
- Dashboard charts
- Synthetic analytics dataset
- SQLite storage with derived data only
- HTML and PDF reports
- Printable privacy checklist
- Automated tests
- Privacy/security test checklist

## Risk Categories

1. Profile Exposure
2. Personal Information
3. Location Privacy
4. Content Exposure
5. Connections
6. Tagging
7. Account Security
8. Third-Party Apps
9. Social Engineering
10. Digital Footprint

## Risk Score

Higher score = higher assessed exposure/risk.

- 0–20: LOW
- 21–40: MODERATE
- 41–70: HIGH
- 71–100: CRITICAL

The weights and thresholds are educational assumptions and should be calibrated before professional risk decisions.

## Architecture

User -> Questionnaire -> Validation -> Feature Extraction -> Category Scoring -> Overall Score -> Findings -> Recommendations -> Dashboard -> Report

## Technology Stack

- Python 3.10+
- Flask
- SQLite
- HTML/CSS/JavaScript
- ReportLab for optional PDF reports
- pytest

## Installation

### Windows

```powershell
cd Social-Media-Privacy-Risk-Assessment
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python data/generate_dataset.py
python backend/app.py
```

Open:

http://127.0.0.1:5000

### macOS/Linux

```bash
cd Social-Media-Privacy-Risk-Assessment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python data/generate_dataset.py
python backend/app.py
```

Open:

http://127.0.0.1:5000

## Usage

1. Click Start Privacy Assessment.
2. Answer the questionnaire using fictional/self-reported information.
3. Submit the assessment.
4. Review overall and category scores.
5. Read findings and recommendations.
6. Try the improvement simulator.
7. Generate a report.
8. Print the privacy checklist.

## API

- `GET /api/health`
- `GET /api/questions`
- `POST /api/assessment`
- `GET /api/assessment/<id>`
- `GET /api/assessment/<id>/recommendations`
- `POST /api/assessment/simulate-improvement`
- `GET /api/dashboard/stats`
- `GET /api/privacy-checklist`
- `GET /api/report/<id>/html`
- `GET /api/report/<id>/pdf`
- `DELETE /api/assessment/<id>`

## Privacy Design

The application does not ask for actual phone numbers, addresses, passwords, private messages, exact locations, or birth dates. It asks whether such information is publicly visible.

Stored assessment data contains an assessment ID, category scores, overall score, risk level, finding types/descriptions, recommendations, and timestamps.

## Ethical Disclaimer

This project is designed for defensive cybersecurity and privacy education. It uses synthetic or voluntarily provided assessment responses and does not scrape, track, or profile real social-media users. The score is an educational framework, not a guarantee of compromise or safety.

## Limitations

- It does not verify actual platform settings.
- It does not scrape social media.
- It does not infer a person's identity.
- It does not perform real geolocation tracking.
- It does not guarantee protection from attacks.
- Risk weights are educational and require calibration for professional use.

## Future Improvements

- Platform-specific privacy checklists
- Privacy maturity scoring
- Enterprise GRC templates
- Accessibility/localization
- Secure client-side-only mode
- Anonymous aggregate trends
- Historical score comparison
- Awareness quizzes
- Organization-specific policies

## Learning Outcomes

- Flask REST APIs
- SQLite data modeling
- Risk scoring
- Data validation
- Privacy-by-design
- Security awareness
- Automated testing
- Synthetic data generation
- Dashboard design
- Technical documentation

## Author

Student Cybersecurity Project
