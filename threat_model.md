# Defensive Threat Model

| Asset | Threat | Exposure | Potential Impact | Existing Control | Recommended Control |
|---|---|---|---|---|---|
| Social account | Account takeover | Weak authentication | Unauthorized access | MFA question | Enable MFA |
| Identity information | Impersonation | Overshared profile data | Fraud/social engineering | Exposure scoring | Minimize public information |
| Contact information | Phishing | Public phone/email | Targeted scams | PII scoring | Restrict visibility |
| Location privacy | Stalking/unwanted attention | Real-time location | Physical/privacy risk | Location questions | Avoid live location broadcasts |
| Private content | Unwanted access | Weak settings | Confidentiality loss | Visibility scoring | Review audience settings |
| Social relationships | Social engineering | Public connections | Convincing fraud | Connection controls | Verify unfamiliar requests |
| Third-party access | Excessive permissions | Old integrations | Unnecessary data access | App review questions | Revoke unused permissions |
