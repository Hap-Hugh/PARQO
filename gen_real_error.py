
from postgres import *
from psql_explain_decoder import *
from sklearn.neighbors import KernelDensity
import random
import pandas as pd
from prep_error_list import plot_error, cal_rel_error
from querylets import *
import copy

file_name_to_save_real_error = ''
kk = '1=1'
cache_right = {}
db = 'imdb'

def gen_real_error():
    global file_name_to_save_real_error            

    if db == 'imdb':
        local_selections = pd.read_csv('lsc/job/LSC-JOB.csv')
        # ['Table', 'Condition', 'Frequency']
        condition_dict = {'k': [], 't': [], 'cn': [], 'n': [], 'mc': [], 'mi': [], 'it_pi': [], 'it_mi': [], 'it_miidx': [], 'an': [], 'lt': [], 'pi': [], 'ci':[], 'mi_idx':[], 'kt':[], 'ct':[], 'rt':[], 'cct':[], 'chn':[]}
    
    if db == 'dsb':
        local_selections = pd.read_csv('lsc/dsb/DSB-072.csv')
        table_names_from_csv = local_selections['Table'].unique()

        condition_dict = {key: [] for key in table_names_from_csv}
        # condition_dict = {
        #     "call_center": [], "catalog_returns": [],
        #     "catalog_sales": [], "customer": [], 
        #     "customer_address": [], "customer_demographics": [],
        #     "date_dim": [],
        #     "household_demographics": [],
        #     "income_band": [], "item": [],
        #     "ship_mode": [], "store": [], "store_sales": [],
        #     "warehouse": [], "web_sales": [], 
        #     }
        
    if db == 'stats': 
        local_selections = pd.read_csv('lsc/stats/LSC-Stats.csv')
        condition_dict = {'b': [], 'c': [], 'u': [], 'ph': [], 'p': [], 'pl': [], 'v': []}

    local_selections_grouped = local_selections.groupby('Table')
    frequency_dict = copy.deepcopy(condition_dict)
    frequency_dict['x'] = [2]
    

    for table in condition_dict.keys():
        for _, row in local_selections_grouped.get_group(table).iterrows():
            if row['Condition'] == '1=1':
                continue
            condition_dict[table].append(row['Condition'])
            frequency_dict[table].append(int(row['Frequency']))
    condition_dict['x'] = ['1=1']
    

    if db == 'imdb': 
        frequency_dict['mk'] =[1]
        condition_dict['mk'] = ['1=1']
        frequency_dict['akat'] =[1]
        condition_dict['akat'] = ['1=1']
        frequency_dict['cc'] =[1]
        condition_dict['cc'] = ['1=1']
        
        data_list = []
        left = 'x'
        left_single = 'ci_full'
        right = "x"
        right_single = 'mk_k_r'
        template_name = f'template_mk_ci__k'

        

        for id_1, left_condition in enumerate(condition_dict[left]):
            for id_2, right_condition in enumerate(condition_dict[right]):
                right_condition = "k.keyword ='character-name-in-title'"
                template = querylet(db, left_condition, right_condition, template_name)
                left_template = querylet(db, right_condition, left_condition, 'template_'+left_single)
                right_template = querylet(db, left_condition, right_condition, 'template_'+right_single)
                # template_full = querylet(db, left_condition, right_condition, 'template_'+template_name + '_full')
                print(template)
                file_name_to_save_real_error = template_name.split('template_')[1]

                # data = cal_local_selectivity(template, template_full)
                # input() # WARNING
                data = cal_join_selectivity(template, left_template, right_template, id_2)
                
                if data:
                    print(data, cal_rel_error(data[0], data[1]), math.log(data[1] / data[0]))
                    data_list.extend([data]*frequency_dict[right][id_2]*frequency_dict[left][id_1])
        output = [str(data[0]) +" "+ str(data[1]) for data in data_list]
        # print(output)
        input()
        with open('./data/abs-error-'+db+'/' + file_name_to_save_real_error + '.txt', 'w') as fp:
            fp.write('\n'.join(output))
        plot_pdf()
        exit()

        for right in condition_dict.keys():
            for left in condition_dict.keys():
                for l_r_b in ['l', 'r', 'both']:
                    data_list = []
                    right = right
                    template_name = f'{left}_{right}_{l_r_b}'
                    
                    # fix 'it'
                    # if left.split('_')[0] == 'it' and left.split('_')[1] == right:
                    #     template_name = f'{left}_{l_r_b}'
                    # elif right.split('_')[0] == 'it' and right.split('_')[1] == left:
                    #     template_name = f'{right.split('_')[1]}_{right.split('_')[0]}_{l_r_b}'
                    # else:
                    #     continue

                    # if template_name.split('_')[0] == 'it' or template_name.split('_')[1] == 'it':
                    #     print(template_name)
                    #     input()
                    # else:
                    #     continue

                    # don't care those redundent template; only care simplest ones now 
                    if not check_tempalte(db, 'template_'+template_name):
                        continue
                    if os.path.exists(f'./data/abs-error-imdb/{template_name}.txt'):
                        print("yes")
                        continue
                    else:
                        print("No", template_name)
                        input()
                        # continue
                    for id_1, left_condition in enumerate(condition_dict[left]):
                        for id_2, right_condition in enumerate(condition_dict[right]):

                            if l_r_b == 'l':
                                template = querylet(db, right_condition, left_condition, 'template_'+template_name)
                            else:
                                template = querylet(db, left_condition, right_condition, 'template_'+template_name)
                            
                            if l_r_b == 'l':
                                right_single = right+'_full'
                                freq_right = 'x'
                            else:
                                right_single = right
                                freq_right = right
                            if l_r_b == 'r':
                                left_single = left + '_full'
                                freq_left = 'x'
                            else:
                                left_single = left
                                freq_left = left
                            left_template = querylet(db, right_condition, left_condition, 'template_'+left_single)
                            right_template = querylet(db, left_condition, right_condition, 'template_'+right_single)
                            # template_full = querylet(db, left_condition, right_condition, 'template_'+template_name + '_full')
                            print(template)
                            # input()
                            print(left_template)
                            print(right_template)
                            
                            
                            file_name_to_save_real_error = template_name
                            # data = cal_local_selectivity(template, template_full)
                            # input() # WARNING
                            data = cal_join_selectivity(template, left_template, right_template, id_2)
                            
                            if data:
                                print(data, cal_rel_error(data[0], data[1]), math.log(data[1] / data[0]))
                                data_list.extend([data]*frequency_dict[freq_right][id_2]*frequency_dict[freq_left][id_1])
                            if l_r_b == 'l':
                                break # since we don't need to go through right conditions
                        if l_r_b == 'r':
                            break # since we don't need to go through left conditions
                    output = [str(data[0]) +" "+ str(data[1]) for data in data_list]
                    # print(output)
                    input()
                    with open('./data/abs-error-'+db+'/' + file_name_to_save_real_error + '.txt', 'w') as fp:
                        fp.write('\n'.join(output))
                    plot_pdf()

    if db == 'stats':

        data_list = []
        left = 'x'
        left_single = 'b_full'
        right = 'c'
        right_single = 'c_ph_l'
        template_name = f'template_ph_b__c'

        

        for id_1, left_condition in enumerate(condition_dict[left]):
            for id_2, right_condition in enumerate(condition_dict[right]):
                template = stats_complex_querylet(cc=right_condition, template=template_name)
                left_template = stats_single_querylet(left_condition, left_single)
                right_template = stats_join_querylet(left_alias='c', right_alias='ph', l_r_b='l', 
                                                     cc=right_condition, kk=left_condition)

                print(template)
                file_name_to_save_real_error = 'ph_b__c'

                # data = cal_local_selectivity(template, template_full)
                # input() # WARNING
                data = cal_join_selectivity(template, left_template, right_template, id_2)
                
                if data:
                    print(data, cal_rel_error(data[0], data[1]), math.log(data[1] / data[0]))
                    data_list.extend([data]*frequency_dict[right][id_2]*frequency_dict[left][id_1])
        output = [str(data[0]) +" "+ str(data[1]) for data in data_list]
        # print(output)
        input()
        with open('./data/abs-error-'+db+'/' + file_name_to_save_real_error + '.txt', 'w') as fp:
            fp.write('\n'.join(output))
        plot_pdf()
        exit()
    
        # for l_id, left in enumerate(['p', 'c', 'ph', 'pl', 'v']):

        #     for r_id, right in enumerate(['p', 'c', 'ph', 'pl', 'v']):
        # for l_id, left in enumerate(['u', 'c', 'b', 'v']):

        #     for r_id, right in enumerate(['u', 'c', 'b', 'v']):
        for l_id, left in enumerate(['ph']):

            for r_id, right in enumerate(['b']):
                # if r_id <= l_id: continue
            
                for l_r_b in ['both']:

                    data_list = []

                    # right = 'income_band'
                    template_name = f'{left}_{right}_{l_r_b}'
                    template_id = '_2'

                    for id_1, left_condition in enumerate(random.sample(condition_dict[left], 10)):
                        for id_2, right_condition in enumerate(random.sample(condition_dict[right], 10)):

                            file_name_to_save_real_error = template_name + template_id

                            
                            template = stats_join_querylet(left, right, l_r_b, left_condition, right_condition)
                            if l_r_b == 'l':
                                right_single = right+'_full'
                                freq_right = 'x'
                            else:
                                right_single = right
                                freq_right = right
                            if l_r_b == 'r':
                                left_single = left + '_full'
                                freq_left = 'x'
                            else:
                                left_single = left
                                freq_left = left
                            left_template = stats_single_querylet(left_condition, left_single)
                            right_template = stats_single_querylet(right_condition, right_single)
                            print(template)
                            print(left_template)
                            print(right_template)
                            
                            # data = cal_local_selectivity(template, template_full)
                            # input() # WARNING
                            data = cal_join_selectivity(template, left_template, right_template, id_2)
                            
                            if data:
                                print(data, cal_rel_error(data[0], data[1]), math.log(data[1] / data[0]))
                                data_list.extend([data]*frequency_dict[freq_right][id_2]*frequency_dict[freq_left][id_1])
                                                        
                            # input()
                            if l_r_b == 'l':
                                break # since we don't need to go through right conditions
                        if l_r_b == 'r':
                            break # since we don't need to go through left conditions

                    output = [str(data[0]) +" "+ str(data[1]) for data in data_list]
                    # print(output)
                    # input()
                    with open('./data/abs-error-'+db+'/' + file_name_to_save_real_error + '.txt', 'w') as fp:
                        fp.write('\n'.join(output))
                    plot_pdf()
        
    if db == 'dsb':
        data_list = []
        
        left = 'x'
        left_single = 'warehouse_full'
        
        right = 'catalog_sales'
        right_single = 'inventory_catalog_sales_r'
        
        template_name = f'inventory_warehouse__catalog_sales'
        query_let_type_is_join = True
        file_name_to_save_real_error = 'inventory_warehouse__catalog_sales_072'
        for id_1, left_condition in enumerate(condition_dict[left]):
            for id_2, right_condition in enumerate(condition_dict[right]):
                
                # left_condition = left_condition.replace("s2.", "")
                right_condition = right_condition.replace("d1.", "")

                if query_let_type_is_join:
                    template = querylet(db, left_condition, right_condition, 'template_'+ template_name)
                    left_template = querylet(db, right_condition, left_condition.replace('d1.', ''), 'template_'+left_single)
                    right_template = querylet(db, left_condition, right_condition.replace('d2.', ''), 'template_'+right_single)
                
                    print(template)
                    
                    data = cal_join_selectivity(template, left_template, right_template, id_2)
                else:
                    template = querylet(db, left_condition, right_condition, 'template_'+ template_name)
                    template_full = querylet(db, left_condition, right_condition, 'template_'+ template_name + '_full')
                    print(template_full)
                    print(template)
                    
                    data = cal_local_selectivity(template, template_full)
                
                if data:
                    print(data, cal_rel_error(data[0], data[1]), math.log(data[1] / data[0]))
                    data_list.extend([data]*frequency_dict[right][id_2]*frequency_dict[left][id_1])
        output = [str(data[0]) +" "+ str(data[1]) for data in data_list]
        # print(output)
        input()
        with open('./data/abs-error-'+db+'/' + file_name_to_save_real_error + '.txt', 'w') as fp:
            fp.write('\n'.join(output))
        plot_pdf()
        exit()



