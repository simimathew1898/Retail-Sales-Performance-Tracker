import streamlit as st
import pandas as pd
from snowflake_connector import fetch_fct_sales

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("Retail Sales Performance Dashboard")

# Fetch data
df = fetch_fct_sales()

# Show filters
region_filter = st.sidebar.multiselect("Select Region(s)", df['REGION'].unique(), default=df['REGION'].unique())
category_filter = st.sidebar.multiselect("Select Category", df['CATEGORY'].unique(), default=df['CATEGORY'].unique())

filtered_df = df[(df['REGION'].isin(region_filter)) & (df['CATEGORY'].isin(category_filter))]

# Show KPIs
st.metric("Total Sales", f"${filtered_df['TOTAL_SALES'].sum():,.2f}")
st.metric("Total Profit", f"${filtered_df['TOTAL_PROFIT'].sum():,.2f}")
st.metric("Total Orders", f"{filtered_df['TOTAL_ORDERS'].sum():,}")

# Bar chart
st.subheader("Sales by Category")
sales_by_cat = filtered_df.groupby("CATEGORY")["TOTAL_SALES"].sum()
st.bar_chart(sales_by_cat)

# Data preview
st.subheader("Raw Data")
st.dataframe(filtered_df)
