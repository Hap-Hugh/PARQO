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
def get_raw_table_size(sql, ins_id=None, output_file=None):
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
    
    CACHE_sampled = {'sampled_title_4': 505663, 
            'sampled_movie_companies_4': 457005, 
            'sampled_movie_keyword_4': 951732, 
            'sampled_cast_info_4': 7357520, 
            'sampled_movie_link_4': 5192, 
            'sampled_movie_info_4': 2776549, 
            'sampled_complete_cast_4': 16307, 
            'sampled_aka_title_4': 43703, 
            'sampled_movie_info_idx_4': 312978, 
            'sampled_keyword_4': 67013, 
            'sampled_company_name_4': 69212, 
            'sampled_aka_name_4': 267920, 
            'sampled_name_4': 267920, 
            'sampled_person_info_4': 555764, 
            'sampled_link_type_4': 16, 
            'sampled_info_type_4': 92, 
            'sampled_company_type_4': 2, 
            'sampled_kind_type_4': 6, 
            'sampled_char_name_4': 673815, 
            'sampled_role_type_4': 11, 
            'sampled_comp_cast_type_4': 4
        }
        
    CACHE_random = {"random_title_4": 506115,
            "random_movie_companies_4": 520016,
            "random_movie_keyword_4": 898705,
            "random_cast_info_4": 7241864,
            "random_movie_link_4": 6039,
            "random_movie_info_4": 2962516,
            "random_complete_cast_4": 26967,
            "random_aka_title_4": 71930,
            "random_movie_info_idx_4": 275646,
            "random_keyword_4": 70464,
            "random_company_name_4": 89745,
            "random_aka_name_4": 349953,
            "random_name_4": 349953,
            "random_person_info_4": 715037,
            "random_link_type_4": 16,
            "random_info_type_4": 95,
            "random_company_type_4": 2,
            "random_kind_type_4": 6,
            "random_char_name_4": 889769,
            "random_role_type_4": 11,
            "random_comp_cast_type_4": 4,
        }
    # cat_7
    CACHE_list = [
    # cat_1
            {"cat_title_1": 662825,
            "cat_movie_companies_1": 1307690,
            "cat_movie_keyword_1": 2886675,
            "cat_cast_info_1": 10396795,
            "cat_movie_link_1": 0,
            "cat_movie_info_1": 8301049,
            "cat_complete_cast_1": 59753,
            "cat_aka_title_1": 293190,
            "cat_movie_info_idx_1": 629900,
            "cat_keyword_1": 111444,
            "cat_company_name_1": 188439,
            "cat_aka_name_1": 636922,
            "cat_name_1": 636922,
            "cat_person_info_1": 747759,
            "cat_link_type_1": 0,
            "cat_info_type_1": 95,
            "cat_company_type_1": 2,
            "cat_kind_type_1": 1,
            "cat_char_name_1": 1698948,
            "cat_role_type_1": 11,
            "cat_comp_cast_type_1": 4,},

            {"cat_title_2": 90852,                                                                                                                                                                                                                                   
            "cat_movie_companies_2": 194257,                                                                                                                                                                                                                        
            "cat_movie_keyword_2": 183129,                                                                                                                                                                                                                          
            "cat_cast_info_2": 889397,                                                                                                                                                                                                                              
            "cat_movie_link_2": 12360,                                                                                                                                                                                                                              
            "cat_movie_info_2": 769577,                                                                                                                                                                                                                             
            "cat_complete_cast_2": 2784,                                                                                                                                                                                                                            
            "cat_aka_title_2": 20313,                                                                                                                                                                                                                               
            "cat_movie_info_idx_2": 113058,                                                                                                                                                                                                                         
            "cat_keyword_2": 24656,                                                                                                                                                                                                                                 
            "cat_company_name_2": 31166,                                                                                                                                                                                                                            
            "cat_aka_name_2": 86924,                                                                                                                                                                                                                                
            "cat_name_2": 86924,                                                                                                                                                                                                                                    
            "cat_person_info_2": 362877,                                                                                                                                                                                                                            
            "cat_link_type_2": 16,                                                                                                                                                                                                                                  
            "cat_info_type_2": 92,                                                                                                                                                                                                                                  
            "cat_company_type_2": 2,                                                                                                                                                                                                                                
            "cat_kind_type_2": 1,                                                                                                                                                                                                                                   
            "cat_char_name_2": 163962,                                                                                                                                                                                                                              
            "cat_role_type_2": 11,                                                                                                                                                                                                                                  
            "cat_comp_cast_type_2": 4},


            {                                                                                                                                                                                               
            "cat_title_3": 100537,                                                                                                                                                                                                                                  
            "cat_movie_companies_3": 200368,                                                                                                                                                                                                                        
            "cat_movie_keyword_3": 250907,                                                                                                                                                                                                                          
            "cat_cast_info_3": 1949617,                                                                                                                                                                                                                             
            "cat_movie_link_3": 0,                                                                                                                                                                                                                                  
            "cat_movie_info_3": 803708,
            "cat_complete_cast_3": 7793,
            "cat_aka_title_3": 26938,
            "cat_movie_info_idx_3": 111147,
            "cat_keyword_3": 33954,
            "cat_company_name_3": 28005,
            "cat_aka_name_3": 150085,
            "cat_name_3": 150085,
            "cat_person_info_3": 526111,
            "cat_link_type_3": 0,
            "cat_info_type_3": 92,
            "cat_company_type_3": 2,
            "cat_kind_type_3": 1,
            "cat_char_name_3": 370299,
            "cat_role_type_3": 11,
            "cat_comp_cast_type_3": 4},

            {"cat_title_4": 118234,                                                                                                                                                                                                                                  
            "cat_movie_companies_4": 159504,                                                                                                                                                                                                                        
            "cat_movie_keyword_4": 472540,                                                                                                                                                                                                                          
            "cat_cast_info_4": 1378081,                                                                                                                                                                                                                             
            "cat_movie_link_4": 0,                                                                                                                                                                                                                                  
            "cat_movie_info_4": 882915,                                                                                                                                                                                                                             
            "cat_complete_cast_4": 3063,                                                                                                                                                                                                                            
            "cat_aka_title_4": 13497,                                                                                                                                                                                                                               
            "cat_movie_info_idx_4": 83550,
            "cat_keyword_4": 26897,
            "cat_company_name_4": 27477,
            "cat_aka_name_4": 106038,
            "cat_name_4": 106038,
            "cat_person_info_4": 337584,
            "cat_link_type_4": 0,
            "cat_info_type_4": 93,
            "cat_company_type_4": 2,
            "cat_kind_type_4": 1,
            "cat_char_name_4": 132278,
            "cat_role_type_4": 11,
            "cat_comp_cast_type_4": 4,
            },

            {"cat_title_5": 0,                                                                                                                                                                                                                                       
            "cat_movie_companies_5": 0,
            "cat_movie_keyword_5": 0,
            "cat_cast_info_5": 0,
            "cat_movie_link_5": 0,
            "cat_movie_info_5": 0,
            "cat_complete_cast_5": 0,
            "cat_aka_title_5": 0,
            "cat_movie_info_idx_5": 0,
            "cat_keyword_5": 0,
            "cat_company_name_5": 0,
            "cat_aka_name_5": 0,
            "cat_name_5": 0,
            "cat_person_info_5": 0,
            "cat_link_type_5": 0,
            "cat_info_type_5": 0,
            "cat_company_type_5": 0,
            "cat_kind_type_5": 0,
            "cat_char_name_5": 0,
            "cat_role_type_5": 0,
            "cat_comp_cast_type_5": 0,
            },
            {
            "cat_title_6": 12600,                                                                                                                                                                                                                                   
            "cat_movie_companies_6": 30002,                                                                                                                                                                                                                         
            "cat_movie_keyword_6": 85218,                                                                                                                                                                                                                           
            "cat_cast_info_6": 210569,                                                                                                                                                                                                                              
            "cat_movie_link_6": 0,                                                                                                                                                                                                                                  
            "cat_movie_info_6": 115135,                                                                                                                                                                                                                             
            "cat_complete_cast_6": 65,                                                                                                                                                                                                                              
            "cat_aka_title_6": 4565,                                                                                                                                                                                                                                
            "cat_movie_info_idx_6": 16662,                                                                                                                                                                                                                          
            "cat_keyword_6": 11909,                                                                                                                                                                                                                                 
            "cat_company_name_6": 4506,                                                                                                                                                                                                                             
            "cat_aka_name_6": 11555,                                                                                                                                                                                                                                
            "cat_name_6": 11555,                                                                                                                                                                                                                                    
            "cat_person_info_6": 77766,                                                                                                                                                                                                                             
            "cat_link_type_6": 0,
            "cat_info_type_6": 53,
            "cat_company_type_6": 2,
            "cat_kind_type_6": 1,
            "cat_char_name_6": 41077,
            "cat_role_type_6": 11,
            "cat_comp_cast_type_6": 3,
            },
            {"cat_title_7": 1543264,
            "cat_movie_companies_7": 717308,
            "cat_movie_keyword_7": 645461,
            "cat_cast_info_7": 21419885,
            "cat_movie_link_7": 17637,
            "cat_movie_info_7": 3963336,
            "cat_complete_cast_7": 61628,
            "cat_aka_title_7": 2876,
            "cat_movie_info_idx_7": 425718,
            "cat_keyword_7": 64727,
            "cat_company_name_7": 12428,
            "cat_aka_name_7": 289570,
            "cat_name_7": 289570,
            "cat_person_info_7": 643878,
            "cat_link_type_7": 15,
            "cat_info_type_7": 57,
            "cat_company_type_7": 2,
            "cat_kind_type_7": 1,
            "cat_char_name_7": 1184657,
            "cat_role_type_7": 11,
            "cat_comp_cast_type_7": 4,},
            ]
    
    alias_list = sql.split('FROM')[1].split('WHERE')[0].strip().split('\n')
    raw_size_list = []
    
    
    for i in alias_list:
        key = i.split('AS')[0].strip()
        if ins_id == None: # original
            raw_size_list.append(CACHE[key])
        elif ins_id > 0:
            raw_size_list.append(CACHE_list[ins_id-1][key])
        elif ins_id == 0: # random
            raw_size_list.append(CACHE_random[key])
        elif ins_id == -1: # sampled
            raw_size_list.append(CACHE_sampled[key])
        
    
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
    cursor.execute('SET top_n = 0')
    cursor.execute("SET print_single_tbl_queries=true;")
    cursor.execute("SET print_sub_queries=true;")
    cursor.execute("SET ml_cardest_enabled=false;")
    cursor.execute("SET ml_joinest_enabled=false;")
    cursor.execute(sql)
    

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
    cursor.execute('SET top_n = 0')
    cursor.execute("SET print_single_tbl_queries=true;")
    cursor.execute("SET print_sub_queries=true;")
    cursor.execute("SET ml_cardest_enabled=false;")
    cursor.execute("SET ml_joinest_enabled=false;")
    cursor.execute(sql)

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
