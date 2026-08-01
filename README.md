# Business-Analysis-UAT-Simulation-for-Client-Reporting
End-to-end operations project simulating client report delivery: business requirements documentation, Python-based report pipeline, UAT test case design, and project status tracking from requirements to sign-off.

## Table of Contents

- [Overview](#overview)
- [Business Scenario](#business-scenario)
- [Project Workflow](#project-workflow)
- [How to Run This Project](#how-to-run-this-project)
- [Requirements Traceability](#requirements-traceability)
- [Tools Used](#tools-used)
- [Key Learnings](#key-learnings)
- [Future Improvements](#future-improvements)

---

## Overview

In most operations and reporting roles, the hardest part of a project isn't writing the query — it's translating a stakeholder's request into requirements clear enough to build against, and then proving the final report actually meets those requirements before it reaches a client.

This project was built to practice that full lifecycle, start to finish, using a realistic scenario rather than just a technical exercise.

## Business Scenario

An operations team currently produces a **monthly client account statement** through a manual, spreadsheet-based process that is time-consuming and error-prone. The business requests an automated version of this report. Stakeholders across Operations, Client Relationship, and Compliance need the new report to be accurate, consistent, and ready for client distribution — with zero discrepancies against the source data.

## Project Workflow

The project follows five phases, matching how a real reporting request would typically move through an operations team:

| Phase | What Happens |
|---|---|
| **1. Requirements Gathering** | Stakeholder needs are captured and documented in a formal Business Requirements Document (BRD) |
| **2. Data Setup** | A mock client account and transaction dataset stands in for a production data source |
| **3. Report Build** | A Python pipeline generates the statement directly from the source data |
| **4. User Acceptance Testing** | Test cases are written and executed to verify the report against the BRD's acceptance criteria |
| **5. Project Tracking** | Milestones, owners, and status are logged from kickoff through sign-off |

## How to Run This Project

Each step can be run independently, in order, from the command line:

```bash
# 1. Generate the mock source data
cd 02_data
python3 generate_mock_data.py

# 2. Build the report from that data
cd ../03_pipeline
python3 generate_report.py

# 3. Rebuild the UAT test case workbook (optional — already included)
cd ../04_uat_scripts
python3 build_uat_workbook.py

# 4. Rebuild the project tracker (optional — already included)
cd ../05_project_tracking
python3 build_status_tracker.py

# 5. Generate the sample client statement PDF
cd ../06_sample_output
python3 build_sample_statement.py
```

**Requirements:** Python 3, `pandas`, `openpyxl`, `reportlab`, `faker`

## Requirements Traceability

Every rule in the report pipeline is traced back to a specific requirement in the BRD, so the code and the documentation stay linked:

| Requirement ID | Description | Verified By |
|---|---|---|
| FR-01 | One row per transaction for the reporting month | UAT-04 |
| FR-02 | Opening balance, transactions, and closing balance shown per account | UAT-06 |
| FR-03 | Closing balance = opening balance + net transactions | UAT-03 |
| FR-04 | Closed accounts excluded from the report | UAT-01, UAT-08 |
| FR-05 | All active accounts included in a single run | UAT-02 |
| FR-06 | Account holder, account ID, and statement period shown | UAT-05, UAT-10 |

Full detail on each test case — including actual results — is in `04_uat_scripts/UAT_Test_Cases.xlsx`.

## Tools Used

Python, Pandas, OpenPyXL, ReportLab, structured business documentation (BRD, UAT scripts), Excel-based project tracking

## Key Learnings

Working through this project made clear how much of an operations analyst's value sits outside the data pull itself. Writing requirements precise enough to be *testable* is harder than it sounds — a vague requirement produces a report no one can confidently sign off on. Designing UAT cases also forced a shift in thinking: from "does the code run" to "does the output match what the business actually asked for," including edge cases like closed accounts, missing data, and zero-transaction months. Keeping the tracker updated throughout also showed how visibility, not just execution, is a core part of delivering a request stakeholders can trust.

## Future Improvements

- Add a second report type to test how well the requirements and UAT framework generalize
- Automate UAT checks in Python instead of verifying and logging results manually
- Add a sign-off log capturing stakeholder comments at each milestone
