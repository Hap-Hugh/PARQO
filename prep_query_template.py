from prep_cardinality import get_raw_table_size, get_maps, ori_cardest
import pandas as pd
import numpy as np

np.random.seed(2023)
available_it_for_mi = ['genres'] * 13 + ['budget'] * 2 + ['release dates'] * 20 + ['countries'] * 10
available_it_for_pi = ['mini biography'] * 3 + ['trivia'] * 2 + ['height'] * 1
available_it_for_miidx = ['top 250 rank'] * 2 + ['bottom 10 rank'] * 2 + ['rating'] * 16 + ['votes'] * 11

cct_for_cc_subject_id = ["IN ('cast', 'crew')"] * 4 + ["= 'cast'"] * 12 + ["!= 'complete+verified'"] * 2 
cct_for_cc_status_id = ["= 'complete'"] * 3 + ["LIKE '%complete%'"] * 7 + [" = 'complete+verified'"] * 9


def gen_sql_by_template(query_id, K):
    local_selections = pd.read_csv('local-sel-condition.csv')
    local_selections_grouped = local_selections.groupby('Table')
    # ['Table', 'Condition', 'Frequency']
    condition_dict = {'k': [], 't': [], 'cn': [], 'n': [], 'mc': [], 'mi': [], 'it_pi': [], 'it_mi': [], 'it_miidx': [], 'an': [], 'lt': [], 'pi': [], 'ci':[], 'mi_idx':[], 'kt':[], 'ct':[], 'rt':[], 'cct':[], 'chn':[]}
    frequency_dict = {'x': [1], 'k': [], 't': [], 'cn': [], 'n': [], 'mc': [], 'mi': [], 'it_pi': [], 'it_mi': [], 'it_miidx': [],  'an': [], 'lt': [], 'pi': [], 'ci':[], 'mi_idx':[], 'kt':[], 'ct':[], 'rt':[], 'cct':[], 'chn':[]}
    for table in condition_dict.keys():
        for _, row in local_selections_grouped.get_group(table).iterrows():
            if row['Condition'] == '1=1':
                continue
            condition_dict[table].append(row['Condition'])
            frequency_dict[table].append(int(row['Frequency']))
            # condition_dict[table].extend([row['Condition']] * int(row['Frequency']))

    sampled_literals = []
    query_to_local_selection_dict = {
        '33a': ['cn', 'it_miidx', 'it_miidx', 'kt', 'kt', 'lt', 'mi_idx', 't'],
        '32a': ['k'],
        '31a': ['ci', 'cn', 'it_mi', 'it_miidx', 'k', 'mi', 'n'],
        '30a': ['cct', 'cct', 'ci', 'it_mi', 'it_miidx', 'k', 'mi', 'n', 't'],
        '29a': ['cct', 'cct', 'chn', 'ci', 'cn', 'it_mi', 'it_pi', 'k', 'mi', 'n', 'rt', 't'],
        '28a': ['cct', 'cct', 'cn', 'it_mi', 'it_miidx', 'k', 'kt', 'mc', 'mi', 'mi_idx', 't'],
        '27a': ['cct', 'cct', 'cn', 'ct', 'k', 'lt', 'mc', 'mi', 't'],
        '26a': ['cct', 'cct', 'chn', 'it_miidx', 'k', 'kt', 'mi_idx', 't'],
        '25a': ['ci', 'it_mi', 'it_miidx', 'k', 'mi', 'n'],
        '24a': ['ci', 'cn', 'it_mi', 'k', 'mi', 'n', 'rt', 't'],
        '23a': ['cct', 'cn', 'it_mi', 'kt', 'mi', 't'],
        '22a': ['cn', 'it_mi', 'it_miidx', 'k', 'kt', 'mc', 'mi', 'mi_idx', 't'],
        '21a': ['cn', 'ct', 'k', 'lt', 'mc', 'mi', 't'],
        '20a': ['cct', 'cct', 'chn', 'k', 'kt', 't'],
        '19a': ['ci', 'cn', 'it_mi', 'mc', 'mi', 'n', 'rt', 't'],
        '18a': ['ci', 'it_mi', 'it_miidx', 'n'],
        '17a': ['cn', 'k', 'n'], 
        '16a': ['cn', 'k', 't'],
        '15a': ['cn', 'it_mi', 'mc', 'mi', 't'],
        '14a': ['it_mi', 'it_miidx', 'k', 'kt', 'mi', 'mi_idx', 't'],
        '13a': ['cn', 'ct', 'it_miidx', 'it_mi', 'kt'],
        '12a': ['cn', 'ct', 'it_mi', 'it_miidx', 'mi', 'mi_idx', 't'],
        '11a': ['cn', 'ct', 'k', 'lt', 'mc', 't'],
        '10a': ['ci', 'cn', 'rt', 't'],
        '9a': ['ci', 'cn', 'mc', 'n', 'rt', 't'],
        '8a': ['ci', 'cn', 'mc', 'n', 'rt'],
        '7a': ['an', 'it_pi', 'lt', 'n', 'pi', 't'],
        '6a': ['k', 'n', 't'],
        '5a': ['ct', 'mc', 'mi', 't'],
        '4a': ['it_miidx', 'k', 'mi_idx', 't'],
        '3a': ['k', 'mi', 't'],
        '2a': ['cn', 'k'],
        '1a': ['ct', 'it_miidx', 'mc']}
    
    for i, table in enumerate(query_to_local_selection_dict[query_id]):
        total_frequency = sum(frequency_dict[table])
        probabilities = [freq / total_frequency for freq in frequency_dict[table]]
        sampled_literals.append(np.random.choice(condition_dict[table], p=probabilities, size=K*2))

    sampled_literals = np.transpose(sampled_literals).tolist()
    # Should avoid same conditions, # of parameter will change
    sampled_literals = [i for i in sampled_literals if len(set(i)) == len(i)][:K] 
    
    if query_id == '1a':
        for i in sampled_literals:
            i[1] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_1a(i) for i in sampled_literals]
    
    if query_id == '2a':
        sql_list = [change_query_2a(i) for i in sampled_literals]
        
    if query_id == '3a':
        sql_list = [change_query_3a(i) for i in sampled_literals]
    if query_id == '4a':
        for i in sampled_literals:
            i[0] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_4a(i) for i in sampled_literals]
    if query_id == '5a':
        sql_list = [change_query_5a(i) for i in sampled_literals]
    
    if query_id == '6a':
        sql_list = [change_query_6a(i) for i in sampled_literals]

    if query_id == '7a':
        for i in sampled_literals:
            i[1] = np.random.choice(available_it_for_pi)
        sql_list = [change_query_7a(i) for i in sampled_literals]

    if query_id == '8a':
        sql_list = [change_query_8a(i) for i in sampled_literals]
    if query_id == '9a':
        sql_list = [change_query_9a(i) for i in sampled_literals]
    if query_id == '10a':
        sql_list = [change_query_10a(i) for i in sampled_literals]
    if query_id == '11a':
        sql_list = [change_query_11a(i) for i in sampled_literals]
    
    if query_id == '12a':
        for i in sampled_literals:
            i[2] = np.random.choice(available_it_for_mi)
        sql_list = [change_query_12a(i) for i in sampled_literals]
    
    if query_id == '13a':
        # Should avoid 
        for i in sampled_literals:
            i[3] = np.random.choice(available_it_for_mi)
        sql_list = [change_query_13a(i) for i in sampled_literals]
    
    if query_id == '14a':
        for i in sampled_literals:
            i[0] = np.random.choice(available_it_for_mi)
            i[1] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_14a(i) for i in sampled_literals]


    if query_id == '15a':
        for i in sampled_literals:
            i[1] = np.random.choice(available_it_for_mi)
        sql_list = [change_query_15a(i) for i in sampled_literals]
    if query_id == '16a':
        sql_list = [change_query_16a(i) for i in sampled_literals]

    if query_id == '17a':
        sql_list = [change_query_17a(i) for i in sampled_literals]
    if query_id == '18a':
        for i in sampled_literals:
            i[1] = np.random.choice(available_it_for_mi)
            i[2] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_18a(i) for i in sampled_literals]
    
    if query_id == '19a':
        for i in sampled_literals:
            i[2] = np.random.choice(available_it_for_mi)
        sql_list = [change_query_19a(i) for i in sampled_literals]
    
    if query_id == '20a':
        sql_list = [change_query_20a(i) for i in sampled_literals]

    if query_id == '21a':
        sql_list = [change_query_21a(i) for i in sampled_literals]

    if query_id == '22a':
        for i in sampled_literals:
            i[1] = np.random.choice(available_it_for_mi)
            i[2] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_22a(i) for i in sampled_literals]
    
    if query_id == '23a':
        for i in sampled_literals:
            i[2] = np.random.choice(available_it_for_mi)
        sql_list = [change_query_23a(i) for i in sampled_literals]
    if query_id == '24a':
        for i in sampled_literals:
            i[2] = np.random.choice(available_it_for_mi)
        sql_list = [change_query_24a(i) for i in sampled_literals]  
    
    if query_id == '25a':
        for i in sampled_literals:
            i[1] = np.random.choice(available_it_for_mi)
            i[2] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_25a(i) for i in sampled_literals]
    
    if query_id == '26a':
        for i in sampled_literals:
            i[3] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_26a(i) for i in sampled_literals]
    
    if query_id == '27a':
        for i in sampled_literals:
            i[0] = np.random.choice(cct_for_cc_subject_id)
            i[1] = np.random.choice(cct_for_cc_status_id)
        sql_list = [change_query_27a(i) for i in sampled_literals]

    if query_id == '28a':
        for i in sampled_literals:
            i[0] = np.random.choice(cct_for_cc_subject_id)
            i[1] = np.random.choice(cct_for_cc_status_id)
            i[3] = np.random.choice(available_it_for_mi)
            i[4] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_28a(i) for i in sampled_literals]
    if query_id == '29a':
        for i in sampled_literals:
            i[0] = np.random.choice(cct_for_cc_subject_id)
            i[1] = np.random.choice(cct_for_cc_status_id)
            i[5] = np.random.choice(available_it_for_mi)
            i[6] = np.random.choice(available_it_for_pi)
        sql_list = [change_query_29a(i) for i in sampled_literals]
    if query_id == '30a':
        for i in sampled_literals:
            i[0] = np.random.choice(cct_for_cc_subject_id)
            i[1] = np.random.choice(cct_for_cc_status_id)
            i[3] = np.random.choice(available_it_for_mi)
            i[4] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_30a(i) for i in sampled_literals]
    # print(sampled_literals)
    
    if query_id == '31a':
        for i in sampled_literals:
            i[2] = np.random.choice(available_it_for_mi)
            i[3] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_31a(i) for i in sampled_literals]
    if query_id == '32a':
        sql_list = [change_query_32a(i) for i in sampled_literals]
    
    if query_id == '33a':
        for i in sampled_literals:
            i[1] = np.random.choice(available_it_for_miidx)
        sql_list = [change_query_33a(i) for i in sampled_literals]

    return sql_list, sampled_literals



