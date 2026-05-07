import pandas as pd
import numpy as np

from app.config import DATA_PATH
from app.config import PROCESSED_DATA_PATH


def generate_synthetic_data():

    np.random.seed(42)

    categories = [
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Entertainment",
        "Healthcare",
        "Education"
    ]

    payment_methods = [
        "UPI",
        "Cash",
        "Credit Card",
        "Debit Card"
    ]

    descriptions = [
        "Lunch",
        "Groceries",
        "Movie",
        "Online Shopping",
        "Electricity Bill",
        "Bus Fare",
        "Medicine",
        "Books"
    ]

    dates = pd.date_range(start="2025-01-01", periods=180)

    data = {
        "Date": np.random.choice(dates, 500),

        "Category": np.random.choice(categories, 500),

        "Amount": np.random.randint(100, 5000, 500),

        "Payment_Method": np.random.choice(payment_methods, 500),

        "Description": np.random.choice(descriptions, 500)
    }

    df = pd.DataFrame(data)

    df.to_csv(DATA_PATH, index=False)

    return df


def load_and_clean_data():

    df = pd.read_csv(DATA_PATH)

    df.dropna(inplace=True)

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    df["Day"] = df["Date"].dt.day_name()

    df.to_csv(PROCESSED_DATA_PATH, index=False)

    return df