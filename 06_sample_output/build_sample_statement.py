"""
Builds a sample client-facing PDF statement for one account, using the
actual output produced by 03_pipeline/generate_report.py.
"""

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

report_df = pd.read_csv("../03_pipeline/statement_output.csv")
source_df = pd.read_csv("../02_data/mock_client_data.csv")

# Pick one account to render as the sample statement
account_id = "ACC-1001"
account_summary = report_df[report_df["account_id"] == account_id].iloc[0]
account_txns = source_df[
    (source_df["account_id"] == account_id) & (source_df["account_status"] == "Active")
].sort_values("transaction_date")

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleStyle", parent=styles["Title"], fontSize=18)
normal = styles["Normal"]

doc = SimpleDocTemplate("sample_monthly_report.pdf", pagesize=letter,
                         topMargin=0.6 * inch, bottomMargin=0.6 * inch)
story = []

story.append(Paragraph("Monthly Client Account Statement", title_style))
story.append(Spacer(1, 6))
story.append(Paragraph(f"Statement Period: {account_summary['statement_period']}", normal))
story.append(Spacer(1, 12))

summary_data = [
    ["Account ID", account_summary["account_id"]],
    ["Account Holder", account_summary["account_holder"]],
    ["Opening Balance", f"${account_summary['opening_balance']:,.2f}"],
    ["Closing Balance", f"${account_summary['closing_balance']:,.2f}"],
    ["Number of Transactions", str(int(account_summary["transaction_count"]))],
]
summary_table = Table(summary_data, colWidths=[2.2 * inch, 3.2 * inch])
summary_table.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D9D9D9")),
    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F2F2F2")),
]))
story.append(summary_table)
story.append(Spacer(1, 18))

story.append(Paragraph("Transaction Detail", styles["Heading2"]))
story.append(Spacer(1, 6))

txn_header = ["Date", "Type", "Amount"]
txn_rows = [txn_header]
for _, row in account_txns.iterrows():
    amount = float(row["transaction_amount"])
    txn_rows.append([
        row["transaction_date"],
        row["transaction_type"],
        f"${amount:,.2f}" if amount >= 0 else f"(${abs(amount):,.2f})"
    ])

txn_table = Table(txn_rows, colWidths=[1.8 * inch, 2.2 * inch, 1.6 * inch])
txn_table.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4472C4")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D9D9D9")),
    ("ALIGN", (2, 0), (2, -1), "RIGHT"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F7F7")]),
]))
story.append(txn_table)
story.append(Spacer(1, 18))

note_style = ParagraphStyle("Note", parent=normal, fontSize=8, textColor=colors.grey)
story.append(Paragraph(
    "This statement was generated automatically from the monthly reporting pipeline. "
    "For questions, contact the Client Relationship team.", note_style
))

doc.build(story)
print("Saved sample_monthly_report.pdf")
