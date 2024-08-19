import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.neighbors import KernelDensity
from utility import *
import sys

err_files_dict_job = {}
err_files_dict_job['17'] = {
                        1: 'cn.txt', 
                        2: 'k.txt',
                        5: 'n.txt',
                        7: 'ci_mc__q17.txt', 
                        8: 'mk_ci__q17.txt', 
                        9: 'n_ci_l.txt', 
                        10: 't_ci__n.txt',
                        11: 'mc_cn_r.txt', 
                        12: 'mk_k_r.txt', 
                        13: 'mk_mc__q2.txt',
                        14: 't_mc__cn.txt', 
                        15: 't_mk__k.txt',
                        }



err_files_dict_job['16'] = {
    2: 'cn.txt',
    3: 'k.txt',
    7: 't.txt',
    8: 'ci_an_pure.txt', # ci an 
    9: 'n_an_pure.txt', # n an 
    10: 'mc_ci_pure.txt', # mc ci
    11: 'mk_ci_pure.txt', # mk ci !
    12: 'n_ci_pure.txt', # n ci !
    13: 't_ci_l.txt', # t ci
    14: 'mc_cn_r.txt', # mc cn
    15: 'mk_k_r.txt', # mk k
    16: 'mk_mc__q2.txt', # mix mk (cn mc) and mc (k mk)
    17: 't_mc_l.txt', # t mc
    18: 't_mk_l.txt', # t mk
}


err_files_dict_job['15'] = {
    1: 'cn.txt',
    # 3: 'it.txt',
    5: 'mc.txt',
    6: 'mi.txt',
    8: 't.txt',
    9: 'mc_akat_l.txt', # mc aka_t
    10: 'mi_akat_l.txt', # mi aka_t
    11: 'mk_akat__mc.txt', # mk aka_t on mc
    12: 't_akat_l.txt', # t aka_t
    13: 'mc_cn_both.txt', # mc cn
    14: 'mc_ct_l.txt', # mc ct
    15: 'mi_it_both.txt', # mi it
    16: 'mk_k__pure.txt', # mk k todo
    17: 'mi_mc_both.txt', # mi mc
    18: 'mk_mc_r.txt', # mk mc
    19: 't_mc_both.txt', # t mc
    20: 'mk_mi_r.txt', # mk mi
    21: 't_mi_both.txt', # t mi
    22: 't_mk_l.txt', # t mk
}



err_files_dict_job['14'] = {
    2: 'k.txt', #
    4: 'mi.txt', #
    5: 'mi_idx.txt', #
    7: 't.txt', #
    8: 'mi_it_both.txt', #
    9: 'mi_idx_it_both.txt', # 
    10: 'mk_k_r.txt', #
    11: 't_kt_both.txt', # 
    12: 'mi_idx_mi_both.txt', # 
    13: 'mk_mi_r.txt', # 
    14: 't_mi_both.txt', # 
    15: 'mk_mi_idx_r.txt', # 
    16: 't_mi_idx_both.txt', # 
    17: 't_mk_l.txt', # 
}

err_files_dict_job['13'] = {
    0: 'cn.txt', #
    # 2: 'it.txt', #
    # 3: 'it.txt', #
    5: 'mc.txt', #
    6: 'mi.txt', #
    8: 't.txt', #
    9: 'mc_cn_r.txt', # 
    10: 'mc_ct_r.txt', #
    11: 'mi_idx_it_r.txt', # 
    12: 'mi_it_r.txt', # 
    13: 't_kt_r.txt', # 
    14: 'mi_mc__it.txt', # use mc (it mi)
    15: 'mi_idx_mc_pure.txt', # use the
    16: 't_mc__kt.txt', # use mc (kt t)
    17: 'mi_idx_mi__it.txt', # use mi_idx it mi
    18: 't_mi__q13.txt', # use t (it mi); mi (kt t)
    19: 't_mi_idx__it.txt', # use t (it mi_idx)
}
err_files_dict_job['12'] = {
    0: 'cn.txt', #
    1: 'ct.txt', #
    # 2: 'it.txt', #
    # 3: 'it.txt', #
    5: 'mi.txt', #
    6: 'mi_idx.txt', #
    7: 't.txt', #
    8: 'mc_cn_r.txt', #
    9: 'mc_ct_r.txt', # 
    10: 'mi_it_both.txt', #
    11: 'mi_idx_it_both.txt', # 
    12: 'mi_mc_l.txt', # 
    13: 'mi_idx_mc_l.txt', # 
    14: 't_mc_l.txt', # 
    15: 'mi_idx_mi_both.txt', # 
    16: 't_mi_both.txt', # 
    17: 't_mi_idx_both.txt', # 
}

err_files_dict_job['11'] = {
    0: 'cn.txt', #
    1: 'ct.txt', #
    2: 'k.txt', #
    3: 'lt.txt', #
    4: 'mc.txt', #
    7: 't.txt', #
    8: 'mc_cn_both.txt', #
    9: 'mc_ct_both.txt', # 
    10: 'mk_k_r.txt', #
    11: 'ml_lt_r.txt', # 
    12: 'mk_mc_r.txt', # 
    13: 'ml_mc_r.txt', # 
    14: 't_mc_both.txt', # 
    15: 'ml_mk__k.txt', # 
    16: 't_mk_l.txt', # 
    17: 't_ml_l_1.txt', # 
}
err_files_dict_job['10'] = {
    1: 'ci.txt', #
    2: 'cn.txt', #
    5: 'rt.txt', #
    6: 't.txt', #
    7: 'ci_chn_l.txt', #
    8: 'mc_ci_r.txt', #
    9: 'rt_ci_both.txt', # 
    10: 't_ci_both.txt', #
    11: 'mc_cn_r.txt', # 
    12: 'mc_ct__q10.txt', # 
    13: 't_mc_l.txt', # 
}
err_files_dict_job['9'] = {
    2: 'ci.txt', #
    3: 'cn.txt', #
    4: 'mc.txt', #
    5: 'n.txt', #
    6: 'rt.txt', #
    7: 't.txt', #
    8: 'ci_an_l.txt', #
    9: 'n_an_l.txt', # 
    10: 'ci_chn_l.txt', #
    11: 'mc_ci_both.txt', # 
    12: 'n_ci_both.txt', # 
    13: 'rt_ci_both.txt', # ~
    14: 't_ci_both.txt', # 
    15: 'mc_cn_both.txt', # 
    16: 't_mc_both.txt', # 
}

err_files_dict_job['8'] = {
    1: 'ci.txt', #
    2: 'cn.txt', #
    3: 'mc.txt', #
    4: 'n.txt', #
    5: 'rt.txt', #
    7: 'ci_an_l.txt', # 
    8: 'n_an_l.txt', # 
    9: 'mc_ci_both.txt', # 
    10: 'n_ci_both.txt', # 
    11: 'rt_ci_r.txt', # 
    12: 't_ci_both.txt', # 
    13: 'mc_cn_both.txt', # 
    14: 't_mc_both.txt', # 
}

