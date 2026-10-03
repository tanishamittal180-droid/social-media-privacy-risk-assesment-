# Interview Questions and Answers

## 1. Explain your project.
I developed a Social Media Privacy Risk Assessment Framework that evaluates a user's social-media privacy practices without scraping or accessing actual accounts. The user completes a structured questionnaire covering profile visibility, personal-information exposure, location sharing, posts, connections, tagging, account security, third-party applications, social-engineering awareness, and digital-footprint management. The system converts responses into category-wise risk scores and calculates an overall 0–100 score. It identifies high-risk areas and generates prioritized recommendations. I also implemented an improvement simulator and privacy-by-design storage.

## 2. What is the difference between privacy and security?
Privacy concerns how personal information is exposed, shared, and used. Security focuses on protecting accounts, systems, and information from unauthorized access or misuse. A user can have MFA and still expose a phone number or location publicly.

## 3. What is a digital footprint?
A digital footprint is information associated with online activity and presence. My project assesses only self-reported privacy practices such as old public posts, unused accounts, and privacy-setting reviews. It does not track users.

## 4. How does the scoring system work?
Questionnaire responses become category risk contributions. Ten category scores are normalized to 0–100 and combined using configurable weights. Higher values mean higher assessed risk. The weights and thresholds are educational assumptions and require calibration before professional use.

## 5. How can oversharing increase cybersecurity risk?
Public information can provide context that makes fraudulent messages appear more believable. Examples include employer, college, travel, family references, and interests. The framework identifies exposure without assuming that every public detail causes an incident.

## 6. Why include MFA?
Privacy and account security overlap. If an account is taken over, private content and contacts may be exposed. MFA adds an additional authentication layer and is therefore included in the account-security category.

## 7. What risks can third-party applications create?
Applications may retain permissions that are no longer necessary. The framework asks whether integrations are reviewed and encourages least privilege and revocation of unused access.

## 8. What is Privacy by Design?
Privacy by Design means considering privacy throughout development. I applied data minimization by asking whether a phone number is public instead of asking for the number itself. I also avoid passwords, exact locations, and private messages.

## 9. What is the improvement simulator?
It creates a temporary copy of the answers, applies hypothetical safer settings, recalculates the score, and displays the difference. It is explicitly a framework simulation, not a real-world safety guarantee.

## 10. How did you test the project?
I created automated tests for private/public profiles, individual risk factors, score boundaries, recommendations, the API, simulation, and validation. I also document security/privacy checks such as XSS review, data minimization, deletion, and environment-variable handling.
