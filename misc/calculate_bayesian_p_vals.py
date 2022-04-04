import time
import numpy as np
import pickle5 as pickle
import read_data as dat
from scipy.stats import norm, beta, gaussian_kde
from matplotlib import pyplot as plt

nchains=4
nsamples=18000
nthin=1
nwarmup=2000

reps = 50

seed = int(time.time())
print('seed:', seed)#
rD = np.random.default_rng(seed)

outfile = open('bayesian_p_vals.out', 'w')

material = np.array(dat.mat, int) - 1
batch = np.array(dat.translated_batch, int) - 1

A_mean, A_scale = 0.186, 0.0224

Y = dat.Y[np.newaxis,::]

def calc_p_val(filename,
               filepath,
               nchains,
               nsamples,
               nthin,
               nwarmup):
               
    fit = pickle.load( open(filepath + filename, 'rb') )[int(nwarmup/nthin*nchains)::]

    mu_cols = [col for col in fit.columns if col.startswith('mu.')]
    T_cols =  [col for col in fit.columns if col.startswith('T.')]
    log_phi_cols = [col for col in fit.columns if col.startswith('log_phi.')]

    mu = np.array(fit[mu_cols])

    phi = np.exp(np.array(fit[log_phi_cols]))

    sigma_squared = mu * (1 - mu) / (np.take(phi, material) + 1)

    alp_prime = mu * np.take(phi, material, axis=1)
    bet_prime = (1-mu) * np.take(phi, material, axis=1)

    new_shape = list(alp_prime.shape).append(reps)
    
    T_prime = beta.rvs(a=alp_prime, b=bet_prime, size=new_shape)
    Y_prime = norm.rvs(loc = T_prime*A_mean, scale = T_prime*A_scale, size=new_shape)


    #Q = np.sum(np.power(np.subtract(Y, mu), 2), axis=1)
    Q = np.sum( (Y-mu) * (Y-mu) / sigma_squared, axis=1)
    Q_prime = np.sum( (Y_prime-mu) * (Y_prime-mu) / sigma_squared, axis=1)

    pval = np.sum(np.greater(Q_prime, Q)) / Q.size
    return Q, Q_prime, pval


Q, Q_prime, pval = calc_p_val('AH_model_1_DEFAULT_INIT_11_10_0.3_1.fit',
                              'model_1/fits/pickle/',
                              nchains,
                              nsamples,
                              nthin,
                              nwarmup)

print('model_1 (with BE):', pval)
outfile.write('model_1 (with BE): %.3f\n' %pval)

Q, Q_prime, pval = calc_p_val('AH_model_1_DEFAULT_INIT_NO_BATCH_EFFECT_11_10_0.3_1.fit',
                              'model_1/fits/pickle/',
                              nchains,
                              nsamples,
                              nthin,
                              nwarmup)

print('model_1 (without BE):', pval)
outfile.write('model_1 (without BE): %.3f\n' %pval)

Q, Q_prime, pval = calc_p_val('AH_model_2_DEFAULT_INIT_11_10_0.3_2.fit',
                              'model_2/fits/pickle/',
                              nchains,
                              nsamples,
                              nthin,
                              nwarmup)

print('model_2 (with BE):', pval)
outfile.write('model_2 (with BE): %.3f\n' %pval)

Q, Q_prime, pval = calc_p_val('AH_model_2_DEFAULT_INIT_NO_BATCH_EFFECT_11_10_0.3_2.fit',
                              'model_2/fits/pickle/',
                              nchains,
                              nsamples,
                              nthin,
                              nwarmup)

print('model_2 (without BE):', pval)
outfile.write('model_2 (without BE): %.3f\n' %pval)

Q, Q_prime, pval = calc_p_val('AH_model_3_DEFAULT_INIT_11_10_0.3_1.fit',
                              'model_3/fits/pickle/',
                              nchains,
                              nsamples,
                              nthin,
                              nwarmup)

print('model_3 (with BE):', pval)
outfile.write('model_3 (with BE): %.3f\n' %pval)

Q, Q_prime, pval = calc_p_val('AH_model_3_DEFAULT_INIT_NO_BATCH_EFFECT_11_10_0.3_1.fit',
                              'model_3/fits/pickle/',
                              nchains,
                              nsamples,
                              nthin,
                              nwarmup)

print('model_3 (without BE):', pval)
outfile.write('model_3 (without BE): %.3f\n' %pval)

Q, Q_prime, pval = calc_p_val('AH_model_4_DEFAULT_INIT_11_10_0.3_1.fit',
                              'model_4/fits/pickle/',
                              nchains,
                              nsamples,
                              nthin,
                              nwarmup)
                              

print('model_4 (with BE):', pval)
outfile.write('model_4 (with BE): %.3f\n' %pval)

Q, Q_prime, pval = calc_p_val('AH_model_4_DEFAULT_INIT_NO_BATCH_EFFECT_11_10_0.3_1.fit',
                              'model_4/fits/pickle/',
                              nchains,
                              nsamples,
                              nthin,
                              nwarmup)

print('model_4 (without BE):', pval)
outfile.write('model_4 (without BE): %.3f\n' %pval)






