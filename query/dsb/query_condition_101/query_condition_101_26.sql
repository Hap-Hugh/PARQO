
i_category IN ('Children', 'Jewelry', 'Women')
ca_state in ('IN', 'LA', 'NE', 'VA', 'WV')
d1.d_year = 1999
hd_income_band_sk BETWEEN 6 AND 12 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 67 * 0.01 AND 87 * 0.01

;


