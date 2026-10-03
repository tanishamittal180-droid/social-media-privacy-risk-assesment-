# Project Report: Social Media Privacy Risk Assessment Framework

## Abstract
The Social Media Privacy Risk Assessment Framework is a defensive cybersecurity and privacy-awareness application. It evaluates self-reported social-media privacy practices through a structured questionnaire, converts responses into category-wise risk scores, calculates an overall 0–100 risk score, identifies weaknesses, and provides prioritized recommendations. The system is intentionally privacy-preserving: it does not scrape social-media accounts, access private profiles, track users, or request unnecessary personal information.

## Introduction
Social-media platforms support communication and professional identity but can also expose personal information, location context, historical content, and account-security weaknesses. Users need practical methods to understand their exposure without invasive monitoring.

## Problem Statement
Existing privacy controls are often distributed across platform settings and may be difficult for beginners to evaluate systematically. A repeatable educational assessment can turn privacy hygiene into measurable actions.

## Objectives
- Build a privacy-first assessment workflow.
- Evaluate ten privacy/security categories.
- Generate explainable risk scores.
- Provide personalized recommendations.
- Simulate improvements.
- Demonstrate secure data minimization.
- Provide dashboard and report outputs.

## Social Media Privacy Background
Privacy is concerned with control over personal information and its exposure. Public visibility is not automatically unsafe; context, audience, sensitivity, and purpose matter.

## Digital Footprint
An active footprint includes content intentionally shared. Other online activity can also generate data depending on the service. This project only evaluates self-reported practices.

## Privacy vs Security
Privacy and security overlap but are distinct. Strong account authentication does not automatically minimize information exposure.

## Social Engineering
Public context can sometimes make fraudulent communication more believable. The project teaches verification and cautious communication rather than creating attack scripts.

## Proposed Framework
The workflow is questionnaire -> validation -> feature extraction -> category scoring -> overall score -> findings -> recommendations -> dashboard/report.

## Questionnaire Design
The questionnaire contains 40+ questions covering profile visibility, personal information, location, content, connections, tagging, account security, third-party apps, social engineering, and digital footprint.

## Synthetic Dataset
A Python generator creates 1,000 fictional records. No real people or real account data are used.

## Feature Engineering
Responses are normalized into numerical risk contributions. Public exposure, location sharing, weak authentication, unreviewed integrations, and risky messaging behaviors increase relevant category risk.

## Risk Scoring
Ten categories are combined using configurable weights. The current thresholds are educational assumptions.

## Findings and Recommendations
Each finding includes a category, severity, explanation, and remediation step. Recommendations are prioritized as Immediate, Important, or Good Practice.

## Improvement Simulator
The simulator compares an original answer set with a hypothetical safer answer set. The result is explicitly presented as a model simulation.

## Privacy by Design
The system asks whether information is public rather than collecting the information itself. Database storage contains derived scores and finding metadata.

## Testing
Automated tests cover scoring, boundaries, API validation, simulation, and recommendation generation.

## Results
The application demonstrates a complete privacy-risk workflow, synthetic analytics, explainable findings, and remediation guidance.

## Limitations
The framework does not verify actual platform settings, scrape content, or guarantee real-world security. Weights should be calibrated before professional use.

## Future Scope
Platform-specific checklists, privacy maturity models, organizational policies, localization, accessibility, client-side-only mode, and longitudinal comparisons can be added.

## Conclusion
The project demonstrates how cybersecurity risk assessment and privacy engineering can be combined into a transparent, non-invasive educational tool.