def change_query_33a(literals):
    sql = f'''
    SELECT MIN(cn1.name) AS first_company,
       MIN(cn2.name) AS second_company,
       MIN(mi_idx1.info) AS first_rating,
       MIN(mi_idx2.info) AS second_rating,
       MIN(t1.title) AS first_movie,
       MIN(t2.title) AS second_movie
    FROM company_name AS cn1,
        company_name AS cn2,
        info_type AS it1,
        info_type AS it2,
        kind_type AS kt1,
        kind_type AS kt2,
        link_type AS lt,
        movie_companies AS mc1,
        movie_companies AS mc2,
        movie_info_idx AS mi_idx1,
        movie_info_idx AS mi_idx2,
        movie_link AS ml,
        title AS t1,
        title AS t2
    WHERE {literals[0].replace('cn', 'cn1')}
    AND it1.info = '{literals[1]}'
    AND it2.info = '{literals[1]}'
    AND {literals[3].replace('kt', 'kt1')}
    AND {literals[3].replace('kt', 'kt1')}
    AND {literals[5]}
    AND {literals[6].replace('mi_idx', 'mi_idx2')}
    AND {literals[7].replace('t.', 't2.')}
    AND lt.id = ml.link_type_id
    AND t1.id = ml.movie_id
    AND t2.id = ml.linked_movie_id
    AND it1.id = mi_idx1.info_type_id
    AND t1.id = mi_idx1.movie_id
    AND kt1.id = t1.kind_id
    AND cn1.id = mc1.company_id
    AND t1.id = mc1.movie_id
    AND ml.movie_id = mi_idx1.movie_id
    AND ml.movie_id = mc1.movie_id
    AND mi_idx1.movie_id = mc1.movie_id
    AND it2.id = mi_idx2.info_type_id
    AND t2.id = mi_idx2.movie_id
    AND kt2.id = t2.kind_id
    AND cn2.id = mc2.company_id
    AND t2.id = mc2.movie_id
    AND ml.linked_movie_id = mi_idx2.movie_id
    AND ml.linked_movie_id = mc2.movie_id
    AND mi_idx2.movie_id = mc2.movie_id;
    '''
    return sql


