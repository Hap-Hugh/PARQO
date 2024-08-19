
i_category IN ('Children', 'Home', 'Men')
ca_state in ('KS', 'NJ', 'OK', 'SC', 'TX')
d1.d_year = 1999
hd_income_band_sk BETWEEN 20 AND 26 AND hd_buy_potential = '0-500'
ss_sales_price / ss_list_price BETWEEN 1 * 0.01 AND 21 * 0.01

;