def cal_join_selectivity(join_template, left_template, right_template, id):
    global cache_right
    est_join_count, act_join_count = get_est_act_count(join_template)
    est_left_count, act_left_count = get_est_act_count(left_template)
    if id not in cache_right.keys():
        est_right_count, act_right_count = get_est_act_count(right_template)
        cache_right[id] = [est_right_count, act_right_count]
    else:
        est_right_count, act_right_count = cache_right[id]
        print("=== Use cached")
    print(f"join rows est: {est_join_count}, act: {act_join_count}")
    print(f"left rows est: {est_left_count},  act {act_left_count}")
    print(f"right rows est: {est_right_count}, act: {act_right_count}")
    if est_left_count == 0 or act_left_count == 0 or est_right_count == 0 or act_right_count == 0 or act_join_count == 0:
        return False
    est_sel_join = max(1, est_join_count) / (est_left_count * est_right_count)
    act_sel_join = max(1, act_join_count) / (act_left_count * act_right_count)
    return [act_sel_join, est_sel_join]


def cal_local_selectivity(local_template, full_table_template):
    est_count, act_count = get_est_act_count(local_template)
    est_count_full, act_count_full = get_est_act_count(full_table_template)
    if act_count_full == 0 or est_count_full == 0:
        return False
    else:
        return [max(1, act_count)/act_count_full, max(1, est_count)/act_count_full]


