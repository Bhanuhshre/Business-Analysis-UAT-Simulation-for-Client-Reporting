"""
Builds the monthly client account statement from the mock source data,
per the requirements defined in:
01_business_requirements/BRD_Monthly_Client_Report.md

Rules implemented (traced to BRD requirement IDs):
    FR-01  One row per transaction for the reporting month
    FR-02  Opening balance, transactions, closing balance per account
    FR-03  Closing balance = opening balance + net of transactions
    FR-04  Closed accounts excluded
    FR-05  All active accounts included in a single run
    FR-06  Account holder name, account ID, statement period shown

Input:
    ../02_data/mock_client_data.csv

Output:
    statement_output.csv   (one row per account with computed closing balance)
"""

import pandas as pd

INPUT_PATH = "../02_data/mock_client_data.csv"
OUTPUT_PATH = "statement_output.csv"

df = pd.read_csv(INPUT_PATH)

# FR-04: exclude closed accounts
active_df = df[df["account_status"] == "Active"].copy()

# Ensure numeric transaction amounts (blank rows become 0 net effect)
active_df["transaction_amount"] = pd.to_numeric(
    active_df["transaction_amount"], errors="coerce"
).fillna(0)

statements = []

# FR-05: process every active account in a single run
for account_id, group in active_df.groupby("account_id"):
    account_holder = group["account_holder"].iloc[0]
    statement_period = group["statement_period"].iloc[0]
    opening_balance = group["opening_balance"].iloc[0]

    net_transactions = group["transaction_amount"].sum()
    closing_balance = round(opening_balance + net_transactions, 2)  # FR-03
    transaction_count = (group["transaction_amount"] != 0).sum()

    statements.append({
        "account_id": account_id,          # FR-06
        "account_holder": account_holder,  # FR-06
        "statement_period": statement_period,  # FR-06
        "opening_balance": round(opening_balance, 2),  # FR-02
        "transaction_count": transaction_count,        # FR-01
        "net_transactions": round(net_transactions, 2),
        "closing_balance": closing_balance,             # FR-02 / FR-03
    })

report_df = pd.DataFrame(statements).sort_values("account_id")
report_df.to_csv(OUTPUT_PATH, index=False)

print(f"Generated statements for {len(report_df)} active accounts -> {OUTPUT_PATH}")

