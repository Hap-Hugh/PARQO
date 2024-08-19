
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'M' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'M' and cd_education_status = 'Advanced Degree'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = 'Advanced Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 6 AND 8


ca_country = 'United States'  and ca_state in ('FL', 'KS', 'TX')
ca_country = 'United States'  and ca_state in ('DE', 'MI', 'WI')
ca_country = 'United States'  and ca_state in ('MT', 'TX', 'VA')
ca_country = 'United States'  and ca_state in ('FL', 'KS', 'TX')
ca_country = 'United States'  and ca_state in ('DE', 'MI', 'WI')
ca_country = 'United States'  and ca_state in ('MT', 'TX', 'VA')
ca_state in ('IA', 'NV', 'WA')
ca_state in ('CO', 'NC', 'NE', 'OK', 'VA')
ca_state in ('CO', 'NC', 'NE', 'OK', 'VA')
ca_state = 'NC'
ca_city = 'Springdale'
ca_gmt_offset = -6

d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002 and d_moy = 4
d_year = 2002 and d_moy = 4
d_year = 2002 and d_moy = 4
d_dow = 3
d_moy = 4
d_year between 1998 and 1998 + 1
d_year = 2002 and d_moy BETWEEN 4 AND 4 + 2
d_year = 2002 and d_moy BETWEEN 4 AND 4 + 2
d_date BETWEEN (CAST ('2002-03-14' AS date) - interval '30 day') AND (CAST ('2002-03-14' AS date) + interval '30 day')
d_month_seq between 1185 and 1185 + 23

c_birth_month = 4

cs_wholesale_cost BETWEEN 31 AND 36
cs_wholesale_cost BETWEEN 31 AND 36
cs_wholesale_cost BETWEEN 74 AND 93
cs_list_price between 167 and 196

ss_wholesale_cost BETWEEN 31 AND 36
ss_list_price between 167 and 196
ss_list_price between 167 and 196
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01


i_category = 'Shoes'
i_category = 'Shoes'
i_category = 'Shoes'
i_category in ('Books', 'Jewelry')
i_category IN ('Books', 'Jewelry', 'Shoes')
i_category IN ('Books', 'Jewelry', 'Shoes')
i_category = 'Shoes' and i_manager_id BETWEEN 28 AND 67
i_category IN ('Books', 'Jewelry', 'Shoes') and i_manager_id IN (43, 47, 61, 62, 63, 71, 84, 96, 98, 100)
i_manager_id between 81 and 100

s_state = 'NC'
s_state in ('IA', 'NV', 'WA')

cr_reason_sk = 29

hd_buy_potential = '501-1000'
hd_buy_potential like '0-500%'
hd_buy_potential = '0-500'
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '0-500'


ib_lower_bound >= 2 * 10000 AND ib_upper_bound <= 2 * 10000 + 50000


sm_type = 'EXPRESS'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 31 AND 36

;


