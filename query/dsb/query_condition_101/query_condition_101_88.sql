
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('CA', 'FL', 'MT', 'TX', 'WI')
d1.d_year = 1999
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 10 * 0.01 AND 30 * 0.01

;


