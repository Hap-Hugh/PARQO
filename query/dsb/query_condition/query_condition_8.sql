
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_marital_status = 'S' and cd_education_status = 'Unknown'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'S' AND cd_dep_count BETWEEN 0 AND 2


ca_country = 'United States'  and ca_state in ('AL', 'CA', 'TN')
ca_country = 'United States'  and ca_state in ('GA', 'IN', 'PA')
ca_country = 'United States'  and ca_state in ('LA', 'NY', 'PA')
ca_country = 'United States'  and ca_state in ('AL', 'CA', 'TN')
ca_country = 'United States'  and ca_state in ('GA', 'IN', 'PA')
ca_country = 'United States'  and ca_state in ('LA', 'NY', 'PA')
ca_state in ('IA', 'KY', 'VA')
ca_state in ('HI', 'NE', 'NM', 'OH', 'TX')
ca_state in ('HI', 'NE', 'NM', 'OH', 'TX')
ca_state = 'MS'
ca_city = 'Pleasant Hill'
ca_gmt_offset = -6

d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002 and d_moy = 1
d_year = 2002 and d_moy = 1
d_year = 2002 and d_moy = 1
d_dow = 5
d_moy = 1
d_year between 2000 and 2000 + 1
d_year = 2002 and d_moy BETWEEN 1 AND 1 + 2
d_year = 2002 and d_moy BETWEEN 1 AND 1 + 2
d_date BETWEEN (CAST ('2002-02-08' AS date) - interval '30 day') AND (CAST ('2002-02-08' AS date) + interval '30 day')
d_month_seq between 1185 and 1185 + 23

c_birth_month = 1

cs_wholesale_cost BETWEEN 57 AND 62
cs_wholesale_cost BETWEEN 57 AND 62
cs_wholesale_cost BETWEEN 73 AND 92
cs_list_price between 205 and 234

ss_wholesale_cost BETWEEN 57 AND 62
ss_list_price between 205 and 234
ss_list_price between 205 and 234
ss_sales_price / ss_list_price BETWEEN 59 * 0.01 AND 79 * 0.01


i_category = 'Books'
i_category = 'Books'
i_category = 'Books'
i_category in ('Books', 'Home')
i_category IN ('Books', 'Home', 'Shoes')
i_category IN ('Books', 'Home', 'Shoes')
i_category = 'Books' and i_manager_id BETWEEN 8 AND 47
i_category IN ('Books', 'Home', 'Shoes') and i_manager_id IN (3, 10, 11, 19, 22, 30, 37, 42, 43, 90)
i_manager_id between 9 and 28

s_state = 'MS'
s_state in ('IA', 'KY', 'VA')

cr_reason_sk = 51

hd_buy_potential = '1001-5000'
hd_buy_potential like 'Unknown%'
hd_buy_potential = 'Unknown'
hd_income_band_sk BETWEEN 13 AND 19 AND hd_buy_potential = 'Unknown'


ib_lower_bound >= 6 * 10000 AND ib_upper_bound <= 6 * 10000 + 50000


sm_type = 'LIBRARY'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 57 AND 62

;


