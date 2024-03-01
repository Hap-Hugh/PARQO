from tqdm import tqdm
import numpy as np
import math
import time
import multiprocessing
import matplotlib.pyplot as plt

def card(a):
    if int(a) == 0:
        return 1
    else:
        return int(a)

def list_multiply(a, b):
    assert len(a) == len(b), "Input lists have different length."
    result = []
    for i in range(len(a)):
        result.append(a[i] * b[i])
    return result


def tmpt(i, order):
    return ' (tmpt_' + str(i) + ' ' + order[i] + ') '

def tmpt_short(i, order):
    return ' tmpt_' + str(i) + ' ' + order[i]

def tmpt_card(join_list, rows):
    card_str = 'Rows('
    for i in range(len(join_list)):
        card_str = card_str + join_list[i]
    return card_str + ' #' + str(rows) + ')'


def join_hint(join_list, mtd=None):
    join_str =[]
    if mtd is None:
        join_str = '('
    else:
        try:
            join_str = mtd + '('
        except TypeError:
            print("HERE:", mtd)
            exit()
    for i in range(len(join_list)):
        join_str = join_str + join_list[i]
    return join_str + ')'


def clean(json_file, new_json_file, del_line_key=None):
    if del_line_key is None:
        del_line_key = ['QUERY PLAN', 'row)', '----']
    with open(json_file, 'r') as f:
        with open(new_json_file, 'w') as new_f:
            while True:

                line = f.readline()
                if not line:
                    break

                need_to_del = 0
                for i in del_line_key:
                    if i in line:
                        need_to_del = 1

                if need_to_del == 0:
                    line = line.replace('+', '')
                    line = line.strip() + '\n'

                new_f.write(line)
        new_f.close()
    f.close()


def get_cost_list(json_file, is_estimate=0):
    est_cost_list = []
    actual_cost_list = []
    with open(json_file, 'r') as f:
        new_query_flag = 0
        while True:
            line = f.readline()
            if not line:
                break
            # Beginning of the new query
            if line == '[\n':
                new_query_flag = 1
                continue
            # The total cost / actual cost is right after the beginning of 'plan'
            if new_query_flag == 1 and "Total Cost" in line:
                cost = line.split(':')[1].split(',')[0]
                if is_estimate:
                    new_query_flag = 0
                est_cost_list.append(float(cost))
                continue
            if new_query_flag == 1 and "Actual Total Time" in line:
                cost = line.split(':')[1].split(',')[0]
                new_query_flag = 0
                actual_cost_list.append(float(cost))
                continue
    return est_cost_list, actual_cost_list


def exp_sample_card(N, lower_bound, upper_bound, card=None):
    sample_list = []

    return sample_list


def evenly_sample_card(N, lower_bound, upper_bound, card=None):
    sample_list = np.arange(1, N)
    norm_list = (sample_list - np.min(sample_list)) / (np.max(sample_list) - np.min(sample_list))
    if lower_bound == 0 and upper_bound == 1:
        return norm_list
    else:
        return norm_list * (upper_bound - lower_bound) + lower_bound


def find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim, err_info_dict):
    r = 0
    if len(err_info_dict[cur_dim]) > 1:
        cur_err_hist = err_info_dict[cur_dim][1]
    else:
        # sometimes for table with no local selection conditions, we don't have error data on that one
        return -1
    
    for j in range(len(cur_err_hist)):
        if est_card[cur_dim] / (raw_card[cur_dim]+1) < cur_err_hist[j][0][0]:
            break
        r = j
    return r


