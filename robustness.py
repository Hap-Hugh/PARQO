import numpy as np
import argparse
import psycopg2
import time
import os
# import vegas
import json
from tqdm import tqdm
import logging
from psql_explain_decoder import decode
from prep_error_list import *
from prep_cardinality import *
from prep_plan_set import *
from utility import card, list_multiply, modify_query
from postgres import *
from parse import *
from prep_selectivity import *
from sensitive_dict import *
from cached_robust_plan_dict import *
from SALib.analyze import sobol as sobol_ana
from SALib.sample import sobol
from SALib.analyze import morris as morris_ana
from SALib.sample import morris
import matplotlib.pyplot as plt
import test_related_work
import math
from prep_query_template import gen_sql_by_template
from kl import cal_kl


parser = argparse.ArgumentParser()
parser.add_argument('--sample', type=int, default=50, help='# of samples of monte carlo method')
parser.add_argument('--t', type=float, default=0.2, help='Tolerance of being near optimal')
parser.add_argument('--db', type=str, default='imdbloadbase', help='stats or imdbload')
parser.add_argument('--query_id', type=str, required=True, help='query id in job, e.g. 2a')
parser.add_argument('--rel_error', action='store_false', help='True to use relative error')
parser.add_argument('--cal_sen', type=str, required=False, help='sobol, morris, local')
parser.add_argument('--method', type=str, default='sobol', required=False, help='sobol, morris, local')
parser.add_argument('--div',type=int, default=2, help='I do not want to say.')
parser.add_argument('--exe', action='store_true')
parser.add_argument('--test_18', action='store_true')
parser.add_argument("--b", type=float, default=1)
parser.add_argument("--inst_id", type=int, default=-2)
parser.add_argument('--plot_err', action='store_true')
parser.add_argument('--debug', action='store_true')
parser.add_argument('--pqo', action='store_true')
parser.add_argument('--naive', action='store_true')


args = parser.parse_args()
db_name = args.db
query_id = args.query_id
tolerance = args.t


##### 1. Setup DB and Query #####
if args.cal_sen == 'morris' or args.method == 'morris':
    cal_sen_method = '_morris'
    if db_name == 'imdbloadbase':
        sen_dict = sen_dict_morris  
    if db_name == 'dsb':
        sen_dict =  dsb_sen_dict_morris
    if db_name == 'stats':
        sen_dict =  stats_sen_dict_morris
elif args.cal_sen == 'local' or args.method == 'local':
    cal_sen_method = '_local'
    sen_dict = sen_dict_local
else:
    cal_sen_method = ''
    if db_name == 'imdbloadbase':
        sen_dict = sen_dict_sobol  
    if db_name == 'dsb':
        sen_dict =  dsb_sen_dict_sobol
    if db_name == 'stats':
        sen_dict =  stats_sen_dict_sobol



if db_name == 'stats':
    with open(f'./query/stats/stats_{query_id}.sql') as p:
        sql = p.read()
    err_files_dict = err_files_dict_stats
if db_name == 'imdbloadbase':
    with open('./query/join-order-benchmark/' + query_id + '.sql') as p:
        sql = p.read()
    err_files_dict = err_files_dict_job
if db_name == 'dsb':
    with open(f'./query/dsb/query{query_id}_spj_1.sql') as p:
        sql = p.read()
    err_files_dict = err_files_dict_dsb

if args.inst_id == 0:
    ON_SAMPLE = "on-random/"   
    sql = modify_query("random_", "_4", sql)
elif args.inst_id == -1:
    ON_SAMPLE = "on-sample/"   
    sql = modify_query("sampled_", "_4", sql)
elif args.inst_id >= 1:
    ON_SAMPLE = "on-cat/"   
    sql = modify_query("cat_", f"_{args.inst_id}", sql)
else:
    ON_SAMPLE = 'on-base/' + db_name + '/'
    args.inst_id = None
    
if args.debug: print(sql)
# input()

##### 2. Setup Basic Info: CE and Raw Cardinality #####

explain = "EXPLAIN (SUMMARY, COSTS, FORMAT JSON)"
file_of_base_sel = './cardinality/new_single.txt'  # file to be sent to pg folder, contains cardinality for base_rel
file_of_join_sel = './cardinality/join.txt'  # file to be sent to pg folder, contains cardinality for join_rel


### original Postgres's est_card cardinality
table_name_id_dict, join_maps, join_info, pair_rel_info = get_maps(db_name, sql, debug=args.debug)
est_base_card, est_join_card_info = ori_cardest(db_name, sql)
est_join_card = list(est_join_card_info[:, 2])
est_card = est_base_card + est_join_card

### number of rows of base_rel
raw_base_card = get_raw_table_size(sql, args.inst_id, db_name)


### raw_join_card: number of rows of left_table * number of rows of right_table
raw_join_card = [i[2] for i in join_info]
raw_card = raw_base_card + raw_join_card

num_of_base_rel = len(raw_base_card)
num_of_pair_rel = len(pair_rel_info)
num_of_join_rel = len(raw_join_card)
all_basic_rels = list(range(num_of_base_rel + num_of_pair_rel)) # basic includes single and pair
all_rels = list(range(num_of_base_rel + num_of_join_rel)) # all include all

assert len(est_base_card) == len(raw_base_card)
assert len(est_join_card) == len(raw_join_card)

# f = open(f'log/{ON_SAMPLE}imdbloadbase_{query_id}++basicinfo.txt', 'w')
# for i in range(len(est_card)):
#     print(f"{i}, {est_card[i]}, {raw_card[i]}, {est_card[i]/raw_card[i]}", file=f)
# f.close()


### selectivity = est_card / raw_card
est_base_sel = [est_base_card[i]/raw_base_card[i] for i in range(num_of_base_rel)]
est_join_sel = [est_join_card[i]/raw_join_card[i] for i in range(num_of_join_rel)]
est_sel = est_base_sel + est_join_sel
if args.debug:
    print("Original est sel on base rel are: ", est_base_sel)
    print("Original est sel on join rel are: ", est_join_sel)
    print(f"Total {num_of_base_rel+num_of_join_rel} rels, {num_of_base_rel} base rels, {num_of_join_rel} join rels")


##### 3. Setup Error Profiles: for each considered dimensions #####

### GET ALL ERROR PROFILES AND SAVE THE PLOT OF ERROR PROFILES
### err_info_dict[i] = [cur_err_list, cur_err_hist, cur_kde_list]
### cur_err_list is a sorted relative error list;
### cur_err_hist is a bin list, each bin contains list of (est_sel, rel_error)
### cur_kde_list is a list of kde corespond to each bin in cur_err_hist
err_info_dict = {}
for i in range(num_of_base_rel + num_of_pair_rel):

    cur_err_list, cur_err_hist = prepare_error_data(db_name, query_id, sensi_dim=i, max_sel=1.0, 
                                                    rel_error=args.rel_error, div=args.div, debug=args.debug, pqo=args.pqo)
    if cur_err_list == [] and cur_err_hist == []: # Don't need to build err profile for this dimension
        err_info_dict[i] = []
        continue
    cur_kde_list = cal_pdf(cur_err_hist, rel_error=args.rel_error, bandwidth=args.b, naive=args.naive)
    err_info_dict[i] = [cur_err_list, cur_err_hist, cur_kde_list]

    if args.plot_err:
        r = find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim=i, err_info_dict=err_info_dict)
        pdf_after_bin = err_info_dict[i][2][r]
        err_data_used_by_pdf = [_[1] for _ in err_info_dict[i][1][r]] # (est_sel, rel_err)
        err_data_used_by_pdf = np.array(err_data_used_by_pdf).reshape(-1, 1)
        plot_error(err_data_used_by_pdf, pdf_after_bin, rel_error=True, name=f'data/plot_after_bin/{query_id}/{i}')


### Recenter the original selecitivty estimation (on all dims) based on mean of err distributions
center_err = gen_center_from_err_dist(est_card, raw_card, all_basic_rels, err_info_dict, num_of_samples=1000, debug=args.debug, naive=args.naive)
# center_err = None
# center_err = [0] * len(all_basic_rels)
# input()


print(f"Generated corrected plan by recenter selectivity from error distribution", )
if center_err:
    for i, item in enumerate(center_err):
        print(f"{i}: {item}", end=", ")

##### 4. Setup Candidate Plan Set: Generated by Sampling #####