def change_query_32a(literals):
    sql = f'''
    SELECT MIN(lt.link) AS link_type,
       MIN(t1.title) AS first_movie,
       MIN(t2.title) AS second_movie
    FROM keyword AS k,
        link_type AS lt,
        movie_keyword AS mk,
        movie_link AS ml,
        title AS t1,
        title AS t2
    WHERE {literals[0]}
    AND mk.keyword_id = k.id
    AND t1.id = mk.movie_id
    AND ml.movie_id = t1.id
    AND ml.linked_movie_id = t2.id
    AND lt.id = ml.link_type_id
    AND mk.movie_id = t1.id;
    '''
    return sql


def change_query_31a(literals):
    sql = f'''
    SELECT MIN(mi.info) AS movie_budget,
       MIN(mi_idx.info) AS movie_votes,
       MIN(n.name) AS writer,
       MIN(t.title) AS violent_liongate_movie
    FROM cast_info AS ci,
        company_name AS cn,
        info_type AS it1,
        info_type AS it2,
        keyword AS k,
        movie_companies AS mc,
        movie_info AS mi,
        movie_info_idx AS mi_idx,
        movie_keyword AS mk,
        name AS n,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND it1.info = '{literals[2]}'
    AND it2.info = '{literals[3]}'
    AND {literals[4]}
    AND {literals[5]}
    AND {literals[6]}
    AND t.id = mi.movie_id
    AND t.id = mi_idx.movie_id
    AND t.id = ci.movie_id
    AND t.id = mk.movie_id
    AND t.id = mc.movie_id
    AND ci.movie_id = mi.movie_id
    AND ci.movie_id = mi_idx.movie_id
    AND ci.movie_id = mk.movie_id
    AND ci.movie_id = mc.movie_id
    AND mi.movie_id = mi_idx.movie_id
    AND mi.movie_id = mk.movie_id
    AND mi.movie_id = mc.movie_id
    AND mi_idx.movie_id = mk.movie_id
    AND mi_idx.movie_id = mc.movie_id
    AND mk.movie_id = mc.movie_id
    AND n.id = ci.person_id
    AND it1.id = mi.info_type_id
    AND it2.id = mi_idx.info_type_id
    AND k.id = mk.keyword_id
    AND cn.id = mc.company_id;
    '''
    return sql

def change_query_30a(literals):
    sql = f'''
    SELECT MIN(mi.info) AS movie_budget,
       MIN(mi_idx.info) AS movie_votes,
       MIN(n.name) AS writer,
       MIN(t.title) AS complete_violent_movie
    FROM complete_cast AS cc,
        comp_cast_type AS cct1,
        comp_cast_type AS cct2,
        cast_info AS ci,
        info_type AS it1,
        info_type AS it2,
        keyword AS k,
        movie_info AS mi,
        movie_info_idx AS mi_idx,
        movie_keyword AS mk,
        name AS n,
        title AS t
    WHERE cct1.kind {literals[0]}
    AND cct2.kind {literals[1]}
    AND {literals[2]}
    AND it1.info = '{literals[3]}'
    AND it2.info = '{literals[4]}'
    AND {literals[5]}
    AND {literals[6]}
    AND {literals[7]}
    AND {literals[8]}
    AND t.id = mi.movie_id
    AND t.id = mi_idx.movie_id
    AND t.id = ci.movie_id
    AND t.id = mk.movie_id
    AND t.id = cc.movie_id
    AND ci.movie_id = mi.movie_id
    AND ci.movie_id = mi_idx.movie_id
    AND ci.movie_id = mk.movie_id
    AND ci.movie_id = cc.movie_id
    AND mi.movie_id = mi_idx.movie_id
    AND mi.movie_id = mk.movie_id
    AND mi.movie_id = cc.movie_id
    AND mi_idx.movie_id = mk.movie_id
    AND mi_idx.movie_id = cc.movie_id
    AND mk.movie_id = cc.movie_id
    AND n.id = ci.person_id
    AND it1.id = mi.info_type_id
    AND it2.id = mi_idx.info_type_id
    AND k.id = mk.keyword_id
    AND cct1.id = cc.subject_id
    AND cct2.id = cc.status_id;
    '''
    return sql


