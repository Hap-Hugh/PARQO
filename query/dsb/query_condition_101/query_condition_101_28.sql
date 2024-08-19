
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('KS', 'NC', 'NE', 'SD', 'TX')
d1.d_year = 2000
hd_income_band_sk BETWEEN 6 AND 12 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 35 * 0.01 AND 55 * 0.01

;


