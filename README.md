# 🔐 Social Media Privacy Risk Assessment Framework

## 📌 Project Overview

The **Social Media Privacy Risk Assessment Framework** is a cybersecurity and privacy-awareness platform designed to analyze social media profile information and identify potential privacy and security risks.

The system evaluates information such as publicly exposed personal information, location data, images, metadata, account settings, and other privacy-related indicators. It then provides a risk assessment along with practical recommendations to reduce unnecessary exposure.

The project is designed primarily for **education, privacy awareness, defensive cybersecurity, and authorized security assessment**.

---

# 🎯 Objectives

The main objectives of this project are:

* Identify privacy risks in social media profiles.
* Detect potentially exposed Personally Identifiable Information (PII).
* Identify possible location and geolocation exposure.
* Analyze image-related privacy risks.
* Detect metadata exposure.
* Evaluate privacy/security settings.
* Generate an overall privacy-risk assessment.
* Provide actionable recommendations.
* Educate users about social-media privacy.
* Demonstrate practical privacy and cybersecurity concepts.

---

# ✨ Key Features

## 👤 1. Social Media Profile Analysis

The platform can analyze an imported social-media profile dataset or authorized profile information.

Possible information analyzed includes:

* Username
* Display name
* Biography
* Email address
* Phone number
* Website links
* Location
* Public posts
* Profile images
* Other publicly exposed information

The system identifies information that may unnecessarily increase privacy exposure.

---

# 🔎 2. PII Exposure Detection

The system searches for potentially sensitive information such as:

* Email addresses
* Phone numbers
* Physical addresses
* Usernames
* URLs
* Organization information
* Other identifiable information

Example:

```text
PII ANALYSIS
--------------------------------
Email detected       : YES
Phone detected       : YES
Address detected     : NO
Website detected     : YES

PII Exposure Level   : HIGH
```

The system should distinguish between **detection** and **actual risk** because not every piece of personal information has the same privacy impact.

---

# 📍 3. Location Privacy Analysis

The platform identifies possible location-related exposure.

It can analyze:

* Profile location
* Post locations
* Geotags
* GPS metadata
* Location mentions
* Repeated location patterns

Example:

```text
LOCATION ANALYSIS
--------------------------------
Profile Location : Detected
Geotagged Posts  : 4
GPS Metadata     : Detected

Risk:
Location exposure requires review.
```

---

# 🖼️ 4. Image Privacy Analysis

Images can reveal information that users may not intentionally publish.

The framework can identify potential risks associated with:

* Faces
* Children/minors
* Identity documents
* Screenshots
* Vehicle information
* House/building information
* Background information
* Sensitive objects
* Location clues

Example:

```text
IMAGE ANALYSIS
--------------------------------
Images analyzed        : 15
Faces detected         : 11
Location clues         : 3
Document-like images   : 1

Recommendation:
Review publicly visible images.
```

The system should avoid making definitive claims about a person's identity from an image unless the application has a legitimate and authorized purpose for doing so.

---

# 🧾 5. Metadata Analysis

Images and files may contain metadata that users do not see directly.

Possible metadata includes:

* GPS coordinates
* Timestamp
* Device information
* Camera information
* Software information

Example:

```text
METADATA CHECK
--------------------------------
GPS Data        : Detected
Camera Model    : Detected
Timestamp       : Detected

Privacy Risk:
Potential metadata exposure.
```

---

# ⚙️ 6. Privacy Settings Assessment

The framework can evaluate available account-security and privacy settings.

Examples:

* Account visibility
* Profile visibility
* Location sharing
* Contact discoverability
* Two-factor authentication
* Message permissions
* Tagging settings
* Mention settings
* Third-party application access

Example:

```text
PRIVACY SETTINGS
--------------------------------
Private Account       : NO
Location Sharing      : ON
2FA                   : OFF
Contact Discovery     : ON

Areas Requiring Review: 4
```

---

