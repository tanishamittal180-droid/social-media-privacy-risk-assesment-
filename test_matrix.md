# 30-Test Matrix

| ID | Scenario | Expected Result |
|---|---|---|
| T01 | Fully private profile | LOW/low exposure |
| T02 | Fully public synthetic profile | HIGH/CRITICAL exposure |
| T03 | Public phone | Personal-information score increases |
| T04 | Public email | Personal-information score increases |
| T05 | Public birthday | Personal-information score increases |
| T06 | Public location | Location score increases |
| T07 | Real-time check-ins | High location contribution |
| T08 | Travel plans | Location contribution |
| T09 | Workplace exposure | Content/personal exposure considered |
| T10 | Education exposure | Personal-information contribution |
| T11 | Public posts | Content score increases |
| T12 | Unknown connections | Connection score increases |
| T13 | Tag review disabled | Tagging risk increases |
| T14 | MFA disabled | Account-security risk increases |
| T15 | Login alerts disabled | Account-security risk increases |
| T16 | Password reuse reported | Account-security weakness is identified |
| T17 | Third-party apps not reviewed | Third-party score increases |
| T18 | Suspicious-link awareness low | Social-engineering risk increases |
| T19 | Old posts not reviewed | Digital-footprint risk increases |
| T20 | Privacy settings not reviewed | Digital-footprint finding |
| T21 | Category calculation | All 10 categories returned |
| T22 | Overall calculation | Score is 0–100 |
| T23 | Score boundary 20 | LOW |
| T24 | Score boundary 40 | MODERATE |
| T25 | Score boundary 70 | HIGH |
| T26 | Recommendations | Prioritized recommendations returned |
| T27 | Improvement simulation | Before/after scores returned |
| T28 | Database save | Assessment retrievable by ID |
| T29 | Sensitive data storage | No raw phone/address/password fields |
| T30 | Report generation | HTML/PDF report available |
