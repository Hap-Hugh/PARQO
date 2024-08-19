
i_category IN ('Children', 'Electronics', 'Jewelry')
ca_state in ('KS', 'KY', 'NC', 'PA', 'RI')
d1.d_year = 1999
hd_income_band_sk BETWEEN 1 AND 7 AND hd_buy_potential = '5001-10000'
ss_sales_price / ss_list_price BETWEEN 47 * 0.01 AND 67 * 0.01

;


