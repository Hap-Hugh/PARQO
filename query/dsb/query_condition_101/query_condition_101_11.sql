
i_category IN ('Children', 'Jewelry', 'Men')
ca_state in ('FL', 'GA', 'NC', 'OH', 'OK')
d1.d_year = 1998
hd_income_band_sk BETWEEN 0 AND 6 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 42 * 0.01 AND 62 * 0.01

;


