
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('CO', 'IA', 'MS', 'MT', 'NE')
d1.d_year = 1999
hd_income_band_sk BETWEEN 13 AND 19 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 53 * 0.01 AND 73 * 0.01

;