err_files_dict_job['7'] = {
    0: 'an.txt',
    # 2: 'it.txt',
    # 3: 'lt.txt',
    5: 'n.txt',
    6: 'pi.txt',
    7: 't.txt',
    8: 'ci_an_r.txt', # 
    9: 'n_an_both.txt', # 
    10: 'pi_an_both.txt', #
    11: 'ml_ci_pure.txt', # 
    12: 'n_ci_l.txt', # 
    13: 'pi_ci_l.txt', # 
    14: 't_ci_l.txt', # 
    15: 'pi_it_both.txt', # 
    16: 'ml_lt_r.txt', # 
    17: 't_ml_l_2.txt', # 
    18: 'pi_n_both.txt'
}
err_files_dict_job['6'] = {
    1: 'k.txt', #
    3: 'n.txt', #
    4: 't.txt', #
    5: 'mk_ci__k.txt', #
    6: 'n_ci_l.txt', #
    7: 't_ci_l.txt', #
    8: 'mk_k_r.txt', #
    9: 't_mk_l.txt', # 
}

err_files_dict_job['5'] = {
    0: 'ct.txt', #
    2: 'mc.txt', #
    3: 'mi.txt', #
    4: 't.txt', #
    5: 'mc_ct_both.txt', #
    6: 'mi_it_r.txt', #
    7: 'mi_mc_both.txt', #
    8: 't_mc_both.txt', #
    9: 't_mi_both.txt', # 
}
err_files_dict_job['4'] = {
    1: 'k.txt', #
    2: 'mi_idx.txt', #
    4: 't.txt', #
    5: 'mi_idx_it_both.txt', #
    6: 'mk_k_r.txt', #
    7: 'mk_mi_idx_r.txt', #
    8: 't_mi_idx_both.txt', #
    9: 't_mk_l.txt', # 
}
err_files_dict_job['3'] = {
    0: 'k.txt', #
    1: 'mi.txt', #
    3: 't.txt', #
    4: 'mk_k_r.txt', #
    5: 'mk_mi_r.txt', #
    6: 't_mi_both.txt', #
    7: 't_mk_l.txt', #
}
err_files_dict_job['2'] = {
    0: 'cn.txt', #
    1: 'k.txt', #
    5: 'mc_cn_r.txt', #
    6: 'mk_k_r.txt', #
    7: 'mk_mc__q2.txt', # mix mk (cn mc) and mc (k mk)
    8: 't_mc__cn.txt', #
    9: 't_mk__k.txt', # 
}

err_files_dict_job['1'] = {
    # 0: 'ct.txt', #
    # 1: 'it.txt', #
    2: 'mc.txt', #
    5: 'mc_ct_both.txt', #
    6: 'mi_idx_it_r.txt', #
    7: 'mi_idx_mc_r.txt', # ~
    8: 't_mc_r.txt', # ~
    9: 't_mi_idx__it.txt', # 
}




err_files_dict_job['18'] = {
    0: 'ci.txt', #
    5: 'n.txt', #
    7: 'mi_mc_pure.txt', # 
    8: 'mi_idx_ci_r.txt', # 
    9: 'n_ci_both.txt', # 
    10: 't_ci_r.txt', # 
    11: 'mi_it_r.txt', # 
    12: 'mi_idx_it_r.txt', # 
    13: 'mi_idx_mi__it.txt', # mi_idx_mi
    14: 't_mi__it.txt', # t_mi
    15: 't_mi_idx__it.txt', # t-mi_idx
}


err_files_dict_job['19'] = {
    2: 'ci.txt', #
    3: 'cn.txt', #
    5: 'mc.txt', #
    6: 'mi.txt', #
    7: 'n.txt', #
    9: 't.txt', # 
    10: 'ci_an_l.txt', #
    11: 'n_an_l.txt', # 
    12: 'ci_chn_l.txt', # 
    13: 'mc_ci_both.txt', # 
    14: 'mi_ci_both.txt', # 
    15: 'n_ci_both.txt', # 
    16: 'rt_ci_both.txt', # 
    17: 't_ci_both.txt', # 
    18: 'mc_cn_both.txt', # 
    19: 'mi_it_both.txt', #
    20: 'mi_mc_both.txt', #
    21: 't_mc_both.txt', #
    22: 't_mi_both.txt', #
}


# err_files_dict_job['20'] = {
#     1: 'cct.txt', #
#     2: 'cct.txt', #
#     3: 'chn.txt', #
#     5: 'k.txt', #
#     9: 't.txt', # 
#     10: 'cct-cc-1-l.txt', # 
#     11: 'cct-cc-2-l.txt', # 
#     12: 'ci-cc--cct.txt', #  mix cc's two join keys
#     13: 'mk-cc--cct.txt', #  #  mix cc's two join keys
#     14: 't-cc-l.txt', # 
#     15: 'ci-chn-r.txt', # 
#     16: 'mk-ci--chn.txt', # 
#     17: 'n-ci--chn.txt', # 
#     18: 't-ci-l.txt', # 
#     19: 'mk-k-r.txt', #
#     20: 't-kt-both.txt', #
#     21: 't-mk-l.txt', #
# }

err_files_dict_job['20'] = {
    1: 'cct.txt', #
    2: 'cct.txt', #
    3: 'chn.txt', #
    5: 'k.txt', #
    9: 't.txt', # 
    10: 'cct_cc_1_l.txt', # 
    11: 'cct_cc_2_l.txt', # 
    12: 'ci_cc__cct.txt', #  
    13: 'mk_cc__cct.txt', #  
    14: 't_cc_l.txt', # 
    15: 'ci_chn_r.txt', # 
    16: 'mk_ci__chn.txt', # 
    17: 'n_ci__chn.txt', # 
    18: 't_ci_l.txt', # 
    19: 'mk_k_r.txt', #
    20: 't_kt_both.txt', #
    21: 't_mk_l.txt', #
}
err_files_dict_job['21'] = {
    0: 'cn.txt', #
    1: 'ct.txt', #
    2: 'k.txt', #
    3: 'lt.txt', #
    4: 'mc.txt', #
    5: 'mi.txt', #
    8: 't.txt', #
    9: 'mc_cn_both.txt', # 
    10: 'mc_ct_both.txt', #
    11: 'mk_k_r.txt', # 
    12: 'ml_lt_r.txt', # 
    13: 'mi_mc_both.txt', # 
    14: 'mk_mc_r.txt', # 
    15: 'ml_mc_r.txt', # 
    16: 't_mc_both.txt', # 
    17: 'mk_mi_r.txt', # 
    18: 'ml_mi_r.txt', #
    19: 't_mi_both.txt', #
    20: 'ml_mk__k.txt', #
    21: 't_mk_l.txt', #
    22: 't_ml_l_1.txt', #
}
err_files_dict_job['22'] = {
    0: 'cn.txt', #
    # 2: 'it.txt', #
    # 3: 'it.txt', #
    4: 'k.txt', #
    6: 'mc.txt', #
    7: 'mi.txt', #
    8: 'mi_idx.txt', #
    10: 't.txt', #
    11: 'mc_cn_both.txt', # 
    12: 'mc_ct_l.txt', # 
    13: 'mi_it_both.txt', # 
    14: 'mi_idx_it_both.txt', # 
    15: 'mk_k_r.txt', # 
    16: 't_kt_both.txt', # 
    17: 'mi_mc_both.txt', # 
    18: 'mi_idx_mc_both.txt', # 
    19: 'mk_mc_r.txt', #
    20: 't_mc_both.txt', #
    21: 'mi_idx_mi_both.txt', #
    22: 'mk_mi_r.txt', #
}
err_files_dict_job['23'] = {
    1: 'cct.txt', #
    2: 'cn.txt', #
    # 4: 'it.txt', #
    8: 'mi.txt', #
    10: 't.txt', #
    11: 'cct_cc_2_l.txt', # 
    12: 'mc_cc_pure.txt', # 
    13: 'mi_cc_l.txt', # 
    14: 'mk_cc__q23.txt', # cct+mi
    15: 't_cc_l.txt', # 
    16: 'mc_cn_r.txt', # 
    17: 'mc_ct_r.txt', # 
    18: 'mi_it_both.txt', # 
    19: 'mk_k_r.txt', #
    20: 't_kt_both.txt', #
    21: 'mi_mc_l.txt', #
    22: 'mk_mc__cn.txt', #
    23: 't_mc_l.txt', #
    24: 'mk_mi_r.txt', #
    25: 't_mi_both.txt', #
    26: 't_mk_l.txt', #
}
err_files_dict_job['24'] = {
    2: 'ci.txt', #
    3: 'cn.txt', #
    # 4: 'it.txt', #
    5: 'k.txt', #
    7: 'mi.txt', #
    9: 'n.txt', #
    10: 'rt.txt', # 
    11: 't.txt', # 
    12: 'ci_an_l.txt', # 
    13: 'n_an_l.txt', # 
    14: 'ci_chn_l.txt', # 
    15: 'mc_ci_r.txt', # 
    16: 'mi_ci_both.txt', # 
    17: 'mk_ci_r.txt', # 
    18: 'n_ci_both.txt', # 
    19: 'rt_ci_both.txt', #
    20: 't_ci_both.txt', #
    21: 'mc_cn_r.txt', #
    22: 'mi_it_both.txt', #
    23: 'mk_k_r.txt', #
    24: 'mi_mc_l.txt', #
    25: 'mk_mc__cn.txt', #
    26: 't_mc_l.txt', #
    27: 'mk_mi_r.txt', #
    28: 't_mi_both.txt', #
    29: 't_mk_l.txt', #

}

