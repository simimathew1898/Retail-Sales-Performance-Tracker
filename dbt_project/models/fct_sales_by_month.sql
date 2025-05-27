with source as (
    select * from {{ ref('stg_orders') }}
),

transformed as (
    select
        date_trunc('month', order_date) as order_month,
        category,
        region,
        sum(sales) as total_sales,
        sum(profit) as total_profit,
        count(distinct order_id) as total_orders
    from source
    group by 1, 2, 3
)

select * from transformed
