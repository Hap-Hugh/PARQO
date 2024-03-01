import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.neighbors import KernelDensity
from utility import *

err_files_dict = {}
err_files_dict['17a'] = {
                        1: 'cn.txt', 
                        2: 'k.txt',
                        5: 'n.txt',
                        7: 'ci-mc--q17.txt', 
                        8: 'mk-ci--k.txt', 
                        9: 'n-ci-l.txt', 
                        10: 't-ci--n.txt',
                        11: 'mc-cn-r.txt', 
                        12: 'mk-k-r.txt', 
                        13: 'mk-mc--q2.txt',
                        14: 't-mc--cn.txt', 
                        15: 't-mk--k.txt',
                        }

err_files_dict['16a'] = {
    2: 'cn.txt',
    3: 'k.txt',
    7: 't.txt',
    8: 'ci-an-pure.txt', # ci an 
    9: 'n-an-pure.txt', # n an 
    10: 'ci-mc-pure.txt', # mc ci
    11: 'mk-ci-pure.txt', # mk ci !
    12: 'n-ci-pure.txt', # n ci !
    13: 't-ci-l.txt', # t ci
    14: 'mc-cn-r.txt', # mc cn
    15: 'mk-k-r.txt', # mk k
    16: 'mk-mc--q2.txt', # mix mk (cn mc) and mc (k mk)
    17: 't-mc-l.txt', # t mc
    18: 't-mk-l.txt', # t mk
}


err_files_dict['15a'] = {
    # 1: 'cn.txt',
    # 3: 'it.txt',
    5: 'mc.txt',
    6: 'mi.txt',
    8: 't.txt',
    9: 'mc-akat-l.txt', # mc aka_t
    10: 'mi-akat-l.txt', # mi aka_t
    11: 'mk-akat--mc.txt', # mk aka_t on mc
    12: 't-akat-l.txt', # t aka_t
    13: 'mc-cn-both.txt', # mc cn
    14: 'mc-ct-l.txt', # mc ct
    15: 'mi-it-both.txt', # mi it
    16: 'mk-k-pure.txt', # mk k
    17: 'mi-mc-both.txt', # mi mc
    18: 'mk-mc-r.txt', # mk mc
    19: 't-mc-both.txt', # t mc
    20: 'mk-mi-r.txt', # mk mi
    21: 't-mi-both.txt', # t mi
    22: 't-mk-l.txt', # t mk
}

err_files_dict['14a'] = {
    2: 'k.txt', #
    4: 'mi.txt', #
    5: 'miidx.txt', #
    7: 't.txt', #
    8: 'mi-it-both.txt', #
    9: 'miidx-it-both.txt', # 
    10: 'mk-k-r.txt', #
    11: 't-kt-both.txt', # 
    12: 'miidx-mi-both.txt', # 
    13: 'mk-mi-r.txt', # 
    14: 't-mi-both.txt', # 
    15: 'mk-miidx-r.txt', # 
    16: 't-miidx-both.txt', # 
    17: 't-mk-l.txt', # 
}

err_files_dict['13a'] = {
    0: 'cn.txt', #
    2: 'it.txt', #
    3: 'it.txt', #
    5: 'mc.txt', #
    6: 'mi.txt', #
    8: 't.txt', #
    9: 'mc-cn-r.txt', # 
    10: 'mc-ct-r.txt', #
    11: 'miidx-it-r.txt', # 
    12: 'mi-it-r.txt', # 
    13: 't-kt-r.txt', # 
    14: 'mi-mc--it.txt', # use mc (it mi)
    15: 'miidx-mc-pure.txt', # use the pure
    16: 't-mc--kt.txt', # use mc (kt t)
    17: 'miidx-mi--it.txt', # use miidx it mi
    18: 't-mi--itkt.txt', # use t (it mi); mi (kt t)
    19: 't-miidx--it.txt', # use t (it miidx)
}
err_files_dict['12a'] = {
    0: 'cn.txt', #
    1: 'ct.txt', #
    2: 'it.txt', #
    3: 'it.txt', #
    5: 'mi.txt', #
    6: 'miidx.txt', #
    7: 't.txt', #
    8: 'mc-cn-r.txt', #
    9: 'mc-ct-r.txt', # 
    10: 'mi-it-both.txt', #
    11: 'miidx-it-both.txt', # 
    12: 'mi-mc-l.txt', # 
    13: 'miidx-mc-l.txt', # 
    14: 't-mc-l.txt', # 
    15: 'miidx-mi-both.txt', # 
    16: 't-mi-both.txt', # 
    17: 't-miidx-both.txt', # 
}

