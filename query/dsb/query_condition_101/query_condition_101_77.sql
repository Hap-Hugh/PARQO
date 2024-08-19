
i_category IN ('Children', 'Home', 'Women')
ca_state in ('KS', 'LA', 'MO', 'NY', 'TX')
d1.d_year = 2000
hd_income_band_sk BETWEEN 10 AND 16 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 19 * 0.01 AND 39 * 0.01

;


