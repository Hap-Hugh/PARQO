
i_category IN ('Children', 'Jewelry', 'Shoes')
ca_state in ('MO', 'OH', 'SD', 'TX', 'WA')
d1.d_year = 1999
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 29 * 0.01 AND 49 * 0.01

;


