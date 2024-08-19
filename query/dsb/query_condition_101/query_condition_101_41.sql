
i_category IN ('Children', 'Electronics', 'Men')
ca_state in ('CA', 'IL', 'KY', 'MN', 'TN')
d1.d_year = 1999
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 46 * 0.01 AND 66 * 0.01

;