err_files_dict['11a'] = {
    0: 'cn.txt', #
    1: 'ct.txt', #
    2: 'k.txt', #
    3: 'lt.txt', #
    4: 'mc.txt', #
    7: 't.txt', #
    8: 'mc-cn-both.txt', #
    9: 'mc-ct-both.txt', # 
    10: 'mk-k-r.txt', #
    11: 'ml-lt-r.txt', # 
    12: 'mk-mc-r.txt', # 
    13: 'ml-mc-r.txt', # 
    14: 't-mc-both.txt', # 
    15: 'ml-mk--k.txt', # 
    16: 't-mk-l.txt', # 
    17: 't-ml-l-1.txt', # 
}
err_files_dict['10a'] = {
    1: 'ci.txt', #
    2: 'cn.txt', #
    5: 'rt.txt', #
    6: 't.txt', #
    7: 'ci-chn-l.txt', #
    8: 'mc-ci-r.txt', #
    9: 'rt-ci-both.txt', # 
    10: 't-ci-both.txt', #
    11: 'mc-cn-r.txt', # 
    12: 'mc-ct--q10.txt', # 
    13: 't-mc-l.txt', # 
}
err_files_dict['9a'] = {
    2: 'ci.txt', #
    3: 'cn.txt', #
    4: 'mc.txt', #
    5: 'n.txt', #
    6: 'rt.txt', #
    7: 't.txt', #
    8: 'ci-an-l.txt', #
    9: 'n-an-l.txt', # 
    10: 'ci-chn-l.txt', #
    11: 'mc-ci-both.txt', # 
    12: 'n-ci-both.txt', # 
    13: 'rt-ci-both.txt', # ~
    14: 't-ci-both.txt', # 
    15: 'mc-cn-both.txt', # 
    16: 't-mc-both.txt', # 
}

err_files_dict['8a'] = {
    1: 'ci.txt', #
    2: 'cn.txt', #
    3: 'mc.txt', #
    4: 'n.txt', #
    5: 'rt.txt', #
    7: 'ci-an-l.txt', # 
    8: 'n-an-l.txt', # 
    9: 'mc-ci-both.txt', # 
    10: 'n-ci-both.txt', # 
    11: 'rt-ci-r.txt', # 
    12: 't-ci-both.txt', # 
    13: 'mc-cn-both.txt', # 
    14: 't-mc-both.txt', # 
}

err_files_dict['7a'] = {
    0: 'an.txt',
    2: 'it.txt',
    3: 'lt.txt',
    5: 'n.txt',
    6: 'pi.txt',
    7: 't.txt',
    8: 'ci-an-r.txt', # 
    9: 'n-an-both.txt', # 
    10: 'pi-an-both.txt', #
    11: 'ml-ci-pure.txt', # 
    12: 'n-ci-l.txt', # 
    13: 'pi-ci-l.txt', # 
    14: 't-ci-l.txt', # 
    15: 'pi-it-both.txt', # 
    16: 'ml-lt-r.txt', # 
    17: 't-ml-l-2.txt', # 
    18: 'pi-n-both.txt'
}
err_files_dict['6a'] = {
    1: 'k.txt', #
    3: 'n.txt', #
    4: 't.txt', #
    5: 'mk-ci-pure.txt', #
    6: 'n-ci-l.txt', #
    7: 't-ci-l.txt', #
    8: 'mk-k-r.txt', #
    9: 't-mk-l.txt', # 
}

