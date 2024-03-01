
from postgres import *
from psql_explain_decoder import *
from sklearn.neighbors import KernelDensity
import random
import pandas as pd
from prep_error_list import plot_error, cal_rel_error

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
file_name_to_save_real_error = ''
kk = '1=1'
cache_right = {}

def gen_real_error():
    local_selections = pd.read_csv('local-sel-condition.csv')
    local_selections_grouped = local_selections.groupby('Table')
    condition_dict = {'k': [], 't': [], 'cn': [], 'n': [], 'mc': [], 'mi': [], 'it_pi': [], 'it_mi': [], 'it_miidx': [], 'an': [], 'lt': [], 'pi': [], 'ci':[], 'mi_idx':[], 'kt':[], 'ct':[], 'rt':[], 'cct':[], 'chn':[]}
    frequency_dict = {'x': [1], 'k': [], 't': [], 'cn': [], 'n': [], 'mc': [], 'mi': [], 'it_pi': [], 'it_mi': [], 'it_miidx': [], 'an': [], 'lt': [], 'pi': [], 'ci':[], 'mi_idx':[], 'kt':[], 'ct':[], 'rt':[], 'cct':[], 'chn':[]}
    for table in condition_dict.keys():
        for _, row in local_selections_grouped.get_group(table).iterrows():
            if row['Condition'] == '1=1':
                continue
            condition_dict[table].append(row['Condition'])
            frequency_dict[table].append(int(row['Frequency']))

    condition_dict['x'] = ['1=1']
    data_list = []
    
    
    
    left = 'x'
    right = 'n'
    
    
    
    
    

    for id_1, kk in enumerate(condition_dict[left]):
        for id_2, cc in enumerate(condition_dict[right]):

            cc = "n.name LIKE 'B%'"
            ### mk k
            template_mk_k = f'''
                SELECT * FROM keyword AS k, movie_keyword AS mk
                WHERE {cc} AND mk.keyword_id = k.id;
                '''
            # mk ci --Q17 --k
            template_mk_ci__k = f'''
                SELECT * FROM cast_info AS ci, keyword AS k, movie_keyword AS mk
                where {cc} AND mk.keyword_id = k.id and ci.movie_id = mk.movie_id;
            '''
            
            ### t ci: use t (ci n) -- Q17
            template_t_ci__n = f'''
                SELECT * FROM cast_info AS ci, name AS n, title AS t
                WHERE {cc} AND n.id = ci.person_id AND ci.movie_id = t.id;
            '''

            ### ci mc Q17 pure
            template_ci_mc__cn = f'''select * from cast_info AS ci, movie_companies AS mc, company_name AS cn
                where {cc} and ci.movie_id = mc.movie_id AND mc.company_id = cn.id; '''

            template_ci_mc__n = f'''select * from cast_info AS ci, movie_companies AS mc, name AS n
                where {cc} and ci.movie_id = mc.movie_id AND n.id = ci.person_id; '''


            ### ml lt: use (lt) (k mk ml) -- Q32
            template_ml_lt = f'''
                SELECT *
                FROM keyword AS k,
                    link_type AS lt,
                    movie_keyword AS mk,
                    movie_link AS ml
                WHERE {cc}
                AND mk.keyword_id = k.id
                AND mk.movie_id = ml.movie_id
                AND lt.id = ml.link_type_id;
            '''
            
            ### ml mk: use (ml) (k mk) -- Q32
            template_ml_mk__k = f'''
                SELECT *
                FROM keyword AS k,
                    movie_keyword AS mk,
                    movie_link AS ml
                WHERE {cc}
                AND mk.keyword_id = k.id
                AND mk.movie_id = ml.movie_id;
            '''
            ### t mk: use (t) (mk) and (t) (k mk) -- Q32
            template_t_mk_1 = f'''
                SELECT *
                FROM movie_keyword AS mk,
                    title AS t
                WHERE {cc}
                AND t.id = mk.movie_id;
            '''
            template_t_mk_2 = f'''
                SELECT *
                FROM keyword AS k, movie_keyword AS mk, title AS t
                WHERE {cc} AND {cc} AND mk.keyword_id = k.id AND t.id = mk.movie_id
                ;
            '''


            ### t ml: use (t) (ml) -- Q32
            template_t_ml_1 = f'''
                SELECT * FROM movie_link AS ml, title AS t
                WHERE {cc} AND ml.movie_id = t.id;
            '''

            ### t ml: Saved in t-ml-2.txt when join on linked_movie_id
            template_t_ml_2 = f'''
                SELECT *
                FROM movie_link AS ml,
                title AS t
                WHERE {cc}
                AND ml.linked_movie_id = t.id;
            '''

            # t ci -- Q16 condition on left
            template_t_ci_l = f'''
                SELECT * FROM cast_info AS ci, title AS t
                WHERE {cc} AND ci.movie_id = t.id;
            '''

            # mc cn -- Q16
            template_mc_cn = f'''
                SELECT * FROM company_name AS cn, movie_companies AS mc
                WHERE {cc} AND {cc} AND mc.company_id = cn.id;
            '''


            # t mc -- Q16 left
            template_t_mc_l = f'''
                SELECT * FROM movie_companies AS mc, title AS t
                WHERE {cc} AND t.id = mc.movie_id;
            '''


            # t mk -- Q16
            template_t_mk = f'''
                SELECT * FROM movie_keyword AS mk, title AS t
                WHERE {cc} AND t.id = mk.movie_id;
            '''

            # n ci -- Q16 pure
            template_n_ci = f'''
                SELECT * FROM cast_info AS ci, name AS n
                WHERE n.name LIKE 'B%' AND n.id = ci.person_id;
            '''

            # n an -- Q16 pure
            template_n_an = f'''
                SELECT * FROM aka_name AS an, name AS n
                WHERE {cc} AND an.person_id = n.id;
            '''


            # ci an -- Q16 pure
            template_ci_an = f'''
                SELECT * FROM aka_name AS an, cast_info AS ci, title AS t
                Where {cc} AND ci.movie_id = t.id AND an.person_id = ci.person_id;
            '''

            # mc aka_t -- Q15
            template_mc_akat_l = f'''
                SELECT * FROM aka_title AS aka_t, movie_companies AS mc
                WHERE {cc} AND mc.movie_id = aka_t.movie_id;
            '''

            # mi aka_t -- Q15
            template_mi_akat_l = f'''
                SELECT * FROM aka_title AS aka_t, movie_info AS mi
                WHERE {cc} AND mi.movie_id = aka_t.movie_id;
            '''

            # mk aka_t -- Q15 aka_t (mk mc)
            template_mk_akat__mc = f'''
                SELECT * FROM aka_title AS aka_t, movie_companies AS mc, movie_keyword AS mk
                WHERE {cc} AND mk.movie_id = mc.movie_id AND mk.movie_id = aka_t.movie_id;
            '''

            # t aka_t -- Q15
            template_t_akat_l = f'''
                SELECT *
                FROM aka_title AS aka_t, title AS t
                WHERE {cc}
                AND t.id = aka_t.movie_id;
            '''

            # mc ct -- Q15 left
            template_mc_ct_l = f'''
                SELECT * FROM company_type AS ct, movie_companies AS mc
                WHERE {cc} AND ct.id = mc.company_type_id;
            '''

            # mi it -- Q15
            template_mi_it_r = f'''
                SELECT * FROM movie_info AS mi, info_type AS it
                WHERE {cc} AND it.id = mi.info_type_id;
            '''

            # mk mi -- Q15 right
            template_mk_mi_r = f'''
                SELECT * FROM movie_info AS mi, movie_keyword AS mk
                WHERE {cc} AND mk.movie_id = mi.movie_id;
            '''
            # mk mc -- Q15
            template_mk_mc_r = f'''
                select * from movie_companies AS mc, movie_keyword AS mk
                where {cc} and mk.movie_id = mc.movie_id;
            '''
            # t mi -- Q15 both
            template_t_mi_both = f'''
                SELECT * FROM movie_info AS mi, title AS t
                WHERE {cc} AND t.id = mi.movie_id;
            '''

            # mi mc -- Q15 both
            template_mi_mc = f'''
                SELECT * FROM movie_companies AS mc, movie_info AS mi
                WHERE {cc} AND {kk} AND mi.movie_id = mc.movie_id;
            '''

            # ci an -- Q7 condition on right
            template_ci_an_r = f'''
                select * from aka_name AS an, cast_info AS ci
                where {cc} and an.person_id = ci.person_id;
            '''
            # n an -- Q7 condition on both
            template_n_an = f'''
                SELECT * FROM aka_name AS an, name AS n
                WHERE {cc} AND {kk} AND an.person_id = n.id;
            '''
            # pi an -- Q7 condition on both
            template_pi_an = f'''
                SELECT * FROM aka_name AS an, person_info AS pi
                WHERE {cc} AND {kk} AND pi.person_id = an.person_id;
            '''
            # ml ci --Q7 pure
            template_ml_ci = f'''
                SELECT * FROM cast_info AS ci, movie_link AS ml
                where {cc} and ci.movie_id = ml.linked_movie_id;
            '''
            # pi ci -- Q7 condition on left
            template_pi_ci_l = f'''
                SELECT * FROM cast_info AS ci, person_info AS pi
                where {cc} and pi.person_id = ci.person_id;
            '''

            # pi it -- Q7 condition on both table
            template_pi_it = f'''
                select * from info_type AS it, person_info AS pi
                where {cc} and {kk} and it.id = pi.info_type_id;
            '''
            # ml lt -- Q7 right
            template_ml_lt_r = f'''
                SELECT * FROM link_type AS lt, movie_link AS ml
                WHERE {cc} AND lt.id = ml.link_type_id;
            '''
            
            # pi n --Q7 both
            template_pi_n = f'''
                select * from name AS n, person_info AS pi
                where {cc} and {kk} AND n.id = pi.person_id;
            '''

            # mi it -- Q14 both
            template_mi_it_both = f'''
                SELECT * FROM movie_info AS mi, info_type AS it
                WHERE {cc} AND {kk} and it.id = mi.info_type_id;
            '''
            # miidx it -- Q14 both
            template_miidx_it = f'''
                SELECT * FROM info_type AS it, movie_info_idx AS mi_idx
                where {cc} and {kk} and it.id = mi_idx.info_type_id;
            '''
            # t kt -- Q14 both
            template_t_kt = f'''
                select * from kind_type AS kt, title AS t
                where {cc} and {kk} and kt.id = t.kind_id;
            '''
            # miidx mi --Q14 both
            template_miidx_mi =f'''
                select * from movie_info AS mi, movie_info_idx AS mi_idx
                where {cc} and mi.movie_id = mi_idx.movie_id;
            '''
            # mk mi -- Q14 both
            template_mk_mi = f'''
                SELECT * FROM movie_info AS mi, movie_keyword AS mk
                WHERE {cc} AND {kk} and mk.movie_id = mi.movie_id;
            '''
            # mk miidx --Q14 r
            template_mk_miidx = f'''
                select * from movie_info_idx AS mi_idx, movie_keyword AS mk
                where {cc} and mk.movie_id = mi_idx.movie_id;
            '''
            # t miidx --Q14 both
            template_t_miidx = f'''
                select * from movie_info_idx AS mi_idx, title AS t
                where {cc} and {kk} and t.id = mi_idx.movie_id;
            '''
            # t mk -- Q14 left
            template_t_mk_l = f'''
                SELECT * FROM movie_keyword AS mk, title AS t
                WHERE {cc} AND t.id = mk.movie_id;
            '''
            # miidx it -- Q13 right
            template_miidx_it_r = f'''
                SELECT * FROM info_type AS it, movie_info_idx AS mi_idx
                where {cc} and it.id = mi_idx.info_type_id;
            '''
            # t kt -- Q13 right
            template_t_kt_right = f'''
                select * from kind_type AS kt, title AS t
                where {cc} and kt.id = t.kind_id;
            '''
            # mi mc -- Q13 mc (it mi) condition on it
            template_mi_mc__it = f'''
                select * from info_type AS it, movie_companies AS mc, movie_info AS mi
                where {cc} and it.id = mi.info_type_id and mi.movie_id = mc.movie_id;
            '''
            # miidx mc -- Q13 pure
            template_miidx_mc = f'''
                select * from movie_companies AS mc, movie_info_idx AS miidx 
                where {cc} AND miidx.movie_id = mc.movie_id;
            '''
            # t mc --Q13 mc (kt t) condition on kt
            template_t_mc__kt = f'''
                select * from kind_type AS kt, movie_companies AS mc, title AS t
                where {cc} and kt.id = t.kind_id and mc.movie_id = t.id;
            '''
            # miidx mi --Q13 miidx (it mi) condition on it
            template_miidx_mi__it = f'''
                select * from info_type AS it,movie_info AS mi,movie_info_idx AS miidx
                where {cc} and it.id = mi.info_type_id AND mi.movie_id = miidx.movie_id;
            '''
            # t mi --Q13 t (it mi) condition on it
            template_t_mi__it = f'''
                select * from info_type AS it, movie_info AS mi, title AS t
                where {cc} and mi.movie_id = t.id and it.id = mi.info_type_id; 
            '''
            # t mi --Q13 mi (kt t)
            template_t_mi__kt = f'''
                select * from kind_type AS kt, title AS t, movie_info AS mi
                where {cc} and mi.movie_id = t.id and kt.id = t.kind_id; 
            '''
            # t miidx --Q13 t (it miidx)
            template_t_miidx__it = f'''
                select * from info_type AS it, movie_info_idx AS miidx,title AS t
                where {cc} and miidx.movie_id = t.id AND it.id = miidx.info_type_id;
            '''
            # mc cn -- Q12 right
            template_mc_cn_r = f'''
                SELECT * FROM company_name AS cn, movie_companies AS mc
                WHERE {cc} AND mc.company_id = cn.id;
            '''
            # mc ct -- Q12 right
            template_mc_ct_r = f'''
                SELECT * FROM company_type AS ct, movie_companies AS mc
                WHERE {cc} AND ct.id = mc.company_type_id;
            '''
            # mi mc -- Q12 left
            template_mi_mc_l = f'''
                SELECT * FROM movie_companies AS mc, movie_info AS mi
                WHERE {cc} AND mi.movie_id = mc.movie_id;
            '''
            # miidx mc -- Q12 left
            template_miidx_mc_l = f'''
                select * from movie_companies AS mc, movie_info_idx AS mi_idx 
                where {cc} AND mi_idx.movie_id = mc.movie_id;
            '''
            # mc ct -- Q11 both
            template_mc_ct_both = f'''
                SELECT * FROM company_type AS ct, movie_companies AS mc
                WHERE {cc} AND {kk} AND ct.id = mc.company_type_id;
            '''
            # ml mc --Q11 right
            template_ml_mc_r = f'''
                select * from movie_companies AS mc,movie_link AS ml
                where {cc} and ml.movie_id = mc.movie_id;
            '''
            # t mc -- Q11 both
            template_t_mc_both = f'''
                SELECT * FROM movie_companies AS mc, title AS t
                WHERE {cc} AND {kk} AND t.id = mc.movie_id;
            '''
            # ci an -- Q8 condition on left
            template_ci_an_l = f'''
                select * from aka_name AS an, cast_info AS ci
                where {cc} and an.person_id = ci.person_id;
            '''
            # n an -- Q8 condition on left
            template_n_an_l = f'''
                SELECT * FROM aka_name AS an, name AS n
                WHERE {cc} AND an.person_id = n.id;
            '''
            # mc ci -- Q8 both
            templat_mc_ci_both = f'''
                SELECT * FROM cast_info AS ci, movie_companies AS mc
                WHERE {cc} and {kk} AND ci.movie_id = mc.movie_id;
            '''
            # n ci -- Q8 both
            template_n_ci_both = f'''
                SELECT * FROM cast_info AS ci, name AS n
                WHERE {cc} AND {kk} AND n.id = ci.person_id;
            '''
            # rt ci -- Q8 left
            template_rt_ci_r = f'''
                select * from role_type AS rt, cast_info AS ci
                where {cc} and ci.role_id = rt.id;
            '''
            # t ci -- Q8 both
            template_t_ci_both = f'''
                SELECT * FROM cast_info AS ci, title AS t
                WHERE {cc} AND {kk} AND ci.movie_id = t.id;
            '''
            # t mc -- right
            template_t_mc_r = f'''
                SELECT * FROM movie_companies AS mc, title AS t
                WHERE {cc} AND t.id = mc.movie_id;
            '''
            # ci chn -- Q9 left
            template_ci_chn_l = f'''
                SELECT * FROM char_name AS chn, cast_info AS ci
                where {cc} and chn.id = ci.person_role_id;
            '''
            # rt ci -- Q9 both
            template_rt_ci_both = f'''
                select * from role_type AS rt, cast_info AS ci
                where {cc} and {kk} AND ci.role_id = rt.id;
            '''
            # mc ci -- Q10 right
            templat_mc_ci_r = f'''
                SELECT * FROM cast_info AS ci, movie_companies AS mc
                WHERE {cc} AND ci.movie_id = mc.movie_id;
            '''
            # mc ct -- Q10 ct (ci mc) 
            template_mc_ct__ci = f'''
                SELECT * FROM cast_info AS ci, company_type AS ct, movie_companies AS mc
                WHERE {cc} and ci.movie_id = mc.movie_id AND ct.id = mc.company_type_id;
            '''
            # mc ct -- Q10 ct (cn mc)
            template_mc_ct__cn = f'''
                SELECT * FROM company_name AS cn, company_type AS ct, movie_companies AS mc
                WHERE {cc} and cn.id = mc.company_id AND ct.id = mc.company_type_id;
            '''
            # n ci -- Q6 left
            template_n_ci_l = f'''
                SELECT * FROM cast_info AS ci, name AS n
                WHERE {cc} AND n.id = ci.person_id;
            '''
            # mk ci --Q6 pure
            template_mk_ci_pure = f'''
                SELECT * FROM cast_info AS ci, movie_keyword AS mk
                where {cc} and ci.movie_id = mk.movie_id;
            '''
            # mi it -- Q5 left
            template_mi_it = f'''
                SELECT * FROM movie_info AS mi, info_type AS it
                WHERE {cc} AND it.id = mi.info_type_id;
            '''        
            # mk mc -- Q2 mk (cn mc)
            template_mk_mc__cn = f'''
                select * from company_name AS cn, movie_companies AS mc, movie_keyword AS mk
                where {cc} AND cn.id = mc.company_id and mk.movie_id = mc.movie_id;
            '''    
            # mk mc -- Q2 mc (k mk)
            template_mk_mc__k = f'''
                select * from keyword AS k, movie_companies AS mc, movie_keyword AS mk
                where {cc} AND mk.keyword_id = k.id and mk.movie_id = mc.movie_id;
            '''    
            # t mc -- Q2 t (cn mc)
            template_t_mc__cn = f'''
                SELECT * FROM company_name AS cn, movie_companies AS mc, title AS t
                WHERE {cc} AND cn.id = mc.company_id AND t.id = mc.movie_id;
            '''
            # t mk --Q2 t (k mk)
            template_t_mk__k = f'''
                SELECT * FROM keyword AS k, movie_keyword AS mk, title AS t
                WHERE {cc} AND mk.keyword_id = k.id AND t.id = mk.movie_id;
            '''
            # cct cc -- Q20 left join on subject_id
            template_cct_cc_1_l = f'''
                select * from complete_cast AS cc,comp_cast_type AS cct
                where {cc} AND cct.id = cc.subject_id;
            '''  
            # cct cc -- Q20 left join on status_id
            template_cct_cc_2_l = f'''
                select * from complete_cast AS cc,comp_cast_type AS cct
                where {cc} AND cct.id = cc.status_id;
            '''    
            # t cc -- Q20 left
            template_t_cc = f'''
                select * from complete_cast AS cc, title AS t
                where {cc} and t.id = cc.movie_id;
            '''      
            # ci chn -- Q20 right
            template_ci_chn_r = f'''
                SELECT * FROM char_name AS chn, cast_info AS ci
                where {cc} and chn.id = ci.person_role_id;
            '''
            # ci cc --Q20 ci (cc cct)
            template_ci_cc__cct = f'''
                select * from complete_cast AS cc, comp_cast_type AS cct, cast_info AS ci
                where {cc} and ci.movie_id = cc.movie_id and cct.id = cc.status_id;
            '''
            # mk cc -- Q20 mk (cc cct)
            template_mk_cc__cct = f'''
                select * from complete_cast AS cc, comp_cast_type AS cct, movie_keyword AS mk
                where {cc} and mk.movie_id = cc.movie_id and cct.id = cc.status_id;
            '''
            # mk ci -- Q20 mk (chn ci)
            template_mk_ci__chn = f'''
                SELECT * FROM char_name AS chn, cast_info AS ci, movie_keyword AS mk
                where {cc} and ci.movie_id = mk.movie_id AND chn.id = ci.person_role_id;
            '''
            # n ci -- Q20 n (chn ci)
            template_n_ci__chn = f'''
                SELECT * FROM char_name AS chn, cast_info AS ci, name AS n
                where {cc} AND chn.id = ci.person_role_id AND n.id = ci.person_id;
            '''
            # t mi --  left
            template_t_mi_l = f'''
                SELECT * FROM movie_info AS mi,title AS t
                where {cc} AND mi.movie_id = t.id;
            '''
            # ml mi -- Q21 r
            template_ml_mi_r = f'''
                select * from movie_info AS mi,movie_link AS ml
                where {cc} AND ml.movie_id = mi.movie_id;
            '''
            # ml mi -- Q22 
            template_ml_mi_both = f'''
                select * from movie_info AS mi,movie_link AS ml
                where {cc} AND ml.movie_id = mi.movie_id;
            '''
            # miidx mc -- Q22 left
            template_miidx_mc_both = f'''
                select * from movie_companies AS mc, movie_info_idx AS mi_idx 
                where {cc} AND {kk} AND mi_idx.movie_id = mc.movie_id;
            '''
            # mc cc -- Q23 pure
            template_mc_cc_pure = f'''
                select * from complete_cast AS cc,movie_companies AS mc
                where {cc} and mc.movie_id = cc.movie_id;
            '''
            # mk cc -- Q23 mk (cc mi)
            template_mk_cc__mi = f'''
                select * from complete_cast AS cc, comp_cast_type AS cct, movie_info AS mi
                where {cc} and mi.movie_id = cc.movie_id and cct.id = cc.status_id;
            '''
            # mi cc -- Q23 left
            template_mi_cc_l = f'''
                select * from complete_cast AS cc, comp_cast_type AS cct, movie_info AS mi
                where {cc} and mi.movie_id = cc.movie_id;
            '''
            # mk ci --Q24 r
            template_mk_ci_r = f'''
                SELECT * FROM cast_info AS ci, movie_keyword AS mk
                where {cc} and ci.movie_id = mk.movie_id;
            '''
            # mi ci -- Q24 both
            template_mi_ci_both = f'''
                select * from cast_info AS ci, movie_info AS mi
                where {cc} and {kk} and mi.movie_id = ci.movie_id;
            '''
            ### t ml -- Q21 left
            template_t_ml_l = f'''
                SELECT * FROM movie_link AS ml, title AS t
                WHERE {cc} AND ml.movie_id = t.id;
            '''
            ### miidx ci
            template_miidx_ci_r = f'''
                SELECT * FROM cast_info AS ci, movie_info_idx AS mi_idx 
                where {cc} AND ci.movie_id = mi_idx.movie_id;'''
            ### t ci 25
            template_t_ci_r = f'''
                SELECT * FROM cast_info AS ci,title AS t
                where {cc} AND t.id = ci.movie_id;
            '''
            ### miidx cc  q26
            template_miidx_cc_l = f'''
                SELECT * FROM complete_cast AS cc, movie_info_idx AS mi_idx
                where {cc} AND cc.movie_id = mi_idx.movie_id;
            '''
            ### mc cc q27
            template_mc_cc_l = f'''
                SELECT * FROM complete_cast AS cc,  movie_companies AS mc
                where {cc} and mc.movie_id = cc.movie_id;
            '''
            ### ml cc on cct.subject_id 27
            template_ml_cc__cct = f'''
                SELECT * FROM complete_cast AS cc, comp_cast_type AS cct, movie_link AS ml
                where {cc} and ml.movie_id = cc.movie_id AND cct.id = cc.subject_id;
            '''
            ### ml cc on cct.status_id 27
            template_ml_cc__cct = f'''
                SELECT * FROM complete_cast AS cc, comp_cast_type AS cct, movie_link AS ml
                where {cc} and ml.movie_id = cc.movie_id AND cct.id = cc.status_id;
            '''
            # pi ci -- Q7 condition on left
            template_pi_ci_both = f'''
                SELECT * FROM cast_info AS ci, person_info AS pi
                where {cc} and {kk} and pi.person_id = ci.person_id;
            '''
            # ci cc --Q30 ci (cc cct)
            template_ci_cc_l = f'''
                select * from complete_cast AS cc, cast_info AS ci
                where {cc} and ci.movie_id = cc.movie_id;
            '''
            # t miidx --Q30 left
            template_t_miidx_l = f'''
                select * from movie_info_idx AS mi_idx, title AS t
                where {cc} and t.id = mi_idx.movie_id;
            '''

            # ml miidx -- Q33 r
            template_ml_miidx_r = f'''
                select * from movie_info_idx AS mi_idx, movie_link AS ml
                where {cc} and ml.linked_movie_id = mi_idx.movie_id;
            '''

            # mk miidx -- Q31 --k
            template_mk_miidx__k = f'''
                select * from movie_info_idx AS mi_idx, movie_keyword AS mk, keyword AS k
                where {cc} and mk.movie_id = mi_idx.movie_id AND k.id = mk.keyword_id;
            '''

            template_miidx_mc__it = f'''
                select * from movie_companies AS mc, movie_info_idx AS mi_idx, info_type AS it
                where {cc} AND mi_idx.movie_id = mc.movie_id AND it.id = mi_idx.info_type_id;
            '''


            template_mc = f''' select * from movie_companies AS mc where {cc}; '''
            template_cn = f''' select * from company_name AS cn WHERE {cc}; '''
            template_it = f''' select * from info_type AS it where {cc}; '''
            template_mi = f''' select * from movie_info AS mi where {cc}; '''
            template_t = f''' select * from title AS t where {cc}; '''
            template_an = f'''select * from aka_name AS an where {cc};'''
            template_lt = f'''select * from link_type AS lt where {cc};'''
            template_n = f'''select * from name AS n where {cc};'''
            template_pi = f'''select * from person_info AS pi where {cc};'''
            template_miidx = f'''select * from movie_info_idx AS mi_idx where {cc};'''
            template_ct = f'''select * from company_type AS ct where {cc}'''
            template_ci = f'''select * from cast_info AS ci where {cc};'''
            template_cct = f'''select * from comp_cast_type AS cct where {cc};'''
            template_chn = f'''select * from char_name AS chn where {cc};'''
            template_rt = f'''select * from role_type as rt where {cc};'''
            template_k = f'''select * from keyword as k where {cc};'''
            template_kt = f'''select * from kind_type AS kt where {cc}'''
            template_mc_full = f''' select * from movie_companies AS mc; '''
            template_cn_full = f''' select * from company_name AS cn; '''
            template_it_full = f''' select * from info_type AS it; '''
            template_mi_full = f''' select * from movie_info AS mi; '''
            template_t_full = f''' select * from title AS t; '''
            template_an_full = f'''select * from aka_name AS an;'''
            template_lt_full = f'''select * from link_type AS lt;'''
            template_n_full = f'''select * from name AS n;'''
            template_pi_full = f'''select * from person_info AS pi;'''
            template_miidx_full = f'''select * from movie_info_idx AS mi_idx;'''
            template_ct_full = f'''select * from company_type AS ct'''
            template_rt_full = f'''select * from role_type AS rt;'''
            template_ci_full = f'''select * from cast_info AS ci;'''
            template_cct_full = f'''select * from comp_cast_type AS cct;'''
            template_chn_full = f'''select * from char_name AS chn;'''
            template_rt_full = f'''select * from role_type as rt;'''
            template_k_full = f'''select * from keyword as k;'''
            template_mk_full = f'''select * from movie_keyword as mk;'''
            template_ml_full = f'''select * from movie_link as ml;'''
            template_akat_full = f'''select * from aka_title AS aka_t;'''
            template_cc_full = f'''select * from complete_cast AS cc;'''




            global file_name_to_save_real_error
            
            template = template_n_ci
            file_name_to_save_real_error = 'ci-mc--n'

            left_template = template_n
            right_template = template_ci_full
            template_full = template_mc_full
            print(template)
            

            data = cal_join_selectivity(template, left_template, right_template, id_2)
            
            if data:
                print(data, cal_rel_error(data[0], data[1]), math.log(data[1] / data[0]))
                data_list.extend([data]*frequency_dict[right][id_2]*frequency_dict[left][id_1])

    output = [str(data[0]) +" "+ str(data[1]) for data in data_list]
    input()
    with open('./data/abs_error/' + file_name_to_save_real_error + '.txt', 'w') as fp:
        fp.write('\n'.join(output))


