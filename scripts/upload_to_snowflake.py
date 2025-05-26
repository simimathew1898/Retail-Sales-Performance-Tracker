import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Step 1: Read the CSV
df = pd.read_csv('data/Superstore.csv', encoding='ISO-8859-1')

# Clean column names for Snowflake (remove spaces and special characters)
df.columns = [col.strip().replace(' ', '_').replace('-', '_').lower() for col in df.columns]

print("Column names after cleaning:", df.columns.tolist())


# Step 2: Connect to Snowflake
conn = snowflake.connector.connect(
    user='USERNAME',
    password='PASSWORD*',
    account='goyjbep-ib68545',
    warehouse='DEMO_WH',
    database='SUPERSTORE_DB',
    schema='RAW'
)

# Step 3: Create a cursor
cur = conn.cursor()

# Step 4: Create the table (overwrite if exists)
cur.execute("""
    CREATE OR REPLACE TABLE RAW_SUPERSTORE (
        row_id INT,
        order_id STRING,
        order_date DATE,
        ship_date DATE,
        ship_mode STRING,
        customer_id STRING,
        customer_name STRING,
        segment STRING,
        country STRING,
        city STRING,
        state STRING,
        postal_code STRING,
        region STRING,
        product_id STRING,
        category STRING,
        sub_category STRING,
        product_name STRING,
        sales FLOAT,
        quantity INT,
        discount FLOAT,
        profit FLOAT
    );
""")


# Step 5: Upload data using write_pandas
success, nchunks, nrows, _ = write_pandas(
    conn, 
    df, 
    table_name='RAW_SUPERSTORE',
    quote_identifiers=False  
)
print("\nUpload Successful: " + str(success))
print("\nRows Uploaded: " + str(nrows))

# Close connection
cur.close()
conn.close()