# 📊 7. Privacy Risk Score

The application can calculate a risk score based on identified exposure categories.

Example categories:

| Category           | Example                 |
| ------------------ | ----------------------- |
| PII Exposure       | Email, phone number     |
| Location Exposure  | Geotags, location posts |
| Image Exposure     | Faces, documents        |
| Metadata Exposure  | GPS/device metadata     |
| Account Security   | 2FA/settings            |
| Third-Party Access | Connected applications  |
| Public Exposure    | Public profile/content  |

Example:

```text
PRIVACY RISK REPORT
================================

Overall Risk: 68 / 100

PII Exposure       : High
Location Exposure  : Medium
Image Exposure     : Medium
Metadata Exposure  : High
Account Security   : Medium

Recommended Action:
Review exposed personal information,
location information, metadata, and
account security settings.
```

The score is an **awareness aid**, not a scientifically validated measurement of a person's actual security.

---

# 🚦 Risk Levels

The framework can use the following descriptive categories:

|  Score | Level        | Description                   |
| -----: | ------------ | ----------------------------- |
|   0–20 | 🟢 Low       | Limited detected exposure     |
|  21–40 | 🟡 Moderate  | Some privacy concerns         |
|  41–60 | 🟠 Elevated  | Several areas require review  |
|  61–80 | 🔴 High      | Significant exposure detected |
| 81–100 | 🚨 Very High | Extensive exposure detected   |

The exact scoring thresholds can be configured according to the project's assessment methodology.

---

# 💡 8. Privacy Recommendations

After identifying risks, the platform provides remediation guidance.

Examples:

### Email Exposure

**Risk:** Email address is publicly visible.

**Recommendation:**

* Remove it from public profile information where unnecessary.
* Avoid publishing personal email addresses.
* Use privacy controls where available.

### Location Exposure

**Risk:** Posts reveal repeated locations.

**Recommendation:**

* Disable unnecessary location sharing.
* Review old posts.
* Avoid posting real-time locations publicly.

### Metadata Exposure

**Risk:** Images contain GPS metadata.

**Recommendation:**

* Remove metadata before publishing sensitive images.
* Disable unnecessary location tagging.

### Account Security

**Risk:** Two-factor authentication is disabled.

**Recommendation:**

* Enable 2FA where supported.
* Use a unique strong password.
* Review active sessions and connected applications.

---

# 🧠 Privacy Awareness Center

The project can include educational modules covering:

* Social-media privacy
* Phishing
* Social engineering
* Identity theft
* Oversharing
* Location tracking
* Image privacy
* Metadata
* Password security
* Multi-factor authentication
* Account takeover
* Data brokers
* Third-party applications
* Digital footprint

Each module can contain:

```text
Topic
 ↓
Explanation
 ↓
Example
 ↓
Risk
 ↓
Prevention
 ↓
Recommended Action
```

---

# 📥 Supported Input

The framework can be designed to accept authorized profile data in formats such as:

```text
CSV
JSON
TXT
Images
Exported social-media data
```

Example JSON:

```json
{
  "username": "example_user",
  "bio": "Student",
  "email": "example@example.com",
  "location": "Example City",
  "posts": [],
  "images": []
}
```

---

# 🏗️ System Architecture

```text
                    USER
                      │
                      ▼
             ┌─────────────────┐
             │ Upload Profile  │
             │ Data / Dataset  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Input Validation│
             └────────┬────────┘
                      │
          ┌───────────┼────────────┐
          │           │            │
          ▼           ▼            ▼
        PII       Location      Images
      Analysis     Analysis      Analysis
          │           │            │
          └───────────┼────────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Metadata Check  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Privacy Settings│
             │    Analysis     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Risk Assessment │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Recommendations │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Privacy Report  │
             └─────────────────┘
```

---

# 💻 Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* React.js (optional)

## Backend

* Python
* Flask / FastAPI

## Data Processing

