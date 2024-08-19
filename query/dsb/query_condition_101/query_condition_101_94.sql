
i_category IN ('Children', 'Home', 'Women')
ca_state in ('KS', 'MI', 'ND', 'SD', 'TN')
d1.d_year = 1999
hd_income_band_sk BETWEEN 6 AND 12 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 17 * 0.01 AND 37 * 0.01

;


