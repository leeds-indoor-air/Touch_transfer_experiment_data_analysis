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

beta_plot, ax = plt.subplots(1, 1, sharex=True)
for ch in chains:
    ax.plot(np.array(ch['beta_1']), alpha=0.33)

    
ax.set_title(r'$\beta_1$')
ax.set_xlabel('iteration')

beta_plot.set_size_inches(8, 9)
beta_plot.tight_layout()
beta_plot.savefig('model_4/trace_plots/' + _file + '_NO_BATCH_EFFECT_beta_trace.png')

M_plot, ax = plt.subplots(5, 1, sharex=True)
for ch in chains:
    ax[0].plot(np.array(ch['M.1']), alpha=0.33)
    ax[1].plot(np.array(ch['M.2']), alpha=0.33)
    ax[2].plot(np.array(ch['M.3']), alpha=0.33)
    ax[3].plot(np.array(ch['M.4']), alpha=0.33)
    ax[4].plot(np.array(ch['M.5']), alpha=0.33)
        
    
ax[0].set_title(r'$M.1$')
ax[1].set_title(r'$M.2$')
ax[2].set_title(r'$M.3$')
ax[3].set_title(r'$M.4$')
ax[4].set_title(r'$M.5$')

ax[4].set_xlabel('iteration')

M_plot.set_size_inches(8, 9)
M_plot.tight_layout()
M_plot.savefig('model_4/trace_plots/'  + _file + '_NO_BATCH_EFFECT_M_trace.png')

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
log_phi_plot.savefig('model_4/trace_plots/'  + _file + '_NO_BATCH_EFFECT_log_phi_trace.png')

lp_plot, ax = plt.subplots(1, 1, sharex=True)
for ch in chains:
    ax.plot(np.array(ch['lp__']), alpha=0.33)

ax.set_title(r'lp__')
ax.set_xlabel('iteration')

lp_plot.set_size_inches(8, 2)
lp_plot.tight_layout()
lp_plot.savefig('model_4/trace_plots/' + _file + '_NO_BATCH_EFFECT_lp__.png')



