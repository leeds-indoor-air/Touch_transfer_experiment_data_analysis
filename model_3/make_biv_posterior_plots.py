import numpy as np
import pickle5 as pickle
import sys
from scipy import stats
from matplotlib import pyplot as plt
from matplotlib.colors import BoundaryNorm
import read_data as data

if len(sys.argv) != 2:
    print('<exec> material')
    sys.exit()
    
mat = sys.argv[1]
mat_int = str(data.Material[mat])
mat_title = data.Material_titles[mat]
print(mat, mat_int, mat_title)

nchains=4
nsamples=18000
nthin=1
nwarmup=2000

path = 'model_3/fits/pickle/AH_model_3_DEFAULT_INIT_11_10_0.3_1.fit'
fit = pickle.load(open(path, 'rb'))[int(nwarmup*nchains/nthin)::]
    
bet0 = fit['beta_0']
bet1 = fit['beta_1']
M = fit['M.' + mat_int]
phi = np.exp(fit['log_phi.' + mat_int])
sigma = np.exp(fit['log_sigma'])

bet0_min, bet0_max = np.amin(bet0), np.amax(bet0)
bet1_min, bet1_max = np.amin(bet1), np.amax(bet1)
M_min, M_max = np.amin(M), np.amax(M)
phi_min, phi_max = np.amin(phi), np.amax(phi)
sigma_min, sigma_max = np.amin(sigma), np.amax(sigma)

bet0_bins = np.linspace(bet0_min, bet0_max, num=40, endpoint=False)
bet1_bins = np.linspace(bet1_min, bet1_max, num=40, endpoint=False)
M_bins = np.linspace(M_min, M_max, num=40, endpoint=False)
phi_bins = np.linspace(phi_min, phi_max, num=40, endpoint=False)
sigma_bins = np.linspace(sigma_min, sigma_max, num=40, endpoint=False)

cmap = plt.get_cmap('inferno')

fig = plt.figure(figsize = (16.5, 11.7))

left, bottom = 0.05, 0.05
spacing = 0.05

width = (1.0 - 2*left - 4*spacing)/5.0
height = (1.0 - 2*bottom - 4*spacing)/5.0

#1st row
ax00 = fig.add_axes( [left, bottom + 4*spacing + 4*height, width, height] )
ax01 = fig.add_axes( [left + width + spacing, bottom + 4*spacing + 4*height, width, height] )
ax02 = fig.add_axes( [left + 2*width + 2*spacing, bottom + 4*spacing + 4*height, width, height] )
ax03 = fig.add_axes( [left + 3*width + 3*spacing, bottom + 4*spacing + 4*height, width, height] )
ax04 = fig.add_axes( [left + 4*width + 4*spacing, bottom + 4*spacing + 4*height, width, height] )

#2nd row
ax11 = fig.add_axes( [left + width + spacing, bottom + 3*spacing + 3*height, width, height] )
ax12 = fig.add_axes( [left + 2*width + 2*spacing, bottom + 3*spacing + 3*height, width, height] )
ax13 = fig.add_axes( [left + 3*width + 3*spacing, bottom + 3*spacing + 3*height, width, height] )
ax14 = fig.add_axes( [left + 4*width + 4*spacing, bottom + 3*spacing + 3*height, width, height] )

#3rd row
ax22 = fig.add_axes( [left + 2*width + 2*spacing, bottom + 2*spacing + 2*height, width, height] )
ax23 = fig.add_axes( [left + 3*width + 3*spacing, bottom + 2*spacing + 2*height, width, height] )
ax24 = fig.add_axes( [left + 4*width + 4*spacing, bottom + 2*spacing + 2*height, width, height] )

#4th row
ax33 = fig.add_axes( [left + 3*width + 3*spacing, bottom + spacing + height, width, height] )
ax34 = fig.add_axes( [left + 4*width + 4*spacing, bottom + spacing + height, width, height] )

#5th row
ax44 = fig.add_axes( [left + 4*width + 4*spacing, bottom, width, height] )


ax00.hist(bet0, density=True, bins=40)
ax11.hist(bet1, density=True, bins=40)
ax22.hist(M, density=True, bins=40)
ax33.hist(phi, density=True, bins=40)
ax44.hist(sigma, density=True, bins=40)

