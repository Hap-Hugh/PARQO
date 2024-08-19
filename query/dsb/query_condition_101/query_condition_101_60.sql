
i_category IN ('Children', 'Electronics', 'Women')
ca_state in ('AL', 'GA', 'MS', 'SC', 'SD')
d1.d_year = 1999
hd_income_band_sk BETWEEN 9 AND 15 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 43 * 0.01 AND 63 * 0.01

;


