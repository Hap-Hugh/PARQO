from prep_cardinality import *
import math

def prep_sel(table_name_id_dict, join_maps, join_info,
            est_base_sel, f_base_sel, 
            est_join_sel, f_join_sel, 
            error, relation_list, recentered_error=None, rela_error=True, debug=False):
    assert len(error) == len(relation_list)
    num_of_base_rel = len(est_base_sel)

    num_of_edges = int((len(join_maps) * len(join_maps) - count_neg_one(join_maps)) * 0.5)
    base_output_sel = []
    join_output_sel = []
    changed_relation_list = []
    
    for i in est_base_sel:
        base_output_sel.append(i)
    for i in est_join_sel:
        join_output_sel.append(i)
    
    
    for i in range(len(relation_list)):
        assert relation_list[i] < num_of_base_rel + num_of_edges
        table_id = relation_list[i]
        cur_error = error[i]
        if table_id < num_of_base_rel:
            new_sel = cal_new_sel_by_err(cur_error, est_base_sel[table_id], rela_error)
            base_output_sel[table_id] = new_sel
        else:   
            new_sel = cal_new_sel_by_err(cur_error, est_join_sel[table_id - num_of_base_rel], rela_error)
            join_output_sel[table_id - num_of_base_rel] = new_sel

    

    sensitive_list = relation_list.copy()
    if recentered_error:
        for table_id in range(len(recentered_error)):
            if recentered_error[table_id] == 0:
                continue
            if table_id in relation_list: ### that value is already been corrected by sampled error
                continue
            sensitive_list.append(table_id)
            if table_id < num_of_base_rel:
                new_sel = cal_new_sel_by_err(recentered_error[table_id], est_base_sel[table_id], rela_error)
                base_output_sel[table_id] = new_sel
            else:
                new_sel = cal_new_sel_by_err(recentered_error[table_id], est_join_sel[table_id - num_of_base_rel], rela_error)
                join_output_sel[table_id - num_of_base_rel] = new_sel

    
    for i in range(num_of_edges, len(join_output_sel)):
        parameter_info = join_info[i]
        right_tables = parameter_info[1]
        left_table = parameter_info[0][0]

        no_sensitive_flag = 1
        for r_t in right_tables:
            for sen_dim in sensitive_list:
                # print(join_maps[left_table][r_t], sen_dim - num_of_base_rel)
                if join_maps[left_table][r_t] == sen_dim - num_of_base_rel:
                    no_sensitive_flag = 0
        if no_sensitive_flag:
            continue




        new_sel = 1
        tables_w_join_condition = []
        for r_t in right_tables:
            if join_maps[left_table][r_t] != -1: # there is a edge
                tables_w_join_condition.append(r_t)

        
        USE_AVG_OF_ALL_POSSIBLE_EDGES = False
        if USE_AVG_OF_ALL_POSSIBLE_EDGES:
            sel_list = []
            for t in tables_w_join_condition:
                edge_id = join_maps[left_table][t]
                new_sel_i = new_sel * join_output_sel[edge_id]
                sel_list.append(new_sel_i)
            new_sel = sum(sel_list) / len(sel_list)
            changed_relation_list.append(i + num_of_base_rel)
        else:
            for t in tables_w_join_condition:
                edge_id = join_maps[left_table][t]
                new_sel = new_sel * join_output_sel[edge_id]
                changed_relation_list.append(i + num_of_base_rel)
                break

        join_output_sel[i] = new_sel
    

    changed_relation_list = sensitive_list + changed_relation_list

    write_to_file(base_output_sel, f_base_sel)
    write_pointers_to_file(changed_relation_list)
    write_to_file(join_output_sel, f_join_sel)
    return base_output_sel, join_output_sel


def count_neg_one(two_d_list):
    count = 0

    for sublist in two_d_list:
        for element in sublist:
            if element == -1:
                count += 1

    return count

def cal_new_sel_by_err(cur_error, ori_sel, rela_error=True):
    if not rela_error:
        return cur_error + ori_sel
    if cur_error > 0:
        new_sel = ori_sel * math.exp(cur_error)
    else:
        new_sel = ori_sel / math.exp(-cur_error)
    new_sel = min(new_sel, 1.0)
    new_sel = max(new_sel, 0.0)
    return new_sel