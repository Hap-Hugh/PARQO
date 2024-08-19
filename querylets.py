basic_tables_stats = {
    'u': 'users',
    'c': 'comments',
    'b': 'badges',
    'ph': 'postHistory',
    'p': 'posts',
    'pl': 'postLinks',
    'v': 'votes',
}


def querylet(db, kk, cc, template_name):
    querylet_imdb_dict = {
        'template_mk_k_r' : f'''
            SELECT * FROM keyword AS k, movie_keyword AS mk
            WHERE {cc} AND mk.keyword_id = k.id;
            ''',
        # mk ci --Q17 --k
        'template_mk_ci__k' : f'''
            SELECT * FROM cast_info AS ci, keyword AS k, movie_keyword AS mk
            where {cc} AND mk.keyword_id = k.id and ci.movie_id = mk.movie_id;
        ''',

        # mk ci --Q17 --k
        'template_mk_ci__n' : f'''
            SELECT * FROM cast_info AS ci, movie_keyword AS mk, name AS n
            where {cc} AND n.id = ci.person_id and ci.movie_id = mk.movie_id;
        ''',

        ### t ci: use t (ci n) -- Q17
        'template_t_ci__n' : f'''
            SELECT * FROM cast_info AS ci, name AS n, title AS t
            WHERE {cc} AND n.id = ci.person_id AND ci.movie_id = t.id;
        ''',

        ### ci mc Q17 pure
        'template_ci_mc__cn' : f'''select * from cast_info AS ci, movie_companies AS mc, company_name AS cn
            where {cc} and ci.movie_id = mc.movie_id AND mc.company_id = cn.id; ''',
        'template_ci_mc__pure' : f'''select * from cast_info AS ci, movie_companies AS mc, company_name AS cn
            where {cc} and ci.movie_id = mc.movie_id AND mc.company_id = cn.id; ''',
        
        'template_ci_mc__n' : f'''select * from cast_info AS ci, movie_companies AS mc, name AS n
            where {cc} and ci.movie_id = mc.movie_id AND n.id = ci.person_id; ''',

        'template_mk_k_pure' : f'''
            SELECT * FROM keyword AS k, movie_keyword AS mk
            WHERE {cc} AND mk.keyword_id = k.id;
            ''',

        ### ml mk: use (ml) (k mk) -- Q32
        'template_ml_mk__k' : f'''
            SELECT *
            FROM keyword AS k,
                movie_keyword AS mk,
                movie_link AS ml
            WHERE {cc}
            AND mk.keyword_id = k.id
            AND mk.movie_id = ml.movie_id;
        ''',
        ### t mk: use (t) (mk) and (t) (k mk) -- Q32
        'template_t_mk_1' : f'''
            SELECT *
            FROM movie_keyword AS mk,
                title AS t
            WHERE {cc}
            AND t.id = mk.movie_id;
        ''',
        'template_t_mk_2' : f'''
            SELECT *
            FROM keyword AS k, movie_keyword AS mk, title AS t
            WHERE {cc} AND {kk} AND mk.keyword_id = k.id AND t.id = mk.movie_id
            ;
        ''',


        ### t ml: use (t) (ml) -- Q32
        'template_t_ml_l_1' : f'''
            SELECT * FROM movie_link AS ml, title AS t
            WHERE {cc} AND ml.movie_id = t.id;
        ''',
        'template_t_ml_1_pure': f'''
            SELECT * FROM movie_link AS ml, title AS t
            WHERE {cc} AND ml.movie_id = t.id;
        ''',

        ### t ml: Saved in t-ml-2.txt when join on linked_movie_id
        'template_t_ml_l_2' : f'''
            SELECT *
            FROM movie_link AS ml,
            title AS t
            WHERE {cc}
            AND ml.linked_movie_id = t.id;
        ''',
        'template_t_ml_2_pure' : f'''
            SELECT *
            FROM movie_link AS ml,
            title AS t
            WHERE {cc}
            AND ml.linked_movie_id = t.id;
        ''',


        # t ci -- Q16 condition on left
        'template_t_ci_l' : f'''
            SELECT * FROM cast_info AS ci, title AS t
            WHERE {cc} AND ci.movie_id = t.id;
        ''',

        # mc cn -- Q16
        'template_mc_cn_both' : f'''
            SELECT * FROM company_name AS cn, movie_companies AS mc
            WHERE {cc} AND {kk} AND mc.company_id = cn.id;
        ''',


        # t mc -- Q16 left
        'template_t_mc_l' : f'''
            SELECT * FROM movie_companies AS mc, title AS t
            WHERE {cc} AND t.id = mc.movie_id;
        ''',


        # t mk -- Q16
        'template_t_mk_l' : f'''
            SELECT * FROM movie_keyword AS mk, title AS t
            WHERE {cc} AND t.id = mk.movie_id;
        ''',
        'template_t_mk_pure' : f'''
            SELECT * FROM movie_keyword AS mk, title AS t
            WHERE {cc} AND t.id = mk.movie_id;
        ''',

        # n ci -- Q16 pure
        'template_n_ci__pure' : f'''
            SELECT * FROM cast_info AS ci, name AS n
            WHERE {cc} AND n.id = ci.person_id;
        ''',

        # n an -- Q16 pure
        'template_n_an__pure' : f'''
            SELECT * FROM aka_name AS an, name AS n
            WHERE {cc} AND an.person_id = n.id;
        ''',


        # ci an -- Q16 pure
        'template_ci_an__pure' : f'''
            SELECT * FROM aka_name AS an, cast_info AS ci
            Where {cc} AND an.person_id = ci.person_id;
        ''',

        'template_ci_an__t' : f'''
            SELECT * FROM aka_name AS an, cast_info AS ci, title AS t
            Where {cc} AND ci.movie_id = t.id AND an.person_id = ci.person_id;
        ''',

        # mc aka_t -- Q15
        'template_mc_akat_l' : f'''
            SELECT * FROM aka_title AS aka_t, movie_companies AS mc
            WHERE {cc} AND mc.movie_id = aka_t.movie_id;
        ''',
        'template_mc_akat_pure' : f'''
            SELECT * FROM aka_title AS aka_t, movie_companies AS mc
            WHERE {cc} AND mc.movie_id = aka_t.movie_id;
        ''',

        # mi aka_t -- Q15
        'template_mi_akat_l' : f'''
            SELECT * FROM aka_title AS aka_t, movie_info AS mi
            WHERE {cc} AND mi.movie_id = aka_t.movie_id;
        ''',
        'template_mi_akat_pure' : f'''
            SELECT * FROM aka_title AS aka_t, movie_info AS mi
            WHERE {cc} AND mi.movie_id = aka_t.movie_id;
        ''',


        # mk aka_t -- Q15 aka_t (mk mc)
        'template_mk_akat__mc' : f'''
            SELECT * FROM aka_title AS aka_t, movie_companies AS mc, movie_keyword AS mk
            WHERE {cc} AND mk.movie_id = mc.movie_id AND mk.movie_id = aka_t.movie_id;
        ''',
        'template_mk_akat_pure' : f'''
            SELECT * FROM aka_title AS aka_t, movie_keyword AS mk
            WHERE {cc} AND mk.movie_id = aka_t.movie_id;
        ''',

        # t aka_t -- Q15
        'template_t_akat_l' : f'''
            SELECT *
            FROM aka_title AS aka_t, title AS t
            WHERE {cc}
            AND t.id = aka_t.movie_id;
        ''',
        'template_t_akat_pure' : f'''
            SELECT *
            FROM aka_title AS aka_t, title AS t
            WHERE {cc}
            AND t.id = aka_t.movie_id;
        ''',

        # mc ct -- Q15 left
        'template_mc_ct_l' : f'''
            SELECT * FROM company_type AS ct, movie_companies AS mc
            WHERE {cc} AND ct.id = mc.company_type_id;
        ''',
        'template_mc_ct_pure' : f'''
            SELECT * FROM company_type AS ct, movie_companies AS mc
            WHERE {cc} AND ct.id = mc.company_type_id;
        ''',

        # mi it -- Q15
        'template_mi_it_r' : f'''
            SELECT * FROM movie_info AS mi, info_type AS it
            WHERE {cc} AND it.id = mi.info_type_id;
        ''',

        # mk mi -- Q15 right
        'template_mk_mi_r' : f'''
            SELECT * FROM movie_info AS mi, movie_keyword AS mk
            WHERE {cc} AND mk.movie_id = mi.movie_id;
        ''',
        'template_mk_mi_pure' : f'''
            SELECT * FROM movie_info AS mi, movie_keyword AS mk
            WHERE {cc} AND mk.movie_id = mi.movie_id;
        ''',
        # mk mc -- Q15
        'template_mk_mc_r' : f'''
            select * from movie_companies AS mc, movie_keyword AS mk
            where {cc} and mk.movie_id = mc.movie_id;
        ''',
        'template_mk_mc_pure' : f'''
            select * from movie_companies AS mc, movie_keyword AS mk
            where {cc} and mk.movie_id = mc.movie_id;
        ''',
        # t mi -- Q15 both
        'template_t_mi_both' : f'''
            SELECT * FROM movie_info AS mi, title AS t
            WHERE {cc} AND t.id = mi.movie_id;
        ''',

        # mi mc -- Q15 both
        'template_mi_mc_both' : f'''
            SELECT * FROM movie_companies AS mc, movie_info AS mi
            WHERE {cc} AND {kk} AND mi.movie_id = mc.movie_id;
        ''',

        # ci an -- Q7 condition on right
        'template_ci_an_r' : f'''
            select * from aka_name AS an, cast_info AS ci
            where {cc} and an.person_id = ci.person_id;
        ''',
        # n an -- Q7 condition on both
        'template_n_an_both' : f'''
            SELECT * FROM aka_name AS an, name AS n
            WHERE {cc} AND {kk} AND an.person_id = n.id;
        ''',
        # pi an -- Q7 condition on both
        'template_pi_an_both' : f'''
            SELECT * FROM aka_name AS an, person_info AS pi
            WHERE {cc} AND {kk} AND pi.person_id = an.person_id;
        ''',
        # ml ci --Q7 pure
        'template_ml_ci_pure' : f'''
            SELECT * FROM cast_info AS ci, movie_link AS ml
            where {cc} and ci.movie_id = ml.linked_movie_id;
        ''',
        # pi ci -- Q7 condition on left
        'template_pi_ci_l' : f'''
            SELECT * FROM cast_info AS ci, person_info AS pi
            where {cc} and pi.person_id = ci.person_id;
        ''',

        # pi it -- Q7 condition on both table
        'template_pi_it_both' : f'''
            select * from info_type AS it, person_info AS pi
            where {cc} and {kk} and it.id = pi.info_type_id;
        ''',
        # ml lt -- Q7 right
        'template_ml_lt_r' : f'''
            SELECT * FROM link_type AS lt, movie_link AS ml
            WHERE {cc} AND lt.id = ml.link_type_id;
        ''',

        # pi n --Q7 both
        'template_pi_n_both' : f'''
            select * from name AS n, person_info AS pi
            where {cc} and {kk} AND n.id = pi.person_id;
        ''',

        # mi it -- Q14 both
        'template_mi_it_both' : f'''
            SELECT * FROM movie_info AS mi, info_type AS it
            WHERE {cc} AND {kk} and it.id = mi.info_type_id;
        ''',
        # mi_idx it -- Q14 both
        'template_mi_idx_it_both' : f'''
            SELECT * FROM info_type AS it, movie_info_idx AS mi_idx
            where {cc} and {kk} and it.id = mi_idx.info_type_id;
        ''',
        # t kt -- Q14 both
        'template_t_kt_both' : f'''
            select * from kind_type AS kt, title AS t
            where {cc} and {kk} and kt.id = t.kind_id;
        ''',
        # mi_idx mi --Q14 both
        'template_mi_idx_mi_both' : f'''
            select * from movie_info AS mi, movie_info_idx AS mi_idx
            where {cc} and {kk} and mi.movie_id = mi_idx.movie_id;
        ''',

        'template_mi_idx_mi_r' : f'''
            select * from movie_info AS mi, movie_info_idx AS mi_idx
            where {cc} and mi.movie_id = mi_idx.movie_id;
        ''',
        # mk mi -- Q14 both
        # 'template_mk_mi_both' : f'''
        #     SELECT * FROM movie_info AS mi, movie_keyword AS mk
        #     WHERE {cc} AND {kk} and mk.movie_id = mi.movie_id;
        # ''',
        # mk mi_idx --Q14 r
        'template_mk_mi_idx_r' : f'''
            select * from movie_info_idx AS mi_idx, movie_keyword AS mk
            where {cc} and mk.movie_id = mi_idx.movie_id;
        ''',
        'template_mk_mi_idx_pure' : f'''
            select * from movie_info_idx AS mi_idx, movie_keyword AS mk
            where {cc} and mk.movie_id = mi_idx.movie_id;
        ''',
        # t mi_idx --Q14 both
        'template_t_mi_idx_both' : f'''
            select * from movie_info_idx AS mi_idx, title AS t
            where {cc} and {kk} and t.id = mi_idx.movie_id;
        ''',
        # t mk -- Q14 left
        'template_t_mk_l' : f'''
            SELECT * FROM movie_keyword AS mk, title AS t
            WHERE {cc} AND t.id = mk.movie_id;
        ''',
        # mi_idx it -- Q13 right
        'template_mi_idx_it_r' : f'''
            SELECT * FROM info_type AS it, movie_info_idx AS mi_idx
            where {cc} and it.id = mi_idx.info_type_id;
        ''',
        'template_mi_idx_it_pure' : f'''
            SELECT * FROM info_type AS it, movie_info_idx AS mi_idx
            where {cc} and it.id = mi_idx.info_type_id;
        ''',
        # t kt -- Q13 right
        'template_t_kt_r' : f'''
            select * from kind_type AS kt, title AS t
            where {cc} and kt.id = t.kind_id;
        ''',
        'template_t_kt_pure' : f'''
            select * from kind_type AS kt, title AS t
            where {cc} and kt.id = t.kind_id;
        ''',
        # mi mc -- Q13 mc (it mi) condition on it
        'template_mi_mc__it' : f'''
            select * from info_type AS it, movie_companies AS mc, movie_info AS mi
            where {cc} and it.id = mi.info_type_id and mi.movie_id = mc.movie_id;
        ''',
        # mi_idx mc -- Q13 pure
        'template_mi_idx_mc_pure' : f'''
            select * from movie_companies AS mc, movie_info_idx AS mi_idx 
            where {cc} AND mi_idx.movie_id = mc.movie_id;
        ''',
        # t mc --Q13 mc (kt t) condition on kt
        'template_t_mc__kt' : f'''
            select * from kind_type AS kt, movie_companies AS mc, title AS t
            where {cc} and kt.id = t.kind_id and mc.movie_id = t.id;
        ''',
        # mi_idx mi --Q13 mi_idx (it mi) condition on it
        'template_mi_idx_mi__it' : f'''
            select * from info_type AS it,movie_info AS mi,movie_info_idx AS mi_idx
            where {cc} and it.id = mi.info_type_id AND mi.movie_id = mi_idx.movie_id;
        ''',
        # t mi --Q13 t (it mi) condition on it
        'template_t_mi__it' : f'''
            select * from info_type AS it, movie_info AS mi, title AS t
            where {cc} and mi.movie_id = t.id and it.id = mi.info_type_id; 
        ''',
        # t mi --Q13 mi (kt t)
        'template_t_mi__kt' : f'''
            select * from kind_type AS kt, title AS t, movie_info AS mi
            where {cc} and mi.movie_id = t.id and kt.id = t.kind_id; 
        ''',
        # t mi_idx --Q13 t (it mi_idx)
        'template_t_mi_idx__it' : f'''
            select * from info_type AS it, movie_info_idx AS mi_idx,title AS t
            where {cc} and mi_idx.movie_id = t.id AND it.id = mi_idx.info_type_id;
        ''',
        # mc cn -- Q12 right
        'template_mc_cn_r' : f'''
            SELECT * FROM company_name AS cn, movie_companies AS mc
            WHERE {cc} AND mc.company_id = cn.id;
        ''',
        'template_mc_cn_pure' : f'''
            SELECT * FROM company_name AS cn, movie_companies AS mc
            WHERE {cc} AND mc.company_id = cn.id;
        ''',
        # mc ct -- Q12 right
        'template_mc_ct_r' : f'''
            SELECT * FROM company_type AS ct, movie_companies AS mc
            WHERE {cc} AND ct.id = mc.company_type_id;
        ''',
        # mi mc -- Q12 left
        'template_mi_mc_l' : f'''
            SELECT * FROM movie_companies AS mc, movie_info AS mi
            WHERE {cc} AND mi.movie_id = mc.movie_id;
        ''',
        'template_mi_mc_pure' : f'''
            SELECT * FROM movie_companies AS mc, movie_info AS mi
            WHERE {cc} AND mi.movie_id = mc.movie_id;
        ''',
        # mi_idx mc -- Q12 left
        'template_mi_idx_mc_l' : f'''
            select * from movie_companies AS mc, movie_info_idx AS mi_idx 
            where {cc} AND mi_idx.movie_id = mc.movie_id;
        ''',
        # mi_idx mc -- Q1 right
        'template_mi_idx_mc_r' : f'''
            select * from movie_companies AS mc, movie_info_idx AS mi_idx 
            where {cc} AND mi_idx.movie_id = mc.movie_id;
        ''',
        # mc ct -- Q11 both
        'template_mc_ct_both' : f'''
            SELECT * FROM company_type AS ct, movie_companies AS mc
            WHERE {cc} AND {kk} AND ct.id = mc.company_type_id;
        ''',
        # ml mc --Q11 right
        'template_ml_mc_r' : f'''
            select * from movie_companies AS mc,movie_link AS ml
            where {cc} and ml.movie_id = mc.movie_id;
        ''',
        # t mc -- Q11 both
        'template_t_mc_both' : f'''
            SELECT * FROM movie_companies AS mc, title AS t
            WHERE {cc} AND {kk} AND t.id = mc.movie_id;
        ''',
        # ci an -- Q8 condition on left
        'template_ci_an_l' : f'''
            select * from aka_name AS an, cast_info AS ci
            where {cc} and an.person_id = ci.person_id;
        ''',
        # n an -- Q8 condition on left
        'template_n_an_l' : f'''
            SELECT * FROM aka_name AS an, name AS n
            WHERE {cc} AND an.person_id = n.id;
        ''',
        # mc ci -- Q8 both
        'template_mc_ci_both' : f'''
            SELECT * FROM cast_info AS ci, movie_companies AS mc
            WHERE {cc} and {kk} AND ci.movie_id = mc.movie_id;
        ''',
        # n ci -- Q8 both
        'template_n_ci_both' : f'''
            SELECT * FROM cast_info AS ci, name AS n
            WHERE {cc} AND {kk} AND n.id = ci.person_id;
        ''',
        # rt ci -- Q8 left
        'template_rt_ci_r' : f'''
            select * from role_type AS rt, cast_info AS ci
            where {cc} and ci.role_id = rt.id;
        ''',
        # t ci -- Q8 both
        'template_t_ci_both' : f'''
            SELECT * FROM cast_info AS ci, title AS t
            WHERE {cc} AND {kk} AND ci.movie_id = t.id;
        ''',
        # t mc -- right
        'template_t_mc_r' : f'''
            SELECT * FROM movie_companies AS mc, title AS t
            WHERE {cc} AND t.id = mc.movie_id;
        ''',
        'template_t_mc_pure' : f'''
            SELECT * FROM movie_companies AS mc, title AS t
            WHERE {cc} AND t.id = mc.movie_id;
        ''',
        # ci chn -- Q9 left
        'template_ci_chn_l' : f'''
            SELECT * FROM char_name AS chn, cast_info AS ci
            where {cc} and chn.id = ci.person_role_id;
        ''',
        'template_ci_chn_pure' : f'''
            SELECT * FROM char_name AS chn, cast_info AS ci
            where {cc} and chn.id = ci.person_role_id;
        ''',
        # rt ci -- Q9 both
        'template_rt_ci_both' : f'''
            select * from role_type AS rt, cast_info AS ci
            where {cc} and {kk} AND ci.role_id = rt.id;
        ''',
        # mc ci -- Q10 right
        'template_mc_ci_r' : f'''
            SELECT * FROM cast_info AS ci, movie_companies AS mc
            WHERE {cc} AND ci.movie_id = mc.movie_id;
        ''',
        'template_mc_ci_pure' : f'''
            SELECT * FROM cast_info AS ci, movie_companies AS mc
            WHERE {cc} AND ci.movie_id = mc.movie_id;
        ''',
        # mc ct -- Q10 ct (ci mc) 
        'template_mc_ct__ci' : f'''
            SELECT * FROM cast_info AS ci, company_type AS ct, movie_companies AS mc
            WHERE {cc} and ci.movie_id = mc.movie_id AND ct.id = mc.company_type_id;
        ''',
        # mc ct -- Q10 ct (cn mc)
        'template_mc_ct__cn' : f'''
            SELECT * FROM company_name AS cn, company_type AS ct, movie_companies AS mc
            WHERE {cc} and cn.id = mc.company_id AND ct.id = mc.company_type_id;
        ''',
        # n ci -- Q6 left
        'template_n_ci_l' : f'''
            SELECT * FROM cast_info AS ci, name AS n
            WHERE {cc} AND n.id = ci.person_id;
        ''',
        # mk ci --Q6 pure
        'template_mk_ci_pure' : f'''
            SELECT * FROM cast_info AS ci, movie_keyword AS mk
            where {cc} and ci.movie_id = mk.movie_id;
        ''',
        # mi it -- Q5 left
        'template_mi_it_l' : f'''
            SELECT * FROM movie_info AS mi, info_type AS it
            WHERE {cc} AND it.id = mi.info_type_id;
        ''',        
        'template_mi_it_pure' : f'''
            SELECT * FROM movie_info AS mi, info_type AS it
            WHERE {cc} AND it.id = mi.info_type_id;
        ''',    
        # mk mc -- Q2 mk (cn mc)
        'template_mk_mc__cn' : f'''
            select * from company_name AS cn, movie_companies AS mc, movie_keyword AS mk
            where {cc} AND cn.id = mc.company_id and mk.movie_id = mc.movie_id;
        ''',    
        # mk mc -- Q2 mc (k mk)
        'template_mk_mc__k' : f'''
            select * from keyword AS k, movie_companies AS mc, movie_keyword AS mk
            where {cc} AND mk.keyword_id = k.id and mk.movie_id = mc.movie_id;
        ''',    
        # t mc -- Q2 t (cn mc)
        'template_t_mc__cn' : f'''
            SELECT * FROM company_name AS cn, movie_companies AS mc, title AS t
            WHERE {cc} AND cn.id = mc.company_id AND t.id = mc.movie_id;
        ''',
        # t mk --Q2 t (k mk)
        'template_t_mk__k' : f'''
            SELECT * FROM keyword AS k, movie_keyword AS mk, title AS t
            WHERE {cc} AND mk.keyword_id = k.id AND t.id = mk.movie_id;
        ''',
        # cct cc -- Q20 left join on subject_id
        'template_cct_cc_1_l' : f'''
            select * from complete_cast AS cc,comp_cast_type AS cct
            where {cc} AND cct.id = cc.subject_id;
        ''',  
        # cct cc -- Q20 left join on status_id
        'template_cct_cc_2_l' : f'''
            select * from complete_cast AS cc,comp_cast_type AS cct
            where {cc} AND cct.id = cc.status_id;
        ''',    
        'template_cct_cc_pure' : f'''
            select * from complete_cast AS cc,comp_cast_type AS cct
            where {cc} AND cct.id = cc.subject_id;
        ''',
        # t cc -- Q20 left
        'template_t_cc_l' : f'''
            select * from complete_cast AS cc, title AS t
            where {cc} and t.id = cc.movie_id;
        ''',   
        'template_t_cc_pure' : f'''
            select * from complete_cast AS cc, title AS t
            where {cc} and t.id = cc.movie_id;
        ''',      
        # ci chn -- Q20 right
        'template_ci_chn_r' : f'''
            SELECT * FROM char_name AS chn, cast_info AS ci
            where {cc} and chn.id = ci.person_role_id;
        ''',
        # ci cc --Q20 ci (cc cct)
        'template_ci_cc__cct' : f'''
            select * from complete_cast AS cc, comp_cast_type AS cct, cast_info AS ci
            where {cc} and ci.movie_id = cc.movie_id and cct.id = cc.status_id;
        ''',
        # mk cc -- Q20 mk (cc cct)
        'template_mk_cc__cct' : f'''
            select * from complete_cast AS cc, comp_cast_type AS cct, movie_keyword AS mk
            where {cc} and mk.movie_id = cc.movie_id and cct.id = cc.status_id;
        ''',
        'template_mk_cc_pure' : f'''
            select * from complete_cast AS cc, movie_keyword AS mk
            where {cc} and mk.movie_id = cc.movie_id;
        ''',
        # mk ci -- Q20 mk (chn ci)
        'template_mk_ci__chn' : f'''
            SELECT * FROM char_name AS chn, cast_info AS ci, movie_keyword AS mk
            where {cc} and ci.movie_id = mk.movie_id AND chn.id = ci.person_role_id;
        ''',
        # n ci -- Q20 n (chn ci)
        'template_n_ci__chn' : f'''
            SELECT * FROM char_name AS chn, cast_info AS ci, name AS n
            where {cc} AND chn.id = ci.person_role_id AND n.id = ci.person_id;
        ''',
        # t mi --  left
        'template_t_mi_l' : f'''
            SELECT * FROM movie_info AS mi,title AS t
            where {cc} AND mi.movie_id = t.id;
        ''',
        # t mi --  right
        'template_t_mi_r' : f'''
            SELECT * FROM movie_info AS mi,title AS t
            where {cc} AND mi.movie_id = t.id;
        ''',
        'template_t_mi_pure' : f'''
            SELECT * FROM movie_info AS mi,title AS t
            where {cc} AND mi.movie_id = t.id;
        ''',
        # ml mi -- Q21 r
        'template_ml_mi_r' : f'''
            select * from movie_info AS mi,movie_link AS ml
            where {cc} AND ml.movie_id = mi.movie_id;
        ''',
        # ml mi -- Q22 
        'template_ml_mi_both' : f'''
            select * from movie_info AS mi,movie_link AS ml
            where {cc} AND ml.movie_id = mi.movie_id;
        ''',
        # mi_idx mc -- Q22 left
        'template_mi_idx_mc_both' : f'''
            select * from movie_companies AS mc, movie_info_idx AS mi_idx 
            where {cc} AND {kk} AND mi_idx.movie_id = mc.movie_id;
        ''',
        # mc cc -- Q23 pure
        'template_mc_cc_pure' : f'''
            select * from complete_cast AS cc,movie_companies AS mc
            where {cc} and mc.movie_id = cc.movie_id;
        ''',
        # mk cc -- Q23 mk (cc mi)
        'template_mk_cc__mi' : f'''
            select * from complete_cast AS cc, comp_cast_type AS cct, movie_info AS mi
            where {cc} and mi.movie_id = cc.movie_id and cct.id = cc.status_id;
        ''',
        # mi cc -- Q23 left
        'template_mi_cc_l' : f'''
            select * from complete_cast AS cc, comp_cast_type AS cct, movie_info AS mi
            where {cc} and mi.movie_id = cc.movie_id;
        ''',
        # mk ci --Q24 r
        'template_mk_ci_r' : f'''
            SELECT * FROM cast_info AS ci, movie_keyword AS mk
            where {cc} and ci.movie_id = mk.movie_id;
        ''',
        # mi ci -- Q24 both
        'template_mi_ci_both' : f'''
            select * from cast_info AS ci, movie_info AS mi
            where {cc} and {kk} and mi.movie_id = ci.movie_id;
        ''',
        'template_mi_ci_pure' : f'''
            select * from cast_info AS ci, movie_info AS mi
            where {cc} and mi.movie_id = ci.movie_id;
        ''',
        ### t ml -- Q21 left
        'template_t_ml_l' : f'''
            SELECT * FROM movie_link AS ml, title AS t
            WHERE {cc} AND ml.movie_id = t.id;
        ''',
        ### mi_idx ci
        'template_mi_idx_ci_r' : f'''
            SELECT * FROM cast_info AS ci, movie_info_idx AS mi_idx 
            where {cc} AND ci.movie_id = mi_idx.movie_id;''',
        'template_mi_idx_ci_l' : f'''
            SELECT * FROM cast_info AS ci, movie_info_idx AS mi_idx 
            where {cc} AND ci.movie_id = mi_idx.movie_id;''',
        'template_mi_idx_ci_pure' : f'''
            SELECT * FROM cast_info AS ci, movie_info_idx AS mi_idx 
            where {cc} AND ci.movie_id = mi_idx.movie_id;''',
        
        ### t ci 25
        'template_t_ci_r' : f'''
            SELECT * FROM cast_info AS ci,title AS t
            where {cc} AND t.id = ci.movie_id;
        ''',
        'template_t_ci_pure' : f'''
            SELECT * FROM cast_info AS ci,title AS t
            where {cc} AND t.id = ci.movie_id;
        ''',
        ### mi_idx cc  q26
        'template_mi_idx_cc_l' : f'''
            SELECT * FROM complete_cast AS cc, movie_info_idx AS mi_idx
            where {cc} AND cc.movie_id = mi_idx.movie_id;
        ''',
        'template_mi_idx_cc_pure' : f'''
            SELECT * FROM complete_cast AS cc, movie_info_idx AS mi_idx
            where {cc} AND cc.movie_id = mi_idx.movie_id;
        ''',
        ### mc cc q27
        'template_mc_cc_l' : f'''
            SELECT * FROM complete_cast AS cc,  movie_companies AS mc
            where {cc} and mc.movie_id = cc.movie_id;
        ''',
        ### ml cc on cct.subject_id 27
        'template_ml_cc__cct_1' : f'''
            SELECT * FROM complete_cast AS cc, comp_cast_type AS cct, movie_link AS ml
            where {cc} and ml.movie_id = cc.movie_id AND cct.id = cc.subject_id;
        ''',
        ### ml cc on cct.status_id 27
        'template_ml_cc__cct_2' : f'''
            SELECT * FROM complete_cast AS cc, comp_cast_type AS cct, movie_link AS ml
            where {cc} and ml.movie_id = cc.movie_id AND cct.id = cc.status_id;
        ''',
        # pi ci -- Q7 condition on left
        'template_pi_ci_both' : f'''
            SELECT * FROM cast_info AS ci, person_info AS pi
            where {cc} and {kk} and pi.person_id = ci.person_id;
        ''',
        # ci cc --Q30 ci (cc cct)
        'template_ci_cc_l' : f'''
            select * from complete_cast AS cc, cast_info AS ci
            where {cc} and ci.movie_id = cc.movie_id;
        ''',
        'template_ci_cc_pure' : f'''
            select * from complete_cast AS cc, cast_info AS ci
            where {cc} and ci.movie_id = cc.movie_id;
        ''',
        # t mi_idx --Q30 left
        'template_t_mi_idx_l' : f'''
            select * from movie_info_idx AS mi_idx, title AS t
            where {cc} and t.id = mi_idx.movie_id;
        ''',
        'template_t_mi_idx_pure' : f'''
            select * from movie_info_idx AS mi_idx, title AS t
            where {cc} and t.id = mi_idx.movie_id;
        ''',

        # ml mi_idx -- Q33 r
        'template_ml_mi_idx_r' : f'''
            select * from movie_info_idx AS mi_idx, movie_link AS ml
            where {cc} and ml.linked_movie_id = mi_idx.movie_id;
        ''',

        # mk mi_idx -- Q31 --k
        'template_mk_mi_idx__k' : f'''
            select * from movie_info_idx AS mi_idx, movie_keyword AS mk, keyword AS k
            where {cc} and mk.movie_id = mi_idx.movie_id AND k.id = mk.keyword_id;
        ''',

        'template_mi_idx_mc__it' : f'''
            select * from movie_companies AS mc, movie_info_idx AS mi_idx, info_type AS it
            where {cc} AND mi_idx.movie_id = mc.movie_id AND it.id = mi_idx.info_type_id;
        ''',


        'template_mc' : f''' select * from movie_companies AS mc where {cc}; ''',
        'template_cn' : f''' select * from company_name AS cn WHERE {cc}; ''',
        'template_it' : f''' select * from info_type AS it where {cc}; ''',
        'template_mi' : f''' select * from movie_info AS mi where {cc}; ''',
        'template_t' : f''' select * from title AS t where {cc}; ''',
        'template_an' : f'''select * from aka_name AS an where {cc};''',
        'template_lt' : f'''select * from link_type AS lt where {cc};''',
        'template_n' : f'''select * from name AS n where {cc};''',
        'template_pi' : f'''select * from person_info AS pi where {cc};''',
        'template_mi_idx' : f'''select * from movie_info_idx AS mi_idx where {cc};''',
        'template_ct' : f'''select * from company_type AS ct where {cc}''',
        'template_ci' : f'''select * from cast_info AS ci where {cc};''',
        'template_cct' : f'''select * from comp_cast_type AS cct where {cc};''',
        'template_chn' : f'''select * from char_name AS chn where {cc};''',
        'template_rt' : f'''select * from role_type as rt where {cc};''',
        'template_k' : f'''select * from keyword as k where {cc};''',
        'template_kt' : f'''select * from kind_type AS kt where {cc}''',
        'template_mc_full' : f''' select * from movie_companies AS mc; ''',
        'template_cn_full' : f''' select * from company_name AS cn; ''',
        'template_it_full' : f''' select * from info_type AS it; ''',
        'template_mi_full' : f''' select * from movie_info AS mi; ''',
        'template_t_full' : f''' select * from title AS t; ''',
        'template_an_full' : f'''select * from aka_name AS an;''',
        'template_lt_full' : f'''select * from link_type AS lt;''',
        'template_n_full' : f'''select * from name AS n;''',
        'template_pi_full' : f'''select * from person_info AS pi;''',
        'template_mi_idx_full' : f'''select * from movie_info_idx AS mi_idx;''',
        'template_ct_full' : f'''select * from company_type AS ct''',
        'template_rt_full' : f'''select * from role_type AS rt;''',
        'template_ci_full' : f'''select * from cast_info AS ci;''',
        'template_cct_full' : f'''select * from comp_cast_type AS cct;''',
        'template_chn_full' : f'''select * from char_name AS chn;''',
        'template_rt_full' : f'''select * from role_type as rt;''',
        'template_k_full' : f'''select * from keyword as k;''',
        'template_mk_full' : f'''select * from movie_keyword as mk;''',
        'template_ml_full' : f'''select * from movie_link as ml;''',
        'template_akat_full' : f'''select * from aka_title AS aka_t;''',
        'template_cc_full' : f'''select * from complete_cast AS cc;''',
        'template_kt_full' : f'''select * from kind_type AS kt;''',
    }
    
    basic_tables = {
            "call_center": [], "catalog_returns": [],
            "catalog_sales": [], "customer": [], 
            "customer_address": [], "customer_demographics": [],
            "date_dim": [],
            "household_demographics": [],
            "income_band": [], "item": [],
            "ship_mode": [], "store": [], "store_sales": [],
            "warehouse": [], "web_sales": [], "store_returns": []
        }

    querylet_dsb_dict = {
        'template_store_sales_store_returns_l': f"select * from store_sales, store_returns where {cc} and ss_item_sk = sr_item_sk;",
        'template_web_sales_store_sales_r': f"select * from store_sales, web_sales where {cc} and ss_customer_sk = ws_bill_customer_sk;",
        'template_item_store_sales_both': f"select * from store_sales, item where {cc} and {kk} and i_item_sk = ss_item_sk;",
        'template_customer_store_sales_r': f"select * from store_sales, customer where {cc} and ss_customer_sk = c_customer_sk;",
        'template_customer_store_sales__date_dim': f"select * from store_sales, customer, date_dim where {cc} and ss_customer_sk = c_customer_sk and d_date_sk = ss_sold_date_sk;",
        'template_item_store_returns_l': f"select * from store_returns, item where {cc} and i_item_sk = sr_item_sk;",
        'template_item_store_returns__date_dim': f"select * from store_returns, item, date_dim where {cc} and i_item_sk = sr_item_sk and sr_returned_date_sk = d_date_sk;",
        'template_item_web_sales_l': f"select * from item, web_sales where {cc} and i_item_sk = ws_item_sk",
        'template_date_dim_date_dim_non_1': f"select * from date_dim d1, date_dim d2 where {cc} AND d2.d_date between d1.d_date AND (d1.d_date + interval '90 day')",
        'template_customer_address_customer_l': f"select * from customer, customer_address where {cc} and c_current_addr_sk = ca_address_sk;",
        'template_household_demographics_customer_l': f"select * from customer, household_demographics where {cc} and c_current_hdemo_sk = hd_demo_sk;",
        'template_store_sales_store_sales_both': f"select * from store_sales AS s1, store_sales AS s2 where {cc} and {kk} and s1.ss_ticket_number = s2.ss_ticket_number;",
        'template_customer_demographics_customer_l': f"select * from customer, customer_demographics where {cc} and c_current_cdemo_sk = cd_demo_sk;",
        'template_date_dim_store_sales_both': f"select * from date_dim, store_sales where {cc} and {kk} and d_date_sk = ss_sold_date_sk;",
        'template_date_dim_store_sales_l': f"select * from date_dim, store_sales where {cc} and d_date_sk = ss_sold_date_sk;",
        'template_store_store_sales__date_dim': f"select * from store, store_sales, date_dim where {cc} and ss_store_sk = s_store_sk and d_date_sk = ss_sold_date_sk;",
        
        'template_item_store_sales__date_dim': f"select * from store_sales, item, date_dim where {cc} and i_item_sk = ss_item_sk and d_date_sk = ss_sold_date_sk;",
        'template_item_store_sales_l': f"select * from store_sales, item where {cc} and i_item_sk = ss_item_sk;",
        'template_date_dim_web_sales_r': f"select * from date_dim, web_sales where {cc} and ws_sold_date_sk = d_date_sk;",
        'template_customer_web_sales_r': f"select * from web_sales, customer where {cc} and ws_bill_customer_sk = c_customer_sk;",
        'template_inventory_web_sales_r': f"select * from web_sales, inventory where {cc} and ws_warehouse_sk = inv_warehouse_sk;",
        'template_warehouse_web_sales_r': f"select * from web_sales, warehouse where {cc} and ws_warehouse_sk = w_warehouse_sk;",
        'template_item_web_sales_both': f"select * from web_sales, item where {cc} and {kk} and ws_item_sk=i_item_sk;",
        'template_date_dim_date_dim_non_2': f"select * from date_dim d1, date_dim d2 where {cc} AND d2.d_date between d1.d_date AND (d1.d_date + interval '30 day')",
        'template_inventory_item_r': f"select * from inventory, item where {cc} and inv_item_sk = i_item_sk;",
        'template_warehouse_catalog_sales_r': f"select * from warehouse, catalog_sales where {cc} and cs_warehouse_sk = w_warehouse_sk;",
        'template_ship_mode_catalog_sales_both': f"select * from ship_mode, catalog_sales where {cc} and {kk} and cs_ship_mode_sk   = sm_ship_mode_sk;",
        'template_call_center_catalog_sales_both': f"select * from call_center, catalog_sales where {cc} and {kk} and cs_call_center_sk = cc_call_center_sk;",
        'template_date_dim_catalog_sales_both': f"select * from date_dim, catalog_sales where {cc} and {kk} and cs_ship_date_sk = d_date_sk; ",
        'template_date_dim_catalog_returns_l': f"select * from date_dim, catalog_returns where {cc} and cr_returned_date_sk     = d_date_sk;",
        'template_web_returns_web_sales_r': f"select * from web_returns, web_sales where {cc} and ws_item_sk = wr_item_sk AND ws_order_number = wr_order_number; ",
        'template_web_page_web_sales_r': f"select * from web_page, web_sales where {cc} and ws_web_page_sk = wp_web_page_sk;",
        # 'template_customer_demographics_web_sales_both': f"select * from customer_demographics, web_sales_both where {cc} and {kk} and ",
        'template_date_dim_web_sales_both': f"select * from date_dim, web_sales where {cc} and {kk} and ws_sold_date_sk = d_date_sk;",
        'template_customer_demographics_web_returns_l': f"select * from customer_demographics, web_returns where {cc} and cd_demo_sk = wr_refunded_cdemo_sk;",
        'template_customer_address_web_returns_l': f"select * from customer_address, web_returns where {cc} and ca_address_sk = wr_refunded_addr_sk;",
        'template_customer_demographics_customer_demographics_l': f"select * from customer_demographics cd1, customer_demographics cd2 where {cc} and cd1.cd_marital_status = cd2.cd_marital_status and cd1.cd_education_status = cd2.cd_education_status;",
        'template_customer_demographics_catalog_sales_both': f"select * from customer_demographics, catalog_sales where {cc} and {kk} and cs_bill_cdemo_sk = cd_demo_sk;",
        'template_customer_catalog_sales_both': f"select * from customer, catalog_sales where {cc} and {kk} and cs_bill_customer_sk = c_customer_sk;",
        'template_item_catalog_sales_both': f"select * from item, catalog_sales where {cc} and {kk} and cs_item_sk = i_item_sk;",
        'template_item_catalog_sales__date_dim': f"select * from item, catalog_sales, date_dim where {cc} and cs_item_sk = i_item_sk and cs_sold_date_sk = d_date_sk;",
        'template_customer_address_customer_both': f"select * from customer_address, customer where {cc} and {kk} and c_current_addr_sk = ca_address_sk;",
        'template_store_store_sales_r': f"select * from store, store_sales where {cc} and s_store_sk = ss_store_sk;",
        'template_customer_demographics_store_sales_both': f"select * from customer_demographics, store_sales where {cc} and {kk} and cd_demo_sk = ss_cdemo_sk;",
        'template_household_demographics_store_sales_both': f"select * from household_demographics, store_sales where {cc} and {kk} and ss_hdemo_sk=hd_demo_sk;",
        'template_customer_address_store_sales_both': f"select * from customer_address, store_sales where {cc} and {kk} and ss_addr_sk = ca_address_sk;",
        'template_household_demographics_customer_demographics_both': f"select * from household_demographics, customer_demographics where {cc} and {kk} and cd_demo_sk=hd_demo_sk;",
        'template_date_dim_store_returns_l': f"select * from date_dim, store_returns where {cc} and sr_returned_date_sk = d_date_sk;",
        'template_date_dim_catalog_sales_l': f"select * from date_dim, catalog_sales where {cc} and cs_sold_date_sk = d_date_sk;",
        'template_customer_demographics_store_sales_l': f"select * from customer_demographics, store_sales where {cc} and cd_demo_sk = ss_cdemo_sk;",
        'template_store_store_sales_l': f"select * from store, store_sales where {cc} and ss_store_sk = s_store_sk;",
        'template_catalog_returns_catalog_sales_both': f"select * from catalog_sales LEFT OUTER JOIN catalog_returns ON (cs_order_number = cr_order_number AND cs_item_sk = cr_item_sk) where {cc} and {kk} ;",
        'template_item_catalog_returns_both': f"select * from item, catalog_returns where {cc} and {kk} and cr_item_sk = i_item_sk;",
        'template_store_returns_store_sales_r': f"select * from store_returns, store_sales where {cc} and ss_ticket_number = sr_ticket_number AND ss_item_sk = sr_item_sk and ss_customer_sk = sr_customer_sk and ss_store_sk = sr_store_sk;",
        'template_date_dim_date_dim_non_2': f"select * from date_dim d1, date_dim d2 where {cc} and {kk} and d1.d_date BETWEEN (d2.d_date - interval '120 day') AND d2.d_date;",
        'template_store_store_returns_l': f"select * from store_returns, store where {cc} and sr_store_sk = s_store_sk;",
        'template_inventory_catalog_sales_r_072': f"select * from catalog_sales JOIN inventory ON (cs_item_sk = inv_item_sk) where {cc};",
        'template_customer_demographics_catalog_sales_r_072': f"select * from catalog_sales JOIN customer_demographics ON (cs_bill_cdemo_sk = cd_demo_sk) where {cc};",
        
        'template_household_demographics_catalog_sales_both_072': f"select * from household_demographics, catalog_sales where {cc} and {kk} and cs_bill_hdemo_sk = hd_demo_sk;",
        'template_date_dim_catalog_sales_both_072': f"select * from date_dim, catalog_sales where {cc} and {kk} and cs_sold_date_sk = d_date_sk;",
        'template_inventory_item_r_072': f"select * from inventory, item where {cc} and inv_item_sk = i_item_sk;",
        
        'template_customer_address_customer_l_084': f"select * from customer_address, customer where {cc} and c_current_addr_sk = ca_address_sk;",
        'template_income_band_household_demographics_l_084': f"select * from income_band, household_demographics where {cc} and ib_income_band_sk = hd_income_band_sk;",
        'template_inventory_catalog_sales_r': f"select * from catalog_sales JOIN inventory ON (cs_item_sk = inv_item_sk)  where {cc};",
        'template_inventory_warehouse__catalog_sales': f"select * from catalog_sales JOIN inventory ON (cs_item_sk = inv_item_sk) JOIN warehouse ON (w_warehouse_sk=inv_warehouse_sk) where {cc};",
        'template_': f"select * from  where {cc} and",
        'template_': f"select * from  where {cc} and",
        'template_': f"select * from  where {cc} and",
        


        
    }
    
    
    if db == 'imdb':
        if template_name in querylet_imdb_dict.keys():
            return querylet_imdb_dict[template_name]
        else:
            return None
    elif db == 'dsb':
        if template_name.split('template_')[1] in basic_tables.keys():
            return gen_one_table_query(template_name.split('template_')[1], cc)
        elif '_full' in template_name:
            return gen_one_table_query_full(template_name.split('template_')[1].split('_full')[0])
        else:
            return querylet_dsb_dict[template_name]
        

