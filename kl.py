from utility import *
from scipy.stats import entropy
from sklearn.neighbors import KernelDensity
from prep_error_list import plot_error
from prep_selectivity import cal_new_sel_by_err


### 1 is what we already know
### 2 is what we want to estimate
def cal_kl(err_info_dic_1, est_card_1, raw_card_1, 
           err_info_dic_2, est_card_2, raw_card_2,
           dim=None,
           N=100,
           debug=False):
    if not dim:
        dim = list(range(len(err_info_dic_1))) # Consider all dims

    density_product_1 = 1
    density_product_2 = 1
    for i in dim:
        if debug: print("===== Dim ", i)
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
        # print(sel_samples_1)
        # print(density_1, density_2)
        # print(sel_1, sel_2) 
        # print(np.log(density_1 / density_2))



        # print(max_rel_err, min_rel_err)
        # left = min(cal_new_sel_by_err(min_rel_err_1, sel_1), cal_new_sel_by_err(min_rel_err_2, sel_2))
        # right = max(cal_new_sel_by_err(max_rel_err_1, sel_1), cal_new_sel_by_err(max_rel_err_2, sel_2))
        # print(left, right)
        # step = (right - left) / 1000000
        # samples = np.arange(left, right, step)[:1000000]
        
        # x1 = np.log(samples/sel_1) # relative error of 1
        # x2 = np.log(samples/sel_2) # relative error of 2
        # density_1 = np.exp(pdf_after_bin_1.score_samples(x1.reshape(-1, 1))) # please * err_step !! probability correspond to this sample
        # density_2 = np.exp(pdf_after_bin_2.score_samples(x2.reshape(-1, 1)))
        # print(sum(density_1))
        # density_product_1 *= density_1
        # density_product_2 *= density_2
        # print(f"--- PQO: Temp entropy between den1 and den2: {entropy(density_1, density_2)}")

        
        # print(density_1, density_2)
        if debug: print("Temp KL: ", np.log(density_1 / density_2).mean())
        # print("density", density_1, density_2)
        if debug: print(f"est_card_ori: {est_card_1[i]}, table_size: {raw_card_1[i]}, est_card_new: {est_card_2[i]}, table_size: {raw_card_2[i]}")
        # importv pdb; pdb.set_trace()
        # input()
        
    # kl_divergence = entropy(density_product_1, density_product_2)
    # print(entropy(density_product_1, density_product_2), np.log(density_product_1 / density_product_2).mean())
    kl_divergence = np.log(density_product_1 / density_product_2).mean()
    
    return kl_divergence



'''
r = find_bin_id_from_err_hist_list(est_card, raw_card, cur_dim=i, err_info_dict=err_info_dict)
pdf_after_bin = err_info_dict[i][2][r]
err_data_used_by_pdf = [_[1] for _ in err_info_dict[i][1][r]] # (est_sel, rel_err)
err_data_used_by_pdf = np.array(err_data_used_by_pdf).reshape(-1, 1)
plot_error(err_data_used_by_pdf, pdf_after_bin, rel_error=True, name=f'data/plot_after_bin/{query_id}/{i}')
'''



# x1 = np.array([0])
# x2 = np.array([2])

# # Fit KDEs for each dimension separately
# kde_x1 = KernelDensity(kernel='gaussian', bandwidth=2).fit(x1.reshape(-1, 1))
# kde_x2 = KernelDensity(kernel='gaussian', bandwidth=2).fit(x2.reshape(-1, 1))

# plot_error(list(x1), kde_x1, rel_error=True, name='1')
# plot_error(list(x2), kde_x2, rel_error=True, name='2')


# # Generate samples for each dimension
# samples_x1 = np.linspace(-10, 10, 10)[:, np.newaxis]
# samples_x2 = np.linspace(-10, 10, 10)[:, np.newaxis]

# # Calculate densities for the samples
# density_x1 = np.exp(kde_x1.score_samples(samples_x1[:, 0].reshape(-1, 1)))
# density_x2 = np.exp(kde_x2.score_samples(samples_x2[:, 0].reshape(-1, 1)))
# # Calculate KL divergence between the multivariate distributions
# # joint_density_X = [1/3, 1/3, 1/3]
# # joint_density_Y = [9/25, 12/25, 4/25]

# kl_divergence = entropy(density_x1, density_x2)
# print("KL Divergence:", kl_divergence)
# import pdb; pdb.set_trace()
