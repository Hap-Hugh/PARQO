
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('KS', 'MI', 'NE', 'OK', 'WV')
d1.d_year = 1998
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 64 * 0.01 AND 84 * 0.01

;


