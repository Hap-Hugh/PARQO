
i_category IN ('Books', 'Children', 'Men')
ca_state in ('GA', 'MS', 'NC', 'NV', 'PA')
d1.d_year = 1998
hd_income_band_sk BETWEEN 12 AND 18 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 36 * 0.01 AND 56 * 0.01

;


