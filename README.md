# Retail Sales Performance Tracker

This project demonstrates an end-to-end data pipeline using the Superstore sales dataset. The goal is to load, model, and analyze retail performance metrics such as sales, profit, and discounts by region, category, and time.

The pipeline uses Snowflake as the cloud data warehouse, dbt for data transformation, and Streamlit for dashboarding. Python is used for the initial data ingestion.

## Project Overview

The dataset contains historical sales records, including:

- Order and shipment dates
- Customer and regional information
- Product details by category and sub-category
- Metrics such as sales, quantity, profit, and discount

The pipeline focuses on turning raw data into structured insights using cloud and open-source tools.

## Tools and Technologies

- Python – for data ingestion
- Snowflake – cloud-based data warehouse
- dbt Cloud – data modeling and transformation
- Streamlit – building a basic reporting dashboard
- Git & GitHub – version control and documentation

## Folder Structure

Retail-Sales-Performance-Tracker/
├── data/ # Raw CSV file (ignored in .gitignore)
├── scripts/ # Python ingestion scripts
├── dbt_project/ # dbt models, configs, and tests
├── dashboard/ # Streamlit dashboard (to be added)
├── diagrams/ # ER diagrams or architecture visuals
├── .gitignore
├── README.md
└── requirements.txt


## Project Progress

- [x] CSV data previewed and cleaned using pandas
- [x] Data loaded into Snowflake using Python connector
- [ ] dbt models for staging and metrics
- [ ] dbt tests and documentation
- [ ] Interactive dashboard using Streamlit

## Dataset

- Source: [Kaggle – Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- License: Public domain, suitable for portfolio use

## How to Run

1. Clone this repository
2. Install Python requirements: `pip install -r requirements.txt`
3. Place `Superstore.csv` in the `data/` folder (not committed to GitHub)
4. Configure your Snowflake credentials
5. Run `scripts/upload_to_snowflake.py` to create the raw table
6. Follow `dbt_project/` setup instructions for modeling
7. Launch the dashboard (when ready) using Streamlit

## About

This project is intended as a personal learning and portfolio exercise. It showcases core concepts in cloud data engineering including data ingestion, transformation, and reporting.