### Check if we do not have the candidate plan list, we should generate it
### Need to define sensitive dimension first
def get_plan_list(sensitive_rels):
    cur_plan_list = []
    if args.inst_id != None:
        file = './plan/' + ON_SAMPLE + 'tmp_plan_dict_' + db_name + '_' + query_id + '_' + str(args.inst_id) + cal_sen_method + '.txt'
    else:
        file = './plan/' + ON_SAMPLE + 'tmp_plan_dict_' + db_name + '_' + query_id + cal_sen_method +'.txt'
        
        if db_name == 'imdbloadbase': # use the plan generated by full err profile (no train-test split)
            file = './plan/' + ON_SAMPLE + 'saved-tmp_plan_dict_' + db_name + '_' + query_id + cal_sen_method +'.txt'
    
    if os.path.exists(file):
        print(f"Find existed plan set. {file}")
        plan_hint_dict = json.load(open(file))
    else:
        print(f"No existed plan list. Have to generate. Store it at {file}")
        plan_hint_dict = get_plan_set_by_enum(table_name_id_dict, join_maps, join_info, 
                                                db_name, explain + '\n' + sql, 
                                                est_base_card, raw_base_card, file_of_base_sel, 
                                                est_join_card, raw_join_card, file_of_join_sel, 
                                                sensitive_rels, 100, err_info_dict, center_err, top_k=0)

        json.dump(plan_hint_dict, open(file,'w'), indent=2)
    
    for i in plan_hint_dict.values():
        cur_plan_list = cur_plan_list + i
    cur_plan_list = list(sorted(set(cur_plan_list)))
    # if query_id == '17a':
    #     cur_plan_list = [cur_plan_list[7], cur_plan_list[8], cur_plan_list[10], cur_plan_list[44]]
    return cur_plan_list


### calculate the penalty between the input plan and the optimal plan
### penalty = cost(input plan) - cost(opt plan)
def cal_penalty_at_sample(error, hint, cur_dim, 
                          est_base_sel=est_base_sel, est_join_sel=est_join_sel, 
                          return_penalty_val=True, recentered_error=center_err):
    new_base_sel, new_join_sel = prep_sel(table_name_id_dict, join_maps, join_info, 
                                          est_base_sel, file_of_base_sel, 
                                          est_join_sel, file_of_join_sel, 
                                          error=error, recentered_error=recentered_error,
                                          relation_list=cur_dim, rela_error=args.rel_error)
    cost_value_with_hint, join_order_with_hint, scan_mtd_with_hint = get_plan_cost(cursor, sql=sql, hint=hint, explain=explain, debug=True) 
    cost_value_opt, join_order_opt, scan_mtd_opt = get_plan_cost(cursor, sql=sql, explain=explain, debug=True)
    if return_penalty_val:
        return max(cost_value_with_hint - cost_value_opt, 0)
    else:
        return cost_value_with_hint, cost_value_opt, new_base_sel, new_join_sel



def plot_cdf_of_penalty(penalty_list, plan_list, sensitive_rels, N=1000):
    if not penalty_list:
        penalty_list = []
        joint_error_samples = gen_samples_from_joint_err_dist(N, relations=sensitive_rels)
        for i, plan in enumerate(plan_list):
            penalty_list[i] = [cal_penalty_at_sample(x, hint=plan, cur_dim=sensitive_rels, 
                                                     est_base_sel=est_base_sel, 
                                                     est_join_sel=est_join_sel) 
                                                     for x in joint_error_samples]

    plt.figure(figsize=(12, 8))

    plt.xlabel('Cost Penalty', fontsize=30),
    plt.ylabel('Cumulative Probability', fontsize=30)
    colors = ['orange', 'green', 'magenta', 'blue']
    labels = ["PostgreSQL", "WBM", "Recenter", "PARQO", ]
    for i, plan in enumerate(plan_list):
        cdf = np.arange(1, len(penalty_list[i]) + 1) / len(np.sort(penalty_list[i]))
        
        plt.plot(list(np.sort(penalty_list[i])), list(cdf), color=colors[i], label=labels[i], linewidth=2,)

    plt.legend(fontsize=24)
    plt.xticks(fontsize=35)  
    plt.yticks(fontsize=35)
    plt.xscale('log')
    plt.suptitle(f'CDF of Cost Penalty (Q{query_id.replace("q", "").replace("a", "")})', fontsize=35, y=0.98)  # Adjust the y value to position the title
    plt.tight_layout()
    plt.savefig('./penalty-cdf/'+query_id+'penalty_cdf_sen_dim_all_plan.pdf')




### Generate samples from the error distribution on each dimension and then joint them
### 
def gen_samples_from_joint_err_dist(N, relations, random_seeds=True, naive=False):
    if random_seeds:
        np.random.seed(2023)
    joint_error_samples = []
    for table_id in relations:

        if naive:
            # r = find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim=table_id, err_info_dict=err_info_dict)
            # pdf_of_err = err_info_dict[table_id][2][r]
            # err_sample = np.random.normal(loc=pdf_of_err[0], scale=pdf_of_err[1], size=N)
            err_sample = np.random.uniform(-10, 10, N)
        else:
            r = find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim=table_id, err_info_dict=err_info_dict)
            pdf_of_err = err_info_dict[table_id][2][r]
            err_sample = pdf_of_err.sample(N)
        joint_error_samples.append(err_sample)

    # Transfer to joint samples
    if naive:
        joint_error_samples = np.array(joint_error_samples).T.tolist()
    else:
        joint_error_samples = np.array(joint_error_samples).T.tolist()[0]

    if args.debug:
        print(f"Generate {len(joint_error_samples)} selectivities samples based on the joint distribution.")
    return joint_error_samples



        



### Get the optimal plan at the given error sample
### 1. inject the selectivity based on error first 
### 2. call postgres to get the plan
### 3. transfer to hint
def get_opt_plan_at_sample(error, cur_dim, center_err=center_err, return_sel_at_sample=False):
    # We also input center_err here by defual, to avoid: e.g. [8, 9, 10] are sensitive 
    # while 12 is not sensitive but 12 has huge error; center_err should correct those 
    # errors like this.
    base_sel_at_sample, join_sel_at_sample = prep_sel(table_name_id_dict, join_maps, join_info, 
                                            est_base_sel=est_base_sel, f_base_sel=file_of_base_sel, 
                                            est_join_sel=est_join_sel, f_join_sel=file_of_join_sel, 
                                            error=error, recentered_error=center_err, 
                                            relation_list=cur_dim, rela_error=args.rel_error)
    cost_value_opt, join_order, scan_mtd = get_plan_cost(cursor, sql=sql, explain=explain, debug=True)
    ori_opt_plan_at_sample = gen_final_hint(join_order, scan_mtd)
    if return_sel_at_sample:
        return ori_opt_plan_at_sample, cost_value_opt, base_sel_at_sample, join_sel_at_sample
    else:
        return ori_opt_plan_at_sample, cost_value_opt


