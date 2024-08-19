
SELECT min(s_store_name) ,
       min(s_company_id) ,
       min(s_street_number) ,
       min(s_street_name) ,
       min(s_suite_number) ,
       min(s_city) ,
       min(s_zip) ,
       min(ss_ticket_number) ,
       min(ss_sold_date_sk) ,
       min(sr_returned_date_sk) ,
       min(ss_item_sk) ,
       min(d1.d_date_sk)
FROM store_sales ,
     store_returns ,
     store ,
     date_dim d1 ,
     date_dim d2
WHERE d2.d_moy = 3
  AND ss_ticket_number = sr_ticket_number
  AND ss_item_sk = sr_item_sk
  AND ss_sold_date_sk = d1.d_date_sk
  AND sr_returned_date_sk = d2.d_date_sk
  AND ss_customer_sk = sr_customer_sk
  AND ss_store_sk = s_store_sk
  AND sr_store_sk = s_store_sk
  AND d1.d_date BETWEEN (d2.d_date - interval '120 day') AND d2.d_date
  AND d1.d_dow = 1
  AND s_state in ('FL', 'MS', 'NJ') ;


