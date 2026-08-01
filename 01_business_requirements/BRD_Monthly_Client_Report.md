# Business Requirements Document (BRD)

## Report Name
Monthly Client Account Statement

## Document Owner
Varikuti Bhanuhshre (Business/Operations Analyst)

## Version
1.0

## Date
2026

---

## 1. Background

The operations team currently produces monthly client account statements through a manual process involving spreadsheet exports and manual formatting. This process is time-consuming and prone to formatting inconsistencies and missed accounts. The business has requested an automated report to replace the manual process.

## 2. Stakeholders

| Stakeholder | Role | Interest |
|---|---|---|
| Operations Team | Report owner | Timely, accurate, low-effort generation |
| Client Relationship Team | Report distributor | Report must be client-ready and error-free |
| Compliance | Reviewer | Report must include all required disclosures and match source records exactly |
| Technology | Builder | Needs clear, testable requirements to build against |

## 3. Objective

Automate the generation of the monthly client account statement so that it can be produced on a fixed schedule, with no discrepancies against the underlying transaction data, and in a format acceptable for direct client distribution.

## 4. Scope

**In scope:**
- Automated generation of one statement per active client account
- Inclusion of account summary, transaction history for the reporting month, and closing balance
- Exclusion of closed or inactive accounts

**Out of scope:**
- Multi-language statement versions
- Real-time statement generation (monthly batch only)
- Integration with the live production database (mock data used for this project)

## 5. Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | The report must include one row per transaction for the reporting month |
| FR-02 | The report must display an opening balance, list of transactions, and a closing balance per account |
| FR-03 | The closing balance must equal the opening balance plus the net of all listed transactions |
| FR-04 | Closed accounts must not appear in the output |
| FR-05 | The report must be generated for all active accounts in a single run |
| FR-06 | Each statement must display the account holder name, account ID, and statement period |

## 6. Acceptance Criteria

- All active accounts in the source data appear in the output; no active account is missing
- No closed account appears in the output
- Closing balance on every statement mathematically matches opening balance plus net transactions
- Statement period and account details match the source data exactly
- Output is generated without manual intervention once source data is provided

## 7. Assumptions

- Source data is assumed clean and complete for the reporting month (data quality issues are out of scope for this phase)
- Reporting month and account data are provided as a single input file

## 8. Milestones

| Milestone | Target |
|---|---|
| Requirements sign-off | Week 1 |
| Report build complete | Week 2 |
| UAT complete | Week 3 |
| Stakeholder sign-off | Week 4 |

## 9. Sign-off

| Stakeholder | Status |
|---|---|
| Operations Team | Approved |
| Client Relationship Team | Approved |
| Compliance | Approved |

