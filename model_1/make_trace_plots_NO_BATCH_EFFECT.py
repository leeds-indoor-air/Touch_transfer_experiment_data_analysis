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
beta_0_plot.savefig('model_1/trace_plots/' +  _file + '_NO_BATCH_EFFECT_beta_0_trace.png')

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
beta_1_plot.savefig('model_1/trace_plots/' +  _file + '_NO_BATCH_EFFECT_beta_1_trace.png')

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
log_phi_plot.savefig('model_1/trace_plots/' +  _file + '_NO_BATCH_EFFECT_log_phi_trace.png')


lp_plot, ax = plt.subplots(1, 1, sharex=True)
for ch in chains:
    ax.plot(np.array(ch['lp__']), alpha=0.33)

ax.set_title(r'lp__')
ax.set_xlabel('iteration')

lp_plot.set_size_inches(8, 2)
lp_plot.tight_layout()
lp_plot.savefig('model_1/trace_plots/' +  _file + '_NO_BATCH_EFFECT_lp__.png')


