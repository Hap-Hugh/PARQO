
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('IA', 'IN', 'LA', 'ND', 'WI')
d1.d_year = 1998
hd_income_band_sk BETWEEN 13 AND 19 AND hd_buy_potential = '0-500'
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01

;


