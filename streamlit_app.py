import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Expense Dashboard",
    layout="wide"
)

st.title("Personal Expense Tracker Dashboard")

df = pd.read_csv("data/processed/cleaned_expenses.csv")

st.subheader("Dataset Preview")

st.dataframe(df.head())

total_spending = df["Amount"].sum()

st.metric(
    "Total Spending",
    f"₹ {total_spending}"
)

category = df.groupby("Category")["Amount"].sum().reset_index()

fig1 = px.bar(
    category,
    x="Category",
    y="Amount",
    title="Category-wise Spending"
)

st.plotly_chart(fig1, use_container_width=True)

monthly = df.groupby("Month")["Amount"].sum().reset_index()

fig2 = px.line(
    monthly,
    x="Month",
    y="Amount",
    title="Monthly Spending Trend",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

payment = df.groupby("Payment_Method")["Amount"].sum().reset_index()

fig3 = px.pie(
    payment,
    names="Payment_Method",
    values="Amount",
    title="Payment Method Distribution"
)

st.plotly_chart(fig3, use_container_width=True)