err_files_dict['5a'] = {
    0: 'ct.txt', #
    2: 'mc.txt', #
    3: 'mi.txt', #
    4: 't.txt', #
    5: 'mc-ct-both.txt', #
    6: 'mi-it-r.txt', #
    7: 'mi-mc-both.txt', #
    8: 't-mc-both.txt', #
    9: 't-mi-both.txt', # 
}
err_files_dict['4a'] = {
    0: 'it.txt', #
    1: 'k.txt', #
    2: 'miidx.txt', #
    4: 't.txt', #
    5: 'miidx-it-both.txt', #
    6: 'mk-k-r.txt', #
    7: 'mk-miidx-r.txt', #
    8: 't-miidx-both.txt', #
    9: 't-mk-l.txt', # 
}
err_files_dict['3a'] = {
    0: 'k.txt', #
    1: 'mi.txt', #
    3: 't.txt', #
    4: 'mk-k-r.txt', #
    5: 'mk-mi-r.txt', #
    6: 't-mi-both.txt', #
    7: 't-mk-l.txt', #
}
err_files_dict['2a'] = {
    0: 'cn.txt', #
    1: 'k.txt', #
    5: 'mc-cn-r.txt', #
    6: 'mk-k-r.txt', #
    7: 'mk-mc--q2.txt', # mix mk (cn mc) and mc (k mk)
    8: 't-mc--cn.txt', #
    9: 't-mk--k.txt', # 
}

err_files_dict['1a'] = {
    0: 'ct.txt', #
    1: 'it.txt', #
    2: 'mc.txt', #
    5: 'mc-ct-r.txt', #
    6: 'miidx-it-r.txt', #
    7: 'miidx-mc-r.txt', # ~
    8: 't-mc-r.txt', # ~
    9: 't-miidx--it.txt', # 
}



err_files_dict['18a'] = {
    0: 'ci.txt', #
    5: 'n.txt', #
    7: 'mi-mc-pure.txt', # 
    8: 'miidx-ci-r.txt', # 
    9: 'n-ci-both.txt', # 
    10: 't-ci-r.txt', # 
    11: 'mi-it-r.txt', # 
    12: 'miidx-it-r.txt', # 
    13: 'miidx-mi--it.txt', # miidx-mi
    14: 't-mi--it.txt', # t-mi
    15: 't-miidx--it.txt', # t-miidx
}


err_files_dict['19a'] = {
    2: 'ci.txt', #
    3: 'cn.txt', #
    4: 'it.txt', #
    5: 'mc.txt', #
    6: 'mi.txt', #
    7: 'n.txt', #
    8: 'rt.txt', #
    9: 't.txt', # 
    10: 'ci-an-l.txt', #
    11: 'n-an-l.txt', # 
    12: 'ci-chn-l.txt', # 
    13: 'mc-ci-both.txt', # 
    14: 'mi-ci-both.txt', # 
    15: 'n-ci-both.txt', # 
    16: 'rt-ci-both.txt', # 
    17: 't-ci-both.txt', # 
    18: 'mc-cn-both.txt', # 
    19: 'mi-it-both.txt', #
    20: 'mi-mc-both.txt', #
    21: 't-mc-both.txt', #
    22: 't-mi-both.txt', #
}




