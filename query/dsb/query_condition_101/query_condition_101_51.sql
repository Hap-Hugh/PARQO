
i_category IN ('Children', 'Men', 'Women')
ca_state in ('IA', 'NJ', 'OK', 'TX', 'VA')
d1.d_year = 1999
hd_income_band_sk BETWEEN 8 AND 14 AND hd_buy_potential = '0-500'
ss_sales_price / ss_list_price BETWEEN 58 * 0.01 AND 78 * 0.01

;


