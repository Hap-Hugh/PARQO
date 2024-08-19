
i_category IN ('Children', 'Home', 'Women')
ca_state in ('AL', 'MT', 'OR', 'UT', 'WI')
d1.d_year = 1998
hd_income_band_sk BETWEEN 3 AND 9 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 53 * 0.01 AND 73 * 0.01

;


