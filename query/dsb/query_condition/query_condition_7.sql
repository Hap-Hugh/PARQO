
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_marital_status = 'S' and cd_education_status = 'Unknown'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'S' AND cd_dep_count BETWEEN 9 AND 11


ca_country = 'United States'  and ca_state in ('IL', 'KS', 'TX')
ca_country = 'United States'  and ca_state in ('MO', 'MS', 'SC')
ca_country = 'United States'  and ca_state in ('AL', 'IL', 'TX')
ca_country = 'United States'  and ca_state in ('IL', 'KS', 'TX')
ca_country = 'United States'  and ca_state in ('MO', 'MS', 'SC')
ca_country = 'United States'  and ca_state in ('AL', 'IL', 'TX')
ca_state in ('NC', 'TN', 'TX')
ca_state in ('AL', 'FL', 'GA', 'WI', 'WV')
ca_state in ('AL', 'FL', 'GA', 'WI', 'WV')
ca_state = 'MT'
ca_city = 'Woodlawn'
ca_gmt_offset = -6

d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002 and d_moy = 6
d_year = 2002 and d_moy = 6
d_year = 2002 and d_moy = 6
d_dow = 6
d_moy = 6
d_year between 1999 and 1999 + 1
d_year = 2002 and d_moy BETWEEN 6 AND 6 + 2
d_year = 2002 and d_moy BETWEEN 6 AND 6 + 2
d_date BETWEEN (CAST ('2002-04-30' AS date) - interval '30 day') AND (CAST ('2002-04-30' AS date) + interval '30 day')
d_month_seq between 1191 and 1191 + 23

c_birth_month = 6

cs_wholesale_cost BETWEEN 67 AND 72
cs_wholesale_cost BETWEEN 67 AND 72
cs_wholesale_cost BETWEEN 64 AND 83
cs_list_price between 149 and 178

ss_wholesale_cost BETWEEN 67 AND 72
ss_list_price between 149 and 178
ss_list_price between 149 and 178
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01


i_category = 'Shoes'
i_category = 'Shoes'
i_category = 'Shoes'
i_category in ('Books', 'Jewelry')
i_category IN ('Books', 'Jewelry', 'Sports')
i_category IN ('Books', 'Jewelry', 'Sports')
i_category = 'Shoes' and i_manager_id BETWEEN 21 AND 60
i_category IN ('Books', 'Jewelry', 'Sports') and i_manager_id IN (13, 18, 23, 37, 41, 58, 61, 69, 72, 97)
i_manager_id between 62 and 81

s_state = 'MT'
s_state in ('NC', 'TN', 'TX')

cr_reason_sk = 61

hd_buy_potential = '501-1000'
hd_buy_potential like 'Unknown%'
hd_buy_potential = 'Unknown'
hd_income_band_sk BETWEEN 9 AND 15 AND hd_buy_potential = 'Unknown'


ib_lower_bound >= 2 * 10000 AND ib_upper_bound <= 2 * 10000 + 50000


sm_type = 'LIBRARY'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 67 AND 72

;


