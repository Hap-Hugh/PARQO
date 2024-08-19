
i_category IN ('Children', 'Home', 'Jewelry')
ca_state in ('GA', 'IL', 'MO', 'TX', 'WI')
d1.d_year = 2000
hd_income_band_sk BETWEEN 6 AND 12 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 0 * 0.01 AND 20 * 0.01

;


