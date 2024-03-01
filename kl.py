from utility import *
from scipy.stats import entropy
from sklearn.neighbors import KernelDensity
from prep_error_list import plot_error
from prep_selectivity import cal_new_sel_by_err


def cal_kl(err_info_dic_1, est_card_1, raw_card_1, 
           err_info_dic_2, est_card_2, raw_card_2,
           dim=None,
           N=100):
    if not dim:
        dim = list(range(len(err_info_dic_1))) # Consider all dims

    density_product_1 = 1
    density_product_2 = 1
    for i in dim:
        print("===== Dim ", i)
        if err_info_dic_1[i] == []:
            continue
        r_1 = find_bin_id_from_err_hist_list(est_card_1, raw_card_1, cur_dim=i, err_info_dict=err_info_dic_1)
        pdf_after_bin_1 = err_info_dic_1[i][2][r_1]
        sel_1 = max(1, est_card_1[i])/raw_card_1[i]

        r_2 = find_bin_id_from_err_hist_list(est_card_2, raw_card_2, cur_dim=i, err_info_dict=err_info_dic_2)
        pdf_after_bin_2 = err_info_dic_2[i][2][r_2]
        sel_2 = max(1, est_card_2[i])/raw_card_2[i]
        
        max_rel_err_1 = max(err_info_dic_1[i][1][r_1], key=lambda x: x[1])[1]
        min_rel_err_1 = min(err_info_dic_1[i][1][r_1], key=lambda x: x[1])[1]
        max_rel_err_2 = max(err_info_dic_2[i][1][r_2], key=lambda x: x[1])[1]
        min_rel_err_2 = min(err_info_dic_2[i][1][r_2], key=lambda x: x[1])[1]


        err_sample_1 = pdf_after_bin_1.sample(N)
        sel_samples_1 = np.array([cal_new_sel_by_err(e, sel_1) for e in err_sample_1])
        err_samples_2 = np.array([cal_rel_error(s, sel_2) for s in sel_samples_1])
        density_1 = np.exp(pdf_after_bin_1.score_samples(err_sample_1.reshape(-1, 1))) # probability correspond to this sample
        density_2 = np.exp(pdf_after_bin_2.score_samples(err_samples_2.reshape(-1, 1)))
        density_product_1 *= density_1
        density_product_2 *= density_2

        print("Temp KL: ", np.log(density_1 / density_2).mean())
        print(f"est_card_ori: {est_card_1[i]}, table_size: {raw_card_1[i]}, est_card_new: {est_card_2[i]}, table_size: {raw_card_2[i]}")

    kl_divergence = np.log(density_product_1 / density_product_2).mean()
    
    return kl_divergence

