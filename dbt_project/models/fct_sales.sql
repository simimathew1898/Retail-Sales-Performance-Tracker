-- models/fct_sales.sql

select
    category,
    region,
    sum(sales) as total_sales,
    sum(profit) as total_profit,
    count(distinct order_id) as total_orders
from {{ ref('stg_orders') }}
group by category, region
