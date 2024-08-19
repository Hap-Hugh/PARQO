
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = 'Unknown'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 6 AND 8


ca_country = 'United States'  and ca_state in ('GA', 'IA', 'WA')
ca_country = 'United States'  and ca_state in ('PA', 'UT', 'WY')
ca_country = 'United States'  and ca_state in ('MO', 'TX', 'WA')
ca_country = 'United States'  and ca_state in ('GA', 'IA', 'WA')
ca_country = 'United States'  and ca_state in ('PA', 'UT', 'WY')
ca_country = 'United States'  and ca_state in ('MO', 'TX', 'WA')
ca_state in ('AL', 'MI', 'MO')
ca_state in ('AR', 'NY', 'TN', 'TX', 'VA')
ca_state in ('AR', 'NY', 'TN', 'TX', 'VA')
ca_state = 'SD'
ca_city = 'Buena Vista'
ca_gmt_offset = -6

d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002 and d_moy = 1
d_year = 2002 and d_moy = 1
d_year = 2002 and d_moy = 1
d_dow = 2
d_moy = 1
d_year between 2000 and 2000 + 1
d_year = 2002 and d_moy BETWEEN 1 AND 1 + 2
d_year = 2002 and d_moy BETWEEN 1 AND 1 + 2
d_date BETWEEN (CAST ('2002-03-31' AS date) - interval '30 day') AND (CAST ('2002-03-31' AS date) + interval '30 day')
d_month_seq between 1179 and 1179 + 23

c_birth_month = 1

cs_wholesale_cost BETWEEN 78 AND 83
cs_wholesale_cost BETWEEN 78 AND 83
cs_wholesale_cost BETWEEN 15 AND 34
cs_list_price between 74 and 103

ss_wholesale_cost BETWEEN 78 AND 83
ss_list_price between 74 and 103
ss_list_price between 74 and 103
ss_sales_price / ss_list_price BETWEEN 68 * 0.01 AND 88 * 0.01


i_category = 'Books'
i_category = 'Books'
i_category = 'Books'
i_category in ('Children', 'Music')
i_category IN ('Children', 'Music', 'Shoes')
i_category IN ('Children', 'Music', 'Shoes')
i_category = 'Books' and i_manager_id BETWEEN 21 AND 60
i_category IN ('Children', 'Music', 'Shoes') and i_manager_id IN (2, 10, 25, 47, 52, 64, 66, 74, 77, 81)
i_manager_id between 14 and 33

s_state = 'SD'
s_state in ('AL', 'MI', 'MO')

cr_reason_sk = 6

hd_buy_potential = '1001-5000'
hd_buy_potential like 'Unknown%'
hd_buy_potential = 'Unknown'
hd_income_band_sk BETWEEN 1 AND 7 AND hd_buy_potential = 'Unknown'


ib_lower_bound >= 7 * 10000 AND ib_upper_bound <= 7 * 10000 + 50000


sm_type = 'LIBRARY'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 78 AND 83

;


