from prep_cardinality import *
import math

# given a relation_list and error_list, on base_rel or join_rel
# calcualte the new card and write the file to postgres
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
    
    
    ### According to sensitive dimensions list, apply the error and correct the selectivity as output
    for i in range(len(relation_list)):
        # assert relation_list[i] < num_of_base_rel + num_of_edges
        table_id = relation_list[i]
        cur_error = error[i]
        if table_id < num_of_base_rel:
            new_sel = cal_new_sel_by_err(cur_error, est_base_sel[table_id], rela_error)
            base_output_sel[table_id] = new_sel
        else:   
            new_sel = cal_new_sel_by_err(cur_error, est_join_sel[table_id - num_of_base_rel], rela_error)
            join_output_sel[table_id - num_of_base_rel] = new_sel
        # print(table_id, cur_error, new_sel)
        # input()
    
    
    ### 1. If we recentered the selectivity, we should keep those recentered value when it's not sensitive dimensions
    ### 2. For those dimensions that are sensitive dimensions, just use the sampled error to calculate the new_sel
    ### For 1, think about this example: d12 has huge err, but you recentered it and d12 is not sensitive, so your
    ### sample from err distribution will not consider d12; the following will be wrong
    sensitive_list = relation_list.copy()
    if recentered_error:
        for table_id in range(len(recentered_error)):
            if recentered_error[table_id] == 0:
                continue
            if table_id in relation_list: ### that value is already been corrected by sampled error
                continue
            ### if you changed one dim, then this dim should be considered when calculate the selectivity ofcomplex relation
            sensitive_list.append(table_id)
            if table_id < num_of_base_rel:
                new_sel = cal_new_sel_by_err(recentered_error[table_id], est_base_sel[table_id], rela_error)
                base_output_sel[table_id] = new_sel
            else:
                new_sel = cal_new_sel_by_err(recentered_error[table_id], est_join_sel[table_id - num_of_base_rel], rela_error)
                join_output_sel[table_id - num_of_base_rel] = new_sel

    # print("New sensitive list: " ,sensitive_list)
    # input()

    # join_output_sel[0:num_of_edges] = [0.00000349804, 0.00000562709, 0.00000042599195, 0.00000150869, 0.00000581531, 0.00705309742, 0.00000793425, 0.00000150869, 0.00000150869]

    for i in range(num_of_edges, len(join_output_sel)):
        # print(i, join_info[i])
        parameter_info = join_info[i]
        ### First, get the left table and right tables. Note the left table is always a single table. 
        right_tables = parameter_info[1]
        left_table = parameter_info[0][0]
        # print("For ", left_table, right_tables)

        ### Check all the edges (join key) between left table and all right tables
        ### If all the edges between left and right are not sensitive, we don't need
        ### to modify the selectivity, just keep the default pg sel
        sensitive_edges = []
        for sen_dim in sensitive_list:
            if sen_dim - num_of_base_rel >= 0:
                sensitive_edges.append(sen_dim - num_of_base_rel) 
        
        no_sensitive_flag = 1
        for r_t in right_tables:
            if join_maps[left_table][r_t] == -1: # these two tables are not joined
                continue
            else:
                if join_maps[left_table][r_t] in sensitive_edges:
                    no_sensitive_flag = 0
                    break
                # if we only check if the first join edge is sensitive 
                else:
                    break
        
        if no_sensitive_flag:
            continue
        # else:
        #     print(left_table, right_tables, i + num_of_base_rel)
        #     input()
        # input()



        new_sel = 1
        ### Record every right table that has edge with left table, the-
        ### se tables have the possible join edges
        tables_w_join_condition = []
        for r_t in right_tables:
            if join_maps[left_table][r_t] != -1: # there is a edge
                tables_w_join_condition.append(r_t)

        
        ### There are two options: if follow pgsql we just simply choose
        ### one table from tables_w_join_condition to join with left and
        ### calculate the selectivity; however, we could calculate the
        ### average of all edges from all tables in tables_w_join_condition.
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
                # if the sel is changed we also need to update the pointers to be sent
                changed_relation_list.append(i + num_of_base_rel)
                break
        #         print("we find: ", left_table, r_t)
        #         print("edge_id: ", edge_id, "times: ", join_output_sel[edge_id])
        #         input()
                
        # print(new_sel)
        join_output_sel[i] = new_sel
    
    # sensitve_list combines input sensitive dims and recentered dims
    # they are all in basic relations
    changed_relation_list = sensitive_list + changed_relation_list

    write_to_file(base_output_sel, f_base_sel)
    write_pointers_to_file(changed_relation_list)
    # write_pointers_to_file(list(range(len(base_output_sel) + len(join_output_sel))))
    # if max(relation_list) < num_of_base_rel: ## we don't need to change join selectivity
    #     return
    write_to_file(join_output_sel, f_join_sel)
    return base_output_sel, join_output_sel


def count_neg_one(two_d_list):
    count = 0

    for sublist in two_d_list:
        for element in sublist:
            if element == -1:
                count += 1

    return count

### Input a error and the original sel, calculate the new selectivity value
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