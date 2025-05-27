with source as (
    select * from {{ ref('fct_sales_by_month') }}
),

with_ytd as (
    select
        order_month,
        category,
        region,
        total_sales,
        total_profit,
        total_orders,
        sum(total_sales) over (
            partition by category, region, date_trunc('year', order_month)
            order by order_month
            rows between unbounded preceding and current row
        ) as ytd_sales,
        sum(total_profit) over (
            partition by category, region, date_trunc('year', order_month)
            order by order_month
            rows between unbounded preceding and current row
        ) as ytd_profit
    from source
)


select * from with_ytd
