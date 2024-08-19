
i_category IN ('Children', 'Home', 'Jewelry')
ca_state in ('AL', 'FL', 'KY', 'NJ', 'WI')
d1.d_year = 1999
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 23 * 0.01 AND 43 * 0.01

;


