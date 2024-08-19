
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
cd_marital_status = 'M' AND cd_dep_count BETWEEN 1 AND 3


ca_country = 'United States'  and ca_state in ('FL', 'OH', 'PA')
ca_country = 'United States'  and ca_state in ('GA', 'NE', 'WV')
ca_country = 'United States'  and ca_state in ('AL', 'AR', 'VA')
ca_country = 'United States'  and ca_state in ('FL', 'OH', 'PA')
ca_country = 'United States'  and ca_state in ('GA', 'NE', 'WV')
ca_country = 'United States'  and ca_state in ('AL', 'AR', 'VA')
ca_state in ('GA', 'MN', 'MO')
ca_state in ('GA', 'MI', 'MS', 'OR', 'TN')
ca_state in ('GA', 'MI', 'MS', 'OR', 'TN')
ca_state = 'GA'
ca_city = 'Oak Grove'
ca_gmt_offset = -6

d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001 and d_moy = 2
d_year = 2001 and d_moy = 2
d_year = 2001 and d_moy = 2
d_dow = 6
d_moy = 2
d_year between 1998 and 1998 + 1
d_year = 2001 and d_moy BETWEEN 2 AND 2 + 2
d_year = 2001 and d_moy BETWEEN 2 AND 2 + 2
d_date BETWEEN (CAST ('2001-06-06' AS date) - interval '30 day') AND (CAST ('2001-06-06' AS date) + interval '30 day')
d_month_seq between 1183 and 1183 + 23

c_birth_month = 2

cs_wholesale_cost BETWEEN 78 AND 83
cs_wholesale_cost BETWEEN 78 AND 83
cs_wholesale_cost BETWEEN 78 AND 97
cs_list_price between 271 and 300

ss_wholesale_cost BETWEEN 78 AND 83
ss_list_price between 271 and 300
ss_list_price between 271 and 300
ss_sales_price / ss_list_price BETWEEN 47 * 0.01 AND 67 * 0.01


i_category = 'Home'
i_category = 'Home'
i_category = 'Home'
i_category in ('Children', 'Shoes')
i_category IN ('Children', 'Shoes', 'Women')
i_category IN ('Children', 'Shoes', 'Women')
i_category = 'Home' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Children', 'Shoes', 'Women') and i_manager_id IN (5, 43, 47, 58, 62, 75, 85, 93, 96, 97)
i_manager_id between 81 and 100

s_state = 'GA'
s_state in ('GA', 'MN', 'MO')

cr_reason_sk = 46

hd_buy_potential = '1001-5000'
hd_buy_potential like '0-500%'
hd_buy_potential = '0-500'
hd_income_band_sk BETWEEN 5 AND 11 AND hd_buy_potential = '0-500'


ib_lower_bound >= 0 * 10000 AND ib_upper_bound <= 0 * 10000 + 50000


sm_type = 'REGULAR'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 78 AND 83

;


