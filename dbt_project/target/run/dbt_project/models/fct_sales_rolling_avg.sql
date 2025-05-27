
  
    

create or replace transient table SUPERSTORE_DB.STAGING.fct_sales_rolling_avg
    

    
    as (with source as (
    select * from SUPERSTORE_DB.STAGING.fct_sales_by_month
),

rolling as (
    select
        order_month,
        category,
        region,
        total_sales,
        total_profit,
        total_orders,
        avg(total_sales) over (
            partition by category, region
            order by order_month
            rows between 2 preceding and current row
        ) as sales_3mo_avg
    from source
)

select * from rolling
    )
;


  