def change_query_29a(literals):
    sql = f'''
    SELECT MIN(chn.name) AS voiced_char,
       MIN(n.name) AS voicing_actress,
       MIN(t.title) AS voiced_animation
    FROM aka_name AS an,
        complete_cast AS cc,
        comp_cast_type AS cct1,
        comp_cast_type AS cct2,
        char_name AS chn,
        cast_info AS ci,
        company_name AS cn,
        info_type AS it,
        info_type AS it3,
        keyword AS k,
        movie_companies AS mc,
        movie_info AS mi,
        movie_keyword AS mk,
        name AS n,
        person_info AS pi,
        role_type AS rt,
        title AS t
    WHERE cct1.kind {literals[0]}
    AND cct2.kind {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND it.info = '{literals[5]}'
    AND it3.info = '{literals[6]}'
    AND {literals[7]}
    AND {literals[8]}
    AND {literals[9]}
    AND {literals[10]}
    AND {literals[11]}
    AND t.id = mi.movie_id
    AND t.id = mc.movie_id
    AND t.id = ci.movie_id
    AND t.id = mk.movie_id
    AND t.id = cc.movie_id
    AND mc.movie_id = ci.movie_id
    AND mc.movie_id = mi.movie_id
    AND mc.movie_id = mk.movie_id
    AND mc.movie_id = cc.movie_id
    AND mi.movie_id = ci.movie_id
    AND mi.movie_id = mk.movie_id
    AND mi.movie_id = cc.movie_id
    AND ci.movie_id = mk.movie_id
    AND ci.movie_id = cc.movie_id
    AND mk.movie_id = cc.movie_id
    AND cn.id = mc.company_id
    AND it.id = mi.info_type_id
    AND n.id = ci.person_id
    AND rt.id = ci.role_id
    AND n.id = an.person_id
    AND ci.person_id = an.person_id
    AND chn.id = ci.person_role_id
    AND n.id = pi.person_id
    AND ci.person_id = pi.person_id
    AND it3.id = pi.info_type_id
    AND k.id = mk.keyword_id
    AND cct1.id = cc.subject_id
    AND cct2.id = cc.status_id;
    '''
    return sql


def change_query_28a(literals):
    sql = f'''

    SELECT MIN(cn.name) AS movie_company,
       MIN(mi_idx.info) AS rating,
       MIN(t.title) AS complete_euro_dark_movie
    FROM complete_cast AS cc,
        comp_cast_type AS cct1,
        comp_cast_type AS cct2,
        company_name AS cn,
        company_type AS ct,
        info_type AS it1,
        info_type AS it2,
        keyword AS k,
        kind_type AS kt,
        movie_companies AS mc,
        movie_info AS mi,
        movie_info_idx AS mi_idx,
        movie_keyword AS mk,
        title AS t
    WHERE cct1.kind {literals[0]}
    AND cct2.kind {literals[1]}
    AND {literals[2]}
    AND it1.info = '{literals[3]}'
    AND it2.info = '{literals[4]}'
    AND {literals[5]}
    AND {literals[6]}
    AND {literals[7]}
    AND {literals[8]}
    AND {literals[9]}
    AND {literals[10]}
    AND kt.id = t.kind_id
    AND t.id = mi.movie_id
    AND t.id = mk.movie_id
    AND t.id = mi_idx.movie_id
    AND t.id = mc.movie_id
    AND t.id = cc.movie_id
    AND mk.movie_id = mi.movie_id
    AND mk.movie_id = mi_idx.movie_id
    AND mk.movie_id = mc.movie_id
    AND mk.movie_id = cc.movie_id
    AND mi.movie_id = mi_idx.movie_id
    AND mi.movie_id = mc.movie_id
    AND mi.movie_id = cc.movie_id
    AND mc.movie_id = mi_idx.movie_id
    AND mc.movie_id = cc.movie_id
    AND mi_idx.movie_id = cc.movie_id
    AND k.id = mk.keyword_id
    AND it1.id = mi.info_type_id
    AND it2.id = mi_idx.info_type_id
    AND ct.id = mc.company_type_id
    AND cn.id = mc.company_id
    AND cct1.id = cc.subject_id
    AND cct2.id = cc.status_id;


    '''
    return sql


def change_query_27a(literals):
    sql = f'''
    SELECT MIN(cn.name) AS producing_company,
       MIN(lt.link) AS link_type,
       MIN(t.title) AS complete_western_sequel
    FROM complete_cast AS cc,
        comp_cast_type AS cct1,
        comp_cast_type AS cct2,
        company_name AS cn,
        company_type AS ct,
        keyword AS k,
        link_type AS lt,
        movie_companies AS mc,
        movie_info AS mi,
        movie_keyword AS mk,
        movie_link AS ml,
        title AS t
    WHERE cct1.kind {literals[0]}
    AND cct2.kind {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND {literals[6]}
    AND {literals[7]}
    AND {literals[8]}
    AND lt.id = ml.link_type_id
    AND ml.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND t.id = mc.movie_id
    AND mc.company_type_id = ct.id
    AND mc.company_id = cn.id
    AND mi.movie_id = t.id
    AND t.id = cc.movie_id
    AND cct1.id = cc.subject_id
    AND cct2.id = cc.status_id
    AND ml.movie_id = mk.movie_id
    AND ml.movie_id = mc.movie_id
    AND mk.movie_id = mc.movie_id
    AND ml.movie_id = mi.movie_id
    AND mk.movie_id = mi.movie_id
    AND mc.movie_id = mi.movie_id
    AND ml.movie_id = cc.movie_id
    AND mk.movie_id = cc.movie_id
    AND mc.movie_id = cc.movie_id
    AND mi.movie_id = cc.movie_id;
    '''
    return sql


