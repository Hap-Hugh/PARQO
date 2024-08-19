
cd_marital_status = 'M' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_education_status = 'College'
cd_marital_status = 'M' and cd_education_status = 'College'
cd_marital_status = 'M' and cd_education_status = 'College'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = 'College'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 5 AND 7


ca_country = 'United States'  and ca_state in ('AR', 'MT', 'NY')
ca_country = 'United States'  and ca_state in ('NY', 'TN', 'VA')
ca_country = 'United States'  and ca_state in ('MD', 'TN', 'VA')
ca_country = 'United States'  and ca_state in ('AR', 'MT', 'NY')
ca_country = 'United States'  and ca_state in ('NY', 'TN', 'VA')
ca_country = 'United States'  and ca_state in ('MD', 'TN', 'VA')
ca_state in ('IA', 'OK', 'SC')
ca_state in ('DE', 'GA', 'KS', 'MI', 'TX')
ca_state in ('DE', 'GA', 'KS', 'MI', 'TX')
ca_state = 'OR'
ca_city = 'Glenwood'
ca_gmt_offset = -7

d_year = 2000
d_year = 2000
d_year = 2000
d_year = 2000
d_year = 2000
d_year = 2000
d_year = 2000 and d_moy = 1
d_year = 2000 and d_moy = 1
d_year = 2000 and d_moy = 1
d_dow = 7
d_moy = 1
d_year between 2000 and 2000 + 1
d_year = 2000 and d_moy BETWEEN 1 AND 1 + 2
d_year = 2000 and d_moy BETWEEN 1 AND 1 + 2
d_date BETWEEN (CAST ('2000-04-10' AS date) - interval '30 day') AND (CAST ('2000-04-10' AS date) + interval '30 day')
d_month_seq between 1177 and 1177 + 23

c_birth_month = 1

cs_wholesale_cost BETWEEN 39 AND 44
cs_wholesale_cost BETWEEN 39 AND 44
cs_wholesale_cost BETWEEN 2 AND 21
cs_list_price between 34 and 63

ss_wholesale_cost BETWEEN 39 AND 44
ss_list_price between 34 and 63
ss_list_price between 34 and 63
ss_sales_price / ss_list_price BETWEEN 21 * 0.01 AND 41 * 0.01


i_category = 'Shoes'
i_category = 'Shoes'
i_category = 'Shoes'
i_category in ('Home', 'Jewelry')
i_category IN ('Home', 'Jewelry', 'Music')
i_category IN ('Home', 'Jewelry', 'Music')
i_category = 'Shoes' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Home', 'Jewelry', 'Music') and i_manager_id IN (8, 16, 21, 52, 61, 64, 84, 94, 96, 98)
i_manager_id between 39 and 58

s_state = 'OR'
s_state in ('IA', 'OK', 'SC')

cr_reason_sk = 16

hd_buy_potential = '>10000'
hd_buy_potential like '501-1000%'
hd_buy_potential = '501-1000'
hd_income_band_sk BETWEEN 9 AND 15 AND hd_buy_potential = '501-1000'


ib_lower_bound >= 7 * 10000 AND ib_upper_bound <= 7 * 10000 + 50000


sm_type = 'NEXT DAY'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 39 AND 44

;


