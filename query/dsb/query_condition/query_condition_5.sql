
cd_marital_status = 'S' and cd_education_status = '2 yr Degree'
cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Primary'
cd_marital_status = 'S' and cd_education_status = '2 yr Degree'
cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Primary'
cd_gender = 'F' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 1 AND 3


ca_country = 'United States'  and ca_state in ('KY', 'MS', 'SD')
ca_country = 'United States'  and ca_state in ('ID', 'MO', 'SD')
ca_country = 'United States'  and ca_state in ('CA', 'TX', 'WA')
ca_country = 'United States'  and ca_state in ('KY', 'MS', 'SD')
ca_country = 'United States'  and ca_state in ('ID', 'MO', 'SD')
ca_country = 'United States'  and ca_state in ('CA', 'TX', 'WA')
ca_state in ('MI', 'MS', 'VA')
ca_state in ('NM', 'NY', 'OH', 'TX', 'WA')
ca_state in ('NM', 'NY', 'OH', 'TX', 'WA')
ca_state = 'MO'
ca_city = 'Liberty'
ca_gmt_offset = -7

d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002 and d_moy = 12
d_year = 2002 and d_moy = 12
d_year = 2002 and d_moy = 12
d_dow = 1
d_moy = 12
d_year between 2000 and 2000 + 1
d_year = 2002 and d_moy BETWEEN 12 AND 12 + 2
d_year = 2002 and d_moy BETWEEN 12 AND 12 + 2
d_date BETWEEN (CAST ('2002-04-21' AS date) - interval '30 day') AND (CAST ('2002-04-21' AS date) + interval '30 day')
d_month_seq between 1184 and 1184 + 23

c_birth_month = 12

cs_wholesale_cost BETWEEN 61 AND 66
cs_wholesale_cost BETWEEN 61 AND 66
cs_wholesale_cost BETWEEN 81 AND 100
cs_list_price between 271 and 300

ss_wholesale_cost BETWEEN 61 AND 66
ss_list_price between 271 and 300
ss_list_price between 271 and 300
ss_sales_price / ss_list_price BETWEEN 58 * 0.01 AND 78 * 0.01


i_category = 'Books'
i_category = 'Books'
i_category = 'Books'
i_category in ('Home', 'Jewelry')
i_category IN ('Home', 'Jewelry', 'Music')
i_category IN ('Home', 'Jewelry', 'Music')
i_category = 'Books' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Home', 'Jewelry', 'Music') and i_manager_id IN (3, 9, 28, 42, 59, 60, 62, 73, 78, 89)
i_manager_id between 81 and 100

s_state = 'MO'
s_state in ('MI', 'MS', 'VA')

cr_reason_sk = 1

hd_buy_potential = '501-1000'
hd_buy_potential like '0-500%'
hd_buy_potential = '0-500'
hd_income_band_sk BETWEEN 11 AND 17 AND hd_buy_potential = '0-500'


ib_lower_bound >= 0 * 10000 AND ib_upper_bound <= 0 * 10000 + 50000


sm_type = 'LIBRARY'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 61 AND 66

;