def get_est_act_count(template):
    if db=='imdb':
        join_plans = get_real_latency('imdbloadbase', template, times=1, return_json=True, limit_time=False, limit_worker=True, drop_buffer=False)
    else:
        join_plans = get_real_latency(db, template, times=1, return_json=True, limit_time=False, limit_worker=True, drop_buffer=False)

    join_plans = join_plans[0][0][0]['Plan']
    node_type = join_plans['Node Type']
    while True:
        if node_type in ['Aggregate', 'Gather', 'Sort', 'Materialize', 'Sort', 'Hash', 'Gather Merge']:
            join_plans = join_plans["Plans"][0]
            node_type = join_plans['Node Type']
        else:
            break
    print(join_plans)
    est_join_count = join_plans['Plan Rows']
    act_join_count = join_plans['Actual Rows']
    return est_join_count, act_join_count




def plot_pdf():
    print(file_name_to_save_real_error)
    with open('./data/abs-error-'+db+'/' + file_name_to_save_real_error + '.txt', 'r') as fp:
        lines = fp.readlines()
    data = [x.strip().split() for x in lines]
    abs_error_list = []
    cleaned_data = []
    for x in data:
        # if float(x[0]) > 0.001:
        #     continue
        # if float(x[0]) > 1 or float(x[1]) > 1 or float(x[0]) < 0 or float(x[1]) < 0:
        #     continue
        # else:
        cleaned_data.append([float(x[0])/134170, float(x[1])/134170])
    # Err = true - est
    abs_err = [float(x[0]) - float(x[1]) for x in cleaned_data]
    abs_err = sorted(abs_err)
    abs_err = np.array(abs_err).reshape(-1, 1)
    print(max(abs_err), "max abs (true-est) error")
    print(min(abs_err), "min abs (true-est) error")
    count_1 = 0
    count_2 = 0
    for i in abs_err:
        if i > 0:
            count_1 += 1
        else:
            count_2 += 1
    print(count_1/(count_1 + count_2), ": true>est ", count_2/(count_1 + count_2), ": true<est")
    kde = KernelDensity(kernel="gaussian", bandwidth=0.3).fit(abs_err)
    # plot_error(abs_err, kde, name="data/abs-error-dsb/cn-mc_abs")
    
    relative_error_list = []
    for x in data:
        if float(x[0]) == 0 or 0 == float(x[1]):
            continue
        relative_error_list.append(-cal_rel_error(float(x[0]), float(x[1])))
    # print(relative_error_list)
    relative_error_list = np.array(relative_error_list).reshape(-1, 1)
    print(max(relative_error_list), "max rel error")
    print(min(relative_error_list), "min rel error")
    kde = KernelDensity(kernel="gaussian", bandwidth=1).fit(relative_error_list)
    plot_error(relative_error_list, kde, rel_error=True, name='data/abs-error-'+db+'/'+file_name_to_save_real_error)
    

def check_tempalte(db, template_name):
    if not querylet(db, '', '', template_name):
        return False
    else:
        return True


gen_real_error()

# db = 'imdb'
# file_name_to_save_real_error = "mk_ci__q17"
# plot_pdf()