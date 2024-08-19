
i_category IN ('Children', 'Home', 'Women')
ca_state in ('GA', 'OR', 'PA', 'TX', 'WI')
d1.d_year = 2000
hd_income_band_sk BETWEEN 6 AND 12 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 13 * 0.01 AND 33 * 0.01

;


