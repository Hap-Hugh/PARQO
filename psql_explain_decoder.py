import json
from utility import *
'''
Decode the pg_explain result (json format) into readable format

Input: postgres explain (json format)

Output:

Merge Join(Merge Join(Merge Join(Merge Join(Nested Loop(tmpt,mc),Nested Loop(tmpt,mi_idx)),Nested Loop(tmpt,ct)),Nested Loop(tmpt,t)),Nested Loop(tmpt,it))
['Nested Loop', 'Nested Loop', 'Merge Join(mc.movie_id = mi_idx.movie_id)', 'Nested Loop', 'Merge Join(mc.company_type_id = ct.id)', 'Nested Loop', 'Merge Join(mc.movie_id = t.id)', 'Nested Loop', 'Merge Join(mi_idx.info_type_id = it.id)']
['Index Scan(mc)', 'Index Scan(mi_idx)', 'Index Scan(ct)', 'Index Scan(t)', 'Index Scan(it)']

'''

join_type_to_cond_field = {
    'Merge Join' : 'Merge Cond',
    'Hash Join' : 'Hash Cond',
    'Nested Loop' : 'Join Filter'
}

def load(filename):
    with open(filename) as fin:
        data = json.load(fin)
    return data[0][0][0]['Plan']


def decode(plans, parent, file_name=None):
    if len(plans) < 1 or len(plans) > 2:
        raise ValueError('incorrect number of plans')
        
    join_order = ''
    single_scans = []
    join_conds = []
    
    if len(plans) == 2:
        if plans[0]['Parent Relationship'] == 'Inner' and plans[1]['Parent Relationship'] == 'Outer':
            plans[0], plans[1] = plans[1], plans[0]
        if plans[0]['Parent Relationship'] != 'Outer' or plans[1]['Parent Relationship'] != 'Inner':
            raise ValueError('missing inner/outer relationship')
            
    for i in range(len(plans)):
        node_type = plans[i]['Node Type']
        if 'Plans' not in plans[i]:

            single_scans.append(node_type + '(' + plans[i]['Alias'] + ')')

        if node_type in ['Aggregate', 'Gather', 'Sort', 'Materialize', 'Sort', 'Hash', 'Gather Merge']:
            _join_order, _join_conds, _single_scans = decode(plans[i]['Plans'], parent, file_name)
            join_order += _join_order
            join_conds += _join_conds
            single_scans.extend(_single_scans)
        elif node_type == 'Limit':
            join_order += 'tmpt'
        elif node_type in ['Merge Join', 'Hash Join', 'Nested Loop']:
            if file_name:
                est_sel = card(plans[i]["Plan Rows"]) / (card(plans[i]["Plans"][0]["Plan Rows"]) * card(plans[i]["Plans"][1]["Plan Rows"]))
                true_sel = card(plans[i]["Actual Rows"]) / (card(plans[i]["Plans"][0]["Actual Rows"]) * card(plans[i]["Plans"][1]["Actual Rows"]))
                print(f"{est_sel}, {true_sel}", file=file_name)
            join_order += node_type + '('
            _join_order, _join_conds, _single_scans = decode(plans[i]['Plans'], node_type, file_name)
            join_order += _join_order
            join_conds += _join_conds
            cond_field = join_type_to_cond_field[node_type]
            merge_cond = '' if cond_field not in plans[i] else plans[i][cond_field]
            join_conds.append(node_type + merge_cond)
            single_scans.extend(_single_scans)
            join_order += ')'
        elif node_type in ['Index Scan', 'Seq Scan', 'Bitmap Scan', 'Index Only Scan']:
            join_order += plans[i]['Alias']
        else:
            print(plans[i])
            raise NotImplementedError(node_type)
        
        if i < len(plans) - 1:
            join_order += ','
            
    return join_order, join_conds, single_scans
          




def start_with_tab(str, x):
    tab_string = ""
    for i in range(x):
        tab_string = tab_string + "\t"
    if str.startswith(tab_string) and not str.startswith(tab_string + "\t"):
        return True
    else:
        return False


JOIN_KEYWORD = ["MergeJoin", "HashJoin", "NestLoop"]
SCAN_KEYWORD = ["SeqScan", "IdxScan"]


join_kw_to_we_need = {
    'MergeJoin' : 'Merge Join',
    'HashJoin' : 'Hash Join',
    'NestLoop' : 'Nested Loop'
}

scan_kw_to_we_need = {
    "SeqScan": "Seq Scan",
    "IdxScan": "Index Scan"
}


def pre_deal_gather(input_string):
    lines = input_string.split('\n')
    return_lines = []
    for i in range(len(lines)):
        if "Gather" in lines[i] or "Sort" in lines[i] or "GatherMerge" in lines[i]:
            count = lines[i].count("\t")
            # print(count)
            # input()
            for j in range(i+1, len(lines)):
                new_count = lines[j].count("\t")
                if new_count <= count and not "pathkeys:" in lines[j]:
                    break
                else:
                    lines[j] = lines[j].replace("\t", "", 1)
        else:
            return_lines.append(lines[i])
    return "\n".join(return_lines)


def pre_build_plan_tree(input_string):
    lines = input_string.split('\n')
    return_lines = []
    for i in range(len(lines)):
        flag = False
        for jkw in JOIN_KEYWORD:
            if jkw in lines[i]:
                flag = True
                break
        for sjw in SCAN_KEYWORD:
            if sjw in lines[i]:
                flag = True
                break
        if flag:
            return_lines.append(lines[i])
    return "\n".join(return_lines)



def seperate_top_n_plans(preprocessed_string):
    preprocessed_string = preprocessed_string.split('\n')

    plan_list = []
    pointers = []
    for i in range(len(preprocessed_string)):
        # print(preprocessed_string[i])
        # input()
        if start_with_tab(preprocessed_string[i], 1) and '(' in preprocessed_string[i]:
            pointers.append(i)

    for i in range(len(pointers)):
        if i + 1 < len(pointers):
            plan_list.append("\n".join(preprocessed_string[pointers[i]: pointers[i+1]]))
        else:
            plan_list.append("\n".join(preprocessed_string[pointers[i]:]))

    return plan_list




def build_plan_tree(input_string, x):
    lines = input_string.split('\n')
    operator_args = lines[0].strip().split('(')[1].split(')')[0].split()
    operator_name = lines[0].strip().split('(')[0]
    
    if len(operator_args) == 1:
        return operator_args[0]


    left_start = False
    right_start = False
    left_lines = []
    right_lines = []
    for i in range(1, len(lines)):
        if start_with_tab(lines[i], x+1) and not left_start:
            left_start = True
            right_start = False
            left_lines.append(lines[i])
            continue
        if start_with_tab(lines[i], x+1) and left_start:
            left_start = False
            right_start = True
            right_lines.append(lines[i])
            continue
        if left_start:
            left_lines.append(lines[i])
            continue
        if right_start:
            right_lines.append(lines[i])
            continue

    left_result = build_plan_tree("\n".join(left_lines), x+1)
    right_result = build_plan_tree("\n".join(right_lines), x+1)

    return join_kw_to_we_need[operator_name] + "(" + left_result + "," + right_result + ")"


def build_scan_methods(input_string):
    result = []
    lines = input_string.split('\n')
    for i in range(0, len(lines)):
        for k in SCAN_KEYWORD:
            if k in lines[i]:
                operator_args = lines[i].split('(')[1].split(')')[0].split()
                operator_name = lines[i].split('(')[0].split()[0]
                result.append(scan_kw_to_we_need[operator_name] + "(" + operator_args[0] + ")")
                break
    return result

