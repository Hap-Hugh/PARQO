
i_category IN ('Children', 'Jewelry', 'Men')
ca_state in ('IL', 'ND', 'VA', 'WI', 'WV')
d1.d_year = 1999
hd_income_band_sk BETWEEN 8 AND 14 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 4 * 0.01 AND 24 * 0.01

;