def cal_join_selectivity(join_template, left_template, right_template, id):
    global cache_right
    est_join_count, act_join_count = get_est_act_count(join_template)
    est_left_count, act_left_count = get_est_act_count(left_template)
    if id not in cache_right.keys():
        est_right_count, act_right_count = get_est_act_count(right_template)
        cache_right[id] = [est_right_count, act_right_count]
    else:
        est_right_count, act_right_count = cache_right[id]
        print("=== Use cached")
    print(f"join rows est: {est_join_count}, act: {act_join_count}")
    print(f"left rows est: {est_left_count},  act {act_left_count}")
    print(f"right rows est: {est_right_count}, act: {act_right_count}")
    if est_left_count == 0 or act_left_count == 0 or est_right_count == 0 or act_right_count == 0 or act_join_count == 0:
        return False
    est_sel_join = max(1, est_join_count) / (est_left_count * est_right_count)
    act_sel_join = max(1, act_join_count) / (act_left_count * act_right_count)
    return [act_sel_join, est_sel_join]


def cal_local_selectivity(local_template, full_table_template):
    est_count, act_count = get_est_act_count(local_template)
    est_count_full, act_count_full = get_est_act_count(full_table_template)
    if act_count_full == 0 or est_count_full == 0:
        return False
    else:
        return [max(1, act_count)/act_count_full, max(1, est_count)/act_count_full]


