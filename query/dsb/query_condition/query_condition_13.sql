
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'W' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'W' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'S' AND cd_dep_count BETWEEN 6 AND 8


ca_country = 'United States'  and ca_state in ('IL', 'MO', 'VA')
ca_country = 'United States'  and ca_state in ('AK', 'OH', 'TX')
ca_country = 'United States'  and ca_state in ('AR', 'CA', 'ND')
ca_country = 'United States'  and ca_state in ('IL', 'MO', 'VA')
ca_country = 'United States'  and ca_state in ('AK', 'OH', 'TX')
ca_country = 'United States'  and ca_state in ('AR', 'CA', 'ND')
ca_state in ('GA', 'KY', 'MS')
ca_state in ('CA', 'ID', 'KS', 'MA', 'OK')
ca_state in ('CA', 'ID', 'KS', 'MA', 'OK')
ca_state = 'TX'
ca_city = 'Wildwood'
ca_gmt_offset = -7

d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001 and d_moy = 1
d_year = 2001 and d_moy = 1
d_year = 2001 and d_moy = 1
d_dow = 4
d_moy = 1
d_year between 1998 and 1998 + 1
d_year = 2001 and d_moy BETWEEN 1 AND 1 + 2
d_year = 2001 and d_moy BETWEEN 1 AND 1 + 2
d_date BETWEEN (CAST ('2001-03-05' AS date) - interval '30 day') AND (CAST ('2001-03-05' AS date) + interval '30 day')
d_month_seq between 1208 and 1208 + 23

c_birth_month = 1

cs_wholesale_cost BETWEEN 56 AND 61
cs_wholesale_cost BETWEEN 56 AND 61
cs_wholesale_cost BETWEEN 6 AND 25
cs_list_price between 109 and 138

ss_wholesale_cost BETWEEN 56 AND 61
ss_list_price between 109 and 138
ss_list_price between 109 and 138
ss_sales_price / ss_list_price BETWEEN 47 * 0.01 AND 67 * 0.01


i_category = 'Jewelry'
i_category = 'Jewelry'
i_category = 'Jewelry'
i_category in ('Books', 'Music')
i_category IN ('Books', 'Music', 'Shoes')
i_category IN ('Books', 'Music', 'Shoes')
i_category = 'Jewelry' and i_manager_id BETWEEN 49 AND 88
i_category IN ('Books', 'Music', 'Shoes') and i_manager_id IN (7, 11, 16, 29, 45, 50, 55, 70, 89, 99)
i_manager_id between 81 and 100

s_state = 'TX'
s_state in ('GA', 'KY', 'MS')

cr_reason_sk = 45

hd_buy_potential = '>10000'
hd_buy_potential like '0-500%'
hd_buy_potential = '0-500'
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '0-500'


ib_lower_bound >= 3 * 10000 AND ib_upper_bound <= 3 * 10000 + 50000


sm_type = 'EXPRESS'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 56 AND 61

;


