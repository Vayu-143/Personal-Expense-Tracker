from app.config import MONTHLY_BUDGET


def category_analysis(df):

    return df.groupby("Category")["Amount"].sum().sort_values(ascending=False)


def monthly_analysis(df):

    return df.groupby("Month")["Amount"].sum()


def payment_analysis(df):

    return df.groupby("Payment_Method")["Amount"].sum()


def daily_analysis(df):

    return df.groupby("Date")["Amount"].sum()


def top_expenses(df):

    return df.sort_values(by="Amount", ascending=False).head(10)


def budget_analysis(df):

    total_spending = df["Amount"].sum()

    remaining_budget = MONTHLY_BUDGET - total_spending

    return {
        "total_spending": total_spending,
        "remaining_budget": remaining_budget,
        "overspent": total_spending > MONTHLY_BUDGET
    }