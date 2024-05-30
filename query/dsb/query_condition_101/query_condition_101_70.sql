
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('GA', 'HI', 'IL', 'IN', 'TX')
d1.d_year = 1998
hd_income_band_sk BETWEEN 13 AND 19 AND hd_buy_potential = '1001-5000'
ss_sales_price / ss_list_price BETWEEN 24 * 0.01 AND 44 * 0.01

;