err_files_dict['20a'] = {
    1: 'cct.txt', #
    2: 'cct.txt', #
    3: 'chn.txt', #
    5: 'k.txt', #
    9: 't.txt', # 
    10: 'cct-cc-1-l.txt', # 
    11: 'cct-cc-2-l.txt', # 
    12: 'ci-cc--cct.txt', #  mix cc's two join keys
    13: 'mk-cc--cct.txt', #  #  mix cc's two join keys
    14: 't-cc-l.txt', # 
    15: 'ci-chn-r.txt', # 
    16: 'mk-ci--chn.txt', # 
    17: 'n-ci--chn.txt', # 
    18: 't-ci-l.txt', # 
    19: 'mk-k-r.txt', #
    20: 't-kt-both.txt', #
    21: 't-mk-l.txt', #
}
err_files_dict['21a'] = {
    0: 'cn.txt', #
    1: 'ct.txt', #
    2: 'k.txt', #
    3: 'lt.txt', #
    4: 'mc.txt', #
    5: 'mi.txt', #
    8: 't.txt', #
    9: 'mc-cn-both.txt', # 
    10: 'mc-ct-both.txt', #
    11: 'mk-k-r.txt', # 
    12: 'ml-lt-r.txt', # 
    13: 'mi-mc-both.txt', # 
    14: 'mk-mc-r.txt', # 
    15: 'ml-mc-r.txt', # 
    16: 't-mc-both.txt', # 
    17: 'mk-mi-r.txt', # 
    18: 'ml-mi-r.txt', #
    19: 't-mi-both.txt', #
    20: 'ml-mk--k.txt', #
    21: 't-mk-l.txt', #
    22: 't-ml-l-1.txt', #
}
err_files_dict['22a'] = {
    0: 'cn.txt', #
    2: 'it.txt', #
    3: 'it.txt', #
    4: 'k.txt', #
    6: 'mc.txt', #
    7: 'mi.txt', #
    8: 'miidx.txt', #
    10: 't.txt', #
    11: 'mc-cn-both.txt', # 
    12: 'mc-ct-l.txt', # 
    13: 'mi-it-both.txt', # 
    14: 'miidx-it-both.txt', # 
    15: 'mk-k-r.txt', # 
    16: 't-kt-both.txt', # 
    17: 'mi-mc-both.txt', # 
    18: 'miidx-mc-both.txt', # 
    19: 'mk-mc-r.txt', #
    20: 't-mc-both.txt', #
    21: 'miidx-mi-both.txt', #
    22: 'mk-mi-r.txt', #
}
err_files_dict['23a'] = {
    1: 'cct.txt', #
    2: 'cn.txt', #
    4: 'it.txt', #
    8: 'mi.txt', #
    10: 't.txt', #
    11: 'cct-cc-2-l.txt', # 
    12: 'mc-cc-pure.txt', # 
    13: 'mi-cc-l.txt', # 
    14: 'mk-cc--q23.txt', # cct+mi
    15: 't-cc-l.txt', # 
    16: 'mc-cn-r.txt', # 
    17: 'mc-ct-r.txt', # 
    18: 'mi-it-both.txt', # 
    19: 'mk-k-r.txt', #
    20: 't-kt-both.txt', #
    21: 'mi-mc-l.txt', #
    22: 'mk-mc--cn.txt', #
    23: 't-mc-l.txt', #
    24: 'mk-mi-r.txt', #
    25: 't-mi-both.txt', #
    26: 't-mk-l.txt', #
}
err_files_dict['24a'] = {
    2: 'ci.txt', #
    3: 'cn.txt', #
    4: 'it.txt', #
    5: 'k.txt', #
    7: 'mi.txt', #
    9: 'n.txt', #
    10: 'rt.txt', # 
    11: 't.txt', # 
    12: 'ci-an-l.txt', # 
    13: 'n-an-l.txt', # 
    14: 'ci-chn-l.txt', # 
    15: 'mc-ci-r.txt', # 
    16: 'mi-ci-both.txt', # 
    17: 'mk-ci-r.txt', # 
    18: 'n-ci-both.txt', # 
    19: 'rt-ci-both.txt', #
    20: 't-ci-both.txt', #
    21: 'mc-cn-r.txt', #
    22: 'mi-it-both.txt', #
    23: 'mk-k-r.txt', #
    24: 'mi-mc-l.txt', #
    25: 'mk-mc--cn.txt', #
    26: 't-mc-l.txt', #
    27: 'mk-mi-r.txt', #
    28: 't-mi-both.txt', #
    29: 't-mk-l.txt', #

}

err_files_dict['25a'] = {
    0: 'ci.txt', #
    1: 'it.txt', #
    2: 'it.txt', #
    3: 'k.txt', #
    4: 'mi.txt', #
    7: 'n.txt', #
    9: 'mi-ci-both.txt', # 
    10: 'miidx-ci-r.txt', #
    11: 'mk-ci-r.txt', # 
    12: 'n-ci-both.txt', # 
    13: 't-ci-r.txt', # 
    14: 'mi-it-both.txt', # 
    15: 'miidx-it-r.txt', # 
    16: 'mk-k-r.txt', # 
    17: 'miidx-mi-r.txt', # 
    18: 't-mi-r.txt', # 
}

err_files_dict['26a'] = {
    # 1: 'cct.txt', #
    2: 'cct.txt', #
    3: 'chn.txt', #
    # 5: 'it.txt', #
    # 6: 'k.txt', #
    8: 'miidx.txt', #
    11: 't.txt', # 
    12: 'cct-cc-1-l.txt', # 
    13: 'cct-cc-2-l.txt', # 
    14: 'ci-cc--cct.txt', # 
    15: 'miidx-cc-l.txt', # 
    16: 'mk-cc--cct.txt', # 
    17: 't-cc-l.txt', # 
    18: 'ci-chn-r.txt', # 
    19: 'miidx-ci-l.txt', #
    20: 'mk-ci--chn.txt', #
    21: 'n-ci-l.txt', #
    22: 't-ci-l.txt', #
    23: 'miidx-it-both.txt', #
    24: 'mk-k-r.txt', #
    25: 't-kt-both.txt', #
    26: 'mk-miidx-r.txt', #
    27: 't-miidx-both.txt', #
    28: 't-mk-l.txt', #
}

