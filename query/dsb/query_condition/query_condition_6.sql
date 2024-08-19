
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'M' AND cd_dep_count BETWEEN 5 AND 7


ca_country = 'United States'  and ca_state in ('IA', 'MO', 'NC')
ca_country = 'United States'  and ca_state in ('MO', 'TN', 'TX')
ca_country = 'United States'  and ca_state in ('MD', 'NM', 'PA')
ca_country = 'United States'  and ca_state in ('IA', 'MO', 'NC')
ca_country = 'United States'  and ca_state in ('MO', 'TN', 'TX')
ca_country = 'United States'  and ca_state in ('MD', 'NM', 'PA')
ca_state in ('GA', 'OR', 'VA')
ca_state in ('AL', 'GA', 'IN', 'NC', 'OK')
ca_state in ('AL', 'GA', 'IN', 'NC', 'OK')
ca_state = 'TX'
ca_city = 'Riverside'
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
d_dow = 3
d_moy = 2
d_year between 1999 and 1999 + 1
d_year = 2001 and d_moy BETWEEN 2 AND 2 + 2
d_year = 2001 and d_moy BETWEEN 2 AND 2 + 2
d_date BETWEEN (CAST ('2001-03-23' AS date) - interval '30 day') AND (CAST ('2001-03-23' AS date) + interval '30 day')
d_month_seq between 1206 and 1206 + 23

c_birth_month = 2

cs_wholesale_cost BETWEEN 62 AND 67
cs_wholesale_cost BETWEEN 62 AND 67
cs_wholesale_cost BETWEEN 21 AND 40
cs_list_price between 45 and 74

ss_wholesale_cost BETWEEN 62 AND 67
ss_list_price between 45 and 74
ss_list_price between 45 and 74
ss_sales_price / ss_list_price BETWEEN 63 * 0.01 AND 83 * 0.01


i_category = 'Jewelry'
i_category = 'Jewelry'
i_category = 'Jewelry'
i_category in ('Children', 'Home')
i_category IN ('Children', 'Home', 'Shoes')
i_category IN ('Children', 'Home', 'Shoes')
i_category = 'Jewelry' and i_manager_id BETWEEN 45 AND 84
i_category IN ('Children', 'Home', 'Shoes') and i_manager_id IN (5, 12, 37, 38, 46, 66, 68, 79, 84, 90)
i_manager_id between 81 and 100

s_state = 'TX'
s_state in ('GA', 'OR', 'VA')

cr_reason_sk = 60

hd_buy_potential = '1001-5000'
hd_buy_potential like '501-1000%'
hd_buy_potential = '501-1000'
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '501-1000'


ib_lower_bound >= 1 * 10000 AND ib_upper_bound <= 1 * 10000 + 50000


sm_type = 'REGULAR'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 62 AND 67

;


