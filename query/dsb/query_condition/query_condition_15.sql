
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'D' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'D' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_gender = 'F' and cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'S' AND cd_dep_count BETWEEN 0 AND 2


ca_country = 'United States'  and ca_state in ('GA', 'MT', 'SC')
ca_country = 'United States'  and ca_state in ('AL', 'KY', 'NC')
ca_country = 'United States'  and ca_state in ('AL', 'GA', 'VA')
ca_country = 'United States'  and ca_state in ('GA', 'MT', 'SC')
ca_country = 'United States'  and ca_state in ('AL', 'KY', 'NC')
ca_country = 'United States'  and ca_state in ('AL', 'GA', 'VA')
ca_state in ('GA', 'IN', 'MO')
ca_state in ('CO', 'IA', 'KY', 'MN', 'TN')
ca_state in ('CO', 'IA', 'KY', 'MN', 'TN')
ca_state = 'IA'
ca_city = 'Spring Hill'
ca_gmt_offset = -6

d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001
d_year = 2001 and d_moy = 7
d_year = 2001 and d_moy = 7
d_year = 2001 and d_moy = 7
d_dow = 4
d_moy = 7
d_year between 1998 and 1998 + 1
d_year = 2001 and d_moy BETWEEN 7 AND 7 + 2
d_year = 2001 and d_moy BETWEEN 7 AND 7 + 2
d_date BETWEEN (CAST ('2001-04-30' AS date) - interval '30 day') AND (CAST ('2001-04-30' AS date) + interval '30 day')
d_month_seq between 1194 and 1194 + 23

c_birth_month = 7

cs_wholesale_cost BETWEEN 70 AND 75
cs_wholesale_cost BETWEEN 70 AND 75
cs_wholesale_cost BETWEEN 80 AND 99
cs_list_price between 271 and 300

ss_wholesale_cost BETWEEN 70 AND 75
ss_list_price between 271 and 300
ss_list_price between 271 and 300
ss_sales_price / ss_list_price BETWEEN 5 * 0.01 AND 25 * 0.01


i_category = 'Books'
i_category = 'Books'
i_category = 'Books'
i_category in ('Books', 'Children')
i_category IN ('Books', 'Children', 'Shoes')
i_category IN ('Books', 'Children', 'Shoes')
i_category = 'Books' and i_manager_id BETWEEN 20 AND 59
i_category IN ('Books', 'Children', 'Shoes') and i_manager_id IN (19, 27, 28, 39, 56, 60, 63, 74, 95, 99)
i_manager_id between 81 and 100

s_state = 'IA'
s_state in ('GA', 'IN', 'MO')

cr_reason_sk = 31

hd_buy_potential = '501-1000'
hd_buy_potential like 'Unknown%'
hd_buy_potential = 'Unknown'
hd_income_band_sk BETWEEN 2 AND 8 AND hd_buy_potential = 'Unknown'


ib_lower_bound >= 7 * 10000 AND ib_upper_bound <= 7 * 10000 + 50000


sm_type = 'TWO DAY'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 70 AND 75

;