def change_query_26a(literals):
    sql = f'''
        SELECT MIN(chn.name) AS character_name,
            MIN(mi_idx.info) AS rating,
            MIN(n.name) AS playing_actor,
            MIN(t.title) AS complete_hero_movie
        FROM complete_cast AS cc,
            comp_cast_type AS cct1,
            comp_cast_type AS cct2,
            char_name AS chn,
            cast_info AS ci,
            info_type AS it2,
            keyword AS k,
            kind_type AS kt,
            movie_info_idx AS mi_idx,
            movie_keyword AS mk,
            name AS n,
            title AS t
        WHERE cct1.kind = 'cast'
        AND cct2.kind LIKE '%complete%'
        AND {literals[2]}
        AND it2.info = '{literals[3]}'
        AND {literals[4]}
        AND {literals[5]}
        AND {literals[6]}
        AND {literals[7]}
        AND kt.id = t.kind_id
        AND t.id = mk.movie_id
        AND t.id = ci.movie_id
        AND t.id = cc.movie_id
        AND t.id = mi_idx.movie_id
        AND mk.movie_id = ci.movie_id
        AND mk.movie_id = cc.movie_id
        AND mk.movie_id = mi_idx.movie_id
        AND ci.movie_id = cc.movie_id
        AND ci.movie_id = mi_idx.movie_id
        AND cc.movie_id = mi_idx.movie_id
        AND chn.id = ci.person_role_id
        AND n.id = ci.person_id
        AND k.id = mk.keyword_id
        AND cct1.id = cc.subject_id
        AND cct2.id = cc.status_id
        AND it2.id = mi_idx.info_type_id;
    '''
    return sql


def change_query_25a(literals):
    sql = f'''
        SELECT MIN(mi.info) AS movie_budget,
            MIN(mi_idx.info) AS movie_votes,
            MIN(n.name) AS male_writer,
            MIN(t.title) AS violent_movie_title
        FROM cast_info AS ci,
            info_type AS it1,
            info_type AS it2,
            keyword AS k,
            movie_info AS mi,
            movie_info_idx AS mi_idx,
            movie_keyword AS mk,
            name AS n,
            title AS t
        WHERE {literals[0]}
        AND it1.info = '{literals[1]}'
        AND it2.info = '{literals[2]}'
        AND {literals[3]}
        AND {literals[4]}
        AND {literals[5]}
        AND t.id = mi.movie_id
        AND t.id = mi_idx.movie_id
        AND t.id = ci.movie_id
        AND t.id = mk.movie_id
        AND ci.movie_id = mi.movie_id
        AND ci.movie_id = mi_idx.movie_id
        AND ci.movie_id = mk.movie_id
        AND mi.movie_id = mi_idx.movie_id
        AND mi.movie_id = mk.movie_id
        AND mi_idx.movie_id = mk.movie_id
        AND n.id = ci.person_id
        AND it1.id = mi.info_type_id
        AND it2.id = mi_idx.info_type_id
        AND k.id = mk.keyword_id;
    '''
    return sql


def change_query_24a(literals):
    sql = f'''
    SELECT MIN(chn.name) AS voiced_char_name,
       MIN(n.name) AS voicing_actress_name,
       MIN(t.title) AS voiced_action_movie_jap_eng
    FROM aka_name AS an,
        char_name AS chn,
        cast_info AS ci,
        company_name AS cn,
        info_type AS it,
        keyword AS k,
        movie_companies AS mc,
        movie_info AS mi,
        movie_keyword AS mk,
        name AS n,
        role_type AS rt,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND it.info = '{literals[2]}'
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND {literals[6]}
    AND {literals[7]}
    AND t.id = mi.movie_id
    AND t.id = mc.movie_id
    AND t.id = ci.movie_id
    AND t.id = mk.movie_id
    AND mc.movie_id = ci.movie_id
    AND mc.movie_id = mi.movie_id
    AND mc.movie_id = mk.movie_id
    AND mi.movie_id = ci.movie_id
    AND mi.movie_id = mk.movie_id
    AND ci.movie_id = mk.movie_id
    AND cn.id = mc.company_id
    AND it.id = mi.info_type_id
    AND n.id = ci.person_id
    AND rt.id = ci.role_id
    AND n.id = an.person_id
    AND ci.person_id = an.person_id
    AND chn.id = ci.person_role_id
    AND k.id = mk.keyword_id;
    '''
    return sql


def change_query_23a(literals):
    sql = f'''
    SELECT MIN(kt.kind) AS movie_kind,
       MIN(t.title) AS complete_us_internet_movie
    FROM complete_cast AS cc,
        comp_cast_type AS cct,
        company_name AS cn,
        company_type AS ct,
        info_type AS it1,
        keyword AS k,
        kind_type AS kt,
        movie_companies AS mc,
        movie_info AS mi,
        movie_keyword AS mk,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND it1.info = '{literals[2]}'
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND kt.id = t.kind_id
    AND t.id = mi.movie_id
    AND t.id = mk.movie_id
    AND t.id = mc.movie_id
    AND t.id = cc.movie_id
    AND mk.movie_id = mi.movie_id
    AND mk.movie_id = mc.movie_id
    AND mk.movie_id = cc.movie_id
    AND mi.movie_id = mc.movie_id
    AND mi.movie_id = cc.movie_id
    AND mc.movie_id = cc.movie_id
    AND k.id = mk.keyword_id
    AND it1.id = mi.info_type_id
    AND cn.id = mc.company_id
    AND ct.id = mc.company_type_id
    AND cct.id = cc.status_id;

    '''
    return sql



def change_query_22a(literals):
    sql = f'''
    SELECT MIN(cn.name) AS movie_company,
       MIN(mi_idx.info) AS rating,
       MIN(t.title) AS western_violent_movie
    FROM company_name AS cn,
        company_type AS ct,
        info_type AS it1,
        info_type AS it2,
        keyword AS k,
        kind_type AS kt,
        movie_companies AS mc,
        movie_info AS mi,
        movie_info_idx AS mi_idx,
        movie_keyword AS mk,
        title AS t
    WHERE {literals[0]}
    AND it1.info = '{literals[1]}'
    AND it2.info = '{literals[2]}'
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND {literals[6]}
    AND {literals[7]}
    AND {literals[8]}
    AND kt.id = t.kind_id
    AND t.id = mi.movie_id
    AND t.id = mk.movie_id
    AND t.id = mi_idx.movie_id
    AND t.id = mc.movie_id
    AND mk.movie_id = mi.movie_id
    AND mk.movie_id = mi_idx.movie_id
    AND mk.movie_id = mc.movie_id
    AND mi.movie_id = mi_idx.movie_id
    AND mi.movie_id = mc.movie_id
    AND mc.movie_id = mi_idx.movie_id
    AND k.id = mk.keyword_id
    AND it1.id = mi.info_type_id
    AND it2.id = mi_idx.info_type_id
    AND ct.id = mc.company_type_id
    AND cn.id = mc.company_id;
    '''
    return sql


