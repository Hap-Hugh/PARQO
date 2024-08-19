
i_category IN ('Electronics', 'Home', 'Women')
ca_state in ('CA', 'IL', 'MN', 'SC', 'SD')
d1.d_year = 2000
hd_income_band_sk BETWEEN 9 AND 15 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 3 * 0.01 AND 23 * 0.01

;


