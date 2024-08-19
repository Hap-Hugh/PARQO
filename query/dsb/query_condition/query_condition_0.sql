
cd_marital_status = 'S' and cd_education_status = 'Primary'
cd_marital_status = 'W' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Primary'
cd_marital_status = 'W' and cd_education_status = '2 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_education_status = '4 yr Degree'
cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_marital_status = 'W' and cd_education_status = '4 yr Degree'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'W' AND cd_dep_count BETWEEN 6 AND 8


ca_country = 'United States'  and ca_state in ('GA', 'NM', 'TX')
ca_country = 'United States'  and ca_state in ('AK', 'NC', 'OR')
ca_country = 'United States'  and ca_state in ('IN', 'KY', 'NE')
ca_country = 'United States'  and ca_state in ('GA', 'NM', 'TX')
ca_country = 'United States'  and ca_state in ('AK', 'NC', 'OR')
ca_country = 'United States'  and ca_state in ('IN', 'KY', 'NE')
ca_state in ('AR', 'NY', 'TX')
ca_state in ('AR', 'GA', 'IA', 'MN', 'TX')
ca_state in ('AR', 'GA', 'IA', 'MN', 'TX')
ca_state = 'IN'
ca_city = 'Maple Grove'
ca_gmt_offset = -7

d_year = 1999
d_year = 1999
d_year = 1999
d_year = 1999
d_year = 1999
d_year = 1999
d_year = 1999 and d_moy = 1
d_year = 1999 and d_moy = 1
d_year = 1999 and d_moy = 1
d_dow = 1
d_moy = 1
d_year between 2000 and 2000 + 1
d_year = 1999 and d_moy BETWEEN 1 AND 1 + 2
d_year = 1999 and d_moy BETWEEN 1 AND 1 + 2
d_date BETWEEN (CAST ('1999-03-19' AS date) - interval '30 day') AND (CAST ('1999-03-19' AS date) + interval '30 day')
d_month_seq between 1178 and 1178 + 23

c_birth_month = 1

cs_wholesale_cost BETWEEN 60 AND 65
cs_wholesale_cost BETWEEN 60 AND 65
cs_wholesale_cost BETWEEN 56 AND 75
cs_list_price between 40 and 69

ss_wholesale_cost BETWEEN 60 AND 65
ss_list_price between 40 and 69
ss_list_price between 40 and 69
ss_sales_price / ss_list_price BETWEEN 6 * 0.01 AND 26 * 0.01


i_category = 'Shoes'
i_category = 'Shoes'
i_category = 'Shoes'
i_category in ('Children', 'Home')
i_category IN ('Children', 'Home', 'Shoes')
i_category IN ('Children', 'Home', 'Shoes')
i_category = 'Shoes' and i_manager_id BETWEEN 27 AND 66
i_category IN ('Children', 'Home', 'Shoes') and i_manager_id IN (4, 8, 12, 28, 40, 49, 81, 88, 92, 98)
i_manager_id between 63 and 82

s_state = 'IN'
s_state in ('AR', 'NY', 'TX')

cr_reason_sk = 23

hd_buy_potential = '501-1000'
hd_buy_potential like '0-500%'
hd_buy_potential = '0-500'
hd_income_band_sk BETWEEN 14 AND 20 AND hd_buy_potential = '0-500'


ib_lower_bound >= 6 * 10000 AND ib_upper_bound <= 6 * 10000 + 50000


sm_type = 'TWO DAY'

cc_class = 'small'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 60 AND 65

;