### This is a new function to use samples to calculate RM1 (expected penalty) for each plan
### Basically, calculate the avg penalty among samples
### Also, we need to save the selectivity samples for future uses
def exp_penalty_by_samples(cur_plan_list, sensitive_rels, joint_error_samples, tolerance, est_base_sel=est_base_sel, est_join_sel=est_join_sel, save_samples=True):
    print("## RM1: Start to calculate exp penalty by samples from err distribution")
    exp_penalty_list = []
    std_penalty_list = []
    incur_penalty_list = []
    ### Save selectivity samples to future reuse in this dict:
    ### Key: selectivity sample as tuple
    ### Value: 
    ### -- first element: probability of being sampled, 
    ### -- then: the penalty of each plan w.r.t the key (selectivity sample)
    sample_to_penalty_dict = {}  
    
    ### Save the correspond opt cost at this sel sample to reduce overhead; TODO later
    sample_to_opt_cost_dict = {} 

    for hint_id, hint in enumerate(cur_plan_list):
        if len(cur_plan_list) > 1:
            print("## RM1: plan id: ", hint_id)
        start = time.time()
        total_penalty = 0.0
        penalty_list_of_cur_plan = []
        incur_penalty_count = 0
        for error in joint_error_samples:
            cost_value_with_hint, cost_value_opt, new_sel_base, new_sel_join = cal_penalty_at_sample(error=error, hint=hint, 
                                                                                                    cur_dim=sensitive_rels, return_penalty_val=False,       
                                                                                                    est_base_sel=est_base_sel, est_join_sel=est_join_sel)
            # if hint_id == 13:
            print(hint_id, ":", cost_value_with_hint, cost_value_opt, error)
            
            cost_penalty = cost_value_with_hint - cost_value_opt
            cost_penalty_rate = cost_value_with_hint / cost_value_opt
            if tolerance > 0: ## using tolerance; only count the penalty when ratio> 1+tolerance
                if cost_penalty_rate <= 1+tolerance:
                    cost_penalty = 0
                else:
                    incur_penalty_count += 1
                # print(cost_value_with_hint, cost_value_opt)
            
            # if exp_prob_of_penalized:
            #     if cost_penalty_rate <= 1+tolerance:
            #         return 0
            #     else:
            #         return cal_sum_products_of_error_pdf(error)
            total_penalty += cost_penalty
            penalty_list_of_cur_plan.append(cost_penalty)
            new_sel_tuple = tuple(new_sel_base + new_sel_join) 

            if save_samples and args.method == 'sobol':
                if new_sel_tuple not in sample_to_penalty_dict:
                    # Calculate the probility of being sampled
                    probability = cal_prob_of_sample(error, sensitive_rels, est_card, raw_card, err_info_dict, is_error_sample=True)
                    # print(new_sel_tuple)
                    probability_ = cal_prob_of_sample(samples=[new_sel_tuple], 
                                                    sensitive_rels=list(err_files_dict[get_pure_q_id(query_id, db_name)].keys()), 
                                                    est_card=est_card, 
                                                    raw_card=raw_card, 
                                                    err_info_dict=err_info_dict, 
                                                    is_error_sample=False)
                    # Note the probability of sampling an error may not = the probability of sampling the corresponding selectivity
                    # e.g. when the error is large, but the maximum selectivity is always 1
                    # assert round(probability, 7) == round(probability_[0], 7), f"{probability}, {probability_}"
                    sample_to_penalty_dict[new_sel_tuple] = [probability_[0]]
                
                sample_to_penalty_dict[new_sel_tuple].append(cost_penalty)
        end = time.time()
        cur_exp_penalty = round(total_penalty / len(joint_error_samples))
        print(f"Time: {end-start}(s), Penalty: {cur_exp_penalty}")
        exp_penalty_list.append(cur_exp_penalty)
        std_penalty_list.append(np.std(np.array(penalty_list_of_cur_plan)))
        incur_penalty_list.append(incur_penalty_count / len(joint_error_samples))
    
    # Save the samples for query template's reuse
    if save_samples and args.method == 'sobol':
        converted_dict = {str(key): [float(i) for i in value] for key, value in sample_to_penalty_dict.items()}
        with open(f'reuse/{db_name}_{query_id}.json', 'w') as file:
            json.dump(converted_dict, file, indent=4)
        


    return exp_penalty_list, std_penalty_list, incur_penalty_list


### Local OAT method to calculate sensitivity of each dimension
def Local(relations, use_penalty=False):
    ori_cost, ori_join_order, ori_scan_mtd = get_plan_cost_simple(cursor, sql=sql, explain=explain, debug=True)
    hint = gen_final_hint(scan_mtd=ori_scan_mtd, str=ori_join_order)
    slop_list = []
    for t_id in relations:
        delta = 1
        base_output_sel = [est_base_card[i]/raw_base_card[i] for i in range(num_of_base_rel)]
        join_output_sel = [est_join_card[i]/raw_join_card[i] for i in range(num_of_join_rel)]
        if t_id >= num_of_base_rel:
            i = t_id - num_of_base_rel
            delta_sel = delta * join_output_sel[i]
            join_output_sel[i] += delta_sel
            
        else:
            i = t_id
            delta_sel = delta * base_output_sel[i]
            base_output_sel[i] += delta_sel
        write_to_file(base_output_sel, file_of_base_sel)
        write_pointers_to_file([t_id])
        write_to_file(join_output_sel, file_of_join_sel)

            
        cost_after_disturb = get_plan_cost(cursor, sql=sql, hint=hint, explain=explain)
        opt_cost_after_disturb = get_plan_cost(cursor, sql=sql, hint=None, explain=explain)
            
        if use_penalty:
            slop = (cost_after_disturb - opt_cost_after_disturb) / delta_sel
        else:
            slop = (cost_after_disturb - ori_cost ) / delta_sel
        slop_list.append(slop)
    sorted_indices = [(index, round(value)) for index, value in sorted(enumerate(slop_list), key=lambda x: x[1], reverse=True)]
    result = []
    for m in sorted_indices:
        result.append((list(err_files_dict[get_pure_q_id(query_id, db_name)].items())[m[0]], m[1]))
    print(slop_list)
    logging.info(f"Tau: {tolerance}, Delta: {delta}, Slop list: {result}")
    return


### Morris (still Local & OAT) method to calculate sensitivity of each dimension
def Morris(N, relations):
    delta = 0.05 # raletive error: e^0.05 = 1.05 times
    logging.info(f"Morris: Sample size {N}")
    logging.info(f"Morris: Simulated size N = {N*(len(relations)+1)}, delta = {delta}, {len(relations)} dim")
    # By default we apply the recentered_error already
    recentered_opt_plan, recentered_opt_cost, recentered_base_sel, recentered_join_sel = get_opt_plan_at_sample([], [], return_sel_at_sample=True)
    joint_error_samples = gen_samples_from_joint_err_dist(N, relations, False)
    problem = generate_problem(len(relations))
    input_values = morris.sample(problem, N)
    numbers = np.arange(0, len(relations))

 
    # collect input values
    input_values = []
    penalty_of_each_dim = [0] * len(relations)
    for i in tqdm(range(N)):
        input_values_of_cur_sample = []
        initial_value = joint_error_samples[i]
        input_values_of_cur_sample.append(initial_value)
        initial_penalty = cal_penalty_at_sample(error=initial_value, 
                                                hint=recentered_opt_plan, 
                                                est_base_sel=est_base_sel, 
                                                est_join_sel=est_join_sel, 
                                                cur_dim=relations)
        # generate a path
        np.random.shuffle(numbers)
        # add delat to one dimension at a time
        for id, reference in enumerate(numbers):
            initial_value[reference] += delta
            input_values_of_cur_sample.append(initial_value)

            new_penalty = cal_penalty_at_sample(error=initial_value, hint=recentered_opt_plan, 
                                                est_base_sel=est_base_sel, 
                                                est_join_sel=est_join_sel, 
                                                cur_dim=relations)
            penalty_difference = abs(new_penalty - initial_penalty)
            penalty_of_each_dim[reference] += penalty_difference


        input_values = input_values + input_values_of_cur_sample

        if i % 20 == 0:

            USE_SALIB = False

            if USE_SALIB:
                input_values = np.array(input_values)
                Y = np.zeros([input_values.shape[0]])
                for i, error in enumerate(tqdm(input_values)):
                    # cal_penalty_at_sample will use the global variable center_err
                    penalty_at_err_sample = cal_penalty_at_sample(error=error, hint=recentered_opt_plan, 
                                                                    est_base_sel=est_base_sel, 
                                                                    est_join_sel=est_join_sel, 
                                                                    cur_dim=relations)
                    Y[i] = penalty_at_err_sample
                Mo = morris_ana.analyze(problem, input_values, Y, conf_level=0.95,print_to_console=True, num_levels=4)
                logging.info(f"Morris: {Mo}")
                print(Mo)
            else:
                avg_penalty_of_each_dim = [i/N for i in penalty_of_each_dim]
                result = []
                sorted_indices = [(index, round(value)) for index, value in sorted(enumerate(avg_penalty_of_each_dim), key=lambda x: x[1], reverse=True)]
                for m in sorted_indices:
                    result.append((list(err_files_dict[get_pure_q_id(query_id, db_name)].items())[m[0]], m[1]))
            
                print(result)
                logging.info(f"{i} Morris: {result}")
    return


