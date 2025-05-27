
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select category
from SUPERSTORE_DB.STAGING.fct_sales
where category is null



  
  
      
    ) dbt_internal_test