
i_category IN ('Children', 'Home', 'Jewelry')
ca_state in ('GA', 'MO', 'SC', 'TN', 'TX')
d1.d_year = 1999
hd_income_band_sk BETWEEN 7 AND 13 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 3 * 0.01 AND 23 * 0.01

;


