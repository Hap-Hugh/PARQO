
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('MS', 'OH', 'TX', 'VA', 'WI')
d1.d_year = 1998
hd_income_band_sk BETWEEN 2 AND 8 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 65 * 0.01 AND 85 * 0.01

;


