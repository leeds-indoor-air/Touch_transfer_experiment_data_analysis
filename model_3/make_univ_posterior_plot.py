import numpy as np
import pickle5 as pickle
import sys
from scipy import stats
from matplotlib import pyplot as plt
from matplotlib.colors import BoundaryNorm
import read_data as data

nchains=4
nsamples=18000
nthin=1
nwarmup=2000

path = 'model_3/fits/pickle/AH_model_3_DEFAULT_INIT_11_10_0.3_1.fit'
fit = pickle.load(open(path, 'rb'))[int(nwarmup*nchains/nthin)::]
    
bet0_prime = fit['beta_0']
bet1 = fit['beta_1']
bet0 = bet0_prime - bet1 * data.AH_means

M_ABSS = fit['M.1']
M_ABST = fit['M.2']
M_KYD = fit['M.3']
M_MEL = fit['M.4']
M_SS304 = fit['M.5']

phi_ABSS = np.exp(fit['log_phi.1'])
phi_ABST = np.exp(fit['log_phi.2'])
phi_KYD = np.exp(fit['log_phi.3'])
phi_MEL = np.exp(fit['log_phi.4'])
phi_SS304 = np.exp(fit['log_phi.5'])

sigma = np.exp(fit['log_sigma'])

fig = plt.figure(figsize = (10.0, 7.0))

left, bottom = 0.075, 0.075
right, top = 0.025, 0.025
spacing = 0.075

top_width = (1.0 - left - right - 2*spacing)/3.0
bot_width = (1.0 - left - right - spacing)/2.0
height = (1.0 - bottom - top - 2*spacing)/2.0

##Add axes
#top row - 3 panels
other_plots = [ fig.add_axes( [left + i*top_width + i*spacing,
                           bottom + height + spacing,
                           top_width, height] ) for i in range(3)]

#middle row - 2 panels, double width
M_plot = fig.add_axes( [left,
                        bottom,
                        bot_width, height] )

#bottom row - 2 panels, double width
phi_plot = fig.add_axes( [left + bot_width + spacing,
                          bottom,
                          bot_width, height] )


#plot top row
for (j, param), xlab in zip( enumerate([bet0, bet1, sigma]), [r'$\beta_0$', r'$\beta_1$', r'$\sigma$']):
    param_min, param_max = np.amin(param), np.amax(param)
    #t = np.linspace(param_min, param_max, 1000)
    #z = stats.gaussian_kde(param)
    #other_plots[j].plot(t, z(t), 'k-')

    
    other_plots[j].hist(param, bins=40, density=True, color='blue')
    other_plots[j].set_xlabel(xlab)


other_plots[0].set_ylabel('Density')

M_plot.hist(M_ABSS, bins=40, density=True, alpha=0.5, color='red', label='ABSS')
M_plot.hist(M_ABST, bins=40, density=True, alpha=0.5, color='blue', label='ABST')
M_plot.hist(M_KYD, bins=40, density=True, alpha=0.5, color='green', label='Kydex')
M_plot.hist(M_MEL, bins=40, density=True, alpha=0.5, color='yellow', label='Melamine')
M_plot.hist(M_SS304, bins=40, density=True, alpha=0.5, color='black', label='SS304')
#M_plot.legend()

M_plot.set_xlabel(r'$M_{material}$')
M_plot.set_ylabel('Density')

phi_plot.hist(phi_ABSS, bins=40, density=True, alpha=0.5, color='red', label='ABSS')
phi_plot.hist(phi_ABST, bins=40, density=True, alpha=0.5, color='blue', label='ABST')
phi_plot.hist(phi_KYD, bins=40, density=True, alpha=0.5, color='green', label='Kydex')
phi_plot.hist(phi_MEL, bins=40, density=True, alpha=0.5, color='yellow', label='Melamine')
phi_plot.hist(phi_SS304, bins=40, density=True, alpha=0.5, color='black', label='SS304')
phi_plot.legend()

phi_plot.set_xlabel(r'$\phi_{material}$')
#phi_plot.set_ylabel('Density')
phi_plot.set_xlim( (0, 175) )

fig.tight_layout()
fig.savefig('model_3/posterior_plots/univ_posterior_plot_')
