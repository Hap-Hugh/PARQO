from utility import card
import os
import numpy as np
import psycopg2
from postgres import *


def write_to_file(cardinality, file_tobe_sent_to_psql):
    output_card_list = [str(line) for line in cardinality]
    with open(file_tobe_sent_to_psql, 'w') as fp:
        fp.write('\n'.join(output_card_list))
    return


### Send the id of relations to postgres, then postgres will know which
### selectivity is going to read from file. sen_rel_list is like [2, 3, 5]
def write_pointers_to_file(sen_rel_list):
    output_list = [str(line) for line in sen_rel_list]
    with open("./cardinality/pointers.txt", 'w') as fp:
        fp.write('\n'.join(output_list))
    os.system("cp ~/robust-vcm/cardinality/pointers.txt ~/imdb/")
    return




### 3 basic experiments: using all rels; all basic rels; all join rels
def prep_basic_sensitive_rel_id(num_of_base_rel, num_of_join_rel):
    a1 = []
    for i in range(0, num_of_base_rel + num_of_join_rel):
        a1.append(i)
    a2 = []
    for i in range(0, num_of_base_rel):
        a2.append(i)
    a3 = []
    for i in range(num_of_base_rel, num_of_base_rel + num_of_join_rel):
        a3.append(i)
    return a1, a2, a3


'''
Generate the raw size of each table by checking the dict with the table name as the key.
'''
def get_raw_table_size(sql, ins_id=None, db_name='imdbloadbase', output_file=None):
    raw_size_list = get_raw_size_from_txt()
    if output_file:
        raw_size_list = [str(i) for i in raw_size_list]
        with open(output_file, 'w') as fp:
            fp.write('\n'.join(raw_size_list))
    return raw_size_list


'''
Instead of reading estimated cardinality from file, generate the list by
execute the sql and read the result from xxx.txt which is output by psql
'''
def ori_cardest(db_name, sql):
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
    cursor.execute("Explain " + sql)
    

    with open('/winhomes/hx68/imdb/single_tbl_est_record.txt') as f:
        single = f.readlines()
    estimate_single = []
    for line in single:
        if 'rows=' in line:
            l = line.split('rows=')[1].split('width')[0].strip()
            estimate_single.append(int(l))
    
    with open('/winhomes/hx68/imdb/join_est_record_job.txt') as f:
        join = f.readlines()
    estimate_join = [] # all info for join_rel, contains: leftrows, rightrows, estjoinrows

    flag = 0
    for line_id in range(len(join)):
        info_for_join_rel = [] # leftrows, rightrows, estjoinrows
        if line_id < flag:
            continue
        if "RELOPTINFO" in join[line_id]:
            left_name = join[line_id].split('(')[1].split(')')[0].split(' ') # [cn, mc]
            left_rows = join[line_id].split('rows=')[1].split(' ')[0]
            for right_rel_line_id in range(line_id+1, len(join)):
                if "RELOPTINFO" in join[right_rel_line_id]:
                    right_name = join[right_rel_line_id].split('(')[1].split(')')[0].split(' ') # [mk, t]
                    right_rows = join[right_rel_line_id].split('rows=')[1].split(' ')[0]
                    for estimates_line_id in range(right_rel_line_id+1, len(join)):
                        if 'Estimated Rows' in join[estimates_line_id]:
                            l = join[estimates_line_id].split(':')[1].strip()

                            info_for_join_rel = [int(left_rows), int(right_rows), max(1, round(float(l)))]  # leftrows, rightrows, estjoinrows
                            estimate_join.append(info_for_join_rel)
                            flag = estimates_line_id
                            break
                    break
    
    conn.close()
    return estimate_single, np.array(estimate_join)


def get_maps(db_name, sql, debug=False):
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
    cursor.execute("EXPLAIN " + sql)

    with open('/winhomes/hx68/imdb/single_tbl_est_record.txt') as f:
        single = f.readlines()
    estimate_single = []
    tname_id_dict = {}
    count = 0
    for line in single:
        if 'rows=' in line:
            tname = line.split('(')[1].split(')')[0].split(' ')[0]
            l = line.split('rows=')[1].split('width')[0].strip()
            estimate_single.append(int(l))
            if tname in tname_id_dict.keys():
                continue
            tname_id_dict[tname] = count
            count += 1
    single_table_num = len(estimate_single)
    print(tname_id_dict)
    maps = [[-1] * single_table_num for _ in range(single_table_num)]


    with open('/winhomes/hx68/imdb/join_est_record_job.txt') as f:
        join = f.readlines()
    join_relation_list = []
    join_relation_counter = 0
    pair_relation_list = []


    estimate_join = [] # all info for join_rel, contains: leftrows, rightrows, estjoinrows

    flag = 0
    for line_id in range(len(join)):
        info_for_join_rel = [] # leftrows, rightrows, estjoinrows
        if line_id < flag:
            continue
        if "RELOPTINFO" in join[line_id]:
            left_name = join[line_id].split('(')[1].split(')')[0].split(' ')[0] # [cn, mc]
            left_rows = join[line_id].split('rows=')[1].split(' ')[0]
            for right_rel_line_id in range(line_id+1, len(join)):
                if "RELOPTINFO" in join[right_rel_line_id]:
                    right_name = join[right_rel_line_id].split('(')[1].split(')')[0].split(' ') # [mk, t]
                    right_rows = join[right_rel_line_id].split('rows=')[1].split(' ')[0]
                    for estimates_line_id in range(right_rel_line_id+1, len(join)):
                        if 'Estimated Rows' in join[estimates_line_id]:
                            l = join[estimates_line_id].split(':')[1].strip()
                            info_for_join_rel = [int(left_rows), int(right_rows), round(float(l))]  # leftrows, rightrows, estjoinrows
                            estimate_join.append(info_for_join_rel)
                            flag = estimates_line_id


                            # use id to represent the join relation
                            left_id_list = [tname_id_dict[left_name]]
                            right_id_list = [tname_id_dict[i] for i in right_name]
                            # print(left_id_list)
                            # print(right_id_list)
                            join_relation_list.append([left_id_list, right_id_list, int(left_rows) * int(right_rows)])

                            if len(right_name) == 1:
                                right_name = right_name[0]
                                pair_relation_list.append((left_name, right_name))
                                maps[tname_id_dict[right_name]][tname_id_dict[left_name]] = join_relation_counter
                                maps[tname_id_dict[left_name]][tname_id_dict[right_name]] = join_relation_counter
                                join_relation_counter += 1

                            break
                    break
    if debug:
        for i in maps:
            print(i)
        # maps is a 2-d structure to record which two tables can be joined together
        
        print(pair_relation_list)
        # pair_relation_list contains all of the edges (pair of two single tables) in the join graph
        # e.g.: [('mc', 'ci'), ('mk', 'ci'), ('n', 'ci'), ('t', 'ci'), ('mc', 'cn'), ('mk', 'k'), ('mk', 'mc'), ('t', 'mc'), ('t', 'mk')]
        
        print(join_relation_list)
        # join_relation_list: left relation, right relation, raw card (row(left) * row(right)); 
        # e.g.: [6], [0, 1, 3], 4874964462720
    
    return tname_id_dict, maps, join_relation_list, pair_relation_list
