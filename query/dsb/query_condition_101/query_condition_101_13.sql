
i_category IN ('Children', 'Home', 'Jewelry')
ca_state in ('AR', 'GA', 'MI', 'TN', 'WA')
d1.d_year = 1999
hd_income_band_sk BETWEEN 5 AND 11 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 29 * 0.01 AND 49 * 0.01

;


