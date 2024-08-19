
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 9 AND 11


ca_country = 'United States'  and ca_state in ('AL', 'NC', 'OH')
ca_country = 'United States'  and ca_state in ('CA', 'MS', 'NC')
ca_country = 'United States'  and ca_state in ('CA', 'IA', 'NM')
ca_country = 'United States'  and ca_state in ('AL', 'NC', 'OH')
ca_country = 'United States'  and ca_state in ('CA', 'MS', 'NC')
ca_country = 'United States'  and ca_state in ('CA', 'IA', 'NM')
ca_state in ('IA', 'NC', 'VT')
ca_state in ('KY', 'PA', 'TX', 'VA', 'WV')
ca_state in ('KY', 'PA', 'TX', 'VA', 'WV')
ca_state = 'TX'
ca_city = 'Bethel'
ca_gmt_offset = -6

d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001 and d_moy = 9
d_year = 2001 and d_moy = 9
d_year = 2001 and d_moy = 9
d_dow = 6
d_moy = 9
d_year between 1998 and 1998 + 1
d_year = 2001 and d_moy BETWEEN 9 AND 9 + 2
d_year = 2001 and d_moy BETWEEN 9 AND 9 + 2
d_date BETWEEN (CAST ('2001-05-05' AS date) - interval '30 day') AND (CAST ('2001-05-05' AS date) + interval '30 day')
d_month_seq between 1198 and 1198 + 23

c_birth_month = 9

cs_wholesale_cost BETWEEN 68 AND 73
cs_wholesale_cost BETWEEN 68 AND 73
cs_wholesale_cost BETWEEN 28 AND 47
cs_list_price between 271 and 300

ss_wholesale_cost BETWEEN 68 AND 73
ss_list_price between 271 and 300
ss_list_price between 271 and 300
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01


i_category = 'Jewelry'
i_category = 'Jewelry'
i_category = 'Jewelry'
i_category in ('Books', 'Jewelry')
i_category IN ('Books', 'Jewelry', 'Shoes')
i_category IN ('Books', 'Jewelry', 'Shoes')
i_category = 'Jewelry' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Books', 'Jewelry', 'Shoes') and i_manager_id IN (6, 13, 14, 23, 40, 59, 65, 70, 78, 94)
i_manager_id between 12 and 31

s_state = 'TX'
s_state in ('IA', 'NC', 'VT')

cr_reason_sk = 43

hd_buy_potential = '>10000'
hd_buy_potential like '501-1000%'
hd_buy_potential = '501-1000'
hd_income_band_sk BETWEEN 2 AND 8 AND hd_buy_potential = '501-1000'


ib_lower_bound >= 2 * 10000 AND ib_upper_bound <= 2 * 10000 + 50000


sm_type = 'REGULAR'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 68 AND 73

;


