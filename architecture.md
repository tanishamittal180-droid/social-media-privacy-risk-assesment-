# System Architecture

```text
User
 |
 v
Privacy Questionnaire
 |
 v
Input Validation
 |
 v
Feature Extraction / Answer Normalization
 |
 +-------------------------------+
 | Profile Exposure              |
 | Personal Information          |
 | Location Privacy              |
 | Content Exposure              |
 | Connections                   |
 | Tagging                       |
 | Account Security              |
 | Third-Party Apps              |
 | Social Engineering            |
 | Digital Footprint             |
 +-------------------------------+
 |
 v
Category Scores
 |
 v
Weighted Risk Scoring
 |
 v
Overall Score + Risk Level
 |
 +--> Findings Engine
 |
 +--> Recommendation Engine
 |
 +--> Improvement Simulator
 |
 +--> Dashboard / Report
 |
 v
SQLite (derived data only)
```

## Privacy-by-design controls

- Data minimization: ask whether information is exposed rather than collecting the information.
- Purpose limitation: use responses only for assessment.
- Least privilege: store only derived assessment data.
- Privacy by default: no raw profile scraping.
- Transparency: show why a finding was generated.
- User control: provide deletion endpoint.
- Retention limitation: the project can be extended with scheduled deletion.
