
i_category IN ('Electronics', 'Home', 'Jewelry')
ca_state in ('IN', 'KY', 'MI', 'SD', 'TX')
d1.d_year = 1998
hd_income_band_sk BETWEEN 6 AND 12 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01

;