ax00.set_xlim(bet0_min, bet0_max)
ax11.set_xlim(bet1_min, bet1_max)
ax22.set_xlim(M_min, M_max)
ax33.set_xlim(phi_min, phi_max)
ax44.set_xlim(sigma_min, sigma_max)


for pl, lab in zip( [ax00, ax11, ax22, ax33, ax44],
               [r'$\beta_0$', r'$\beta_1$', r'$M$', r'$\phi$', r'$\sigma$']):
    pl.set_ylabel('dens.')
    pl.set_xlabel(lab)

for pl, lab in zip( [ax01, ax02, ax03, ax04],
                    [r'$\beta_1$', r'$M$', r'$\phi$', r'$\sigma$']):
    pl.set_xlabel(r'$\beta_0$')
    pl.set_ylabel(lab)

for pl, lab in zip( [ax12, ax13, ax14],
                    [r'$M$', r'$\phi$', r'$\sigma$']):
    pl.set_xlabel(r'$\beta_1$')
    pl.set_ylabel(lab)

for pl, lab in zip( [ax23, ax24],
                    [r'$\phi$', r'$\sigma$']):
    pl.set_xlabel(r'$M$')
    pl.set_ylabel(lab)

ax34.set_xlabel(r'$\phi$')
ax34.set_ylabel(r'$\sigma$')


#1st row bet0 vs bet1
k = stats.gaussian_kde( np.vstack( (bet0, bet1) ) )
x1, y1 = np.mgrid[bet0_min:bet0_max:40j, bet1_min:bet1_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax01.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('bet0_bet1')

#1st row bet0 vs M
k = stats.gaussian_kde( np.vstack( (bet0, M) ) )
x1, y1 = np.mgrid[bet0_min:bet0_max:40j, M_min:M_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax02.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('bet0_M')

#1st row bet0 vs phi
k = stats.gaussian_kde( np.vstack( (bet0, phi) ) )
x1, y1 = np.mgrid[bet0_min:bet0_max:40j, phi_min:phi_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax03.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('bet0_phi')

#1st row bet0 vs sigma
k = stats.gaussian_kde( np.vstack( (bet0, sigma) ) )
x1, y1 = np.mgrid[bet0_min:bet0_max:40j, sigma_min:sigma_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax04.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('bet0_sigma')

#2nd row bet1 vs M
k = stats.gaussian_kde( np.vstack( (bet1, M) ) )
x1, y1 = np.mgrid[bet1_min:bet1_max:40j, M_min:M_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax12.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('bet1_M')

#2nd row bet1 vs phi
k = stats.gaussian_kde( np.vstack( (bet1, phi) ) )
x1, y1 = np.mgrid[bet1_min:bet1_max:40j, phi_min:phi_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax13.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('bet1_phi')

#2nd row bet1 vs sigma
k = stats.gaussian_kde( np.vstack( (bet1, sigma) ) )
x1, y1 = np.mgrid[bet1_min:bet1_max:40j, sigma_min:sigma_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax14.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('bet1_sigma')

#3rd row M vs phi
k = stats.gaussian_kde( np.vstack( (M, phi) ) )
x1, y1 = np.mgrid[M_min:M_max:40j, phi_min:phi_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax23.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('M_phi')

#3rd row M vs sigma
k = stats.gaussian_kde( np.vstack( (M, sigma) ) )
x1, y1 = np.mgrid[M_min:M_max:40j, sigma_min:sigma_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax24.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('M_sigma')

#4th row phi vs sigma
k = stats.gaussian_kde( np.vstack( (phi, sigma) ) )
x1, y1 = np.mgrid[phi_min:phi_max:40j, sigma_min:sigma_max:40j]
pos = np.vstack( (x1.ravel(), y1.ravel()) )
z1 = np.reshape( k(pos), x1.shape )
ax34.pcolormesh(x1, y1, z1, cmap=cmap, shading='gouraud')
print('phi_sigma')


fig.savefig('model_3/posterior_plots/biv_posterior_plot_' + sys.argv[1])