err_files_dict_job['25'] = {
    0: 'ci.txt', #
    # 1: 'it.txt', #
    # 2: 'it.txt', #
    3: 'k.txt', #
    4: 'mi.txt', #
    7: 'n.txt', #
    9: 'mi_ci_both.txt', # 
    10: 'mi_idx_ci_r.txt', #
    11: 'mk_ci_r.txt', # 
    12: 'n_ci_both.txt', # 
    13: 't_ci_r.txt', # 
    14: 'mi_it_both.txt', # 
    15: 'mi_idx_it_r.txt', # 
    16: 'mk_k_r.txt', # 
    17: 'mi_idx_mi_r.txt', # 
    18: 't_mi_r.txt', # 
}

err_files_dict_job['26'] = {
    # 1: 'cct.txt', #
    2: 'cct.txt', #
    3: 'chn.txt', #
    # 5: 'it.txt', #
    # 6: 'k.txt', #
    8: 'mi_idx.txt', #
    11: 't.txt', # 
    12: 'cct_cc_1_l.txt', # 
    13: 'cct_cc_2_l.txt', # 
    14: 'ci_cc__cct.txt', # 
    15: 'mi_idx_cc_l.txt', # 
    16: 'mk_cc__cct.txt', # 
    17: 't_cc_l.txt', # 
    18: 'ci_chn_r.txt', # 
    19: 'mi_idx_ci_l.txt', #
    20: 'mk_ci__chn.txt', #
    21: 'n_ci_l.txt', #
    22: 't_ci_l.txt', #
    23: 'mi_idx_it_both.txt', #
    24: 'mk_k_r.txt', #
    25: 't_kt_both.txt', #
    26: 'mk_mi_idx_r.txt', #
    27: 't_mi_idx_both.txt', #
    28: 't_mk_l.txt', #
}



err_files_dict_job['27'] = {
    1: 'cct.txt', #
    2: 'cct.txt', #
    3: 'cn.txt', #
    4: 'ct.txt', #
    5: 'k.txt', #
    6: 'lt.txt', #
    7: 'mc.txt', #
    8: 'mi.txt', #
    11: 't.txt', # 
    12: 'cct_cc_1_l.txt', # 
    13: 'cct_cc_2_l.txt', # 
    14: 'mc_cc_l.txt', # 
    15: 'mi_cc_l.txt', # 
    16: 'mk_cc__q23.txt', #  
    17: 'ml_cc__cct_2.txt', # !
    18: 't_cc_l.txt', # 
    19: 'mc_cn_both.txt', #
    20: 'mc_ct_both.txt', #
    21: 'mk_k_r.txt', #
    22: 'ml_lt_r.txt', #
    23: 'mi_mc_both.txt', #
    24: 'mk_mc_r.txt', #
    25: 'ml_mc_r.txt', #
    26: 't_mc_both.txt', #
    27: 'mk_mi_r.txt', #
    28: 'ml_mi_r.txt', #
    29: 't_mi_both.txt', #
    30: 'ml_mk__k.txt', 
    31: 't_mk_l.txt',
    32: 't_ml_l_1.txt'
}

# err_files_dict_job['28'] = {
#     1: 'cct.txt', #
#     2: 'cct.txt', #
#     3: 'cn.txt', #
#     5: 'it.txt', #
#     6: 'it.txt', #
#     7: 'k.txt', #
#     9: 'mc.txt', # 
#     10: 'mi.txt', #
#     11: 'mi_idx.txt', # 
#     13: 't.txt', # 
#     14: 'cct-cc-1-l.txt', # 
#     15: 'cct-cc-2-l.txt', # 
#     16: 'mc-cc-l.txt', # 
#     17: 'mi-cc-l.txt', # 
#     18: 'miidx-cc-l.txt', # 
#     # 19: '.txt', #~
#     20: 't-cc-l.txt', #~
#     21: 'mc-cn-both.txt', #
#     22: 'mc-ct-l.txt', #
#     23: 'mi-it-both.txt', #
#     24: 'miidx-it-both.txt', #
#     25: 'mk-k-r.txt', #
#     26: 't-kt-both.txt', #
#     27: 'mi-mc-both.txt', #
#     28: 'miidx-mc-both.txt', #
#     29: 'mk-mc-r.txt', #
#     30: 't-mc-both.txt', #
#     31: 'miidx-mi-both.txt', #
#     32: 'mk-mi-r.txt', #
#     33: 't-mi-both.txt', #
#     34: 'mk-miidx-r.txt', #
#     35: 't-miidx-both.txt', #
#     36: 't-mk-l.txt', #
# }