def get_est_act_count(template):
    join_plans = get_real_latency('imdbloadbase', template, times=1, return_json=True, limit_time=False, limit_worker=True)
    print(join_plans)
    join_plans = join_plans[0][0][0]['Plan']
    node_type = join_plans['Node Type']
    while True:
        if node_type in ['Aggregate', 'Gather', 'Sort', 'Materialize', 'Sort', 'Hash', 'Gather Merge']:
            join_plans = join_plans["Plans"][0]
            node_type = join_plans['Node Type']
        else:
            break
    print(join_plans)
    est_join_count = join_plans['Plan Rows']
    act_join_count = join_plans['Actual Rows']
    return est_join_count, act_join_count



def get_real_error_from_json(plans):
    print('\n', plans)
    if len(plans["Plans"]) < 1 or len(plans["Plans"]) > 2:
        raise ValueError('incorrect number of plans')
    
    if len(plans["Plans"]) == 2:
        print("Join T1 T2")
        act_join = plans["Actual Rows"]
        act_left = plans["Plans"][0]["Actual Rows"]
        act_right = plans["Plans"][1]["Actual Rows"]
        est_join = plans["Plan Rows"]
        est_left = plans["Plans"][0]["Plan Rows"]
        est_right = plans["Plans"][1]["Plan Rows"]
        print("Act rows of join: ", act_join, "left: ", act_left, "right: ", act_right)
        print("Est rows of join: ", est_join, "left: ", est_left, "right: ", est_right)
        
        cur_act_sel = max(1, act_join) / (max(act_left, 1) * max(act_right, 1))
        cur_est_sel = max(1, est_join) / (max(est_left, 1) * max(est_right, 1))
        
        print(f"actual sel: {cur_act_sel}, est sel: {cur_est_sel}")

    else:
        print(plans["Actual Rows"], (plans["Plans"][0]["Actual Rows"]))
        print(plans["Plan Rows"], (plans["Plans"][0]["Plan Rows"]))
        cur_act_sel = plans["Actual Rows"] / (plans["Plans"][0]["Actual Rows"])
        cur_est_sel = plans["Plan Rows"] / (plans["Plans"][0]["Plan Rows"])
        print("error")
    
    return_list = [cur_act_sel, cur_est_sel]
    return return_list
    # Don't forget to change [2] and [3] to what u need
    for i in [0, 1]:
        sub_query_location = i
        sub_act_join = plans["Plans"][sub_query_location]["Actual Rows"]
        print(plans["Plans"][sub_query_location])

        sub_act = plans["Plans"][sub_query_location]["Actual Rows"]
        sub_est = plans["Plans"][sub_query_location]["Plan Rows"]
        relation_name =  plans["Plans"][sub_query_location]["Relation Name"]
        # Might have error if it's not single relation
        sub_act_sel = max(1, sub_act) / CACHE[relation_name]
        sub_est_sel = max(1, sub_est) / CACHE[relation_name]

        # sub_act_left = plans["Plans"][sub_query_location]["Plans"][0]["Actual Rows"]
        # sub_act_right = plans["Plans"][sub_query_location]["Plans"][1]["Actual Rows"]
        # sub_est_join = plans["Plans"][sub_query_location]["Plan Rows"]
        # sub_est_left = plans["Plans"][sub_query_location]["Plans"][0]["Plan Rows"]
        # sub_est_right = plans["Plans"][sub_query_location]["Plans"][1]["Plan Rows"]

        # sub_act_left = plans["Plans"][sub_query_location]["Plans"][0]["Plans"][0]["Actual Rows"]
        # sub_act_right = plans["Plans"][sub_query_location]["Plans"][0]["Plans"][1]["Actual Rows"]
        # sub_est_join = plans["Plans"][sub_query_location]["Plan Rows"]
        # sub_est_left = plans["Plans"][sub_query_location]["Plans"][0]["Plans"][0]["Plan Rows"]
        # sub_est_right = plans["Plans"][sub_query_location]["Plans"][0]["Plans"][1]["Plan Rows"]
        # print("Act rows of mc-cn join: ", sub_act_join, "left: ", sub_act_left, "right: ", sub_act_right)
        # print("Est rows of mc-cn join: ", sub_est_join, "left: ", sub_est_left, "right: ", sub_est_right)
        # sub_act_sel = sub_act_join / (sub_act_left * sub_act_right)
        # sub_est_sel = sub_est_join / (sub_est_left * sub_est_right)
        print(f"#### {relation_name}:: actual sel: {sub_act_sel}, est sel: {sub_est_sel}, error is: {cal_rel_error(sub_act_sel, sub_est_sel)}\n")
        return_list.append(sub_act_sel)
        return_list.append(sub_est_sel)
    return return_list
    