err_files_dict['27a'] = {
    1: 'cct.txt', #
    2: 'cct.txt', #
    3: 'cn.txt', #
    4: 'ct.txt', #
    5: 'k.txt', #
    6: 'lt.txt', #
    7: 'mc.txt', #
    8: 'mi.txt', #
    11: 't.txt', # 
    12: 'cct-cc-1-l.txt', # 
    13: 'cct-cc-2-l.txt', # 
    14: 'mc-cc-l.txt', # 
    15: 'mi-cc-l.txt', # 
    16: 'mk-cc--q23.txt', #  
    17: 'ml-cc--cct.txt', # !
    18: 't-cc-l.txt', # 
    19: 'mc-cn-both.txt', #
    20: 'mc-ct-both.txt', #
    21: 'mk-k-r.txt', #
    22: 'ml-lt-r.txt', #
    23: 'mi-mc-both.txt', #
    24: 'mk-mc-r.txt', #
    25: 'ml-mc-r.txt', #
    26: 't-mc-both.txt', #
    27: 'mk-mi-r.txt', #
    28: 'ml-mi-r.txt', #
    29: 't-mi-both.txt', #
    30: 'ml-mk--k.txt', 
    31: 't-mk-l.txt',
    32: 't-ml-l-1.txt'
}



err_files_dict['28a'] = {
    1: 'cct.txt', #
    2: 'cct.txt', #
    3: 'cn.txt', #
    5: 'it.txt', #
    6: 'it.txt', #
    7: 'k.txt', #
    9: 'mc.txt', # 
    10: 'mi.txt', #
    11: 'mi_idx.txt', # 
    13: 't.txt', # 
    14: 'cct-cc-1-l.txt', # 
    15: 'cct-cc-2-l.txt', # 
    16: 'mc-cc-l.txt', # 
    17: 'mi-cc-l.txt', # 
    18: 'miidx-cc-l.txt', # 
    # 19: '.txt', #~
    20: 't-cc-l.txt', #~
    21: 'mc-cn-both.txt', #
    22: 'mc-ct-l.txt', #
    23: 'mi-it-both.txt', #
    24: 'miidx-it-both.txt', #
    25: 'mk-k-r.txt', #
    26: 't-kt-both.txt', #
    27: 'mi-mc-both.txt', #
    28: 'miidx-mc-both.txt', #
    29: 'mk-mc-r.txt', #
    30: 't-mc-both.txt', #
    31: 'miidx-mi-both.txt', #
    32: 'mk-mi-r.txt', #
    33: 't-mi-both.txt', #
    34: 'mk-miidx-r.txt', #
    35: 't-miidx-both.txt', #
    36: 't-mk-l.txt', #
}

err_files_dict['29a'] = {
    2: 'cct.txt',
    3: 'cct.txt',
    4: 'chn.txt',
    5: 'ci.txt',
    6: 'cn.txt',
    7: 'it.txt',
    8: 'it.txt',
    9: 'k.txt',
    11: 'mi.txt', # 
    13: 'n.txt', # 
    15: 'rt.txt', # 
    16: 't.txt', # 
    17: 'ci-an-l.txt', # 
    18: 'n-an-l.txt', # 
    19: 'pi-an-both.txt', #
    20: 'cct-cc-1-l.txt', #
    21: 'cct-cc-2-l.txt', #
    22: 'ci-cc--cct.txt', #
    23: 'mc-cc-l.txt', #
    24: 'mi-cc-l.txt', #
    25: 'mk-cc--q23.txt', #
    26: 't-cc-l.txt', #
    27: 'ci-chn-r.txt', #
    28: 'mc-ci-r.txt', #
    29: 'mi-ci-both.txt', #
    30: 'mk-ci-r.txt', #
    31: 'n-ci-both.txt', #
    32: 'pi-ci-both.txt', # ~
    33: 'rt-ci-both.txt', #
    34: 't-ci-both.txt', #
    35: 'mc-cn-r.txt', #
    36: 'mi-it-both.txt', #
    37: 'pi-it-both.txt', #
    38: 'mk-k-r.txt', #
    39: 'mi-mc-l.txt', #
    40: 'mk-mc--q2.txt', #
    41: 't-mc-l.txt', #
    42: 'mk-mi-r.txt', #
    43: 't-mi-both.txt', #
    44: 't-mk-l.txt', #
    45: 'pi-n-both.txt', #
}