### Sobol's Global Sensitivity Analysis ###
def sobols(N, relations):
    logging.info(f"Sobol: Sample size N = {N}, b = {args.b}")
    using_penalty = True
    
    
    recentered_opt_plan, recentered_opt_cost, recentered_base_sel, recentered_join_sel = get_opt_plan_at_sample([], [], return_sel_at_sample=True)
    default_err = [0] * len(all_basic_rels)
    default_opt_plan, default_opt_cost, _, _ = get_opt_plan_at_sample([], [], center_err=None,return_sel_at_sample=True)
    print("Sobol: Postgres default plan's cost: ", default_opt_cost)
    print("Sobol: Postgres plan: ", default_opt_plan)
    print("Sobol: Recentered plan's cost: ", recentered_opt_cost)
    print("Sobol: Recentered plan: ", recentered_opt_plan)
    print("Sobol: We are considering", relations)
    logging.info(f"Recentered plan cost = {recentered_opt_cost}, plan is: {recentered_opt_plan}")
    
    # latency = round(get_real_latency(db_name, sql, hint=recentered_opt_plan, times=11), 1)
    # print(f"Real latency of opt plan at the recentered sel is {latency}")
    # quit()

    

    # Sample from the joint distribution (all dimensions in hand)
    # Note: if you sample from entire dimensions, center_err will not matter
    joint_error_samples = gen_samples_from_joint_err_dist(N, relations, False, naive=args.naive)
    joint_error_samples_b = gen_samples_from_joint_err_dist(N, relations, False, naive=args.naive)



    

    # Build the (2*d) im matrix by sample
    combined_joint_error_samples = np.hstack((np.array(joint_error_samples), np.array(joint_error_samples_b)))
    
    # Define the problem
    problem = generate_problem(len(relations))
    
    # Salib to generate sobol sequence, N*2*d in total
    input_values = sobol.sample(problem, N, combined_joint_error_samples)
    
    # Verify !! after you have the sobol's result (sensitive_rels)
    if False:
        N = 1000
        sensitive_rels=sorted(sen_dict[get_pure_q_id(query_id, db_name)])
        joint_error_samples = gen_samples_from_joint_err_dist(N, sensitive_rels, False)
        joint_error_samples_1 = gen_samples_from_joint_err_dist(N, sensitive_rels, False)
        joint_error_samples_2 = gen_samples_from_joint_err_dist(N, sensitive_rels, False)
        joint_error_samples_3 = gen_samples_from_joint_err_dist(N, sensitive_rels, False)
        cur_plan_list = get_plan_list(sensitive_rels)
        print(f"Generate {len(joint_error_samples)} samples")
        Y_default = np.zeros([len(joint_error_samples)])
        Y_recenter = np.zeros([len(joint_error_samples)])
        Y_related_work = np.zeros([len(joint_error_samples)])
        Y_rob1 = np.zeros([len(joint_error_samples)])
        Y_rob2 = np.zeros([len(joint_error_samples)])
        Y_rob3 = np.zeros([len(joint_error_samples)])
        for i, error in enumerate(tqdm(joint_error_samples)):
            # Should combine sampled error with recentered error
            # Note: cal_penalty_at_sample by default uses the recentered_error
            Y_default[i] = cal_penalty_at_sample(error=error, hint=default_opt_plan, 
                                                est_base_sel=est_base_sel, 
                                                est_join_sel=est_join_sel, 
                                                cur_dim=sensitive_rels)
            Y_recenter[i] = cal_penalty_at_sample(error=joint_error_samples_1[i], hint=recentered_opt_plan, 
                                                est_base_sel=est_base_sel, 
                                                est_join_sel=est_join_sel, 
                                                cur_dim=sensitive_rels)
            Y_rob1[i] = cal_penalty_at_sample(error=joint_error_samples_2[i], hint=cur_plan_list[1], 
                                                est_base_sel=est_base_sel, 
                                                est_join_sel=est_join_sel, 
                                                cur_dim=sensitive_rels)
            # Y_rob2[i] = cal_penalty_at_sample(error=error, hint=cur_plan_list[20], 
            #                                     est_base_sel=est_base_sel, 
            #                                     est_join_sel=est_join_sel, 
            #                                     cur_dim=sensitive_rels)
            # Y_rob3[i] = cal_penalty_at_sample(error=error, hint=cur_plan_list[21], 
            #                                     est_base_sel=est_base_sel, 
            #                                     est_join_sel=est_join_sel, 
            #                                     cur_dim=sensitive_rels)
            Y_related_work[i] = cal_penalty_at_sample(error=joint_error_samples_3[i], hint=cur_plan_list[0], 
                                                est_base_sel=est_base_sel, 
                                                est_join_sel=est_join_sel, 
                                                cur_dim=sensitive_rels)
            joint_error_samples = gen_samples_from_joint_err_dist(N, sensitive_rels, False)
        write_to_file(Y_default, 'penalty-cdf/penalty_of_samples/'+query_id+'sendim_default_1000.txt')
        write_to_file(Y_recenter, 'penalty-cdf/penalty_of_samples/'+query_id+'sendim_recenter_1000.txt')
        write_to_file(Y_rob1, 'penalty-cdf/penalty_of_samples/'+query_id+'sendim_rob_1000.txt')
        # write_to_file(Y_rob2, 'penalty-cdf/penalty_of_samples/'+query_id+'sendim_rob2_1000.txt')
        # write_to_file(Y_rob3, 'penalty-cdf/penalty_of_samples/'+query_id+'sendim_rob3_1000.txt')
        write_to_file(Y_related_work, 'penalty-cdf/penalty_of_samples/'+query_id+'sendim_2018_1000.txt')
        
        print(np.mean(Y_default), np.mean(Y_recenter), np.mean(Y_rob1), np.mean(Y_rob2), np.mean(Y_rob3), np.mean(Y_related_work))
        # quit()
    
    # Plot cdf to verify sensitive_rels after you have sobol's results
    if False:
        sensitive_rels=sorted(sen_dict[get_pure_q_id(query_id, db_name)])
        penalty_list = []
        cur_plan_list = get_plan_list(sensitive_rels)
        # ["PostgreSQL", "WBM", "Recenter", "PARQO", ]
        plan_list = [default_opt_plan, cur_plan_list[0], recentered_opt_plan, cur_plan_list[0]]
        # plan_list = []
        
        for file_name in ['penalty-cdf/penalty_of_samples/'+query_id+'sendim_default_1000.txt',
                          'penalty-cdf/penalty_of_samples/'+query_id+'sendim_2018_1000.txt',  
                        'penalty-cdf/penalty_of_samples/'+query_id+'sendim_recenter_1000.txt',
                        'penalty-cdf/penalty_of_samples/'+query_id+'sendim_rob_1000.txt',
                        ]:
            lines = []
            with open(file_name, 'r') as f:
                while True:
                    line = f.readline()
                    if not line: break
                    line = float(line.strip())
                    lines.append(line)
            penalty_list.append(lines)
        plot_cdf_of_penalty(penalty_list, plan_list, sensitive_rels)
        quit()


    # run the model by sobol sequence
    Y = np.zeros([input_values.shape[0]])
    print("Sobol: Total samples size is", input_values.shape[0])
    start = time.time()
    for i, error in enumerate(tqdm(input_values)):
        if using_penalty:
            # cal_penalty_at_sample will use the global variable center_err
            penalty_at_err_sample = cal_penalty_at_sample(error=error, hint=recentered_opt_plan, 
                                                          est_base_sel=est_base_sel, 
                                                          est_join_sel=est_join_sel, 
                                                          cur_dim=relations)
            Y[i] = penalty_at_err_sample
        else:
            opt_plan_at_sample, cost_value_opt, = get_opt_plan_at_sample(error.tolist(), relations)
            Y[i] = cost_value_opt
    

    end = time.time()
    print(f"Sobol: Collecting output uses {end-start}(s)")
    
    # Analyze the indices (sensitivity) of single & pair parameters
    while len(Y) > 100:
        logging.info(f"Sobols samples size: {len(Y)}")
        Si = sobol_ana.analyze(problem, Y)
        end = time.time()

        print_all_info = False
        if print_all_info:
            print(Si['S1'])
            print(Si['S2'])
            logging.info(Si['S1'])
            logging.info(Si['S2'])
            
        result = []
        sorted_s1 = [(index, value) for index, value in sorted(enumerate(Si['S1']), key=lambda x: abs(x[1]), reverse=True)]
        
        
        for i in sorted_s1:
            result.append((list(err_files_dict[get_pure_q_id(query_id, db_name)].items())[i[0]], i[1]))
        logging.info(result)
        print(sorted_s1)
        print(result)

        top_n_sensitive_dim = top_n_of_2d_matrix(Si['S2'], 5) # print the id as (id_pair_rel + base)
        logging.info(top_n_sensitive_dim)
        Y = Y[:len(Y)//2]
    
    print(f"Sobol: Solving time is {end-start}(s)")
    logging.info(f"Sobol's solving time: {end-start}(s)")
    return  
    


# Calculate the sensitivity per dimension
def cal_dim_sensitivity():
    global sensitive_rels
    
    # dimension_space = list(range(num_of_base_rel, num_of_base_rel + num_of_pair_rel))
    dimension_space = list(err_files_dict[get_pure_q_id(query_id, db_name)].keys())
    # sensitive_rels = [8, 9, 10, 12]
    if args.cal_sen == 'local':
        Local(relations=dimension_space)
    elif args.cal_sen == 'morris':
        Morris(200, relations=dimension_space)
    else:
        sobols(N=256, relations=dimension_space)
    quit()



##### 5. RQO entrance #####
def rqo():
    logging.basicConfig(filename='./log/' + ON_SAMPLE + db_name + '_' + query_id + '_' + str(tolerance) + cal_sen_method + '.log', level=logging.INFO)
    logging.info(f"\n########## Robust Query Optimization ############ \n")
    print(f"\n########## Robustness Query Optimization ############ \n")
    
    
    global hint
    global cursor
    global exp_prob_of_penalized
    global sensitive_rels # move outside


    ### Connect ot postgres server
    conn = psycopg2.connect(host="/tmp", dbname=db_name, user="hx68")
    conn.set_session(autocommit=True)
    cursor = conn.cursor()
    print("## RQO: Connected to Postgres ...")


    ### Start to analyze sensitivity of dimensions
    if not args.cal_sen:
        print("## RQO: Load sensitivity from sen_dict ...")
        # TODO, 17-x should use different sens_dims
        sensitive_rels = sorted(sen_dict[get_pure_q_id(query_id, db_name)]) # read from file
    else:
        print("## RQO: Start analyzing dimension sensitivity...")
        exp_prob_of_penalized = None
        sensitive_rels = cal_dim_sensitivity()
    print("## RQO: Current sensitive dimensions are", sensitive_rels)


    ### Debugging by calling Postgres; Also use this part to inject true selectvities (manually & gradually)
    while 0:
        get_all_predicates(cursor=cursor, sql=sql, explain="EXPLAIN (COSTS, FORMAT JSON)")
        # input()
        ### Correct the sensitive dimension's error (manually & gradually)
        ##
        ### 1. Suppose we don't have recentered error
        # original plan
        # print(center_err) 
        # input()
        inject_error = [0] * len(all_basic_rels) # Regard all of the dimensions as sensitive dimensions
    
        ori_opt_plan, ori_opt_cost, base, join = get_opt_plan_at_sample([0.02, 1.50], [13, 5], center_err=None, return_sel_at_sample=True)
        
        # print(cal_penalty_at_sample([-0.39, 0.04, 7.12], hint=ori_opt_plan, cur_dim=[8, 9, 12],
        #                        est_base_sel=est_base_sel,
        #                        est_join_sel=est_join_sel,
        #                        recentered_error=None,
        #                        return_penalty_val=False))
        # [0.3 ,7.2], [5, 6]
        # [-0.4, 0.2, 7.12], [8, 11, 12],
        print(ori_opt_cost)
        # print(base, est_base_sel)
        # print(len(join), len(est_join_sel))
        # for i in range(len(join)):
        #     if join[i] != est_join_sel[i]:
        #         print(join[i], est_join_sel[i], i)
        #         input()
        # ori_opt_plan, ori_opt_cost, _, _ = get_opt_plan_at_sample(zero_error, all_basic_rels, center_err=None, return_sel_at_sample=True)
        # print(ori_opt_cost)        
        ori_latency = get_real_latency(db_name, sql, hint=ori_opt_plan, times=10, inject=False, output_plan=False, limit_time=10000)
        print(ori_opt_cost, ori_latency)

        # correct the sel of first sensitive dim
        # inject_error = center_err
        # inject_error[38] = 7
        # inject_error[2] = 0.69
        # inject_error[16] = -1
        # inject_error[17] = -0.645
        # inject_error[8] = 0.016
        

        # inject_error[2] = 0.69
        # inject_error[22] = 0.07
        # inject_error[15] = -0.21

        # new_error = [0, 0, 0.019, 0, 0, 0, 0, 0, 0, 0.043, 6.7e-06, 0.203, 7.115, 0, 0.0, 0]
        # new_error = [0, 0, 0.0, 0, 0, 0, 0, 0, -0.1514,  0.0, 0.0, 0.0, 7.115, 0, 0.0, 0]
        
        # new_opt_plan, new_opt_cost, _, _ = get_opt_plan_at_sample(inject_error, all_basic_rels, center_err=center_err, return_sel_at_sample=True)
        new_latency = get_real_latency(db_name, sql, hint=new_opt_plan, times=10, inject=False, output_plan=False, limit_time=10000)
        print(new_opt_cost, new_latency)
        input()   

        recentered_opt_plan, recentered_opt_cost, _, _ = get_opt_plan_at_sample(center_err, all_basic_rels, return_sel_at_sample=True)
        plan = recentered_opt_plan # set the hint to current best plan id
        print("### Recenter by err: ", center_err, recentered_opt_cost)
        print("### Cost after recentered (inject the plan): ", get_plan_cost(cursor, sql, plan, explain="EXPLAIN (COSTS, FORMAT JSON)"))
        print("### Opt cost at recentered (optimizer's default): ", get_plan_cost(cursor, sql, explain="EXPLAIN (COSTS, FORMAT JSON)"))
        input()
        new_error = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.9, 0.0, 2.0, 0]
        new_opt_plan, new_opt_cost, _, _ = get_opt_plan_at_sample(new_error, all_basic_rels, return_sel_at_sample=True)
        print("### New err: ", new_error, new_opt_cost)
        print("### Cost of original plan: ", get_plan_cost(cursor, sql, plan, explain="EXPLAIN (COSTS, FORMAT JSON)"))
        print("### Cost of new opt plan: ", get_plan_cost(cursor, sql, new_opt_plan, explain="EXPLAIN (COSTS, FORMAT JSON)"))
        
        print("### Here are the plans: ")
        input()
        print(plan, new_opt_plan)

        # print(get_real_latency(db_name, sql, hint=tmp_hint, times=10, inject=False, output_plan=False))
        input()


    write_to_file(est_base_sel, file_of_base_sel)
    write_to_file(est_join_sel, file_of_join_sel)
    write_pointers_to_file(list(range(num_of_base_rel + num_of_join_rel)))

    
    ### Get candidate plan set
    cur_plan_list = get_plan_list(sensitive_rels)
    cost_of_all_hints = get_all_plan_cost(cursor, sql, explain, cur_plan_list, debug=args.debug)
    if args.debug:  print(cost_of_all_hints)
    ori_opt_plan_id = cost_of_all_hints.index(min(cost_of_all_hints))
    logging.info(f"Original optimal plan id is {ori_opt_plan_id}")
    logging.info(f"Instance id = {args.inst_id}, Error div = {args.div}, bandwidth = {args.b}, tolerance = {tolerance}, have {args.sample} samples.")
    logging.info(f"Cost of {len(cur_plan_list)} plan: \t{[(id_, i_) for id_, i_ in enumerate(cost_of_all_hints)]}")
    print(f"## RQO: Current we have {len(cur_plan_list)} candidate plans", )
    # print(cur_plan_list[20])
    # input()


    ### Enumerate each candidate plan and calculate the real latency
    if args.exe:
        cur_plan_latency_list = []
        exe_times = 11 # Exe multiple times to reduce noise
        ### should not use get_opt_plan_at_sample with all zero error and no sensitive dims to get the opt plan;
        ### we'd better keep the original selectivity estimation amsp
        default_plan_latency = round(get_real_latency(db_name, sql, times=exe_times, limit_time=1200000, output_plan=True), 1)
        logging.info(f'postgres default latency: {default_plan_latency}')
        recentered_opt_plan, recentered_opt_cost, recentered_base_sel, recentered_join_sel = get_opt_plan_at_sample([], [], center_err=center_err, return_sel_at_sample=True)
        recentered_opt_plan_latency = round(get_real_latency(db_name, sql, hint=recentered_opt_plan , times=exe_times, limit_time=1200000, output_plan=True), 1)
        logging.info(f'recentered plan latency: {recentered_opt_plan_latency}')
        print(default_plan_latency, recentered_opt_plan_latency)
        for i in range(len(cur_plan_list)):
        # for i in [6]:
            latency = round(get_real_latency(db_name, sql, hint=cur_plan_list[i], times=exe_times, limit_time=1200000), 1)
            cur_plan_latency_list.append(latency)
            print(i, ": ", latency)
            logging.info(f"{i}: {latency}")
        logging.info(f"Best latency we know is: {min(cur_plan_latency_list)} ms, with plan id = {cur_plan_latency_list.index(min(cur_plan_latency_list))}, {cur_plan_latency_list} ")
        # quit()


    ### Use Metrics to Calculate Robustness Value
    print("## RQO: Start analyzing robustness...")
    sensitive_rels_trys = [sensitive_rels]  # we could assign multiple try here
    for i, sensitive_rels in enumerate(sensitive_rels_trys):

        logging.info(f"Sensitive predicates: {sensitive_rels_trys[i]}")
        exp_prob_of_penalized = None
        
        exp_penalty_list = []
        RM_card_slope_list = []
        RM_sel_slope_list = []
        RM_integral_list = []
    
        copy_sensitive_rels = [i for i in sensitive_rels]

        
        if args.test_18:


            start = time.time()
            print(f"### Testing 2018 VLDB...")
            RM_sensitive_rels = test_related_work.get_sensitive_edge(db_name, sql)


            RM_sel_slope_list.append(test_related_work.slope_RM(cursor, sql, None, explain, RM_sensitive_rels,
                                                                est_base_card, raw_base_card, file_of_base_sel, 
                                                                est_join_card, raw_join_card, file_of_join_sel, sel=True))
                
            # RM_sensitive_rels = [1, 5, 6]
            for hint_id, hint in enumerate(tqdm(cur_plan_list)):
                print(f"### Calculate the robustness of plan {hint_id}...")
                cur_plan_cost = get_plan_cost_simple(cursor, sql=sql, hint=hint, explain=explain)
                default_plan_cost = get_plan_cost_simple(cursor, sql=sql, explain=explain)
                # print(cur_plan_cost, default_plan_cost)
                if cur_plan_cost / default_plan_cost > 1.2:
                    RM_card_slope_list.append(math.inf)
                    RM_sel_slope_list.append(math.inf)
                    RM_integral_list.append(math.inf)
                    continue
                
                
                # i == 0 means we are comparing the previous work

                RM_card_slope_list.append(test_related_work.slope_RM(cursor, sql, hint, explain, RM_sensitive_rels,
                                                                est_base_card, raw_base_card, file_of_base_sel, 
                                                                est_join_card, raw_join_card, file_of_join_sel, sel=False))
                RM_sel_slope_list.append(test_related_work.slope_RM(cursor, sql, hint, explain, RM_sensitive_rels,
                                                                est_base_card, raw_base_card, file_of_base_sel, 
                                                                est_join_card, raw_join_card, file_of_join_sel, sel=True))
                
                RM_sum_of_integ = 0.0
                base_output_sel = [est_base_card[i]/raw_base_card[i] for i in range(num_of_base_rel)]
                join_output_sel = [est_join_card[i]/raw_join_card[i] for i in range(num_of_join_rel)]

                for sen_rel in RM_sensitive_rels:
                    break
                    for new_sel in np.random.rand(args.sample):
                        if sen_rel >= num_of_base_rel:
                            i = sen_rel - num_of_base_rel
                            join_output_sel[i] = new_sel
                        else:
                            i = sen_rel
                            base_output_sel[i] = new_sel

                        write_to_file(base_output_sel, file_of_base_sel)
                        write_pointers_to_file([sen_rel])
                        write_to_file(join_output_sel, file_of_join_sel)
                        new_cost = get_plan_cost(cursor, sql=sql, hint=hint, explain=explain)
                        RM_sum_of_integ += new_cost
                
                RM_integral_list.append(RM_sum_of_integ)
            sensitive_rels = [i for i in copy_sensitive_rels]
            OLD_1_id = [i for i, x in enumerate(RM_card_slope_list) if x == min(RM_card_slope_list)]
            OLD_2_id = [i for i, x in enumerate(RM_sel_slope_list) if x == min(RM_sel_slope_list)]
            OLD_3_id = [i for i, x in enumerate(RM_integral_list) if x == min(RM_integral_list)]
            end = time.time()
            logging.info(f"Best plan by 2018: {OLD_1_id}, {OLD_2_id}, {OLD_3_id}, overhead {end - start}s")
            print("RQO: Finished test related work. Bye.")
            quit()

        ## ROBUST METRIC 1: exp penalty

        _start = time.time()
        
        joint_err_samples = gen_samples_from_joint_err_dist(args.sample, relations=sensitive_rels, random_seeds=True, naive=args.naive)

        logging.info(f"The number of samples to calculate expected penalty = {args.sample}.")
        exp_penalty_list, std_penalty_list, prob_of_penal = exp_penalty_by_samples(cur_plan_list, sensitive_rels, joint_err_samples, tolerance=tolerance, save_samples=True)
        
        robust_plan_id = [i for i, x in enumerate(exp_penalty_list) if x == min(exp_penalty_list)]
        _end = time.time()
        print(f"## RQO: Calculate expected penalty: {_end - _start}(s)")
        logging.info(f"### Best plan by exp penalty: {robust_plan_id}, overhead {_end - _start}s")
        logging.info(f"exp_penalty_w_tol: \t{[(id_, i_) for id_, i_ in enumerate(exp_penalty_list)]}")
        
        ## ROBUST METRIC 2: std penalty
        robust_plan_id = [i for i, x in enumerate(std_penalty_list) if x == min(std_penalty_list)]
        logging.info(f"### Best plan by std penalty: {robust_plan_id}, overhead {_end - _start}s")
        logging.info(f"std_penalty: \t{[(id_, i_) for id_, i_ in enumerate(std_penalty_list)]}")

        ## ROBUST METRIC 3: std penalty
        robust_plan_id = [i for i, x in enumerate(prob_of_penal) if x == min(prob_of_penal)]
        logging.info(f"### Best plan by prob of penalized: {robust_plan_id}, overhead {_end - _start}s")
        logging.info(f"std_penalty: \t{[(id_, i_) for id_, i_ in enumerate(prob_of_penal)]}")


        conn.close()


