
SELECT min(i_item_sk) ,
       min(w_warehouse_name) ,
       min(d1.d_week_seq) ,
       min(cs_item_sk) ,
       min(cs_order_number) ,
       min(inv_item_sk)
FROM catalog_sales
JOIN inventory ON (cs_item_sk = inv_item_sk)
JOIN warehouse ON (w_warehouse_sk=inv_warehouse_sk)
JOIN item ON (i_item_sk = cs_item_sk)
JOIN customer_demographics ON (cs_bill_cdemo_sk = cd_demo_sk)
JOIN household_demographics ON (cs_bill_hdemo_sk = hd_demo_sk)
JOIN date_dim d1 ON (cs_sold_date_sk = d1.d_date_sk)
JOIN date_dim d2 ON (inv_date_sk = d2.d_date_sk)
JOIN date_dim d3 ON (cs_ship_date_sk = d3.d_date_sk)
LEFT OUTER JOIN promotion ON (cs_promo_sk=p_promo_sk)
LEFT OUTER JOIN catalog_returns ON (cr_item_sk = cs_item_sk
                                    AND cr_order_number = cs_order_number)
WHERE d1.d_week_seq = d2.d_week_seq
  AND inv_quantity_on_hand < cs_quantity
  AND d3.d_date > d1.d_date + interval '3 day'
  AND hd_buy_potential = '>10000'
  AND d1.d_year = 1998
  AND cd_marital_status = 'D'
  AND cd_dep_count BETWEEN 3 AND 5
  AND i_category IN ('Electronics', 'Jewelry', 'Men')
  AND cs_wholesale_cost BETWEEN 80 AND 100 ;


