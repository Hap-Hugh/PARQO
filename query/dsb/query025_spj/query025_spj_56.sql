
SELECT min(i_item_id) ,
       min(i_item_desc) ,
       min(s_store_id) ,
       min(s_store_name) ,
       min(ss_net_profit) ,
       min(sr_net_loss) ,
       min(cs_net_profit) ,
       min(ss_item_sk) ,
       min(sr_ticket_number) ,
       min(cs_order_number)
FROM store_sales ,
     store_returns ,
     catalog_sales ,
     date_dim d1 ,
     date_dim d2 ,
     date_dim d3 ,
     store ,
     item
WHERE d1.d_moy = 5
  AND d1.d_year = 2000
  AND d1.d_date_sk = ss_sold_date_sk
  AND i_item_sk = ss_item_sk
  AND s_store_sk = ss_store_sk
  AND ss_customer_sk = sr_customer_sk
  AND ss_item_sk = sr_item_sk
  AND ss_ticket_number = sr_ticket_number
  AND sr_returned_date_sk = d2.d_date_sk
  AND d2.d_moy BETWEEN 5 AND 5 + 2
  AND d2.d_year = 2000
  AND sr_customer_sk = cs_bill_customer_sk
  AND sr_item_sk = cs_item_sk
  AND cs_sold_date_sk = d3.d_date_sk
  AND d3.d_moy BETWEEN 5 AND 5 + 2
  AND d3.d_year = 2000 ;