* Python
* Pandas
* Regular Expressions
* JSON
* CSV

## Image Analysis

Depending on implementation:

* OpenCV
* Pillow
* Face-detection models

## Database

Possible choices:

* SQLite
* PostgreSQL
* MongoDB

---

# 📁 Recommended Project Structure

```text
social-media-privacy-risk-assessment/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── backend/
│   ├── app.py
│   │
│   ├── routes/
│   │   ├── analysis.py
│   │   ├── privacy.py
│   │   ├── reports.py
│   │   └── awareness.py
│   │
│   ├── services/
│   │   ├── pii_detector.py
│   │   ├── location_analyzer.py
│   │   ├── image_analyzer.py
│   │   ├── metadata_analyzer.py
│   │   └── risk_engine.py
│   │
│   └── database/
│       └── database.py
│
├── frontend/
│   ├── index.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   ├── dashboard.js
│   │   ├── analysis.js
│   │   ├── awareness.js
│   │   └── reports.js
│   │
│   └── assets/
│
├── data/
│   ├── sample_profile.json
│   └── awareness_topics.json
│
├── reports/
│
└── tests/
    ├── test_pii.py
    ├── test_location.py
    ├── test_metadata.py
    └── test_risk.py
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd social-media-privacy-risk-assessment
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start the backend:

```bash
python backend/app.py
```

The application may then be available at:

```text
http://127.0.0.1:5000
```

Open the frontend using the project's configured frontend server or development environment.

---

# 🔌 Example API Endpoints

## Analyze Profile

```http
POST /api/analyze/profile
```

Example:

```json
{
  "username": "example_user",
  "bio": "Example profile",
  "location": "Example City"
}
```

## PII Analysis

```http
POST /api/analyze/pii
```

## Location Analysis

```http
POST /api/analyze/location
```

## Image Analysis

```http
POST /api/analyze/image
```

## Metadata Analysis

```http
POST /api/analyze/metadata
```

## Generate Report

```http
POST /api/report
```

## Awareness Topics

```http
GET /api/awareness
```

---

# 📄 Privacy Report

A generated report can contain:

```text
========================================
SOCIAL MEDIA PRIVACY ASSESSMENT
========================================

Profile:
example_user

Overall Risk:
68 / 100

----------------------------------------
PII EXPOSURE
----------------------------------------
Email: Detected
Phone: Not Detected

----------------------------------------
LOCATION
----------------------------------------
Location Mention: Detected
Geotag: Detected

----------------------------------------
IMAGE PRIVACY
----------------------------------------
Images Analyzed: 10
Potential Sensitive Images: 2

----------------------------------------
METADATA
----------------------------------------
GPS Metadata: Detected

----------------------------------------
RECOMMENDATIONS
----------------------------------------
1. Review publicly visible contact details.
2. Review location-sharing settings.
3. Remove unnecessary metadata.
4. Enable stronger account security.
5. Review old public posts.
========================================
```

---

# 🔒 Data Privacy & Security

Because this application may process sensitive information, privacy must be a core part of its design.

The project should follow principles such as:

* Data minimization
* Purpose limitation
* Secure storage
* Access control
* Encryption where appropriate
* Short data-retention periods
* User consent
* Secure deletion
* Avoiding unnecessary collection of personal information

Sensitive information should not be stored permanently unless there is a legitimate reason to do so.

---

# ⚠️ Ethical & Legal Considerations

This project should only be used with:

* Your own information
* Public information where analysis is permitted
* Data supplied with appropriate authorization
* Synthetic or educational datasets

Do not use the system to collect, profile, track, or analyze another person's private information without appropriate authorization.

The goal of this project is **privacy protection and awareness**, not surveillance.

---

# 🧪 Example Use Case

A user imports their own social-media data.

The system detects:

```text
✓ Email address exposed
✓ Location mentioned
✓ GPS metadata present
✓ Public profile
✓ 2FA not enabled
✓ Several publicly visible images
```

The framework generates:

```text
Privacy Risk: Elevated

