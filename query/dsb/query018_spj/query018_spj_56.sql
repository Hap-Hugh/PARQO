
SELECT min(i_item_id),
       min(ca_country),
       min(ca_state),
       min(ca_county),
       min(cs_quantity),
       min(cs_list_price),
       min(cs_coupon_amt),
       min(cs_sales_price),
       min(cs_net_profit),
       min(c_birth_year),
       min(cd_dep_count)
FROM catalog_sales,
     customer_demographics,
     customer,
     customer_address,
     date_dim,
     item
WHERE cs_sold_date_sk = d_date_sk
  AND cs_item_sk = i_item_sk
  AND cs_bill_cdemo_sk = cd_demo_sk
  AND cs_bill_customer_sk = c_customer_sk
  AND cd_gender = 'F'
  AND cd_education_status = 'Unknown'
  AND c_current_addr_sk = ca_address_sk
  AND d_year = 1999
  AND c_birth_month = 5
  AND ca_state in ('GA', 'IA', 'NJ')
  AND cs_wholesale_cost BETWEEN 5 AND 10
  AND i_category = 'Men' ;