def change_query_21a(literals):
    sql = f'''
    SELECT MIN(cn.name) AS company_name,
       MIN(lt.link) AS link_type,
       MIN(t.title) AS western_follow_up
    FROM company_name AS cn,
        company_type AS ct,
        keyword AS k,
        link_type AS lt,
        movie_companies AS mc,
        movie_info AS mi,
        movie_keyword AS mk,
        movie_link AS ml,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND {literals[6]}
    AND lt.id = ml.link_type_id
    AND ml.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND t.id = mc.movie_id
    AND mc.company_type_id = ct.id
    AND mc.company_id = cn.id
    AND mi.movie_id = t.id
    AND ml.movie_id = mk.movie_id
    AND ml.movie_id = mc.movie_id
    AND mk.movie_id = mc.movie_id
    AND ml.movie_id = mi.movie_id
    AND mk.movie_id = mi.movie_id
    AND mc.movie_id = mi.movie_id;
    '''
    return sql

def change_query_20a(literals):
    sql = f'''
        SELECT MIN(t.title) AS complete_downey_ironman_movie
        FROM complete_cast AS cc,
            comp_cast_type AS cct1,
            comp_cast_type AS cct2,
            char_name AS chn,
            cast_info AS ci,
            keyword AS k,
            kind_type AS kt,
            movie_keyword AS mk,
            name AS n,
            title AS t
        WHERE cct1.kind = 'cast'
        AND cct2.kind LIKE '%complete%'
        AND {literals[2]}
        AND {literals[3]}
        AND {literals[4]}
        AND {literals[5]}
        AND kt.id = t.kind_id
        AND t.id = mk.movie_id
        AND t.id = ci.movie_id
        AND t.id = cc.movie_id
        AND mk.movie_id = ci.movie_id
        AND mk.movie_id = cc.movie_id
        AND ci.movie_id = cc.movie_id
        AND chn.id = ci.person_role_id
        AND n.id = ci.person_id
        AND k.id = mk.keyword_id
        AND cct1.id = cc.subject_id
        AND cct2.id = cc.status_id;
    '''
    return sql



def change_query_19a(literals):
    sql = f'''
    SELECT MIN(n.name) AS voicing_actress,
       MIN(t.title) AS voiced_movie
    FROM aka_name AS an,
        char_name AS chn,
        cast_info AS ci,
        company_name AS cn,
        info_type AS it,
        movie_companies AS mc,
        movie_info AS mi,
        name AS n,
        role_type AS rt,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND it.info = '{literals[2]}'
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND {literals[6]}
    AND {literals[7]}
    AND t.id = mi.movie_id
    AND t.id = mc.movie_id
    AND t.id = ci.movie_id
    AND mc.movie_id = ci.movie_id
    AND mc.movie_id = mi.movie_id
    AND mi.movie_id = ci.movie_id
    AND cn.id = mc.company_id
    AND it.id = mi.info_type_id
    AND n.id = ci.person_id
    AND rt.id = ci.role_id
    AND n.id = an.person_id
    AND ci.person_id = an.person_id
    AND chn.id = ci.person_role_id;

    '''
    return sql

def change_query_18a(literals):
    sql = f'''
    SELECT MIN(mi.info) AS movie_budget,
       MIN(mi_idx.info) AS movie_votes,
       MIN(t.title) AS movie_title
    FROM cast_info AS ci,
        info_type AS it1,
        info_type AS it2,
        movie_info AS mi,
        movie_info_idx AS mi_idx,
        name AS n,
        title AS t
    WHERE {literals[0]}
    AND it1.info = '{literals[1]}'
    AND it2.info = '{literals[2]}'
    AND {literals[3]}
    AND t.id = mi.movie_id
    AND t.id = mi_idx.movie_id
    AND t.id = ci.movie_id
    AND ci.movie_id = mi.movie_id
    AND ci.movie_id = mi_idx.movie_id
    AND mi.movie_id = mi_idx.movie_id
    AND n.id = ci.person_id
    AND it1.id = mi.info_type_id
    AND it2.id = mi_idx.info_type_id;
    '''
    return sql




def change_query_17a(literals):
    sql = f'''
        SELECT MIN(n.name) AS member_in_charnamed_american_movie,
            MIN(n.name) AS a1
        FROM cast_info AS ci,
            company_name AS cn,
            keyword AS k,
            movie_companies AS mc,
            movie_keyword AS mk,
            name AS n,
            title AS t
        WHERE {literals[0]}
        AND {literals[1]}
        AND {literals[2]}
        AND n.id = ci.person_id
        AND ci.movie_id = t.id
        AND t.id = mk.movie_id
        AND mk.keyword_id = k.id
        AND t.id = mc.movie_id
        AND mc.company_id = cn.id
        AND ci.movie_id = mc.movie_id
        AND ci.movie_id = mk.movie_id
        AND mc.movie_id = mk.movie_id;
        '''
    return sql