def gen_center_from_err_dist(est_card, raw_card, cur_dim, err_info_dict, num_of_samples=1000, debug=False, naive=False):
    # np.random.seed(2023)
    center = []
    for table_id in cur_dim:
        if err_info_dict[table_id] == []:
            center.append(0)
        else:
            r = find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim=table_id, err_info_dict=err_info_dict)
            
            if r == -1: # this dimension doesn't have any error
                center.append(0)
            else:
                if debug:
                    print(f"Current dim {table_id}'s est sel: {est_card[table_id]/raw_card[table_id]}, bin id: {r}")
                pdf_of_err = err_info_dict[table_id][2][r]
                if naive:
                    err_sample = np.random.normal(loc=pdf_of_err[0], scale=pdf_of_err[1], size=num_of_samples)
                else:
                    err_sample = pdf_of_err.sample(num_of_samples)

                
                mean = sum(err_sample) / len(err_sample)
                if naive:
                    center.append(mean)
                else:
                    if debug: print("Mean Density:", mean[0])
                    center.append(mean[0])
    return center




def modify_query(a, b, query):
    CACHE = {
        'aka_name': 901343,
        'aka_title': 361472,
        'cast_info': 36244344,
        'char_name': 3140339,
        'comp_cast_type': 4,
        'company_name': 234997,
        'company_type': 4,
        'complete_cast': 135086,
        'info_type': 113,
        'keyword': 134170,
        'kind_type': 7,
        'link_type': 18,
        'movie_companies': 2609129,
        'movie_info': 14835720,
        'movie_info_idx': 1380035,
        'movie_keyword': 4523930,
        'movie_link': 29997,
        'name': 4167491,
        'person_info': 2963664,
        'role_type': 12,
        'title': 2528312,
    }
    table_names = list(CACHE.keys())
    for table_name in table_names:
        query = query.replace(' ' + table_name + ' AS', ' ' + a+table_name+b + ' AS')
    return query




def get_count(cursor_, table_name):
    query_ = f"select count(*) from {table_name};"
    cursor_.execute(query_)
    result = cursor_.fetchall()
    return result[0][0]



def generate_problem(num_vars):
    if num_vars < 1:
        raise ValueError("Number of variables must be greater than or equal to 1.")
    
    names = [f'x{i}' for i in range(0, num_vars)]
    bounds = [[-1, 1] for _ in range(num_vars)]

    problem = {
        'num_vars': num_vars,
        'names': names,
        'bounds': bounds
    }

    return problem


def top_n_of_2d_matrix(matrix, n, base_rel_num = 0):
    matrix_with_zeros = np.nan_to_num(matrix, nan=0.0)
    abs_matrix = np.abs(matrix_with_zeros)  # Take the absolute values of the matrix
    flat_abs_matrix = abs_matrix.ravel()  # Flatten the absolute matrix

    sorted_indices = np.argsort(flat_abs_matrix)[::-1]

    top_indices = sorted_indices[:n]
    x_indices, y_indices = np.unravel_index(top_indices, matrix.shape)

    result = ""
    for i in range(n):
        x, y = x_indices[i], y_indices[i]
        value = matrix[x, y]
        tmp = f"Max absolute value {i+1}: ({base_rel_num + x}, {base_rel_num + y}) - Value: {value}"
        print(tmp)
        result += tmp + "\n"
    return result


def cal_rel_error(true, est):
    if true > est:
        error = math.log(true / est)
    else:
        try:
            error = - math.log(est / true)
        except ValueError:
            print(est, true)
    return error