err_files_dict_job['28'] = {
    1: 'cct.txt', #
    2: 'cct.txt', #
    3: 'cn.txt', #
    # 5: 'it.txt', #
    # 6: 'it.txt', #
    7: 'k.txt', #
    9: 'mc.txt', # 
    10: 'mi.txt', #
    11: 'mi_idx.txt', # 
    13: 't.txt', # 
    14: 'cct_cc_1_l.txt', # 
    15: 'cct_cc_2_l.txt', # 
    16: 'mc_cc_l.txt', # 
    17: 'mi_cc_l.txt', # 
    18: 'mi_idx_cc_l.txt', # 
    # 19: '.txt', #~
    20: 't_cc_l.txt', #~
    21: 'mc_cn_both.txt', #
    22: 'mc_ct_l.txt', #
    23: 'mi_it_both.txt', #
    24: 'mi_idx_it_both.txt', #
    25: 'mk_k_r.txt', #
    26: 't_kt_both.txt', #
    27: 'mi_mc_both.txt', #
    28: 'mi_idx_mc_both.txt', #
    29: 'mk_mc_r.txt', #
    30: 't_mc_both.txt', #
    31: 'mi_idx_mi_both.txt', #
    32: 'mk_mi_r.txt', #
    33: 't_mi_both.txt', #
    34: 'mk_mi_idx_r.txt', #
    35: 't_mi_idx_both.txt', #
    36: 't_mk_l.txt', #
}

err_files_dict_job['29'] = {
    # 2: 'cct.txt',
    # 3: 'cct.txt',
    4: 'chn.txt',
    5: 'ci.txt',
    # 6: 'cn.txt',
    # 7: 'it.txt',
    # 8: 'it.txt',
    # 9: 'k.txt',
    11: 'mi.txt', # 
    13: 'n.txt', # 
    # 15: 'rt.txt', # 
    16: 't.txt', # 
    17: 'ci_an_l.txt', # 
    18: 'n_an_l.txt', # 
    19: 'pi_an_both.txt', #
    20: 'cct_cc_1_l.txt', #
    21: 'cct_cc_2_l.txt', #
    22: 'ci_cc__cct.txt', #
    23: 'mc_cc_l.txt', #
    24: 'mi_cc_l.txt', #
    25: 'mk_cc__q23.txt', #
    26: 't_cc_l.txt', #
    27: 'ci_chn_r.txt', #
    28: 'mc_ci_r.txt', #
    29: 'mi_ci_both.txt', #
    30: 'mk_ci_r.txt', #
    31: 'n_ci_both.txt', #
    32: 'pi_ci_both.txt', # ~
    33: 'rt_ci_both.txt', #
    34: 't_ci_both.txt', #
    35: 'mc_cn_r.txt', #
    36: 'mi_it_both.txt', #
    37: 'pi_it_both.txt', #
    38: 'mk_k_r.txt', #
    39: 'mi_mc_l.txt', #
    40: 'mk_mc__q2.txt', #
    41: 't_mc_l.txt', #
    42: 'mk_mi_r.txt', #
    43: 't_mi_both.txt', #
    44: 't_mk_l.txt', #
    45: 'pi_n_both.txt', #
}

err_files_dict_job['30'] = {
    3: 'ci.txt', #
    10: 'n.txt', #
    11: 't.txt', # 
    12: 'cct_cc_1_l.txt', # 
    13: 'cct_cc_2_l.txt', # 
    14: 'ci_cc_l.txt', #
    15: 'mi_cc_l.txt', # 
    16: 'mi_idx_cc_l.txt', # ~
    17: 'mk_cc__q23.txt', # 
    18: 't_cc_l.txt', # 
    19: 'mi_ci_both.txt', #
    20: 'mi_idx_ci_r.txt', #
    21: 'mk_ci_r.txt', #
    22: 'n_ci_both.txt', #
    23: 't_ci_both.txt', #
    24: 'mi_it_both.txt', #
    25: 'mi_idx_it_r.txt', #
    26: 'mk_k_r.txt', #
    27: 'mi_idx_mi_r.txt', #
    28: 'mk_mi_r.txt', #
    29: 't_mi_both.txt', #
    30: 'mk_mi_idx_r.txt', # ~
    31: 't_mi_idx_l.txt', #
    32: 't_mk_l.txt', #
}


err_files_dict_job['31'] = {
    0: 'ci.txt', #
    1: 'cn.txt', #
    # 2: 'it.txt', #
    # 3: 'it.txt', #
    4: 'k.txt', #
    6: 'mi.txt', #
    9: 'n.txt', #
    11: 'mc_ci_r.txt', # 
    12: 'mi_ci_both.txt', # 
    13: 'mi_idx_ci_r.txt', # 
    14: 'mk_ci_r.txt', # 
    15: 'n_ci_both.txt', # 
    16: 't_ci_r.txt', # 
    17: 'mc_cn_r.txt', # 
    18: 'mi_it_both.txt', # 
    19: 'mi_idx_it_r.txt', #
    20: 'mk_k_r.txt', #
    21: 'mi_mc_l.txt', #
    22: 'mi_idx_mc__it.txt', # ~
    23: 'mk_mc__q2.txt', #
    24: 't_mc__cn.txt', #
    25: 'mi_idx_mi_r.txt', #
    26: 'mk_mi_r.txt', #
    27: 't_mi_r.txt', #
    28: 'mk_mi_idx__k.txt', # ~
    29: 't_mi_idx__it.txt', # 
    30: 't_mk__k.txt',
}


err_files_dict_job['32'] = {
    0: 'k.txt',
    6: 'mk_k_r.txt', 
    8: 'ml_mk__k.txt', # ml mk
    9: 't_mk__k.txt',
    10: 't_ml_1_pure.txt', # t ml
    11: 't_ml_2_pure.txt', # t ml
}


err_files_dict_job['33'] = {
    # 0: 'cn',
    # 2: 'it.txt', #
    # 3: 'it.txt', #
    # 4: 'kt.txt', #
    # 5: 'kt.txt', #
    6: 'lt.txt', #
    10: 'mi_idx.txt', #
    13: 't.txt', # 
    14: 'mc_cn_r.txt', # 
    # 15: 'mc_cn.txt', # ~ mc2 cn2
    17: 'mi_idx_it_r.txt', # 
    18: 'mi_idx_it_both.txt', # 
    20: 't_kt_r.txt', #
    21: 't_kt_both.txt', #
    22: 'ml_lt_r.txt', #
    # 23: 'mi_idx_mc.txt', #~ mi_idx1 mc1
    # 24: 'ml_mc.txt', #~ ml mc1
    # 25: 't_mc.txt', #~ t1 mc1
    26: 'mi_idx_mc_l.txt', #
    # 27: 'ml_mc.txt', #~ ml mc2
    28: 't_mc_l.txt', #
    # 29: 'ml_mi_idx.txt', #~ ml mi_idx1
    # 30: 't_mi_idx.txt', #~t1 mi_idx1
    31: 'ml_mi_idx_r.txt',
    32: 't_mi_idx_both.txt',
    # 33: 't_ml.txt', #~ t1 ml
    34: 't_ml_l_2.txt',
    
}

err_files_dict_dsb = {}

