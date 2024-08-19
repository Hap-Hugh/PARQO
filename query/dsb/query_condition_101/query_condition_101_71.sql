
i_category IN ('Children', 'Home', 'Men')
ca_state in ('AL', 'GA', 'MT', 'OH', 'WI')
d1.d_year = 2000
hd_income_band_sk BETWEEN 9 AND 15 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 79 * 0.01 AND 99 * 0.01

;