err_files_dict['30a'] = {
    3: 'ci.txt', #
    10: 'n.txt', #
    11: 't.txt', # 
    12: 'cct-cc-1-l.txt', # 
    13: 'cct-cc-2-l.txt', # 
    14: 'ci-cc-l.txt', #
    15: 'mi-cc-l.txt', # 
    16: 'miidx-cc-l.txt', # ~
    17: 'mk-cc--q23.txt', # 
    18: 't-cc-l.txt', # 
    19: 'mi-ci-both.txt', #
    20: 'miidx-ci-r.txt', #
    21: 'mk-ci-r.txt', #
    22: 'n-ci-both.txt', #
    23: 't-ci-both.txt', #
    24: 'mi-it-both.txt', #
    25: 'miidx-it-r.txt', #
    26: 'mk-k-r.txt', #
    27: 'miidx-mi-r.txt', #
    28: 'mk-mi-r.txt', #
    29: 't-mi-both.txt', #
    30: 'mk-miidx-r.txt', # ~
    31: 't-miidx-l.txt', #
    32: 't-mk-l.txt', #
}


err_files_dict['31a'] = {
    0: 'ci.txt', #
    1: 'cn.txt', #
    # 2: 'it.txt', #
    # 3: 'it.txt', #
    4: 'k.txt', #
    6: 'mi.txt', #
    9: 'n.txt', #
    11: 'mc-ci-r.txt', # 
    12: 'mi-ci-both.txt', # 
    13: 'miidx-ci-r.txt', # 
    14: 'mk-ci-r.txt', # 
    15: 'n-ci-both.txt', # 
    16: 't-ci-r.txt', # 
    17: 'mc-cn-r.txt', # 
    18: 'mi-it-both.txt', # 
    19: 'miidx-it-r.txt', #
    20: 'mk-k-r.txt', #
    21: 'mi-mc-l.txt', #
    22: 'miidx-mc--it.txt', # ~
    23: 'mk-mc--q2.txt', #
    24: 't-mc--cn.txt', #
    25: 'miidx-mi-r.txt', #
    26: 'mk-mi-r.txt', #
    27: 't-mi-r.txt', #
    28: 'mk-miidx--k.txt', # ~
    29: 't-miidx--it.txt', # 
    30: 't-mk--k.txt',
}


err_files_dict['32a'] = {
    0: 'k.txt',
    6: 'mk-k-r.txt', 
    8: 'ml-mk--k.txt', # ml mk
    9: 't-mk--k.txt',
    10: 't-ml-1-pure.txt', # t ml
    11: 't-ml-2-pure.txt', # t ml
}




### Only prepare data for only one dimension, base sensi_dim to find the abs_error file
def prepare_error_data(query_id, max_sel=1.0, min_sel = 0.0, rel_error=False, div=1, method=None, sensi_dim=-1, debug=False):
    error_list = []
    sel_est_list = []
    err_hist = [[] for _ in range(div)]
    step = 1.0 / div
    base = 1 / pow(10, div - 1)
    count = 0
    # TODO
    files_prefix = './data/abs_error/'

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

    

    r = int(count / div)
    error_list.sort()

    sorted_sel_to_err = sorted(sel_est_list, key=lambda x: x[0])

    for i in range(div):
        if i == div - 1:
            err_hist[i] = sorted_sel_to_err[i*r:]
        else:
            err_hist[i] = sorted_sel_to_err[i*r:(i+1)*r]



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
    for i in err_hist:

        ori_i = i
        i = [j[1] for j in i]
        i = np.array(i).reshape(-1, 1)

        kde_list.append(KernelDensity(kernel="gaussian", bandwidth=b).fit(i))
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
