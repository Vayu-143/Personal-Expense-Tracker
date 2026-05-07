import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def category_chart(category_data):

    plt.figure(figsize=(10, 6))

    category_data.plot(kind="bar")

    plt.title("Category-wise Spending")

    plt.xlabel("Category")

    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("images/category_chart.png")

    plt.close()


def monthly_chart(monthly_data):

    plt.figure(figsize=(10, 6))

    monthly_data.plot(marker="o")

    plt.title("Monthly Spending Trend")

    plt.xlabel("Month")

    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("images/monthly_chart.png")

    plt.close()


def payment_chart(payment_data):

    plt.figure(figsize=(8, 8))

    payment_data.plot(kind="pie", autopct="%1.1f%%")

    plt.ylabel("")

    plt.title("Payment Method Distribution")

    plt.tight_layout()

    plt.savefig("images/payment_chart.png")

    plt.close()


def daily_chart(daily_data):

    plt.figure(figsize=(12, 6))

    daily_data.plot()

    plt.title("Daily Spending Trend")

    plt.xlabel("Date")

    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("images/daily_chart.png")

    plt.close()