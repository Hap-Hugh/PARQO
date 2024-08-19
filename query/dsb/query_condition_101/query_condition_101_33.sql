
i_category IN ('Books', 'Children', 'Jewelry')
ca_state in ('AR', 'CT', 'PA', 'SD', 'WI')
d1.d_year = 2000
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '0-500'
ss_sales_price / ss_list_price BETWEEN 1 * 0.01 AND 21 * 0.01

;


