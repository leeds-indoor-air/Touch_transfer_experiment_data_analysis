'''
Quasi-equilibrium phase
T (deg Cel)
RH (%)
Median half-life (h)
2.5 %
97.5 %
'''
import read_data as dat
import pickle5 as pickle
from matplotlib import pyplot as plt
from matplotlib import cm
from scipy.stats import norm, beta
from scipy.special import expit
import numpy as np
import time
from math import log, exp

nchains=4
nsamples=18000
nthin=1
nwarmup=2000

cmap = cm.get_cmap('coolwarm')

path = 'model_3/fits/pickle/AH_model_3_DEFAULT_INIT_11_10_0.3_1.fit'
fit = pickle.load(open(path, 'rb'))[int(nwarmup*nchains/nthin)::]

seed = int(time.time())
print('seed:', seed)
rD = np.random.default_rng(seed)

table_one = [[10, 40, 26.55, 20.28, 38.75],
             [10, 65, 14.22, 12.17, 17.16],
             [10, 85, 13.78, 10.67, 19.70],
             [22, 40, 6.43, 5.52, 7.56],
             [22, 65, 2.41, 2.03, 2.88],
             [22, 85, 7.50, 6.22, 9.24],
             [27, 40, 3.43, 2.91, 4.12],
             [27, 65, 1.52, 1.05, 2.14],
             [27, 85, 2.79, 2.12, 3.78]]

'''
melamine
posterior mean, stdev - Model 3 (paper) Model 2 (me)
'''
beta_0 = np.array(fit['beta_0'])
beta_1 = np.array(fit['beta_1'])
M = np.array(fit['M.4'])
phi = np.exp(np.array(fit['log_phi.4']))
sigma = np.exp(np.array(fit['log_sigma']))

beta_0_median = np.median(beta_0)
beta_1_median = np.median(beta_1)
M_median = np.median(M)
phi_median = np.median(phi)
sigma_median = np.median(sigma)

print('\nmedians:')
print('beta_0: %s\nbeta_1: %s\nM: %s\nphi: %s\nsigma: %s' %(beta_0_median,
                                                            beta_1_median,
                                                            M_median,
                                                            phi_median,
                                                            sigma_median))

t = np.array([1, 10, 20])  #time to touch
'''
10 deg Cel, 40% RH
convert_AH(RH, temp)
'''

_, _, _, AH_mean, _, _, _, _ = dat.read_in('/home/cenlb/Projects/touch_tx/data/MEL_June2021.csv')




plot_indices = [(0, 0), (0, 1), (0,2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
colors = [cmap(0.25),cmap(0.25),cmap(0.25),
          cmap(0.75),cmap(0.75),cmap(0.75),
          cmap(0.9),cmap(0.9),cmap(0.9)]
fig, ax = plt.subplots(3, 3, sharey = True, sharex=True)
fig.set_size_inches(10, 10)

for n, (i,j) in zip(range(9), plot_indices):
    hl_median = table_one[n][2]
    print('median half life:', hl_median)

    AH = dat.convert_AH(table_one[n][1], table_one[n][0])
    print('Temp: %s, RH: %s' %(table_one[n][0], table_one[n][1]))
    print('AH: %.3f.' %AH)

    #tau = norm.rvs(loc=0.0, scale=sigma, random_state=rD)
    ita = beta_0_median + beta_1_median * (AH - AH_mean)
    mu = expit(ita) * M_median
    alp = mu * phi_median
    bet = (1-mu) * phi_median

    T = beta.rvs(a=alp, b=bet, size=(40000, 3))
    #plt.hist(T, bins=40)
    #plt.show()




    #There is a unit concentration of pathogen at t = 0 in contact area, 
    #so we're not considering variations in fingertip area

    C_0 = 500

    lam = log(2)/hl_median
    print('decay rate: %.3f' %lam)

    C_t = C_0 * np.exp(-lam * t)
    #print('C_t: %.3f' %C_t)

    dose = T * C_t

    parts = ax[i,j].violinplot( dose, showmedians=True, showmeans=False, showextrema=True )
    for p in parts['bodies']:
        p.set_facecolor(colors[n])
        p.set_edgecolor('black')
        p.set_alpha(1)

    
    ax[i,j].set_title(str(table_one[n][0]) + r'$^\circ$C, ' + str(table_one[n][1]) + '% RH')

ax[0, 0].set_xticks([1, 2, 3])
ax[0, 0].set_xticklabels(['1', '10', '20'])
ax[2, 1].set_xlabel('Time post-inoculation (hrs)')
ax[1, 0].set_ylabel(r'Viral concentration (PFU cm$^{-2}$)')
fig.tight_layout()
fig.savefig('QMRA')