### Future Work: use a subset of query to generate several robust plans and cover the entire space
def pqo_query_subset(N=100):
    sql_template, literal_list = gen_sql_by_template(query_id, N)
    optimized_queries_dict = {}
    ### Use the original JOB as the first cached query
    optimized_queries_dict[0] = [[int(x) for x in est_card], [int(x) for x in raw_card], sql]

    ### For PQO: store the basic info of all queries that has optimized by RQO
    filename = f'reuse/{get_pure_q_id(query_id, db_name)}-optimized-queries-b{args.b}.json'
    
    if os.path.exists(filename):
        return    
    for sql_id, para_sql in enumerate(sql_template):
        ### Process new sql
        para_table_name_id_dict, para_join_maps, para_join_info, para_pair_rel_info = get_maps(db_name, para_sql, debug=args.debug)
        para_est_base_card, para_est_join_card_info = ori_cardest(db_name, para_sql)
        para_est_join_card = list(para_est_join_card_info[:, 2])
        para_est_card = para_est_base_card + para_est_join_card


        ### raw_join_card: number of rows of left_table * number of rows of right_table
        para_raw_join_card = [i[2] for i in para_join_info]
        para_raw_card = raw_base_card + para_raw_join_card

        
        ### Find the nearest sql by calculating KL
        nearest_id = -1
        min_kl = 1e6
        print(sql_id, para_sql)
        for q_id, optimized_query in enumerate(optimized_queries_dict.values()):
            kl_val = cal_kl(err_info_dict, optimized_query[0], optimized_query[1], 
                        err_info_dict, para_est_card, para_raw_card, 
                        dim=list(err_files_dict[get_pure_q_id(query_id, db_name)].keys()), N=1)
            

            if math.exp(kl_val)<1000:
                if kl_val < min_kl:
                    min_kl = kl_val
                    nearest_id = q_id
            print(math.exp(kl_val))

        if nearest_id == -1:
            optimized_queries_dict[len(optimized_queries_dict)] = [[int(x) for x in para_est_card], [int(x) for x in para_raw_card], para_sql]

    with open(filename, 'w') as file:
        json.dump(optimized_queries_dict, file, indent=4) 
    
    for q_id, optimized_query in enumerate(optimized_queries_dict.values()):
        print(optimized_query[2])
        with open(f'query/join-order-benchmark/{get_pure_q_id(query_id, db_name)}-{q_id}-b{args.b}.sql', 'w') as sql_file:
            sql_file.write(optimized_query[2])
    return


