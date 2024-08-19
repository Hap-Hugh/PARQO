
i_category IN ('Home', 'Men', 'Music')
ca_state in ('AL', 'KS', 'MS', 'ND', 'WV')
d1.d_year = 1998
hd_income_band_sk BETWEEN 5 AND 11 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 19 * 0.01 AND 39 * 0.01

;