err_files_dict_dsb['102'] = {
    1: 'web_sales_102.txt',
    2: 'date_dim_102.txt',
    8: 'item_102.txt',
    11: 'customer_address_102.txt',

    13: 'date_dim_store_sales_l_102.txt',
    16: 'item_store_sales_l_102.txt',
    
    17: 'date_dim_web_sales_r_102.txt',
    18: 'customer_web_sales_r_102.txt',
    # 19: 'inventory_web_sales_r.txt',
    # 20: 'inventory_web_sales_r.txt',
    # 21: 'inventory_web_sales.txt',
    # 22: 'inventory_web_sales.txt',
    23: 'warehouse_web_sales_r_102.txt',
    24: 'item_web_sales_both_102.txt',
    25: 'date_dim_date_dim_non_2_102.txt',

    # 26: 'inventory_date_dim.txt',
    # 27: 'inventory_date_dim.txt',
    # 28: 'inventory_date_dim.txt',
    # 29: 'inventory_date_dim.txt',
    # 30: 'inventory_date_dim.txt',
    # 31: 'inventory_date_dim.txt',
    # 32: 'inventory_date_dim.txt',
    # 33: 'inventory_date_dim.txt',
    # 34: 'inventory_date_dim.txt',
    # 35: 'customer_demographics_customer.txt',
    # 36: 'household_demographics_customer.txt',
    37: 'customer_address_customer_l_102.txt',
    # 38: 'warehouse_inventory.txt',
    # 39: 'inventory_warehouse.txt',
    # 40: 'inventory_warehouse.txt',
    # 41: 'inventory_warehouse.txt',
    # 42: 'inventory_warehouse.txt',
    # 43: 'inventory_warehouse.txt',
    # 44: 'inventory_warehouse.txt',
    45: 'inventory_item_r_102.txt',
    46: 'inventory_item_r_102.txt',
    47: 'inventory_item_r_102.txt',
    48: 'inventory_item_r_102.txt',
    49: 'inventory_item_r_102.txt',
    50: 'inventory_item_r_102.txt',
    51: 'inventory_item_r_102.txt',
    52: 'inventory_item_r_102.txt',
    53: 'inventory_item_r_102.txt',
    54: 'inventory_item_r_102.txt',
    # 55: 'warehouse_store.txt'
}


err_files_dict_dsb['101'] = {
    0: 'store_sales_101.txt',
    3: 'date_dim_101.txt',
    5: 'item_101.txt',
    7: 'customer_address_101.txt',
    8: 'household_demographics_101.txt',
    10: 'web_sales_store_sales_r_101.txt',
    11: 'item_store_sales_both_101.txt',
    12: 'customer_store_sales_r_101.txt',
    15: 'item_store_returns_l_101.txt',
    17: 'item_web_sales_l_101.txt',
    19: 'date_dim_date_dim_non_1_101.txt', 
    20: 'customer_address_customer_l_101.txt',
    21: 'household_demographics_customer_l_101.txt'
    }

err_files_dict_dsb['100'] = {
    0: 'item_1__100.txt',
    1: 'item_2__100.txt',
    2: 'store_sales_1__100.txt',
    3: 'store_sales_2__100.txt',
    4: 'date_dim_100.txt',
    7: 'customer_demographics_100.txt',
    # 8: 'item_item.txt',
    9: 'item1_s1_both_100.txt',
    10: 'item1_s1_both_100.txt',
    11: 'item1_s1_both_100.txt',
    12: 'item2_s2_both_100.txt',
    13: 'item2_s2_both_100.txt',
    14: 'item2_s2_both_100.txt',
    15: 's1_s2_both_100.txt',
    16: 's1_s2_both_100.txt',
    17: 's1_s2_both_100.txt',
    18: 's1_s2_both_100.txt',
    19: 'date_dim_s1_both_100.txt',
    20: 'customer_s1_r_100.txt',
    22: 'customer_demographics_customer_l_100.txt'
    }

err_files_dict_dsb['091'] = {
    2: 'date_dim.txt',
    4: 'customer_address.txt',
    5: 'customer_demographics.txt',
    6: 'household_demographics.txt',
    8: 'date_dim_catalog_returns_l.txt',
    10: 'customer_address_customer_l.txt',
    11: 'customer_demographics_customer_l.txt',
    12: 'household_demographics_customer_l.txt'
}

err_files_dict_dsb['099'] = {
    0: 'catalog_sales.txt',
    2: 'ship_mode.txt',
    3: 'call_center.txt',
    4: 'date_dim.txt',
    5: 'warehouse_catalog_sales_r.txt',
    6: 'ship_mode_catalog_sales_both.txt',
    7: 'call_center_catalog_sales_both.txt',
    8: 'date_dim_catalog_sales_both.txt'
}

err_files_dict_dsb['085'] = {
    0: 'web_sales.txt',
    3: 'customer_demographics.txt',
    5: 'customer_address.txt',
    6: 'date_dim.txt',
    8: 'web_returns_web_sales_r.txt',
    9: 'web_page_web_sales_r.txt',
    # 10: 'customer_demographics_web_sales_both.txt',
    # 11: 'customer_address_web_sales.txt',
    12: 'date_dim_web_sales_both.txt',
    13: 'customer_demographics_web_returns_l.txt',
    # 14: 'customer_demographics_web_returns_l.txt',
    15: 'customer_address_web_returns_l.txt',
    # 17: 'customer_demographics_customer_demographics_l.txt'
}

err_files_dict_dsb['013'] = {  
    0: 'store_sales.txt',
    2: 'customer_demographics.txt',
    3: 'household_demographics.txt',
    4: 'customer_address.txt',
    5: 'date_dim.txt',
    6: 'store_store_sales_r.txt',
    7: 'customer_demographics_store_sales_both.txt',
    8: 'household_demographics_store_sales_both.txt',
    9: 'customer_address_store_sales_both.txt',
    10: 'date_dim_store_sales_both.txt',
    11: 'household_demographics_customer_demographics_both.txt'}



err_files_dict_dsb['018'] = {
    0: 'catalog_sales.txt',
    1: 'customer_demographics.txt',
    2: 'customer.txt',
    3: 'customer_address.txt',
    4: 'date_dim.txt',
    5: 'item.txt',
    6: 'customer_demographics_catalog_sales_both_1.txt',
    7: 'customer_catalog_sales_both.txt',
    8: 'date_dim_catalog_sales_both.txt',
    9: 'item_catalog_sales_both.txt',
    10: 'customer_address_customer_both.txt'
}

err_files_dict_dsb['019'] = {
    0: 'date_dim_019.txt',
    1: 'store_sales_019.txt',
    2: 'item_019.txt',
    3: 'customer_019.txt',
    4: 'customer_address_019.txt',
    6: 'date_dim_store_sales_both_019.txt',
    7: 'item_store_sales_both_019.txt',
    8: 'customer_store_sales__date_dim_019.txt',
    9: 'store_store_sales_r_019.txt',
    10: 'customer_address_customer_both_019.txt',
    # 11: 'store_customer_address_r_019.txt'
}

err_files_dict_dsb['025'] = {
    3: 'date_dim_1_025.txt',
    4: 'date_dim_2_025.txt',
    5: 'date_dim_3_025.txt',
    # 8: 'store_returns_store_sales.txt',
    # 9: 'catalog_sales_store_sales.txt',
    10: 'date_dim_store_sales_l_025.txt',
    11: 'store_store_sales__date_dim_025.txt', # use d1
    12: 'item_store_sales__date_dim_025.txt', # use d1
    # 13: 'catalog_sales_store_returns.txt',
    14: 'date_dim_store_returns_l_025.txt',
    15: 'item_store_returns__date_dim_025.txt', # use d2
    16: 'date_dim_catalog_sales_l_025.txt',
    17: 'item_catalog_sales__date_dim_025.txt', # use d3
}