Priority Actions:
1. Review public contact information.
2. Remove unnecessary location information.
3. Remove sensitive image metadata.
4. Enable 2FA.
5. Review public posts and images.
```

---

# 📈 Future Enhancements

Future versions can include:

* 🤖 AI-assisted privacy analysis
* 📊 Advanced privacy dashboard
* 📄 PDF privacy reports
* 🔔 Privacy-risk alerts
* 🖼️ Advanced image privacy detection
* 🗺️ Location exposure visualization
* 🧾 EXIF metadata viewer
* 🔐 Password-security module
* 🧑‍🏫 Interactive privacy-awareness quizzes
* 📱 Mobile application
* 🌐 Browser extension
* 🔑 OAuth-based authorized data import
* 📅 Privacy-risk history
* 📈 Risk trend visualization
* 👨‍💼 Admin dashboard
* 🔎 Digital-footprint analysis
* 🧩 Modular risk-scoring engine

---

# 🎓 Learning Outcomes

This project helps students understand:

1. Social-media privacy risks.
2. Personally Identifiable Information (PII).
3. Digital footprints.
4. Location privacy.
5. Image privacy.
6. EXIF metadata.
7. Privacy-by-design principles.
8. Risk assessment.
9. Secure data handling.
10. Cybersecurity awareness.
11. Defensive security practices.
12. Responsible use of personal data.

---

# 🛡️ Project Philosophy

```text
             COLLECT LESS
                  ↓
             EXPOSE LESS
                  ↓
             ANALYZE SAFELY
                  ↓
             IDENTIFY RISKS
                  ↓
             EDUCATE USERS
                  ↓
             REDUCE EXPOSURE
```

The purpose of this project is to help people understand **what information they expose online, why that information can matter, and what practical steps can reduce unnecessary privacy exposure.**

---
# screenshots 
<img width="1363" height="639" alt="Screenshot 2026-10-02 143208" src="https://github.com/user-attachments/assets/3c3f1cf0-0e37-4c5a-a5db-3bcb9ce7d979" />
<img width="1366" height="633" alt="Screenshot 2026-10-02 143243" src="https://github.com/user-attachments/assets/4b29a532-982c-4b99-92a3-eeabb824d561" />
<img width="1358" height="633" alt="Screenshot 2026-10-02 143529" src="https://github.com/user-attachments/assets/806a5569-6c85-4134-b751-013e9cfa4117" />
<img width="1347" height="635" alt="Screenshot 2026-10-02 143545" src="https://github.com/user-attachments/assets/57f8d0b4-704a-49e2-a2e4-78e464583059" />
<img width="1366" height="768" alt="Screenshot 2026-10-02 143558" src="https://github.com/user-attachments/assets/36884efc-77d1-46e7-b471-717f20cf7f51" />
<img width="1366" height="632" alt="Screenshot 2026-10-02 143652" src="https://github.com/user-attachments/assets/8a2dbfdd-adf9-41a8-8df5-d15e467d37a6" />
<img width="1366" height="630" alt="Screenshot 2026-10-02 143738" src="https://github.com/user-attachments/assets/4ac75d24-49b1-435d-826c-f518ec88f8a5" />
<img width="1366" height="768" alt="Screenshot 2026-10-02 144310" src="https://github.com/user-attachments/assets/75872795-4ab0-44b2-9a82-1d81f645515b" />
<img width="1366" height="768" alt="Screenshot 2026-10-02 144342" src="https://github.com/user-attachments/assets/d79f5a8b-2fc9-4154-b9bc-bd7c19e8458f" />

# 👩‍💻 Author

**Social Media Privacy Risk Assessment Framework**

Educational Cybersecurity & Privacy Project

---

# 📜 License

This project may be released under an appropriate open-source license such as the MIT License, subject to the licenses and terms of any third-party libraries, APIs, models, datasets, or services used.
