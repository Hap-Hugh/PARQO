
i_category IN ('Books', 'Children', 'Women')
ca_state in ('GA', 'IN', 'OH', 'PA', 'TX')
d1.d_year = 2000
hd_income_band_sk BETWEEN 12 AND 18 AND hd_buy_potential = '>10000'
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01

;


