
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'S' and cd_education_status = '2 yr Degree'
cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'
cd_marital_status = 'M' and cd_education_status = '2 yr Degree'
cd_marital_status = 'S' and cd_education_status = '2 yr Degree'
cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'
cd_gender = 'F' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_marital_status = 'S' and cd_education_status = 'Unknown'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'S' AND cd_dep_count BETWEEN 4 AND 6


ca_country = 'United States'  and ca_state in ('IA', 'NY', 'TN')
ca_country = 'United States'  and ca_state in ('AK', 'AR', 'TX')
ca_country = 'United States'  and ca_state in ('GA', 'PA', 'VA')
ca_country = 'United States'  and ca_state in ('IA', 'NY', 'TN')
ca_country = 'United States'  and ca_state in ('AK', 'AR', 'TX')
ca_country = 'United States'  and ca_state in ('GA', 'PA', 'VA')
ca_state in ('NV', 'OR', 'WI')
ca_state in ('AL', 'IA', 'KS', 'NY', 'TX')
ca_state in ('AL', 'IA', 'KS', 'NY', 'TX')
ca_state = 'FL'
ca_city = 'Walnut Grove'
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
d_dow = 1
d_moy = 2
d_year between 1999 and 1999 + 1
d_year = 2001 and d_moy BETWEEN 2 AND 2 + 2
d_year = 2001 and d_moy BETWEEN 2 AND 2 + 2
d_date BETWEEN (CAST ('2001-05-02' AS date) - interval '30 day') AND (CAST ('2001-05-02' AS date) + interval '30 day')
d_month_seq between 1187 and 1187 + 23

c_birth_month = 2

cs_wholesale_cost BETWEEN 42 AND 47
cs_wholesale_cost BETWEEN 42 AND 47
cs_wholesale_cost BETWEEN 35 AND 54
cs_list_price between 271 and 300

ss_wholesale_cost BETWEEN 42 AND 47
ss_list_price between 271 and 300
ss_list_price between 271 and 300
ss_sales_price / ss_list_price BETWEEN 60 * 0.01 AND 80 * 0.01


i_category = 'Books'
i_category = 'Books'
i_category = 'Books'
i_category in ('Home', 'Music')
i_category IN ('Home', 'Music', 'Shoes')
i_category IN ('Home', 'Music', 'Shoes')
i_category = 'Books' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Home', 'Music', 'Shoes') and i_manager_id IN (3, 8, 44, 50, 53, 67, 70, 83, 98, 100)
i_manager_id between 32 and 51

s_state = 'FL'
s_state in ('NV', 'OR', 'WI')

cr_reason_sk = 64

hd_buy_potential = '1001-5000'
hd_buy_potential like '501-1000%'
hd_buy_potential = '501-1000'
hd_income_band_sk BETWEEN 3 AND 9 AND hd_buy_potential = '501-1000'


ib_lower_bound >= 1 * 10000 AND ib_upper_bound <= 1 * 10000 + 50000


sm_type = 'LIBRARY'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 42 AND 47

;