### Future work, PARQO's paper uses basic pqo only
def pqo(N=100):
    conn = psycopg2.connect(host="/tmp", dbname=db_name, user="hx68")
    conn.set_session(autocommit=True)
    cursor = conn.cursor()
    logging.basicConfig(filename='./log/' + ON_SAMPLE + db_name + '_' + query_id + '_pqo_' + str(tolerance) + cal_sen_method + '.log', level=logging.INFO)
    

    
    
    # Generate PQO queries
    sql_template, literal_list = gen_sql_by_template(query_id, N, db_name)
    
    
    result = []
    for sql_id, para_sql in enumerate(sql_template):
        logging.info(f"{sql_id}")
        logging.info(f"{para_sql}")

        # ### Check the cost and plan of ori sql and new sql (only check it but we don't care actually)
        # pg_result_ori = get_plan_cost_simple(cursor, sql=sql, explain=explain, debug=True)
        # pq_start = time.time()
        # pg_result_para = get_plan_cost_simple(cursor, sql=para_sql, explain=explain, debug=True)
        # pq_end = time.time()
        # print(f"PG result ori: {pg_result_ori}")
        # print(f"PG result new: {pg_result_para}")
        # if pg_result_ori[1] != pg_result_para[1] or pg_result_ori[2] != pg_result_para[2]:
        #     logging.info("Warning, pg default plan is diff from original query")
        # ### Check the cached plan's cost and how it looks like
        # for ii in plan_space:
        #     print(f"Our plan's cost: {get_plan_cost_simple(cursor, hint=cur_plan_list[ii], sql=para_sql, explain=explain, debug=True)}")
        

        ### Process new sql
        para_table_name_id_dict, para_join_maps, para_join_info, para_pair_rel_info = get_maps(db_name, para_sql, debug=args.debug)
        para_est_base_card, para_est_join_card_info = ori_cardest(db_name, para_sql)
        para_est_join_card = list(para_est_join_card_info[:, 2])
        para_est_card = para_est_base_card + para_est_join_card


        ### raw_join_card: number of rows of left_table * number of rows of right_table
        para_raw_join_card = [i[2] for i in para_join_info]
        para_raw_card = raw_base_card + para_raw_join_card
        
        
        ### Reuse the samples, and calculate the p_new/p_ori
        ### the samples are converted_dict.keys()
        cached_samples_dict_list = []
        cached_plan_dict_list = []
        filename = f'reuse/{get_pure_q_id(query_id, db_name)}-optimized-queries-b{args.b}.json'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                optimized_queries_dict = json.load(file)
            for i in range(len(optimized_queries_dict.values())):
                cached_samples_filename = f'reuse/{get_pure_q_id(query_id, db_name)}-{i}-b{args.b}.json'
                
                with open(cached_samples_filename, 'r') as file:
                    loaded_dict = json.load(file)
                converted_dict = {eval(key): value for key, value in loaded_dict.items()}
                cached_samples_dict_list.append(converted_dict)
                
                plan_file = f'./plan/{ON_SAMPLE}tmp_plan_dict_{db_name}_{get_pure_q_id(query_id, db_name)}-{i}{cal_sen_method}-b{args.b}.txt'
                plan_hint_dict = json.load(open(plan_file))
                cur_list = []
                for i in plan_hint_dict.values():
                    cur_list = cur_list + i
                cur_list = list(sorted(set(cur_list)))
                cached_plan_dict_list.append(cur_list)
        else:
            print("here", filename)
            input()
            cached_samples_filename = f'reuse/{query_id}.json'
            with open(cached_samples_filename, 'r') as file:
                loaded_dict = json.load(file)
            cached_samples_dict = {eval(key): value for key, value in loaded_dict.items()}

        ### Find the nearest rqo-ed query in the cached subset query
        ### Compute KL Divergence between the distributions
        ### Use same err_info_dict since the sql structure is the same
        start = time.time()
        if os.path.exists(filename):
            
            kl_val_list = [cal_kl(err_info_dict, cached_query[0], cached_query[1], 
                        err_info_dict, para_est_card, para_raw_card, 
                        dim=list(err_files_dict[get_pure_q_id(query_id, db_name)].keys()), N=1, debug=False) 
                        for cached_query in optimized_queries_dict.values()]
            nearest_query_id = [i for i, x in enumerate(kl_val_list) if x == min(kl_val_list)][0]
            kl_val = kl_val_list[nearest_query_id]

            cached_samples_dict = cached_samples_dict_list[nearest_query_id]
            plan_space = cached_rob_plan_dict[f"{get_pure_q_id(query_id, db_name)}-{nearest_query_id}-b{args.b}"]
            cur_plan_list = cached_plan_dict_list[nearest_query_id]
            assert kl_val == min(kl_val_list)
        else:
            kl_val = cal_kl(err_info_dict, est_card, raw_card, 
                            err_info_dict, para_est_card, para_raw_card, 
                            dim=list(err_files_dict[get_pure_q_id(query_id, db_name)].keys()), N=1, debug=False)
            plan_space = cached_rob_plan_dict[query_id]
            sensitive_rels = sorted(sen_dict[query_id])
            cur_plan_list = get_plan_list(sensitive_rels)
        
        
        print(f"--- PQO: Final KL divergence between old and new is: {kl_val}; {math.exp(kl_val)}")
        logging.info(f"--- PQO: Need {math.exp(kl_val)} samples to be accurate, We have {len(cached_samples_dict.keys())}")
        print(f'--- PQO: Current literal: {literal_list[sql_id]}')
        # input()
        end = time.time()
        print(f"--- PQO: Overhead to calculate KL: {end-start}(s)")

        if math.exp(kl_val)>1000:
            continue
        if len(plan_space) > 1:
            est_penalty_dict = {}
            
            ### Importance sampling: if p(x) is hard to sample, then 
            ### E(f(x)) = ∫(f(x)*p(x)) = 1/n SUM(f(x)*p(x)/q(x))
            ### p(x) is the new query (calculate by scoresample), q(x) is what we saved (read from json)
            start_2 = time.time()
            p_new_list = cal_prob_of_sample(cached_samples_dict.keys(), 
                                            sensitive_rels=list(err_files_dict[query_id].keys()), 
                                            est_card=para_est_card, raw_card=para_raw_card, 
                                            err_info_dict=err_info_dict)
            end = time.time()
            print(f"--- PQO: Overhead to calculate probability: {end-start_2}(s)")

            p_old_list = [cached_samples_dict[reuse_sample][0] for reuse_sample in cached_samples_dict.keys()]


            for id, reuse_sample in enumerate(cached_samples_dict.keys()): 
                p_new = p_new_list[id]
                p_old = p_old_list[id]
                
                for plan_id in plan_space:
                    est_penalty = (p_new / p_old) * cached_samples_dict[reuse_sample][plan_id+1]  ## plan_id+1 because the 1st in the list is probability
                    if plan_id not in est_penalty_dict:
                        est_penalty_dict[plan_id] = [est_penalty]
                    else:
                        est_penalty_dict[plan_id].append(est_penalty)
            print(f"--- PQO: Example, probability of sample: new is {p_new}, old is {p_old}")

            est_exp_penalty_list = []
            for i in est_penalty_dict.keys():
                est_exp_penalty_list.append(sum(est_penalty_dict[i])/len(est_penalty_dict[i]))
            end = time.time()
            print(f"--- PQO: Overhead of entire optimization: {end-start}(s)")
            # print(f"PG overhead: {pq_end-pq_start}(s)")
            # # input()
            # continue
            logging.info(est_exp_penalty_list)
            rob_plan_id = [plan_space[i] for i, x in enumerate(est_exp_penalty_list) if x == min(est_exp_penalty_list)][0]
        else:
            rob_plan_id = plan_space[0]
        print(f"--- PQO: {sql_id}: most robust plan is {rob_plan_id}, nearest query is {nearest_query_id}")

        pg_latency = round(get_real_latency(db_name, para_sql, hint=None, times=3, limit_time=1000000), 1)
        rob_latency = round(get_real_latency(db_name, para_sql, hint=cur_plan_list[rob_plan_id], times=3, limit_time=100000), 1)
        # test_latency = round(get_real_latency(db_name, para_sql, hint=cur_plan_list[plan_space[0]], times=3, limit_time=10000), 1)
        # test_latency_ = round(get_real_latency(db_name, para_sql, hint=cur_plan_list[plan_space[1]], times=3, limit_time=10000), 1)
        # test_latency__ = round(get_real_latency(db_name, para_sql, hint=cur_plan_list[plan_space[2]], times=3, limit_time=10000), 1)
        # logging.info(f"--- test latency is {test_latency}, {test_latency_}, {test_latency__}")
        
        logging.info(f"Nearest query is {nearest_query_id}")
        logging.info(f"Current Query: {literal_list[sql_id]}")
        logging.info(f"Robust plan is {rob_plan_id}: {rob_latency}")
        logging.info(f"Postgres plan: {pg_latency}")
        result.append((rob_latency, pg_latency))
    write_to_file(result, f'reuse/{db_name}/pqo-{query_id}-b{args.b}.txt')
    return

