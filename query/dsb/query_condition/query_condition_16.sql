
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Advanced Degree'
cd_gender = 'F' and cd_education_status = 'Primary'
cd_marital_status = 'M' and cd_education_status = 'Primary'
cd_marital_status = 'M' and cd_education_status = 'Primary'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = 'Primary'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 0 AND 2


ca_country = 'United States'  and ca_state in ('AR', 'MT', 'NY')
ca_country = 'United States'  and ca_state in ('IN', 'KS', 'MO')
ca_country = 'United States'  and ca_state in ('NJ', 'PA', 'WI')
ca_country = 'United States'  and ca_state in ('AR', 'MT', 'NY')
ca_country = 'United States'  and ca_state in ('IN', 'KS', 'MO')
ca_country = 'United States'  and ca_state in ('NJ', 'PA', 'WI')
ca_state in ('FL', 'GA', 'VA')
ca_state in ('IL', 'LA', 'MA', 'NE', 'OR')
ca_state in ('IL', 'LA', 'MA', 'NE', 'OR')
ca_state = 'IN'
ca_city = 'Lakeside'
ca_gmt_offset = -7

d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001 and d_moy = 12
d_year = 2001 and d_moy = 12
d_year = 2001 and d_moy = 12
d_dow = 2
d_moy = 12
d_year between 1999 and 1999 + 1
d_year = 2001 and d_moy BETWEEN 12 AND 12 + 2
d_year = 2001 and d_moy BETWEEN 12 AND 12 + 2
d_date BETWEEN (CAST ('2001-05-19' AS date) - interval '30 day') AND (CAST ('2001-05-19' AS date) + interval '30 day')
d_month_seq between 1202 and 1202 + 23

c_birth_month = 12

cs_wholesale_cost BETWEEN 17 AND 22
cs_wholesale_cost BETWEEN 17 AND 22
cs_wholesale_cost BETWEEN 57 AND 76
cs_list_price between 153 and 182

ss_wholesale_cost BETWEEN 17 AND 22
ss_list_price between 153 and 182
ss_list_price between 153 and 182
ss_sales_price / ss_list_price BETWEEN 52 * 0.01 AND 72 * 0.01


i_category = 'Shoes'
i_category = 'Shoes'
i_category = 'Shoes'
i_category in ('Books', 'Jewelry')
i_category IN ('Books', 'Jewelry', 'Shoes')
i_category IN ('Books', 'Jewelry', 'Shoes')
i_category = 'Shoes' and i_manager_id BETWEEN 49 AND 88
i_category IN ('Books', 'Jewelry', 'Shoes') and i_manager_id IN (11, 29, 41, 46, 47, 51, 65, 66, 92, 96)
i_manager_id between 36 and 55

s_state = 'IN'
s_state in ('FL', 'GA', 'VA')

cr_reason_sk = 27

hd_buy_potential = '1001-5000'
hd_buy_potential like 'Unknown%'
hd_buy_potential = 'Unknown'
hd_income_band_sk BETWEEN 3 AND 9 AND hd_buy_potential = 'Unknown'


ib_lower_bound >= 6 * 10000 AND ib_upper_bound <= 6 * 10000 + 50000


sm_type = 'EXPRESS'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 17 AND 22

;