def change_query_16a(literals):
    sql = f'''
    SELECT MIN(an.name) AS cool_actor_pseudonym,
       MIN(t.title) AS series_named_after_char
    FROM aka_name AS an,
        cast_info AS ci,
        company_name AS cn,
        keyword AS k,
        movie_companies AS mc,
        movie_keyword AS mk,
        name AS n,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND {literals[2]}
    AND an.person_id = n.id
    AND n.id = ci.person_id
    AND ci.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND t.id = mc.movie_id
    AND mc.company_id = cn.id
    AND an.person_id = ci.person_id
    AND ci.movie_id = mc.movie_id
    AND ci.movie_id = mk.movie_id
    AND mc.movie_id = mk.movie_id;'''
    return sql


def change_query_15a(literals):
    sql = f'''
    SELECT MIN(mi.info) AS release_date,
       MIN(t.title) AS internet_movie
    FROM aka_title AS aka_t,
        company_name AS cn,
        company_type AS ct,
        info_type AS it1,
        keyword AS k,
        movie_companies AS mc,
        movie_info AS mi,
        movie_keyword AS mk,
        title AS t
    WHERE {literals[0]}
    AND it1.info = '{literals[1]}'
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND t.id = aka_t.movie_id
    AND t.id = mi.movie_id
    AND t.id = mk.movie_id
    AND t.id = mc.movie_id
    AND mk.movie_id = mi.movie_id
    AND mk.movie_id = mc.movie_id
    AND mk.movie_id = aka_t.movie_id
    AND mi.movie_id = mc.movie_id
    AND mi.movie_id = aka_t.movie_id
    AND mc.movie_id = aka_t.movie_id
    AND k.id = mk.keyword_id
    AND it1.id = mi.info_type_id
    AND cn.id = mc.company_id
    AND ct.id = mc.company_type_id;
    '''
    return sql


def change_query_14a(literals):

    sql = f'''
    SELECT MIN(mi_idx.info) AS rating,
       MIN(t.title) AS northern_dark_movie
    FROM info_type AS it1,
        info_type AS it2,
        keyword AS k,
        kind_type AS kt,
        movie_info AS mi,
        movie_info_idx AS mi_idx,
        movie_keyword AS mk,
        title AS t
    WHERE it1.info = '{literals[0]}'
    AND it2.info = '{literals[1]}'
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND {literals[6]}
    AND kt.id = t.kind_id
    AND t.id = mi.movie_id
    AND t.id = mk.movie_id
    AND t.id = mi_idx.movie_id
    AND mk.movie_id = mi.movie_id
    AND mk.movie_id = mi_idx.movie_id
    AND mi.movie_id = mi_idx.movie_id
    AND k.id = mk.keyword_id
    AND it1.id = mi.info_type_id
    AND it2.id = mi_idx.info_type_id;    
    '''
    return sql


def change_query_13a(literals):
    sql = f'''
    SELECT MIN(mi.info) AS release_date,
       MIN(miidx.info) AS rating,
       MIN(t.title) AS german_movie
    FROM company_name AS cn,
        company_type AS ct,
        info_type AS it,
        info_type AS it2,
        kind_type AS kt,
        movie_companies AS mc,
        movie_info AS mi,
        movie_info_idx AS miidx,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND it.info = 'rating'
    AND it2.info = '{literals[3]}'
    AND {literals[4]}
    AND mi.movie_id = t.id
    AND it2.id = mi.info_type_id
    AND kt.id = t.kind_id
    AND mc.movie_id = t.id
    AND cn.id = mc.company_id
    AND ct.id = mc.company_type_id
    AND miidx.movie_id = t.id
    AND it.id = miidx.info_type_id
    AND mi.movie_id = miidx.movie_id
    AND mi.movie_id = mc.movie_id
    AND miidx.movie_id = mc.movie_id;
    '''
    return sql


def change_query_12a(literals):
    sql = f'''
    
    SELECT MIN(cn.name) AS movie_company,
       MIN(mi_idx.info) AS rating,
       MIN(t.title) AS drama_horror_movie
    FROM company_name AS cn,
        company_type AS ct,
        info_type AS it1,
        info_type AS it2,
        movie_companies AS mc,
        movie_info AS mi,
        movie_info_idx AS mi_idx,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND it1.info = '{literals[2]}'
    AND it2.info = 'rating'
    AND {literals[4]}
    AND {literals[5]}
    AND {literals[6]}
    AND t.id = mi.movie_id
    AND t.id = mi_idx.movie_id
    AND mi.info_type_id = it1.id
    AND mi_idx.info_type_id = it2.id
    AND t.id = mc.movie_id
    AND ct.id = mc.company_type_id
    AND cn.id = mc.company_id
    AND mc.movie_id = mi.movie_id
    AND mc.movie_id = mi_idx.movie_id
    AND mi.movie_id = mi_idx.movie_id;
    '''
    return sql


def change_query_11a(literals):
    sql = f'''
    SELECT MIN(cn.name) AS from_company,
       MIN(lt.link) AS movie_link_type,
       MIN(t.title) AS non_polish_sequel_movie
    FROM company_name AS cn,
        company_type AS ct,
        keyword AS k,
        link_type AS lt,
        movie_companies AS mc,
        movie_keyword AS mk,
        movie_link AS ml,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND lt.id = ml.link_type_id
    AND ml.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND t.id = mc.movie_id
    AND mc.company_type_id = ct.id
    AND mc.company_id = cn.id
    AND ml.movie_id = mk.movie_id
    AND ml.movie_id = mc.movie_id
    AND mk.movie_id = mc.movie_id;
    '''
    return sql


def change_query_10a(literals):
    sql = f'''
    SELECT MIN(chn.name) AS uncredited_voiced_character,
       MIN(t.title) AS russian_movie
    FROM char_name AS chn,
        cast_info AS ci,
        company_name AS cn,
        company_type AS ct,
        movie_companies AS mc,
        role_type AS rt,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND t.id = mc.movie_id
    AND t.id = ci.movie_id
    AND ci.movie_id = mc.movie_id
    AND chn.id = ci.person_role_id
    AND rt.id = ci.role_id
    AND cn.id = mc.company_id
    AND ct.id = mc.company_type_id;
    '''
    return sql


