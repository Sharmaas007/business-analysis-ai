---
name: Jira User Story Conventions
agent: user_story_creator
applyTo:"**/.agent.md"
  - "*"
description: |
  Enforce simple Jira user story conventions for all user stories generated or managed by the user_story_creator agent.
---

# Jira User Story Conventions

## Default Project
- Project type: SCRUM

## Issue Type
- Use the appropriate Jira issue type (e.g., Story, Task, Bug) as required by the context.

## Summary Format
- Always prefix the summary with "GHCP" (e.g., "GHCP: User can reset password").
- Each user story must have a clear, concise summary (max 1 line).

## Labels
- Add the label: AI generated

- Each user story must have a clear, concise summary (max 1 line).
- Use the format: "As a [user], I want [feature] so that [benefit]" in the description.
- List acceptance criteria as bullet points, each starting with "Given/When/Then" or similar BDD style.
- Use plain, unambiguous language suitable for Jira.
- Ensure all fields (summary, description, acceptance criteria) are present and well-structured.
- Avoid technical jargon unless required for clarity.
- If updating or managing an existing Jira PBI, preserve original context and only enhance clarity or completeness.
- Do not include implementation details or solutions—focus on requirements and outcomes.

## Example

Summary: User can reset password

Description: As a registered user, I want to reset my password so that I can regain access if I forget it.

Acceptance Criteria:
- Given I am on the login page, when I click "Forgot Password", then I am prompted to enter my email address.
- Given I submit a valid email, when I receive the reset link, then I can set a new password.
- Given I set a new password, when I log in, then my new password is accepted.
