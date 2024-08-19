
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('KS', 'MA', 'MO', 'WI', 'WV')
d1.d_year = 2000
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '1001-5000'
ss_sales_price / ss_list_price BETWEEN 40 * 0.01 AND 60 * 0.01

;