def change_query_9a(literals):
    sql = f'''
    SELECT MIN(an.name) AS alternative_name,
       MIN(chn.name) AS character_name,
       MIN(t.title) AS movie
    FROM aka_name AS an,
        char_name AS chn,
        cast_info AS ci,
        company_name AS cn,
        movie_companies AS mc,
        name AS n,
        role_type AS rt,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND ci.movie_id = t.id
    AND t.id = mc.movie_id
    AND ci.movie_id = mc.movie_id
    AND mc.company_id = cn.id
    AND ci.role_id = rt.id
    AND n.id = ci.person_id
    AND chn.id = ci.person_role_id
    AND an.person_id = n.id
    AND an.person_id = ci.person_id;

    '''
    return sql


def change_query_8a(literals):
    sql = f'''
    SELECT MIN(an1.name) AS actress_pseudonym,
       MIN(t.title) AS japanese_movie_dubbed
    FROM aka_name AS an1,
        cast_info AS ci,
        company_name AS cn,
        movie_companies AS mc,
        name AS n,
        role_type AS rt,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND an1.person_id = n.id
    AND n.id = ci.person_id
    AND ci.movie_id = t.id
    AND t.id = mc.movie_id
    AND mc.company_id = cn.id
    AND ci.role_id = rt.id
    AND an1.person_id = ci.person_id
    AND ci.movie_id = mc.movie_id;
    '''
    return sql


def change_query_7a(literals):
    sql = f'''
    SELECT MIN(n.name) AS of_person,
       MIN(t.title) AS biography_movie
    FROM aka_name AS an,
        cast_info AS ci,
        info_type AS it,
        link_type AS lt,
        movie_link AS ml,
        name AS n,
        person_info AS pi,
        title AS t
    WHERE {literals[0]}
    AND it.info ='{literals[1]}'
    AND {literals[2]}
    AND {literals[3]}
    AND {literals[4]}
    AND {literals[5]}
    AND n.id = an.person_id
    AND n.id = pi.person_id
    AND ci.person_id = n.id
    AND t.id = ci.movie_id
    AND ml.linked_movie_id = t.id
    AND lt.id = ml.link_type_id
    AND it.id = pi.info_type_id
    AND pi.person_id = an.person_id
    AND pi.person_id = ci.person_id
    AND an.person_id = ci.person_id
    AND ci.movie_id = ml.linked_movie_id;
    '''
    return sql


def change_query_6a(literals):
    sql = f'''
        SELECT MIN(k.keyword) AS movie_keyword,
       MIN(n.name) AS actor_name,
       MIN(t.title) AS marvel_movie
FROM cast_info AS ci,
     keyword AS k,
     movie_keyword AS mk,
     name AS n,
     title AS t
WHERE {literals[0]}
  AND {literals[1]}
  AND {literals[2]}
  AND k.id = mk.keyword_id
  AND t.id = mk.movie_id
  AND t.id = ci.movie_id
  AND ci.movie_id = mk.movie_id
  AND n.id = ci.person_id;
        '''
    return sql


def change_query_5a(literals):
    sql = f'''
    SELECT MIN(t.title) AS typical_european_movie
    FROM company_type AS ct,
        info_type AS it,
        movie_companies AS mc,
        movie_info AS mi,
        title AS t
    WHERE {literals[0]}
    AND {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND t.id = mi.movie_id
    AND t.id = mc.movie_id
    AND mc.movie_id = mi.movie_id
    AND ct.id = mc.company_type_id
    AND it.id = mi.info_type_id;
    '''
    return sql


def change_query_4a(literals):
    sql = f'''
    SELECT MIN(mi_idx.info) AS rating,
       MIN(t.title) AS movie_title
    FROM info_type AS it,
        keyword AS k,
        movie_info_idx AS mi_idx,
        movie_keyword AS mk,
        title AS t
    WHERE it.info = '{literals[0]}'
    AND {literals[1]}
    AND {literals[2]}
    AND {literals[3]}
    AND t.id = mi_idx.movie_id
    AND t.id = mk.movie_id
    AND mk.movie_id = mi_idx.movie_id
    AND k.id = mk.keyword_id
    AND it.id = mi_idx.info_type_id;
    '''
    return sql

def change_query_3a(literal):
    sql = f'''
    SELECT MIN(t.title) AS movie_title
    FROM keyword AS k,
        movie_info AS mi,
        movie_keyword AS mk,
        title AS t
    WHERE {literal[0]}
    AND {literal[1]}
    AND {literal[2]}
    AND t.id = mi.movie_id
    AND t.id = mk.movie_id
    AND mk.movie_id = mi.movie_id
    AND k.id = mk.keyword_id;
    '''
    return sql

def change_query_2a(literal):
    
    sql = f'''
    SELECT MIN(t.title) AS movie_title
    FROM company_name AS cn,
        keyword AS k,
        movie_companies AS mc,
        movie_keyword AS mk,
        title AS t
    WHERE {literal[0]}
    AND {literal[1]}
    AND cn.id = mc.company_id
    AND mc.movie_id = t.id
    AND t.id = mk.movie_id
    AND mk.keyword_id = k.id
    AND mc.movie_id = mk.movie_id;
    '''
    return sql

def change_query_1a(literal):
    sql = f'''
    SELECT MIN(mc.note) AS production_note,
       MIN(t.title) AS movie_title,
       MIN(t.production_year) AS movie_year
    FROM company_type AS ct,
        info_type AS it,
        movie_companies AS mc,
        movie_info_idx AS mi_idx,
        title AS t
    WHERE {literal[0]}
    AND it.info = '{literal[1]}'
    AND {literal[2]}
    AND ct.id = mc.company_type_id
    AND t.id = mc.movie_id
    AND t.id = mi_idx.movie_id
    AND mc.movie_id = mi_idx.movie_id
    AND it.id = mi_idx.info_type_id;
    '''
    return sql