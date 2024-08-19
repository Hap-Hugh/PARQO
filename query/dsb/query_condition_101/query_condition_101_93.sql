
i_category IN ('Children', 'Jewelry', 'Women')
ca_state in ('GA', 'IL', 'NE', 'NV', 'TN')
d1.d_year = 2000
hd_income_band_sk BETWEEN 13 AND 19 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 8 * 0.01 AND 28 * 0.01

;


