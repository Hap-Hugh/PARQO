
i_category IN ('Books', 'Children', 'Home')
ca_state in ('FL', 'IL', 'NE', 'TN', 'TX')
d1.d_year = 2000
hd_income_band_sk BETWEEN 8 AND 14 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 77 * 0.01 AND 97 * 0.01

;