err_files_dict_dsb['027'] = {
    1: 'customer_demographics_027.txt',
    2: 'date_dim_027.txt',
    3: 'store_027.txt',
    4: 'item_027.txt',
    5: 'customer_demographics_store_sales_l_027.txt',
    6: 'date_dim_store_sales_l_027.txt',
    7: 'store_store_sales_l_027.txt',
    8: 'item_store_sales_l_027.txt'
}

err_files_dict_dsb['040'] = {
    0: 'catalog_sales_040.txt',
    1: 'catalog_returns_040.txt',
    3: 'item_040.txt',
    4: 'date_dim_040.txt',
    5: 'catalog_returns_catalog_sales_both_040.txt',
    6: 'warehouse_catalog_sales_r_040.txt',
    7: 'item_catalog_sales_both_040.txt',
    8: 'date_dim_catalog_sales_both_040.txt',
    9: 'item_catalog_returns_both_040.txt',
}

err_files_dict_dsb['050'] = {
    2: 'store_050.txt',
    3: 'date_dim_1_050.txt',
    4: 'date_dim_2_050.txt',
    # 5: 'store_returns_store_sales_r_050.txt',
    6: 'store_store_sales_l_050.txt',
    7: 'date_dim_store_sales_l_050.txt',
    8: 'store_store_returns_l_050.txt',
    9: 'date_dim_store_returns_l_050.txt',
    10: 'date_dim_date_dim_non_2_050.txt'
}


err_files_dict_dsb['072'] = {
    0: 'catalog_sales_072.txt',
    3: 'item_072.txt',
    5: 'household_demographics_072.txt',
    6: 'date_dim_072.txt',
    9: 'inventory_catalog_sales_r_072.txt',
    10: 'inventory_catalog_sales_r_072.txt',
    11: 'inventory_catalog_sales_r_072.txt',
    12: 'inventory_catalog_sales_r_072.txt',
    13: 'inventory_catalog_sales_r_072.txt',
    14: 'item_catalog_sales_both_072.txt',
    15: 'customer_demographics_catalog_sales_r_072.txt',
    16: 'household_demographics_catalog_sales_both_072.txt',
    17: 'date_dim_catalog_sales_both_072.txt',
    18: 'inventory_warehouse__catalog_sales_072.txt',
    19: 'inventory_warehouse__catalog_sales_072.txt',
    20: 'inventory_warehouse__catalog_sales_072.txt',
    21: 'inventory_warehouse__catalog_sales_072.txt',
    22: 'inventory_warehouse__catalog_sales_072.txt',
    23: 'inventory_item_r_072.txt',
    24: 'inventory_item_r_072.txt',
    25: 'inventory_item_r_072.txt',
    26: 'inventory_item_r_072.txt',
    27: 'inventory_item_r_072.txt',
    28: 'inventory_item_r_072.txt',
    29: 'inventory_item_r_072.txt',
    # 30: 'inventory_date_dim_r_072.txt',
    # 31: 'inventory_date_dim_r_072.txt',
    # 32: 'inventory_date_dim_r_072.txt',
    # 33: 'inventory_date_dim_r_072.txt',
    # 34: 'inventory_date_dim_r_072.txt',
    # 35: 'date_dim_date_dim.txt',
}


err_files_dict_dsb['084'] = {
    1: 'customer_address.txt',
    4: 'income_band.txt',
    6: 'customer_address_customer_l_084.txt',
    # 7: 'customer_demographics_customer.txt',
    # 8: 'household_demographics_customer.txt',
    # 9: 'store_returns_customer.txt',
    # 10: 'store_returns_customer_demographics.txt',
    7: 'tmp.txt',
    8: 'tmp.txt',
    9: 'tmp.txt',
    10: 'tmp.txt',
    11: 'income_band_household_demographics_l_084.txt',}

err_files_dict_stats = {}
err_files_dict_stats['45a'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'pl.txt',
    3: 'ph.txt',
    4: 'v.txt',
    5: 'b.txt',
    6: 'u.txt',
    7: 'p_c_both.txt',
    8: 'c_pl_both.txt',
    9: 'c_ph_l.txt',
    10: 'c_v_both_1.txt',
    11: 'c_b_both.txt',
    12: 'u_c_r.txt',
    13: 'p_pl_both.txt',
    14: 'p_ph_l.txt',
    15: 'p_c_both.txt',
    16: 'ph_pl_both.txt',
    17: 'pl_v_both.txt',
    18: 'ph_v_r.txt',
    19: 'u_b_r.txt',
}
err_files_dict_stats['45b'] = {
    1: 'p.txt',
    2: 'pl.txt',
    7: 'p_c_l.txt',
    8: 'c_pl_r.txt',
    # 9: 'c_ph.txt',
    # 10: 'v_c.txt',
    # 11: 'b_c.txt',
    # 12: 'u_c.txt',
    13: 'p_pl_both.txt',
    14: 'p_ph_l.txt',
    15: 'p_v_l.txt',
    16: 'ph_pl_r.txt',
    17: 'pl_v_l.txt',
    # 18: 'v_ph.txt',
    # 19: 'u_b.txt',
}
err_files_dict_stats['45c'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'pl.txt',
    3: 'ph.txt',
    4: 'v.txt',
    7: 'p_c_both.txt',
    8: 'c_pl_both.txt',
    9: 'c_ph_both.txt',
    10: 'c_v_both_1.txt',
    11: 'c_b_l.txt',
    12: 'u_c_r.txt',
    13: 'p_pl_both.txt',
    14: 'p_ph_both.txt',
    15: 'p_v_both.txt',
    16: 'ph_pl_both.txt',
    17: 'pl_v_both.txt',
    18: 'ph_v_both.txt',
    # 19: 'u_b.txt'
}

err_files_dict_stats['45d'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'pl.txt',
    3: 'ph.txt',
    4: 'v.txt',
    5: 'b.txt',
    6: 'u.txt',
    7: 'p_c_both.txt',
    8: 'c_pl_both.txt',
    9: 'c_ph_l.txt',
    10: 'c_v_both_1.txt',
    11: 'c_b_both.txt',
    12: 'u_c_r.txt',
    13: 'p_pl_both.txt',
    14: 'p_ph_l.txt',
    15: 'p_c_both.txt',
    16: 'ph_pl_both.txt',
    17: 'pl_v_both.txt',
    18: 'ph_v_r.txt',
    19: 'u_b_r.txt',
}


err_files_dict_stats['40d'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'pl.txt',
    3: 'ph.txt',
    5: 'u.txt',
    6: 'p_c_both.txt',
    7: 'c_pl_both.txt',
    8: 'c_ph_both.txt',
    9: 'c_v_l_1.txt',
    10: 'u_c_r.txt',
    11: 'p_pl_both.txt',
    12: 'p_ph_both.txt',
    13: 'ph_pl_both.txt',
    14: 'u_v_l.txt',
}

err_files_dict_stats['40f'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'pl.txt',
    3: 'ph.txt',
    5: 'u.txt',
    6: 'p_c_both.txt',
    7: 'c_pl_both.txt',
    8: 'c_ph_both.txt',
    9: 'c_v_l_2.txt',
    10: 'u_c_r.txt',
    11: 'p_pl_both.txt',
    12: 'p_v_l.txt',
    13: 'p_u_both_2.txt',
    14: 'ph_pl_both.txt',
    15: 'pl_v_l.txt',
    16: 'ph_v_l.txt'
}

