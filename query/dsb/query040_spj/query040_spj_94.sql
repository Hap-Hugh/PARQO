
SELECT min(w_state) ,
       min(i_item_id) ,
       min(cs_item_sk) ,
       min(cs_order_number) ,
       min(cr_item_sk) ,
       min(cr_order_number)
FROM catalog_sales
LEFT OUTER JOIN catalog_returns ON (cs_order_number = cr_order_number
                                    AND cs_item_sk = cr_item_sk) ,warehouse ,
                                                                  item ,
                                                                  date_dim
WHERE i_item_sk = cs_item_sk
  AND cs_warehouse_sk = w_warehouse_sk
  AND cs_sold_date_sk = d_date_sk
  AND d_date BETWEEN (CAST ('2002-05-21' AS date) - interval '30 day') AND (CAST ('2002-05-21' AS date) + interval '30 day')
  AND i_category = 'Men'
  AND i_manager_id BETWEEN 61 AND 100
  AND cs_wholesale_cost BETWEEN 39 AND 58
  AND cr_reason_sk = 17 ;


