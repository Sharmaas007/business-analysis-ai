---
name: BABOK BA Artifact Conventions
agent: ba_artifact_creator
applyTo: **/*.ba.md, **/*.babok.md, **/*.requirement.md, **/*.business_analysis.md, **/*.artifact.md, **/*.ba_artifact.md
---

# BABOK BA Artifact Conventions

## Purpose
- Ensure all Business Analysis (BA) artifacts follow BABOK guidelines for structure, clarity, and completeness.

## General Principles
- Use BABOK terminology and structure for all BA artifacts (e.g., Business Requirement Document, Use Case, Process Model, etc.).
- Clearly state the artifact type at the top (e.g., "Business Requirements Document").
- Each artifact must include:
  - Purpose/Scope
  - Stakeholders
  - Requirements (business, stakeholder, solution, transition as applicable)
  - Acceptance Criteria or Success Measures
  - Assumptions, Constraints, and Risks
- Use clear, unambiguous language suitable for business and technical audiences.
- Number and organize requirements for traceability.
- Use tables, lists, and diagrams where appropriate for clarity.
- Avoid implementation details unless required by the artifact type.

## Example Structure

Business Requirements Document

1. Purpose
2. Scope
3. Stakeholders
4. Business Requirements
   - BR-1: ...
   - BR-2: ...
5. Acceptance Criteria
6. Assumptions and Constraints
7. Risks

## Notes
- If the artifact type is not specified, default to a "Business Requirements Document" structure.
- If any required section is missing, prompt the user to provide the information or add a placeholder.

---

This instruction enforces BABOK-aligned structure and content for all BA artifacts. Example prompt: "Create a business requirements document for a new HR onboarding system following BABOK guidelines."

Related customizations: Consider adding instructions for BABOK-aligned use cases, process models, or stakeholder analysis templates.