def stats_join_querylet(left_alias, right_alias, l_r_b, cc, kk):
    right = basic_tables_stats[right_alias]
    left = basic_tables_stats[left_alias]
    # if left_alias == 'p':
    #     left_con = 'Id'
    # else:
    #     left_con = 'PostId'
    
    # right_con = 'PostId'

    # if left_alias == 'u':
    #     left_con = 'Id'
    # else:
    #     left_con = 'UserId'
    
    # right_con = 'UserId'

    right_con = 'UserId'
    left_con = 'UserId'
    
    if l_r_b == 'l':
        return f'select * from {left} as {left_alias}, {right} as {right_alias} where {left_alias}.{left_con}={right_alias}.{right_con} and {cc};'
    elif l_r_b == 'r':
        return f'select * from {left} as {left_alias}, {right} as {right_alias} where {left_alias}.{left_con}={right_alias}.{right_con} and {kk};'
    else:
        return f'select * from {left} as {left_alias}, {right} as {right_alias} where {left_alias}.{left_con}={right_alias}.{right_con} and {cc} and {kk};'


def gen_one_table_query(table_name, condition):
    return f'select * from {table_name} where {condition};'

def gen_one_table_query_full(table_name):
    return f'select * from {table_name};'


def gen_one_table_query_stats(table_name, alias, condition):
    return f'select * from {table_name} as {alias} where {condition};'


def stats_single_querylet(cc, template_name):


    if template_name in basic_tables_stats.keys():
        return gen_one_table_query_stats(basic_tables_stats[template_name], template_name, cc)
    elif '_full' in template_name:
        return gen_one_table_query_full(basic_tables_stats[template_name.split('_full')[0]])


def stats_complex_querylet(cc, template):
    querylet_dict = {
        'template_ph_b__c': f'select * from comments as c, postHistory as ph, badges as b where {cc} and c.UserId = ph.UserId and b.UserId = ph.UserId;'
    }
    return querylet_dict[template]
