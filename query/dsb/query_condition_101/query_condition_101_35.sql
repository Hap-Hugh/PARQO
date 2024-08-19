
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('AR', 'NC', 'TX', 'WA', 'WV')
d1.d_year = 2000
hd_income_band_sk BETWEEN 7 AND 13 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 17 * 0.01 AND 37 * 0.01

;


