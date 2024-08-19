
i_category IN ('Children', 'Home', 'Jewelry')
ca_state in ('FL', 'MI', 'MO', 'UT', 'WI')
d1.d_year = 2000
hd_income_band_sk BETWEEN 5 AND 11 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 73 * 0.01 AND 93 * 0.01

;