def cal_prob_of_sample(samples, sensitive_rels, est_card, raw_card, err_info_dict, is_error_sample=False, print_overhead=False):
    if is_error_sample: # the input is just a error sample (list of value) 
        err_sample = samples
        assert len(err_sample) == len(sensitive_rels)
        p = 1
        for i, sen_dim in enumerate(sensitive_rels):
            r = find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim=sen_dim, err_info_dict=err_info_dict)
            pdf_of_err = err_info_dict[sen_dim][2][r]
            p = p * np.exp(pdf_of_err.score_samples(np.array(err_sample)[i].reshape(1, -1)))
        return p[0]
    else:
        sel_samples = samples ## the input is a list of selectivity samples
        assert len(list(sel_samples)[0]) == len(est_card), f"{len(list(sel_samples)[0])}, {len(est_card)}"

     
        probability_list = []
        probability = [] ## a 2d array
        use_per_column_method = True
        if use_per_column_method:
            sel_samples = np.array(list(sel_samples))
            for i, sen_dim in enumerate(sensitive_rels):
                sel_list_of_this_dim = sel_samples[:, sen_dim]
                est_sel_of_this_dim =  est_card[sen_dim]/raw_card[sen_dim]
                err_list_of_this_dim = [[cal_rel_error(sel, est_sel_of_this_dim)] for sel in sel_list_of_this_dim]
                r = find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim=sen_dim, err_info_dict=err_info_dict)
                pdf_of_err = err_info_dict[sen_dim][2][r]
                
                p_list_of_this_dim = np.exp(pdf_of_err.score_samples(np.array(err_list_of_this_dim)))
                
                probability.append(p_list_of_this_dim)
            
            num_of_sample = len(list(samples))
            probability_list = [np.prod([row[i] for row in probability]) for i in range(num_of_sample)]

            return probability_list
        else:
            pdf_list = []
            
            for i, sen_dim in enumerate(sensitive_rels):
                r = find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim=sen_dim, err_info_dict=err_info_dict)
                pdf_of_err = err_info_dict[sen_dim][2][r]
                pdf_list.append(pdf_of_err)   
            for sel_sample in sel_samples:
                
                p = 1
                start = time.time()

                for i, sen_dim in enumerate(sensitive_rels):
                    err_of_this_dim = cal_rel_error(sel_sample[sen_dim], est_card[sen_dim]/raw_card[sen_dim])
                    p = p * np.exp(pdf_list[i].score_samples(np.array(err_of_this_dim).reshape(1, -1)))
                end = time.time()
                
                probability_list.append(p[0])
            if print_overhead:
                print(f"-- Overhead of calculate the probability of one sample: {end-start}(s)")         
            return probability_list
        

def parrallel_score_samples(kde, samples, thread_count=int(0.875 * multiprocessing.cpu_count())):
    with multiprocessing.Pool(thread_count) as p:
        return np.concatenate(p.map(kde.score_samples, np.array_split(samples, thread_count)))


def calculate_overall(file_path):
    total_sum = 0
    total_a = 0
    total_b = 0 # postgres
    rob_is_better_count = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        template_size = len(lines)
        for line in lines:
            a, b = map(float, line.strip('()\n').split(','))
            if a < b:
                rob_is_better_count += 1
            total_sum += (a - b)
            total_a += a
            total_b += b
    print(total_a / template_size)
    print(total_b / template_size)
    if total_a > total_b:
        print(- total_a / total_b + 1)
    else:
        print(total_b / total_a - 1)
    print(f"In {rob_is_better_count} cases, our robust plan is better.")
    return total_sum, template_size



def plot_pqo_latency_cdf(file_path, name):
    with open(file_path, 'r') as file:
        data = file.readlines()
    column1 = []
    column2 = []
    for line in data:
        values = line.strip().split(',')
        column1.append(float(values[0][1:]))  
        column2.append(float(values[1][:-1]))
    column1.sort()
    column2.sort()
    cdf_column1 = np.arange(1, len(column1) + 1) / len(column1)
    cdf_column2 = np.arange(1, len(column2) + 1) / len(column2)

    # Plot the CDFs
    plt.plot(column1, cdf_column1, label='Cached PARQO\'s Plan', linewidth=2, color='blue')
    plt.plot(column2, cdf_column2, label='PostgreSQL Plan', linewidth=2, color='orange' )
    plt.xlabel('Execution Time [in ms]', fontsize=18)
    plt.ylabel('Cumulative Probability', fontsize=18)
    plt.title(f'CDF of Execution Time (Q{name})', fontsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.tick_params(axis='x', labelsize=15)
    plt.legend(fontsize=20) 
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./latency-cdf/q'+ name + '-latency-cdf.pdf')
    plt.close()