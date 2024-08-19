
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = '2 yr Degree'
cd_gender = 'F' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_marital_status = 'S' and cd_education_status = 'Unknown'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'S' AND cd_dep_count BETWEEN 7 AND 9


ca_country = 'United States'  and ca_state in ('NC', 'SC', 'SD')
ca_country = 'United States'  and ca_state in ('NC', 'RI', 'TX')
ca_country = 'United States'  and ca_state in ('MI', 'MO', 'WA')
ca_country = 'United States'  and ca_state in ('NC', 'SC', 'SD')
ca_country = 'United States'  and ca_state in ('NC', 'RI', 'TX')
ca_country = 'United States'  and ca_state in ('MI', 'MO', 'WA')
ca_state in ('IA', 'SD', 'UT')
ca_state in ('IA', 'ID', 'MN', 'NH', 'TX')
ca_state in ('IA', 'ID', 'MN', 'NH', 'TX')
ca_state = 'MS'
ca_city = 'Wildwood'
ca_gmt_offset = -7

d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001 and d_moy = 3
d_year = 2001 and d_moy = 3
d_year = 2001 and d_moy = 3
d_dow = 5
d_moy = 3
d_year between 2000 and 2000 + 1
d_year = 2001 and d_moy BETWEEN 3 AND 3 + 2
d_year = 2001 and d_moy BETWEEN 3 AND 3 + 2
d_date BETWEEN (CAST ('2001-02-07' AS date) - interval '30 day') AND (CAST ('2001-02-07' AS date) + interval '30 day')
d_month_seq between 1206 and 1206 + 23

c_birth_month = 3

cs_wholesale_cost BETWEEN 12 AND 17
cs_wholesale_cost BETWEEN 12 AND 17
cs_wholesale_cost BETWEEN 81 AND 100
cs_list_price between 126 and 155

ss_wholesale_cost BETWEEN 12 AND 17
ss_list_price between 126 and 155
ss_list_price between 126 and 155
ss_sales_price / ss_list_price BETWEEN 39 * 0.01 AND 59 * 0.01


i_category = 'Children'
i_category = 'Children'
i_category = 'Children'
i_category in ('Children', 'Electronics')
i_category IN ('Children', 'Electronics', 'Shoes')
i_category IN ('Children', 'Electronics', 'Shoes')
i_category = 'Children' and i_manager_id BETWEEN 54 AND 93
i_category IN ('Children', 'Electronics', 'Shoes') and i_manager_id IN (9, 15, 33, 35, 38, 43, 60, 88, 98, 99)
i_manager_id between 53 and 72

s_state = 'MS'
s_state in ('IA', 'SD', 'UT')

cr_reason_sk = 4

hd_buy_potential = '501-1000'
hd_buy_potential like '501-1000%'
hd_buy_potential = '501-1000'
hd_income_band_sk BETWEEN 6 AND 12 AND hd_buy_potential = '501-1000'


ib_lower_bound >= 4 * 10000 AND ib_upper_bound <= 4 * 10000 + 50000


sm_type = 'EXPRESS'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 12 AND 17

;