err_files_dict_stats['39c'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'pl.txt',
    3: 'v.txt',
    4: 'b.txt',
    5: 'u.txt',
    6: 'p_c_both.txt',
    7: 'c_pl_both.txt',
    8: 'c_v_both_1.txt',
    9: 'p_pl_both.txt',
    10: 'p_v_both.txt',
    11: 'p_b_both_2.txt', #?
    12: 'p_u_both_2.txt', #?
    13: 'pl_v_both.txt',
    14: 'u_b_both.txt',
}
err_files_dict_stats['37b'] = {
    2: 'u.txt',
    3: 'v.txt',
    4: 'b.txt',
    6: 'p_u_r_2.txt',
    7: 'p_v_r.txt',
    8: 'p_b_r.txt',
    9: 'u_v_both.txt',
    10: 'u_b_both.txt',
    11: 'b_v_both.txt',
}

err_files_dict_stats['38a'] = {
    0: 'p.txt',
    1: 'pl.txt',
    2: 'ph.txt',
    3: 'v.txt',
    4: 'b.txt',
    5: 'u.txt',
    6: 'p_pl_both.txt',
    7: 'p_ph_both.txt',
    8: 'p_v_both.txt',
    9: 'p_b_both_2.txt',
    10: 'p_u_both_2.txt',
    11: 'ph_v_both.txt',
    12: 'ph_b_both.txt', # ?
    13: 'ph_u_both.txt', # ?
    14: 'b_v_both.txt',
    15: 'u_v_both.txt',
    16: 'u_b_both.txt',
}

err_files_dict_stats['39d'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'pl.txt',
    3: 'v.txt',
    5: 'u.txt',
    6: 'p_c_both.txt',
    7: 'c_pl_both.txt',
    8: 'c_v_both_1.txt',
    9: 'p_pl_both.txt',
    10: 'p_v_both.txt',
    11: 'p_b_both_2.txt',
    12: 'p_u_both_2.txt',
    13: 'pl_v_both.txt',
    14: 'u_b_l.txt',
}

err_files_dict_stats['34e'] = {
    0: 'c.txt',
    1: 'p.txt',
    4: 'u.txt',
    5: 'p_c_both.txt',
    6: 'c_ph_l.txt',
    7: 'c_b_l.txt',
    8: 'u_c_both.txt',
    9: 'p_ph_l.txt',
    10: 'p_b_l_2.txt',
    11: 'p_u_both_2.txt',
    # 12: 'ph_b__c.txt',
    13: 'ph_u_r.txt',
    14: 'u_b_r.txt',
}
err_files_dict_stats['30a'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'pl.txt',
    3: 'ph.txt',
    4: 'v.txt',
    5: 'p_c_both.txt',
    6: 'c_pl_both.txt',
    7: 'c_ph_both.txt',
    8: 'c_v_both_1.txt',
    9: 'p_pl_both.txt',
    10: 'p_ph_both.txt',
    11: 'p_v_both.txt',
    12: 'ph_pl_both.txt',
    13: 'pl_v_both.txt',
    14: 'ph_v_both.txt',
}

err_files_dict_stats['31a'] = {
    1: 'p.txt',
    2: 'ph.txt',
    3: 'v.txt',
    4: 'u.txt',
    5: 'p_c_l.txt',
    6: 'c_ph_l.txt',
    7: 'c_v_r_2.txt',
    8: 'u_c_l.txt',
    9: 'p_ph_both.txt',
    10: 'p_v_both.txt',
    11: 'p_u_both_2.txt',
    12: 'ph_v_both.txt',
    13: 'ph_u_both.txt',
    14: 'u_v_both.txt',
}

err_files_dict_stats['31c'] = {
    1: 'p.txt',
    2: 'ph.txt',
    3: 'v.txt',
    4: 'u.txt',
    5: 'p_c_l.txt',
    6: 'c_ph_l.txt',
    7: 'c_v_r_2.txt',
    8: 'u_c_l.txt',
    9: 'p_ph_both.txt',
    10: 'p_v_both.txt',
    11: 'p_u_both_2.txt',
    12: 'ph_v_both.txt',
    13: 'ph_u_both.txt',
    14: 'u_v_both.txt',
}

err_files_dict_stats['43b'] = {
    0: 'c.txt',
    1: 'ph.txt',
    2: 'v.txt',
    4: 'c_ph_both.txt',
    5: 'c_v_both_1.txt',
    6: 'p_c_r.txt',
    7: 'ph_v_both.txt',
    8: 'p_ph_r.txt',
    9: 'p_v_r.txt',
}

err_files_dict_stats['18a'] = {
    0: 'c.txt',
    1: 'p.txt',
    3: 'v.txt',
    4: 'p_c_both.txt',
    5: 'c_pl_l.txt',
    6: 'c_v_both_1.txt',
    7: 'p_pl_l.txt',
    8: 'p_v_both.txt',
    9: 'pl_v_r.txt',
}

err_files_dict_stats['21b'] = {
    0: 'v.txt',
    1: 'p.txt',
    2: 'b.txt',
    3: 'u.txt',
    4: 'p_v_both.txt',
    5: 'p_b_both_2.txt',
    6: 'p_u_both_2.txt',
    7: 'u_b_both.txt',
}


err_files_dict_stats['28e'] = {
    0: 'ph.txt',
    1: 'p.txt',
    2: 'u.txt',
    3: 'b.txt',
    4: 'p_ph_both.txt',
    5: 'ph_u_both.txt',
    6: 'ph_b_both.txt',
    7: 'p_u_both_2.txt',
    8: 'p_b_both_2.txt',
    9: 'u_b_both.txt',
}

err_files_dict_stats['20g'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'v.txt',
    3: 'u.txt',
    4: 'p_c_both.txt',
    5: 'c_v_both_1.txt',
    6: 'p_v_both.txt',
    7: 'p_u_both_2.txt',
}


err_files_dict_stats['20a'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'v.txt',
    3: 'u.txt',
    4: 'p_c_both.txt',
    5: 'c_v_both_1.txt',
    6: 'u_c_both.txt',
    7: 'p_v_both.txt',
    8: 'p_u_both_2.txt',
    9: 'u_v_both.txt',
}

err_files_dict_stats['38b'] = {
    0: 'p.txt',
    1: 'pl.txt',
    2: 'ph.txt',
    3: 'v.txt',
    5: 'u.txt',
    6: 'p_pl_both.txt',
    7: 'p_ph_both.txt',
    8: 'p_v_both.txt',
    9: 'p_b_l_2.txt',
    10: 'p_u_both_2.txt',
    11: 'ph_v_both.txt',
    12: 'ph_b_l.txt', # ?
    13: 'ph_u_both.txt', # ?
    14: 'b_v_r.txt',
    15: 'u_v_both.txt',
    16: 'u_b_l.txt',
}

err_files_dict_stats['20c'] = {
    1: 'p.txt',
    3: 'u.txt',
    4: 'p_c_l.txt',
    5: 'c_v_both_2.txt',
    6: 'u_c_l.txt',
    7: 'p_v_l.txt',
    8: 'p_u_both_2.txt',
    9: 'u_v_l.txt',
}


