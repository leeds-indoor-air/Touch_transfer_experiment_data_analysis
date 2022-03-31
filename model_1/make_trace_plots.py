import pandas as pd
from matplotlib import pyplot as plt
import sys
from scipy.special import expit
import numpy as np

if len(sys.argv) != 4:
    print('<exec> path file chains')
    sys.exit()

_path = sys.argv[1]
_file = sys.argv[2]
_nc = int(sys.argv[3])

dat = pd.read_pickle(_path + _file)

chains = [ dat[i::_nc] for i in range(_nc) ]

beta_0_plot, ax = plt.subplots(5, 1, sharex=True)
for ch in chains:
    ax[0].plot(np.array(ch['beta_0.1']), alpha=0.33)
    ax[1].plot(np.array(ch['beta_0.2']), alpha=0.33)
    ax[2].plot(np.array(ch['beta_0.3']), alpha=0.33)
    ax[3].plot(np.array(ch['beta_0.4']), alpha=0.33)
    ax[4].plot(np.array(ch['beta_0.5']), alpha=0.33)
        
    
ax[0].set_title(r'$\beta_0.1$')
ax[1].set_title(r'$\beta_0.2$')
ax[2].set_title(r'$\beta_0.3$')
ax[3].set_title(r'$\beta_0.4$')
ax[4].set_title(r'$\beta_0.5$')

ax[4].set_xlabel('iteration')

beta_0_plot.set_size_inches(8, 9)
beta_0_plot.tight_layout()
beta_0_plot.savefig('model_1/trace_plots/' +  _file + '_beta_0_trace.png')

beta_1_plot, ax = plt.subplots(5, 1, sharex=True)
for ch in chains:
    ax[0].plot(np.array(ch['beta_1.1']), alpha=0.33)
    ax[1].plot(np.array(ch['beta_1.2']), alpha=0.33)
    ax[2].plot(np.array(ch['beta_1.3']), alpha=0.33)
    ax[3].plot(np.array(ch['beta_1.4']), alpha=0.33)
    ax[4].plot(np.array(ch['beta_1.5']), alpha=0.33)
        
    
ax[0].set_title(r'$\beta_1.1$')
ax[1].set_title(r'$\beta_1.2$')
ax[2].set_title(r'$\beta_1.3$')
ax[3].set_title(r'$\beta_1.4$')
ax[4].set_title(r'$\beta_1.5$')

ax[4].set_xlabel('iteration')

beta_1_plot.set_size_inches(8, 9)
beta_1_plot.tight_layout()
beta_1_plot.savefig('model_1/trace_plots/' +  _file + '_beta_1_trace.png')

log_phi_plot, ax = plt.subplots(5, 1, sharex=True)
for ch in chains:
    ax[0].plot(np.array(ch['log_phi.1']), alpha=0.33)
    ax[1].plot(np.array(ch['log_phi.2']), alpha=0.33)
    ax[2].plot(np.array(ch['log_phi.3']), alpha=0.33)
    ax[3].plot(np.array(ch['log_phi.4']), alpha=0.33)
    ax[4].plot(np.array(ch['log_phi.5']), alpha=0.33)

ax[0].set_title(r'$\log \phi.1$')
ax[1].set_title(r'$\log \phi.2$')
ax[2].set_title(r'$\log \phi.3$')
ax[3].set_title(r'$\log \phi.4$')
ax[4].set_title(r'$\log \phi.5$')

ax[4].set_xlabel('iteration')

log_phi_plot.set_size_inches(8, 9)
log_phi_plot.tight_layout()
log_phi_plot.savefig('model_1/trace_plots/' +  _file + '_log_phi_trace.png')


log_sigma_plot, ax = plt.subplots(1, 1, sharex=True)
for ch in chains:
    ax.plot(np.array(ch['log_sigma']), alpha=0.33)

ax.set_title(r'$\log \sigma$')
ax.set_xlabel('iteration')

log_sigma_plot.set_size_inches(8, 2)
log_sigma_plot.tight_layout()
log_sigma_plot.savefig('model_1/trace_plots/' +  _file + '_log_sigma_trace.png')

lp_plot, ax = plt.subplots(1, 1, sharex=True)
for ch in chains:
    ax.plot(np.array(ch['lp__']), alpha=0.33)

ax.set_title(r'lp__')
ax.set_xlabel('iteration')

lp_plot.set_size_inches(8, 2)
lp_plot.tight_layout()
lp_plot.savefig('model_1/trace_plots/' +  _file + '_lp__.png')

tau_plot, ax = plt.subplots(5, 2, sharex=True)
for ch in chains:
    ax[0, 0].plot(np.array(ch['tau.1']), alpha=0.33)
    ax[0, 1].plot(np.array(ch['tau.2']), alpha=0.33)

    ax[1, 0].plot(np.array(ch['tau.3']), alpha=0.33)
    ax[1, 1].plot(np.array(ch['tau.4']), alpha=0.33)

    ax[2, 0].plot(np.array(ch['tau.5']), alpha=0.33)
    ax[2, 1].plot(np.array(ch['tau.6']), alpha=0.33)

    ax[3, 0].plot(np.array(ch['tau.7']), alpha=0.33)
    ax[3, 1].plot(np.array(ch['tau.8']), alpha=0.33)

    ax[4, 0].plot(np.array(ch['tau.9']), alpha=0.33)
    ax[4, 1].plot(np.array(ch['tau.10']), alpha=0.33)


ax[0,0].set_title(r'$\tau_1$')
ax[0,1].set_title(r'$\tau_2$')
ax[1,0].set_title(r'$\tau_3$')
ax[1,1].set_title(r'$\tau_4$')
ax[2,0].set_title(r'$\tau_5$')
ax[2,1].set_title(r'$\tau_6$')
ax[3,0].set_title(r'$\tau_7$')
ax[3,1].set_title(r'$\tau_8$')
ax[4,0].set_title(r'$\tau_9$')
ax[4,1].set_title(r'$\tau_{10}$')

ax[4,0].set_xlabel('iteration')

tau_plot.set_size_inches(16, 8.5)
tau_plot.tight_layout()
tau_plot.savefig('model_1/trace_plots/' +  _file + '_tau_trace.png')


