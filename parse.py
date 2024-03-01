def split_string(tmp, d):
    tmp = tmp.split(d)
    tmp_list = []
    for k in range(len(tmp)):
        tmp_list.append(tmp[k])
        if k < len(tmp) - 1:
            tmp_list.append(d)
    return tmp_list


def parse_string(new_list, d):
    final_list = []
    for i in range(len(new_list)):
        if d in new_list[i]:
            tmp_list = split_string(new_list[i], d)
            final_list += tmp_list
        else:
            final_list.append(new_list[i])
    return final_list

join_type = ['Merge Join', 'Hash Join', 'Nested Loop']
hint_type_dict = {
    'Merge Join': 'MergeJoin', 
    'Hash Join': 'HashJoin', 
    'Nested Loop': 'NestLoop'
}





def gen_join_hints(str):
    new_list = []
    tmp = str.split('(')
    for i in range(len(tmp)):
        new_list.append(tmp[i])
        if i < len(tmp) - 1:
            new_list.append('(')
    final_list = parse_string(new_list, ')')
    final_list = parse_string(final_list, ',')
    for i in final_list:
        if i == '':
            final_list.remove('')
    for i in final_list:    
        if i == ',':
            final_list.remove(',')
    for i in range(len(final_list)):
        final_list[i] = final_list[i].lstrip().rstrip()

    lead = 'Leading ( '
    for i in final_list:
        if i not in join_type:
            lead += i + ' '
    lead = lead + ')'

    visited = [0] * len(final_list)
    join_hints = []

    for i in range(len(final_list)):
        if final_list[i] == ')' and visited[i] == 0:
            tmp_rst = ')'
            visited[i] == 1
            for j in range(i-1, -1, -1):
                if final_list[j] not in ['(', ')'] and final_list[j] not in join_type:
                    tmp_rst = final_list[j] + ' ' + tmp_rst
                if final_list[j] == '(' and visited[j] == 0:
                    tmp_rst = hint_type_dict[final_list[j-1]] + ' ' + final_list[j] + ' ' + tmp_rst
                    visited[j] = 1
                    visited[j-1] = 1
                    break
            join_hints.append(tmp_rst)
            continue
    return join_hints, lead


def gen_scan_hints(scan_mtd):
    scan_hints = []
    for scan in scan_mtd:
        scan = scan.split(' ')
        tmp = ''
        for i in scan:
            tmp += i
        scan_hints.append(tmp)
    return scan_hints

def gen_final_hint(str, scan_mtd):
    result = '/*+'
    for i in gen_scan_hints(scan_mtd):
        result += '\n' + i
    join_hints, leading = gen_join_hints(str)
    for i in join_hints:
        result += '\n' + i
    result += '\n' + leading
    result += ' */'
    return result






