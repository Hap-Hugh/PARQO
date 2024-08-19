import os
from prep_cardinality import *
import numpy as np
import psycopg2
from postgres import *

CACHE_FOREIGN_KEY_CONSTRAINT = [
['t', 'at'],
['t', 'ml'],
['t', 'ci'],
['t', 'kt'],
['t', 'mi'],
['t', 'mi_idx'],
['t', 'mk'],
['t', 'mc'],
['t', 'cc'],
['ci', 'cn'],
['ci', 'rt'],
['ci', 'an'],
['ml', 'lt'],
['cct', 'cc'],
['n', 'pi'],
['an', 'n'],
['pi', 'it'],
['mi', 'it'],
['mc', 'ct'],
['mc', 'cn'],
['mk', 'k'],
['it', 'miidx'],
]


def get_sensitive_edge(db_name, sql):
    sen_id = []
    os.system("rm ~/imdb/single_tbl_est_record.txt")
    os.system("rm ~/imdb/join_est_record_job.txt")

    conn = psycopg2.connect(host="/tmp", dbname=db_name, user="hx68")
    conn.set_session(autocommit=True)
    cursor = conn.cursor()
    cursor.execute('SET enable_material = off')
    # cursor.execute('SET top_n = 0')
    cursor.execute("SET print_single_tbl_queries=true;")
    cursor.execute("SET print_sub_queries=true;")
    cursor.execute("SET ml_cardest_enabled=false;")
    cursor.execute("SET ml_joinest_enabled=false;")
    cursor.execute(sql)

    with open('/winhomes/hx68/imdb/join_est_record_job.txt') as f:
        join = f.readlines()
    id = -1
    rel_1 = ""
    rel_2 = ""
    for line_id in range(len(join)):
        if "query:" in join[line_id]:
            if id == -1:
                id = int(join[line_id].split(": ")[1])
        if "RELOPTINFO" in join[line_id]:
            if rel_1 == "":
                rel_1 = join[line_id].split('(')[1].split(')')[0].split(' ')  # rel_1 is just a table
                continue
            if rel_1 != "" and rel_2 == "":
                rel_2 = join[line_id].split('(')[1].split(')')[0].split(' ')  # rel_2 could be a list
        if id != -1 and rel_1 != "" and rel_2 != "":
            # now we have 5: k, cn mc mk
            # record those m:n relation, which means 1 and 2 don't show in foreign key together
            flag = 0
            for cons in CACHE_FOREIGN_KEY_CONSTRAINT:
                if rel_1[0] not in cons or not any_t_in_c(rel_2, cons):
                    continue
                else:
                    flag = 1
            if flag == 0:
                sen_id.append(id)
            id = -1
            rel_1 = ""
            rel_2 = ""
    print(sen_id)
    return sen_id



def any_t_in_c(table_list, constraint):
    for t in table_list:
        if t in constraint:
            return True
    return False


def slope_RM(cursor, sql, hint, explain, t_list,
            est_base_card, raw_base_card, f_base_card, 
            est_join_card, raw_join_card, f_join_card,
            sel):

    num_of_base_rel = len(est_base_card)
    num_of_join_rel = len(est_join_card)
    
    robustness = 0.0
    # TODO: outdated
    for t_id in t_list:
        base_output_sel = [est_base_card[i]/raw_base_card[i] for i in range(num_of_base_rel)]
        join_output_sel = [est_join_card[i]/raw_join_card[i] for i in range(num_of_join_rel)]
        write_to_file(base_output_sel, f_base_card)
        os.system(" > ~/robust-vcm/cardinality/pointers.txt")
        write_to_file(join_output_sel, f_join_card)
        ori_cost = get_plan_cost(cursor, sql=sql, hint=hint, explain=explain)
        
        if t_id >= num_of_base_rel:
            i = t_id - num_of_base_rel
            if sel: # use selectivity delta
                join_output_sel[i] *= 1.05
            else:   # use cardinality slope metric, delta = 1
                join_output_sel[i] += 1 / raw_join_card[i]
        else:
            i = t_id
            if sel: # use selectivity delta
                base_output_sel[i] *= 1.05
            else:   # use cardinality slope metric, delta = 1
                base_output_sel[i] += 1 / raw_join_card[i]
        write_to_file(base_output_sel, f_base_card)
        write_pointers_to_file([t_id])
        write_to_file(join_output_sel, f_join_card)
        new_cost = get_plan_cost(cursor, sql=sql, hint=hint, explain=explain)
        slope = new_cost - ori_cost
        # print(new_cost, ori_cost)
        print(f"{t_id}: {slope}")
        robustness += slope
    input()
    # for safe
    write_to_file([est_base_card[i]/raw_base_card[i] for i in range(num_of_base_rel)], f_base_card)
    write_to_file([est_join_card[i]/raw_join_card[i] for i in range(num_of_join_rel)], f_join_card) 
    print(round(robustness, 3))
    return robustness

# The third metric we use 

