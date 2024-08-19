
i_category IN ('Books', 'Home', 'Women')
ca_state in ('FL', 'IN', 'KY', 'SD', 'TX')
d1.d_year = 2000
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01

;


