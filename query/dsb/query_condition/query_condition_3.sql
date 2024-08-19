
cd_marital_status = 'D' and cd_education_status = '4 yr Degree'
cd_marital_status = 'W' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'D' and cd_education_status = '4 yr Degree'
cd_marital_status = 'W' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_gender = 'F' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 1 AND 3


ca_country = 'United States'  and ca_state in ('NC', 'NM', 'WA')
ca_country = 'United States'  and ca_state in ('IA', 'MO', 'NC')
ca_country = 'United States'  and ca_state in ('IN', 'ND', 'VT')
ca_country = 'United States'  and ca_state in ('NC', 'NM', 'WA')
ca_country = 'United States'  and ca_state in ('IA', 'MO', 'NC')
ca_country = 'United States'  and ca_state in ('IN', 'ND', 'VT')
ca_state in ('CA', 'IA', 'TN')
ca_state in ('AR', 'IN', 'MO', 'NE', 'TN')
ca_state in ('AR', 'IN', 'MO', 'NE', 'TN')
ca_state = 'GA'
ca_city = 'Clifton'
ca_gmt_offset = -7

d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002 and d_moy = 7
d_year = 2002 and d_moy = 7
d_year = 2002 and d_moy = 7
d_dow = 2
d_moy = 7
d_year between 2000 and 2000 + 1
d_year = 2002 and d_moy BETWEEN 7 AND 7 + 2
d_year = 2002 and d_moy BETWEEN 7 AND 7 + 2
d_date BETWEEN (CAST ('2002-06-28' AS date) - interval '30 day') AND (CAST ('2002-06-28' AS date) + interval '30 day')
d_month_seq between 1179 and 1179 + 23

c_birth_month = 7

cs_wholesale_cost BETWEEN 46 AND 51
cs_wholesale_cost BETWEEN 46 AND 51
cs_wholesale_cost BETWEEN 14 AND 33
cs_list_price between 168 and 197

ss_wholesale_cost BETWEEN 46 AND 51
ss_list_price between 168 and 197
ss_list_price between 168 and 197
ss_sales_price / ss_list_price BETWEEN 77 * 0.01 AND 97 * 0.01


i_category = 'Jewelry'
i_category = 'Jewelry'
i_category = 'Jewelry'
i_category in ('Books', 'Home')
i_category IN ('Books', 'Home', 'Shoes')
i_category IN ('Books', 'Home', 'Shoes')
i_category = 'Jewelry' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Books', 'Home', 'Shoes') and i_manager_id IN (13, 17, 31, 36, 48, 55, 72, 76, 78, 84)
i_manager_id between 81 and 100

s_state = 'GA'
s_state in ('CA', 'IA', 'TN')

cr_reason_sk = 10

hd_buy_potential = '1001-5000'
hd_buy_potential like 'Unknown%'
hd_buy_potential = 'Unknown'
hd_income_band_sk BETWEEN 11 AND 17 AND hd_buy_potential = 'Unknown'


ib_lower_bound >= 0 * 10000 AND ib_upper_bound <= 0 * 10000 + 50000


sm_type = 'TWO DAY'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 46 AND 51

;


