
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = '2 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = '2 yr Degree'
cd_gender = 'F' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_marital_status = 'S' and cd_education_status = 'Unknown'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'S' AND cd_dep_count BETWEEN 3 AND 5


ca_country = 'United States'  and ca_state in ('MN', 'MT', 'WI')
ca_country = 'United States'  and ca_state in ('IA', 'ID', 'NE')
ca_country = 'United States'  and ca_state in ('PA', 'TX', 'WA')
ca_country = 'United States'  and ca_state in ('MN', 'MT', 'WI')
ca_country = 'United States'  and ca_state in ('IA', 'ID', 'NE')
ca_country = 'United States'  and ca_state in ('PA', 'TX', 'WA')
ca_state in ('MS', 'TN', 'TX')
ca_state in ('IA', 'IN', 'MO', 'PA', 'TN')
ca_state in ('IA', 'IN', 'MO', 'PA', 'TN')
ca_state = 'NE'
ca_city = 'Oak Ridge'
ca_gmt_offset = -7

d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002 and d_moy = 1
d_year = 2002 and d_moy = 1
d_year = 2002 and d_moy = 1
d_dow = 1
d_moy = 1
d_year between 2000 and 2000 + 1
d_year = 2002 and d_moy BETWEEN 1 AND 1 + 2
d_year = 2002 and d_moy BETWEEN 1 AND 1 + 2
d_date BETWEEN (CAST ('2002-02-03' AS date) - interval '30 day') AND (CAST ('2002-02-03' AS date) + interval '30 day')
d_month_seq between 1204 and 1204 + 23

c_birth_month = 1

cs_wholesale_cost BETWEEN 35 AND 40
cs_wholesale_cost BETWEEN 35 AND 40
cs_wholesale_cost BETWEEN 29 AND 48
cs_list_price between 45 and 74

ss_wholesale_cost BETWEEN 35 AND 40
ss_list_price between 45 and 74
ss_list_price between 45 and 74
ss_sales_price / ss_list_price BETWEEN 24 * 0.01 AND 44 * 0.01


i_category = 'Children'
i_category = 'Children'
i_category = 'Children'
i_category in ('Books', 'Jewelry')
i_category IN ('Books', 'Jewelry', 'Sports')
i_category IN ('Books', 'Jewelry', 'Sports')
i_category = 'Children' and i_manager_id BETWEEN 59 AND 98
i_category IN ('Books', 'Jewelry', 'Sports') and i_manager_id IN (29, 36, 37, 44, 46, 52, 65, 68, 87, 90)
i_manager_id between 81 and 100

s_state = 'NE'
s_state in ('MS', 'TN', 'TX')

cr_reason_sk = 43

hd_buy_potential = '501-1000'
hd_buy_potential like '501-1000%'
hd_buy_potential = '501-1000'
hd_income_band_sk BETWEEN 10 AND 16 AND hd_buy_potential = '501-1000'


ib_lower_bound >= 7 * 10000 AND ib_upper_bound <= 7 * 10000 + 50000


sm_type = 'NEXT DAY'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 35 AND 40

;


