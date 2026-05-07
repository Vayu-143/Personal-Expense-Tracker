import os

from app.data_loader import generate_synthetic_data
from app.data_loader import load_and_clean_data

from app.analytics import category_analysis
from app.analytics import monthly_analysis
from app.analytics import payment_analysis
from app.analytics import daily_analysis
from app.analytics import top_expenses
from app.analytics import budget_analysis

from app.visualizer import category_chart
from app.visualizer import monthly_chart
from app.visualizer import payment_chart
from app.visualizer import daily_chart

from app.report_generator import generate_report

from app.utils import setup_logging
from app.utils import log_message


os.makedirs("images", exist_ok=True)

os.makedirs("reports", exist_ok=True)

os.makedirs("logs", exist_ok=True)

os.makedirs("data/raw", exist_ok=True)

os.makedirs("data/processed", exist_ok=True)


setup_logging()

log_message("Project Started")


print("Generating synthetic expense data...")

generate_synthetic_data()


print("Loading and cleaning data...")

df = load_and_clean_data()


print("Performing analytics...")

category_data = category_analysis(df)

monthly_data = monthly_analysis(df)

payment_data = payment_analysis(df)

daily_data = daily_analysis(df)

budget_result = budget_analysis(df)

highest_category = category_data.idxmax()


print("Generating charts...")

category_chart(category_data)

monthly_chart(monthly_data)

payment_chart(payment_data)

daily_chart(daily_data)


print("Generating report...")

generate_report(df, budget_result, highest_category)


print("\nTop 10 Expenses")

print(top_expenses(df))


print("\nProject Executed Successfully!")

log_message("Project Completed Successfully")