
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('MO', 'NY', 'TX', 'VA', 'WV')
d1.d_year = 1999
hd_income_band_sk BETWEEN 6 AND 12 AND hd_buy_potential = '0-500'
ss_sales_price / ss_list_price BETWEEN 25 * 0.01 AND 45 * 0.01

;