##### 6. PQO entrance #####
def basic_pqo(N=100):
    conn = psycopg2.connect(host="/tmp", dbname=db_name, user="hx68")
    conn.set_session(autocommit=True)
    cursor = conn.cursor()
    logging.basicConfig(filename='./log/' + ON_SAMPLE + db_name + '_' + query_id + '_pqo_' + str(tolerance) + '.log', level=logging.INFO)

    # ID of plans that we are going to use
    sensitive_rels = sorted(sen_dict[get_pure_q_id(query_id, db_name)])
    cur_plan_list = get_plan_list(sensitive_rels)
    
    if db_name == 'dsb':
        plan_space = cached_rob_plan_dict_dsb[query_id]
    elif db_name == 'stats':
        plan_space = cached_rob_plan_dict_stats[query_id]
    else:
        plan_space = cached_rob_plan_dict[query_id]
    
    # Generate PQO queries
    sql_template, literal_list = gen_sql_by_template(query_id, N, db_name)
    
    ### Reuse the samples, and calculate the p_new/p_ori
    ### the samples are converted_dict.keys()
    if db_name == 'imdbloadbase':
        with open(f'reuse/{query_id}.json', 'r') as file:
            loaded_dict = json.load(file)
    else:
        with open(f'reuse/{db_name}_{query_id}.json', 'r') as file:
            loaded_dict = json.load(file)
    converted_dict = {eval(key): value for key, value in loaded_dict.items()}
    
    result = []
    for sql_id, para_sql in enumerate(sql_template):
        logging.info(f"{sql_id}")
        logging.info(f"{para_sql}")
        ### Check the cost and plan of ori sql and new sql (only check it but we don't care actually)
        pg_result_ori = get_plan_cost_simple(cursor, sql=sql, explain=explain, debug=True)
        pq_start = time.time()
        pg_result_para = get_plan_cost_simple(cursor, sql=para_sql, explain=explain, debug=True)
        pq_end = time.time()
        print(f"PG result ori: {pg_result_ori}")
        print(f"PG result new: {pg_result_para}")
        if pg_result_ori[1] != pg_result_para[1] or pg_result_ori[2] != pg_result_para[2]:
            logging.info("Warning, pg default plan is diff from original query")
        ### Check the cached plan's cost and how it looks like
        for ii in plan_space:
            print(f"Our plan's cost: {get_plan_cost_simple(cursor, hint=cur_plan_list[ii], sql=para_sql, explain=explain, debug=True)}")
        
        ### Process new sql
        para_table_name_id_dict, para_join_maps, para_join_info, para_pair_rel_info = get_maps(db_name, para_sql, debug=args.debug)
        para_est_base_card, para_est_join_card_info = ori_cardest(db_name, para_sql)
        para_est_join_card = list(para_est_join_card_info[:, 2])
        para_est_card = para_est_base_card + para_est_join_card
        ### raw_join_card: number of rows of left_table * number of rows of right_table
        para_raw_join_card = [i[2] for i in para_join_info]
        para_raw_card = raw_base_card + para_raw_join_card
        

        ### Compute KL Divergence between the distributions
        ### Use same err_info_dict since the sql structure is the same
        start = time.time()
        kl_val = cal_kl(err_info_dict, est_card, raw_card, 
                        err_info_dict, para_est_card, para_raw_card, 
                        dim=list(err_files_dict[get_pure_q_id(query_id, db_name)].keys()), N=1)
        
        
        print(f"--- PQO: Final KL divergence between old and new is: {kl_val}; {math.exp(kl_val)}")
        logging.info(f"--- PQO: Need {math.exp(kl_val)} samples to be accurate, We have {len(converted_dict.keys())}")
        if literal_list:
            print(f'--- PQO: Current literal: {literal_list[sql_id]}')
        # input()
        end = time.time()
        print(f"--- PQO: Overhead to calculate KL: {end-start}(s)")
        if math.exp(kl_val)>200:
            continue
        if len(plan_space) > 1:
            est_penalty_dict = {}
            
            ### Importance sampling: if p(x) is hard to sample, then 
            ### E(f(x)) = ∫(f(x)*p(x)) = 1/n SUM(f(x)*p(x)/q(x))
            ### p(x) is the new query (calculate by scoresample), q(x) is what we saved (read from json)
            start_2 = time.time()
            p_new_list = cal_prob_of_sample(converted_dict.keys(), 
                                            sensitive_rels=list(err_files_dict[get_pure_q_id(query_id, db_name)].keys()), 
                                            est_card=para_est_card, raw_card=para_raw_card, 
                                            err_info_dict=err_info_dict)
            end = time.time()
            print(f"--- PQO: Overhead to calculate probability: {end-start_2}(s)")
            p_old_list = [converted_dict[reuse_sample][0] for reuse_sample in converted_dict.keys()]
            for id, reuse_sample in enumerate(converted_dict.keys()): 
                p_new = p_new_list[id]
                p_old = p_old_list[id]
                
                for plan_id in plan_space:
                    est_penalty = (p_new / p_old) * converted_dict[reuse_sample][plan_id+1]  ## plan_id+1 because the 1st in the list is probability
                    if plan_id not in est_penalty_dict:
                        est_penalty_dict[plan_id] = [est_penalty]
                    else:
                        est_penalty_dict[plan_id].append(est_penalty)
            print(f"--- PQO: Example, probability of sample: new is {p_new}, old is {p_old}")
            est_exp_penalty_list = []
            for i in est_penalty_dict.keys():
                est_exp_penalty_list.append(sum(est_penalty_dict[i])/len(est_penalty_dict[i]))
            end = time.time()
            print(f"--- PQO: Overhead of entire optimization: {end-start}(s)")
            print(f"PG overhead: {pq_end-pq_start}(s)")
            # # input()
            # continue
            logging.info(est_exp_penalty_list)
            rob_plan_id = [plan_space[i] for i, x in enumerate(est_exp_penalty_list) if x == min(est_exp_penalty_list)][0]
        else:
            rob_plan_id = plan_space[0]
        print(f"--- PQO: most robust plan is {rob_plan_id}")
        pg_latency = round(get_real_latency(db_name, para_sql, hint=None, times=5, limit_time=100000), 1)
        rob_latency = round(get_real_latency(db_name, para_sql, hint=cur_plan_list[rob_plan_id], times=5, limit_time=100000), 1)
        # test_latency = round(get_real_latency(db_name, para_sql, hint=cur_plan_list[plan_space[0]], times=3, limit_time=10000), 1)
        # test_latency_ = round(get_real_latency(db_name, para_sql, hint=cur_plan_list[plan_space[1]], times=3, limit_time=10000), 1)
        # test_latency__ = round(get_real_latency(db_name, para_sql, hint=cur_plan_list[plan_space[2]], times=3, limit_time=10000), 1)
        # logging.info(f"--- test latency is {test_latency}, {test_latency_}, {test_latency__}")
        
        if literal_list:
            logging.info(f"Current Query: {literal_list[sql_id]}")
        logging.info(f"Robust plan is {rob_plan_id}: {rob_latency}")
        logging.info(f"Postgres plan: {pg_latency}")
        result.append((rob_latency, pg_latency))
    write_to_file(result, f'reuse-test/pqo-{db_name}-{query_id}-b{args.b}.txt')
    return


if __name__ == "__main__":    
    np.random.seed(2023)
    if args.pqo:
        pqo_query_subset()
        # quit()
        basic_pqo()
        print(calculate_overall(f'reuse-test/pqo-{db_name}-{query_id}.txt'))
        # input()
    else:
       rqo()
