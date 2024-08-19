
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_gender = 'F' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 7 AND 9


ca_country = 'United States'  and ca_state in ('GA', 'ND', 'OR')
ca_country = 'United States'  and ca_state in ('AR', 'FL', 'GA')
ca_country = 'United States'  and ca_state in ('GA', 'UT', 'VA')
ca_country = 'United States'  and ca_state in ('GA', 'ND', 'OR')
ca_country = 'United States'  and ca_state in ('AR', 'FL', 'GA')
ca_country = 'United States'  and ca_state in ('GA', 'UT', 'VA')
ca_state in ('IN', 'MI', 'OK')
ca_state in ('AK', 'IL', 'KY', 'ND', 'WY')
ca_state in ('AK', 'IL', 'KY', 'ND', 'WY')
ca_state = 'NC'
ca_city = 'Jamestown'
ca_gmt_offset = -6

d_year = 1998
d_year = 1998
d_year = 1998
d_year = 1998
d_year = 1998
d_year = 1998
d_year = 1998 and d_moy = 2
d_year = 1998 and d_moy = 2
d_year = 1998 and d_moy = 2
d_dow = 2
d_moy = 2
d_year between 2000 and 2000 + 1
d_year = 1998 and d_moy BETWEEN 2 AND 2 + 2
d_year = 1998 and d_moy BETWEEN 2 AND 2 + 2
d_date BETWEEN (CAST ('1998-03-29' AS date) - interval '30 day') AND (CAST ('1998-03-29' AS date) + interval '30 day')
d_month_seq between 1177 and 1177 + 23

c_birth_month = 2

cs_wholesale_cost BETWEEN 31 AND 36
cs_wholesale_cost BETWEEN 31 AND 36
cs_wholesale_cost BETWEEN 81 AND 100
cs_list_price between 124 and 153

ss_wholesale_cost BETWEEN 31 AND 36
ss_list_price between 124 and 153
ss_list_price between 124 and 153
ss_sales_price / ss_list_price BETWEEN 53 * 0.01 AND 73 * 0.01


i_category = 'Shoes'
i_category = 'Shoes'
i_category = 'Shoes'
i_category in ('Books', 'Home')
i_category IN ('Books', 'Home', 'Sports')
i_category IN ('Books', 'Home', 'Sports')
i_category = 'Shoes' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Books', 'Home', 'Sports') and i_manager_id IN (18, 25, 43, 46, 49, 62, 87, 89, 93, 95)
i_manager_id between 5 and 24

s_state = 'NC'
s_state in ('IN', 'MI', 'OK')

cr_reason_sk = 61

hd_buy_potential = '1001-5000'
hd_buy_potential like '501-1000%'
hd_buy_potential = '501-1000'
hd_income_band_sk BETWEEN 5 AND 11 AND hd_buy_potential = '501-1000'


ib_lower_bound >= 7 * 10000 AND ib_upper_bound <= 7 * 10000 + 50000


sm_type = 'LIBRARY'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 31 AND 36

;


