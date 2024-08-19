
i_category IN ('Books', 'Jewelry', 'Women')
ca_state in ('GA', 'IL', 'KS', 'NE', 'TX')
d1.d_year = 1998
hd_income_band_sk BETWEEN 2 AND 8 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 72 * 0.01 AND 92 * 0.01

;


