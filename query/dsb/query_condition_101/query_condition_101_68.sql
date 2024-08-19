
i_category IN ('Children', 'Home', 'Jewelry')
ca_state in ('GA', 'IL', 'LA', 'NM', 'WI')
d1.d_year = 2000
hd_income_band_sk BETWEEN 4 AND 10 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 24 * 0.01 AND 44 * 0.01

;


