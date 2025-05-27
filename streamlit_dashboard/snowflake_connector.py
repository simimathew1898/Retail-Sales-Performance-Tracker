import snowflake.connector
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

def fetch_fct_sales():
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

    print("Account:", os.getenv("SNOWFLAKE_ACCOUNT"))

    query = "SELECT * FROM FCT_SALES"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def fetch_sales_rolling_avg():
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

    query = "SELECT * FROM FCT_SALES_ROLLING_AVG ORDER BY ORDER_MONTH"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def fetch_sales_ytd():
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    query = "SELECT * FROM FCT_SALES_BY_MONTH_YTD"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
