
i_category IN ('Books', 'Children', 'Men')
ca_state in ('CA', 'ID', 'MI', 'ND', 'TX')
d1.d_year = 1999
hd_income_band_sk BETWEEN 5 AND 11 AND hd_buy_potential = '0-500'
ss_sales_price / ss_list_price BETWEEN 26 * 0.01 AND 46 * 0.01

;


