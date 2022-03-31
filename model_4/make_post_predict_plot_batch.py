import numpy as np
import pickle
import sys
from scipy import stats
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap, ScalarMappable
import csv
import time
from scipy.special import expit
import read_data as dat

def set_fig(u):
    ax.append( fig.add_axes( [left, bottom + 4*height + 4*spacing, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left + width + spacing, bottom + 4*height + 4*spacing, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left, bottom + 3*height + 3*spacing, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left + width + spacing, bottom + 3*height + 3*spacing, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left, bottom + 2*height + 2*spacing, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left + width + spacing, bottom + 2*height + 2*spacing, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left, bottom + height + spacing, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left + width + spacing, bottom + height + spacing, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left, bottom, width, height] ) )
    u -= 1
    if u == 0:
        return
    ax.append( fig.add_axes( [left + width + spacing, bottom, width, height] ) )
    return

seed = int(time.time())
print('seed:', seed)
rD = np.random.default_rng(seed)

nchains=4
nsamples=18000
nthin=1
nwarmup=2000

filename = 'AH_model_4_DEFAULT_INIT_11_10_0.3_1.fit'
filepath = 'model_4/fits/pickle/'

fit = pickle.load( open(filepath + filename, 'rb') )


chain1 = fit[int(nwarmup*nchains/nthin) + 0::nchains]
chain2 = fit[int(nwarmup*nchains/nthin) + 1::nchains]
chain3 = fit[int(nwarmup*nchains/nthin) + 2::nchains]
chain4 = fit[int(nwarmup*nchains/nthin) + 3::nchains]

AH_bins = 300
Y_bins = 100

material = np.array(dat.mat, int) - 1
batch = np.array(dat.translated_batch, int) - 1

AH_bins = 300
Y_bins = 100

left, right, bottom = 0.075, 0.05, 0.05
spacing = 0.05

width = (1.0 - left - right - spacing)/2.0
height = (1.0 - 2*bottom - 4*spacing)/5.0

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!! REMEMBER!!! We're now building the batch_translate dict. in opposite direction !!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

bet1 = np.hstack( (chain1['beta_1'],
                   chain2['beta_1'],
                   chain3['beta_1'],
                   chain4['beta_1']))

for mat_, n, i, j, title in [('ABSS', 0, 0, 0, 'ABSS'),
                             ('ABST', 1, 0, 1, 'ABST'),
                             ('KYDEX', 2, 0, 2, 'Kydex'),
                             ('MEL', 3, 1, 0, 'Melamine'),
                             ('SS304', 4, 1, 1, 'Stainless steel 304')]:
    
    print(mat_, n, i, j)
    
    
    phi = np.exp(np.hstack( (chain1['log_phi.' + str(n+1)],
                             chain2['log_phi.' + str(n+1)],
                             chain3['log_phi.' + str(n+1)],
                             chain4['log_phi.' + str(n+1)])))

    M = np.hstack( (chain1['M.' + str(n+1)],
                    chain2['M.' + str(n+1)],
                    chain3['M.' + str(n+1)],
                    chain4['M.' + str(n+1)]))

    A_mean, A_scale = 0.186, 0.0224
    A = stats.norm.rvs(loc = A_mean, scale = A_scale, size=bet1.size)

    ind = np.nonzero(np.equal(material, n))[0]
    min_AH_ = np.amin(np.take(dat.AH_centred_material, ind))
    max_AH_ = np.amax(np.take(dat.AH_centred_material, ind))

    AH_ = np.linspace(min_AH_, max_AH_, AH_bins)
    
    Y_mat = np.take(dat.Y, ind)
    batch_mat = np.take(dat.translated_batch, ind)
    AH_mat = np.take(dat.AH_centred_material, ind)
    AH_mat_mean = dat.AH_means_material[n]
    
    u = np.unique(batch_mat).size
    ax = []
    fig = plt.figure(figsize = (11.7,16.5))
    set_fig(u)

    bid = 1
    batch_translate = {}
    for b in np.unique(batch_mat):
        batch_translate[bid] = b
        bid += 1

    for a in ax:
        #a.set_xlim(0.0, 1.0)
        a.set_ylim(0.0, 0.16)
        #a.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
        #a.set_xticklabels(['0.0', '20.0', '40.0', '60.0', '80.0', '100.0'])
        
    for a, (k, v) in zip(ax, batch_translate.items()):
        a.set_title( 'batch ' + str(v) )

    ax[0].set_xlabel(r'abs. humidity [g m$^{-3}$]')
    ax[0].set_ylabel(r'$\hat{Y}$',rotation = 0)

    for i, ba in enumerate(np.unique(batch_mat)):
        ind2 = np.nonzero( batch_mat == ba )[0]
        ax[i].scatter(np.take(AH_mat, ind2) + AH_mat_mean, np.take(Y_mat, ind2), marker='x', color = 'k')

    u = np.unique(batch_mat).size
    
    for k, x in enumerate(['.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9', '.10']):
        tau = np.hstack( (chain1['tau' + x], chain2['tau' + x], chain3['tau' + x], chain4['tau' + x]))
        ita1_hat = bet1[np.newaxis,::] * AH_[::,np.newaxis] + tau[np.newaxis,::]
        mu_hat = expit(ita1_hat) * M[np.newaxis,::]
        alp_hat = mu_hat * phi
        bet_hat = phi * (1 - mu_hat)
        
        T_hat = stats.beta.rvs(alp_hat, bet_hat, random_state = rD)
        Y_hat = (T_hat * A).T
        
        pcs = np.percentile(Y_hat, [2.5, 97.5], axis=0)
        ax[k].fill_between(AH_ + AH_mat_mean, pcs[0,::], pcs[1,::], alpha=0.1, color='blue')
        u -= 1
        if u==0:
            break


    fig.savefig('model_4/post_predict_plots/AH_model_4_post_predict_batch_' + mat_)