err_files_dict_stats['20f'] = {
    1: 'p.txt',
    3: 'u.txt',
    4: 'p_c_l.txt',
    5: 'c_v_both_2.txt',
    6: 'p_v_r.txt',
    7: 'p_u_both_2.txt',
}


err_files_dict_stats['25b'] = {
    0: 'c.txt',
    1: 'ph.txt',
    3: 'u.txt',
    4: 'c_ph_both.txt',
    5: 'c_b_l.txt',
    6: 'u_c_both.txt',
    7: 'ph_b_l.txt',
    8: 'ph_u_both.txt',
    9: 'u_b_l.txt',
}

err_files_dict_stats['25a'] = {
    0: 'c.txt',
    1: 'ph.txt',
    2: 'b.txt',
    4: 'c_ph_both.txt',
    5: 'c_b_both.txt',
    6: 'u_c_r.txt',
    7: 'ph_b_both.txt',
    8: 'ph_u_l.txt',
    9: 'u_b_r.txt',
}


err_files_dict_stats['1a'] = {
    0: 'b.txt',
    # 1: 'u.txt',
}


err_files_dict_stats['8b'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'u.txt',
    3: 'p_c_both.txt',
    4: 'u_c_both.txt',
    5: 'p_u_both_2.txt',
}

err_files_dict_stats['8d'] = {
    0: 'c.txt',
    1: 'p.txt',
    2: 'u.txt',
    3: 'p_c_both.txt',
    4: 'u_c_both.txt',
    5: 'p_u_both_2.txt',
}

err_files_dict_stats['10b'] = {
    0: 'c.txt',
    1: 'v.txt',
    2: 'u.txt',
    3: 'c_v_both_2.txt',
    4: 'u_c_both.txt',
    5: 'u_v_both.txt',
}

err_files_dict_stats['10c'] = {
    0: 'c.txt',
    1: 'v.txt',
    2: 'u.txt',
    3: 'c_v_both_2.txt',
    4: 'u_c_both.txt',
    5: 'u_v_both.txt',
}

err_files_dict_stats['aa'] = {
    0: '.txt',
    1: '.txt',
    2: '.txt',
    3: '.txt',
    4: '.txt',
    5: '.txt',
    6: '.txt',
    7: '.txt',
    8: '.txt',
    9: '.txt',
    10: '.txt',
    11: '.txt',
    12: '.txt',
    13: '.txt',
    14: '.txt',
    15: '.txt',
    16: '.txt',
    17: '.txt',
    18: '.txt',
    19: '.txt',
}
### Only prepare data for only one dimension, base sensi_dim to find the abs_error file
def prepare_error_data(db_name, query_id, max_sel=1.0, min_sel = 0.0, rel_error=False, div=1, method=None, sensi_dim=-1, debug=False, pqo=False):
    error_list = []
    sel_est_list = []
    err_hist = [[] for _ in range(div)]

    count = 0

    if db_name == 'imdbloadbase':
        query_id = get_pure_q_id(query_id, db_name)
        if pqo:
            files_prefix = './data/abs-error-imdb-saved/'
        else:
            files_prefix = './data/abs-error-imdb/'
        files_prefix = './data/abs-error-imdb/'
        err_files_dict = err_files_dict_job

    elif db_name == 'dsb':
        files_prefix = './data/abs-error-dsb/'
        err_files_dict = err_files_dict_dsb
    elif db_name == 'stats':
        files_prefix = './data/abs-error-stats/'
        err_files_dict = err_files_dict_stats
    
    file_name = ''
    if sensi_dim in err_files_dict[query_id].keys():
        file_name = err_files_dict[query_id][sensi_dim]
        if debug:
            print(f"Generate error for dim {sensi_dim} from {files_prefix + file_name}")
        assert os.path.exists(files_prefix + file_name) == True, files_prefix + file_name
        with open(files_prefix + file_name, 'r') as f:
            while True:
                line = f.readline()
                if not line: break
                line = line.strip().split()
                ### err = true - est
                if rel_error:
                    if float(line[0]) == 0 or 0 == float(line[1]):
                        continue
                    error = cal_rel_error(float(line[0]), float(line[1]))
                else:
                    ### err = true - est
                    error = float(line[0]) - float(line[1])

                sel_est_list.append((float(line[1]), error))
                error_list.append(error)
                count += 1
    else:
        return [], []
    

    # divide 30000 to several buckects, each buckeck has same num of error
    # need to sort the error first
    r = int(count / div)
    error_list.sort()

    sorted_sel_to_err = sorted(sel_est_list, key=lambda x: x[0])

    for i in range(div):
        if i == div - 1:
            err_hist[i] = sorted_sel_to_err[i*r:]
        else:
            err_hist[i] = sorted_sel_to_err[i*r:(i+1)*r]

    # for i in err_hist:
    #     print(len(i), " in ", len(error_list), " (" , round(len(i)/len(error_list), 3), ") ", 
    #         round(min(i, key=lambda x: x[1])[1], 5),  round(max(i, key=lambda x: x[1])[1], 5))


    return error_list, err_hist



### For a specific dimension, return it's pdf function list based on the div
def cal_pdf(err_hist, rel_error=True, bandwidth=1, naive=False):
    
    if naive:
        naive_pdf_list = []
        for i in err_hist:
            i = [j[1] for j in i]
            i = np.array(i).reshape(-1, 1)
            mean = np.mean(i)
            std_dev = np.std(i)
            naive_pdf_list.append([mean, std_dev])
        return naive_pdf_list

    kde_list = []
    b = bandwidth
    # logging.info(f"bandwidth = {b}")
    for i in err_hist:

        # error_hist: [sel, error]
        ori_i = i
        i = [j[1] for j in i]
        i = np.array(i).reshape(-1, 1)
        # i = np.random.choice(i.flatten(), size=max(int(len(i)/100), 1), replace=False)
        # i = np.array(i).reshape(-1, 1)
        kde_list.append(KernelDensity(kernel="gaussian", bandwidth=b).fit(i))
    # print(sys.getsizeof(kde_list))
    return kde_list




def plot_error(error, kde, rel_error=False, name=None):
    fig, ax = plt.subplots(figsize=(12, 8))
    if rel_error:
        X_plot = np.linspace(min(-5, np.min(error) - 2), max(5, np.max(error) + 2), 1000)[:, np.newaxis]
    else:
        X_plot = np.linspace(min(np.min(error), -np.max(error)), max(-np.min(error), np.max(error)), 1000)[:, np.newaxis]
    log_dens = np.exp(kde.score_samples(X_plot))
    ax.plot(
        X_plot[:, 0],
        log_dens,
        
        linestyle="-",
    )
    # plot the original values of error
    ax.plot(error[:, 0], -0.005 - 0.01 * np.random.random(error.shape[0]), "+k")
    # Add labels to the axes
    if rel_error:
        ax.set_xlabel('Log-relative Selectivity Error', fontsize=35)
    else:
        ax.set_xlabel('Error')
    ax.set_ylabel('Probability Density', fontsize=40)
    ax.tick_params(axis='both', which='major', labelsize=30)
    # fig.savefig(f'./{name}.png', dpi=800)
    plt.tight_layout()
    fig.savefig(f'./{name}.pdf')
