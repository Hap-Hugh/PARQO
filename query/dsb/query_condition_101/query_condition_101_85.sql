
i_category IN ('Electronics', 'Home', 'Women')
ca_state in ('CA', 'LA', 'MN', 'OH', 'WY')
d1.d_year = 2000
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 66 * 0.01 AND 86 * 0.01

;