def get_info_from_single_selection(plans, total_rows):
    print(plans)
    input()
    est_sel = max(1, plans['Plan Rows']) / total_rows
    act_sel = max(1, plans['Actual Rows']) / total_rows
    return [act_sel, est_sel]


def plot_pdf():
    print(file_name_to_save_real_error)
    with open('./data/abs_error/' + file_name_to_save_real_error + '.txt', 'r') as fp:
        lines = fp.readlines()
    data = [x.strip().split() for x in lines]
    abs_error_list = []
    cleaned_data = []
    for x in data:
        # if float(x[0]) > 0.001:
        #     continue
        # if float(x[0]) > 1 or float(x[1]) > 1 or float(x[0]) < 0 or float(x[1]) < 0:
        #     continue
        # else:
        cleaned_data.append([float(x[0])/134170, float(x[1])/134170])
    # Err = true - est
    abs_err = [float(x[0]) - float(x[1]) for x in cleaned_data]
    abs_err = sorted(abs_err)
    abs_err = np.array(abs_err).reshape(-1, 1)
    print(max(abs_err), "max abs (true-est) error")
    print(min(abs_err), "min abs (true-est) error")
    count_1 = 0
    count_2 = 0
    for i in abs_err:
        if i > 0:
            count_1 += 1
        else:
            count_2 += 1
    print(count_1/(count_1 + count_2), ": true>est ", count_2/(count_1 + count_2), ": true<est")
    kde = KernelDensity(kernel="gaussian", bandwidth=0.3).fit(abs_err)
    # plot_error(abs_err, kde, name="data/abs_error/cn-mc_abs")
    
    relative_error_list = []
    for x in data:
        if float(x[0]) == 0 or 0 == float(x[1]):
            continue
        relative_error_list.append(cal_rel_error(float(x[0]), float(x[1])))
    # print(relative_error_list)
    relative_error_list = np.array(relative_error_list).reshape(-1, 1)
    print(max(relative_error_list), "max rel error")
    print(min(relative_error_list), "min rel error")
    kde = KernelDensity(kernel="gaussian", bandwidth=1).fit(relative_error_list)
    plot_error(relative_error_list, kde, rel_error=True, name="data/abs_error/"+file_name_to_save_real_error)
    

gen_real_error()
plot_pdf()