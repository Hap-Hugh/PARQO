
cd_marital_status = 'W' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'W' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_gender = 'F' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = 'Unknown'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 7 AND 9


ca_country = 'United States'  and ca_state in ('NC', 'OK', 'SD')
ca_country = 'United States'  and ca_state in ('AR', 'SD', 'TN')
ca_country = 'United States'  and ca_state in ('CO', 'FL', 'MI')
ca_country = 'United States'  and ca_state in ('NC', 'OK', 'SD')
ca_country = 'United States'  and ca_state in ('AR', 'SD', 'TN')
ca_country = 'United States'  and ca_state in ('CO', 'FL', 'MI')
ca_state in ('AL', 'DE', 'VA')
ca_state in ('AR', 'CA', 'IA', 'NE', 'TX')
ca_state in ('AR', 'CA', 'IA', 'NE', 'TX')
ca_state = 'WA'
ca_city = 'Shady Grove'
ca_gmt_offset = -7

d_year = 1998
d_year = 1998
d_year = 1998
d_year = 1998
d_year = 1998
d_year = 1998
d_year = 1998 and d_moy = 4
d_year = 1998 and d_moy = 4
d_year = 1998 and d_moy = 4
d_dow = 3
d_moy = 4
d_year between 2000 and 2000 + 1
d_year = 1998 and d_moy BETWEEN 4 AND 4 + 2
d_year = 1998 and d_moy BETWEEN 4 AND 4 + 2
d_date BETWEEN (CAST ('1998-06-06' AS date) - interval '30 day') AND (CAST ('1998-06-06' AS date) + interval '30 day')
d_month_seq between 1190 and 1190 + 23

c_birth_month = 4

cs_wholesale_cost BETWEEN 17 AND 22
cs_wholesale_cost BETWEEN 17 AND 22
cs_wholesale_cost BETWEEN 28 AND 47
cs_list_price between 109 and 138

ss_wholesale_cost BETWEEN 17 AND 22
ss_list_price between 109 and 138
ss_list_price between 109 and 138
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01


i_category = 'Books'
i_category = 'Books'
i_category = 'Books'
i_category in ('Home', 'Music')
i_category IN ('Home', 'Music', 'Shoes')
i_category IN ('Home', 'Music', 'Shoes')
i_category = 'Books' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Home', 'Music', 'Shoes') and i_manager_id IN (20, 34, 37, 41, 46, 47, 62, 65, 71, 93)
i_manager_id between 43 and 62

s_state = 'WA'
s_state in ('AL', 'DE', 'VA')

cr_reason_sk = 44

hd_buy_potential = '1001-5000'
hd_buy_potential like 'Unknown%'
hd_buy_potential = 'Unknown'
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = 'Unknown'


ib_lower_bound >= 3 * 10000 AND ib_upper_bound <= 3 * 10000 + 50000


sm_type = 'REGULAR'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 17 AND 22

;


