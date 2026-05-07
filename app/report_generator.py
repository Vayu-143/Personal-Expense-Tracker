from app.config import REPORT_PATH


def generate_report(df, budget_result, top_category):

    report = f"""
==============================
PERSONAL EXPENSE REPORT
==============================

Total Spending: {df['Amount'].sum()}

Average Expense: {df['Amount'].mean():.2f}

Highest Spending Category: {top_category}

Remaining Budget: {budget_result['remaining_budget']}

Overspent: {budget_result['overspent']}

==============================
"""

    with open(REPORT_PATH, "w") as file:

        file.write(report)