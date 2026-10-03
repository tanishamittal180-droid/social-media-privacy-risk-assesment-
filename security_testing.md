# Security and Privacy Testing Checklist

## Data minimization
- [ ] Application does not request passwords.
- [ ] Application does not request actual phone numbers.
- [ ] Application does not request actual addresses.
- [ ] Application does not request exact location.
- [ ] Application does not request private messages.
- [ ] Stored database contains derived data only.

## Input validation
- [ ] Missing answers are rejected.
- [ ] Invalid enumerated values are rejected.
- [ ] Request body size is limited.
- [ ] Unknown simulation fields are rejected.

## XSS
- [ ] User-controlled report values are HTML-escaped.
- [ ] Do not insert untrusted content with unsafe HTML in future extensions.
- [ ] Keep templates escaped by default if a template engine is introduced.

## Rate limiting
This educational local build does not include production rate limiting. For deployment, add Flask-Limiter or an API gateway rate limiter.

## Authentication
This local student version does not create user accounts. If accounts are added, use secure sessions, MFA for administrators, authorization checks, CSRF protection, password hashing, and secure cookies.

## Secrets
- [ ] Use environment variables for secrets.
- [ ] Never commit .env.
- [ ] Rotate demo secrets before deployment.

## Reports
- [ ] Reports contain no unnecessary sensitive data.
- [ ] Report generation uses escaped text.
- [ ] Delete generated reports when no longer needed.

## Deletion
The API exposes DELETE /api/assessment/{id}. A production version should add authentication/authorization before enabling deletion of shared records.

## Ethical controls
- [ ] No scraping.
- [ ] No private-account access.
- [ ] No account enumeration.
- [ ] No tracking of real individuals.
