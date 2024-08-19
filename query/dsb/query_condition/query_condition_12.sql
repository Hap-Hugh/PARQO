
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_marital_status = 'M' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = '4 yr Degree'
cd_gender = 'F' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_marital_status = 'S' and cd_education_status = 'Unknown'
cd_gender = 'F' and cd_marital_status = 'S' and cd_education_status = 'Unknown'
( (cd_marital_status = 'M' and cd_education_status = 'Unknown') or (cd_marital_status = 'W' and cd_education_status = 'Advanced Degree'))
cd_marital_status = 'S' AND cd_dep_count BETWEEN 2 AND 4


ca_country = 'United States'  and ca_state in ('GA', 'MO', 'PA')
ca_country = 'United States'  and ca_state in ('KY', 'NY', 'TX')
ca_country = 'United States'  and ca_state in ('KY', 'MI', 'TN')
ca_country = 'United States'  and ca_state in ('GA', 'MO', 'PA')
ca_country = 'United States'  and ca_state in ('KY', 'NY', 'TX')
ca_country = 'United States'  and ca_state in ('KY', 'MI', 'TN')
ca_state in ('AL', 'TX', 'WI')
ca_state in ('AR', 'IA', 'KS', 'KY', 'WV')
ca_state in ('AR', 'IA', 'KS', 'KY', 'WV')
ca_state = 'WV'
ca_city = 'Walnut Grove'
ca_gmt_offset = -6

d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002
d_year = 2002 and d_moy = 2
d_year = 2002 and d_moy = 2
d_year = 2002 and d_moy = 2
d_dow = 2
d_moy = 2
d_year between 2000 and 2000 + 1
d_year = 2002 and d_moy BETWEEN 2 AND 2 + 2
d_year = 2002 and d_moy BETWEEN 2 AND 2 + 2
d_date BETWEEN (CAST ('2002-06-25' AS date) - interval '30 day') AND (CAST ('2002-06-25' AS date) + interval '30 day')
d_month_seq between 1191 and 1191 + 23

c_birth_month = 2

cs_wholesale_cost BETWEEN 70 AND 75
cs_wholesale_cost BETWEEN 70 AND 75
cs_wholesale_cost BETWEEN 19 AND 38
cs_list_price between 271 and 300

ss_wholesale_cost BETWEEN 70 AND 75
ss_list_price between 271 and 300
ss_list_price between 271 and 300
ss_sales_price / ss_list_price BETWEEN 80 * 0.01 AND 100 * 0.01


i_category = 'Music'
i_category = 'Music'
i_category = 'Music'
i_category in ('Music', 'Shoes')
i_category IN ('Music', 'Shoes', 'Sports')
i_category IN ('Music', 'Shoes', 'Sports')
i_category = 'Music' and i_manager_id BETWEEN 61 AND 100
i_category IN ('Music', 'Shoes', 'Sports') and i_manager_id IN (4, 5, 30, 34, 61, 72, 82, 91, 93, 100)
i_manager_id between 80 and 99

s_state = 'WV'
s_state in ('AL', 'TX', 'WI')

cr_reason_sk = 56

hd_buy_potential = '1001-5000'
hd_buy_potential like 'Unknown%'
hd_buy_potential = 'Unknown'
hd_income_band_sk BETWEEN 10 AND 16 AND hd_buy_potential = 'Unknown'


ib_lower_bound >= 1 * 10000 AND ib_upper_bound <= 1 * 10000 + 50000


sm_type = 'REGULAR'

cc_class = 'large'

w_gmt_offset = -5

ws_wholesale_cost BETWEEN 70 AND 75

;


