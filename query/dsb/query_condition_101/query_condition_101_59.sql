
i_category IN ('Children', 'Home', 'Women')
ca_state in ('AL', 'AR', 'KY', 'NC', 'WI')
d1.d_year = 1998
hd_income_band_sk BETWEEN 0 AND 6 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 41 * 0.01 AND 61 * 0.01

;


