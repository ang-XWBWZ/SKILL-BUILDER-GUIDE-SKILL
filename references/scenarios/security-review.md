# Security Boundary Skills

Create a security-specific skill for recurring changes that touch authority, sensitive data, untrusted input, secrets, external integrations, or privileged operations.

## Boundary map

For each candidate, record:

| Element | Questions |
|---|---|
| Asset | What data, capability, or availability property is protected? |
| Actor | Who can invoke the action and how are they authenticated? |
| Trust boundary | Where does untrusted data or authority enter? |
| Control | What validates, authorizes, logs, rate-limits, or contains failure? |
| Evidence | Which test, policy, configuration, or source path proves it? |

## Authoring notes

- Make residual risk and owner approval explicit rather than hiding uncertainty.
- Include misuse cases relevant to the project: injection, replay, access escalation, disclosure, unsafe default, dependency compromise, or audit gaps.
- Keep secrets out of all examples and outputs.
- Treat security reviews as risk reduction, not proof of complete security.

## Done definition

The skill lets an agent identify touched boundaries, test the applicable controls, and escalate decisions that require security or ownership authority.
