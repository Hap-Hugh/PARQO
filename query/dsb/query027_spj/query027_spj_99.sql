
SELECT min(i_item_id),
       min(s_state),
       min(ss_quantity),
       min(ss_list_price),
       min(ss_coupon_amt),
       min(ss_sales_price),
       min(ss_item_sk),
       min(ss_ticket_number)
FROM store_sales,
     customer_demographics,
     date_dim,
     store,
     item
WHERE ss_sold_date_sk = d_date_sk
  AND ss_item_sk = i_item_sk
  AND ss_store_sk = s_store_sk
  AND ss_cdemo_sk = cd_demo_sk
  AND cd_gender = 'F'
  AND cd_marital_status = 'D'
  AND cd_education_status = '4 yr Degree'
  AND d_year = 2001
  AND s_state = 'KY'
  AND i_category = 'Electronics' ;


