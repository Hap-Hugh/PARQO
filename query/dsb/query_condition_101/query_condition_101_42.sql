
i_category IN ('Electronics', 'Home', 'Jewelry')
ca_state in ('AR', 'FL', 'IA', 'MA', 'TX')
d1.d_year = 1999
hd_income_band_sk BETWEEN 12 AND 18 AND hd_buy_potential = '501-1000'
ss_sales_price / ss_list_price BETWEEN 12 * 0.01 AND 32 * 0.01

;


