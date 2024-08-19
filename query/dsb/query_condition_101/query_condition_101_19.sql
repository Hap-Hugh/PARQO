
i_category IN ('Books', 'Children', 'Home')
ca_state in ('AR', 'IA', 'MS', 'NE', 'PA')
d1.d_year = 1999
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01

;


