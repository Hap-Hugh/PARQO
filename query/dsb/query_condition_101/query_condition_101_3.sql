
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('FL', 'MI', 'MO', 'TN', 'TX')
d1.d_year = 1999
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 59 * 0.01 AND 79 * 0.01

;


