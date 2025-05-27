
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select order_month
from SUPERSTORE_DB.STAGING.fct_sales_by_month
where order_month is null



  
  
      
    ) dbt_internal_test