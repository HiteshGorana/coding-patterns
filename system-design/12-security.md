# 12) Security

## Basics
Security in system design reduces risk from threats while preserving usability and compliance.

Core components:
- Threat modeling basics
- OWASP Top 10 awareness
- Secrets management (KMS/Vault concepts)
- Encryption at rest / in transit
- Key rotation
- RBAC/ABAC
- Network security (zero trust, segmentation)
- Audit logs and compliance basics

## How It Works
1. Identify assets and threat actors.
2. Map trust boundaries and attack paths.
3. Apply preventive and detective controls.
4. Continuously rotate secrets and audit access.

```text
Assets -> Threats -> Controls -> Monitoring -> Response
```

Cause-effect idea:
- Hardcoded secrets -> credential leakage risk.
- Broad permissions -> privilege escalation blast radius.

## Simple Example
Internal admin portal:
- SSO + RBAC roles.
- mTLS between services.
- Secrets from vault at runtime.
- Audit logs for privileged actions.

Analogy: Security is airport control layers: identity check, baggage scan, restricted zones, and surveillance.

## Why and What-If Questions
- Why least privilege?
  - Limits damage from compromised accounts.
- What if encryption keys are stale?
  - Rotate keys and re-encrypt sensitive data by policy.
- What if one subnet is breached?
  - Segmentation reduces lateral movement.

## Practical Applications
- Compliance audits (SOC2, ISO-style controls).
- Protecting customer PII and payments.
- Secure service-to-service communication.

## Compare With Related Ideas
- RBAC vs ABAC: role-based simplicity vs attribute-based flexibility.
- Encryption in transit vs at rest: protects network path vs stored data.

## Retention Tips
- Use a threat model template for every major feature.
- Keep a security checklist in CI for secret scanning and dependency checks.

## Interview Quick Revision (2 Minutes)
- 30 sec: Define this concept in one sentence and state the primary design goal.
- 30 sec: Name 3 core components and how they connect.
- 30 sec: Explain one key tradeoff with a clear "when to choose what" rule.
- 30 sec: Describe one failure mode and the mitigation.

## Common Mistakes
- Jumping to technologies before clarifying requirements and constraints.
- Ignoring failure modes, observability, and rollback/fallback planning.
- Not stating assumptions, data/API boundaries, and scaling limits explicitly.
