import pandas as pd
from matplotlib import pyplot as plt
import sys
from scipy.special import expit

if len(sys.argv) != 4:
    print('<exec> path file chains')
    sys.exit()

_path = sys.argv[1]
_file = sys.argv[2]
_nc = int(sys.argv[3])

dat = pd.read_pickle(_path + _file)

chains = [ dat[i::_nc] for i in range(_nc) ]

beta_plot, ax = plt.subplots(2, 1, sharex=True)
for ch in chains:
    ax[0].plot(ch['beta_0'], alpha=0.33)
    ax[1].plot(ch['beta_1'], alpha=0.33)
    
ax[0].set_title(r'$\beta_0$')
ax[1].set_title(r'$\beta_1$')

ax[1].set_xlabel('iteration')

beta_plot.set_size_inches(8, 9)
beta_plot.tight_layout()
beta_plot.savefig('model_3/trace_plots/' + _file + '_beta_trace.png')

M_plot, ax = plt.subplots(5, 1, sharex=True)
for ch in chains:
    ax[0].plot(ch['M.1'], alpha=0.33)
    ax[1].plot(ch['M.2'], alpha=0.33)
    ax[2].plot(ch['M.3'], alpha=0.33)
    ax[3].plot(ch['M.4'], alpha=0.33)
    ax[4].plot(ch['M.5'], alpha=0.33)
        
    
ax[0].set_title(r'$M.1$')
ax[1].set_title(r'$M.2$')
ax[2].set_title(r'$M.3$')
ax[3].set_title(r'$M.4$')
ax[4].set_title(r'$M.5$')

ax[4].set_xlabel('iteration')

M_plot.set_size_inches(8, 9)
M_plot.tight_layout()
M_plot.savefig('model_3/trace_plots/' + _file + '_M_trace.png')

log_phi_plot, ax = plt.subplots(5, 1, sharex=True)
for ch in chains:
    ax[0].plot(ch['log_phi.1'], alpha=0.33)
    ax[1].plot(ch['log_phi.2'], alpha=0.33)
    ax[2].plot(ch['log_phi.3'], alpha=0.33)
    ax[3].plot(ch['log_phi.4'], alpha=0.33)
    ax[4].plot(ch['log_phi.5'], alpha=0.33)

ax[0].set_title(r'$\log \phi.1$')
ax[1].set_title(r'$\log \phi.2$')
ax[2].set_title(r'$\log \phi.3$')
ax[3].set_title(r'$\log \phi.4$')
ax[4].set_title(r'$\log \phi.5$')

ax[4].set_xlabel('iteration')

log_phi_plot.set_size_inches(8, 9)
log_phi_plot.tight_layout()
log_phi_plot.savefig('model_3/trace_plots/' + _file + '_log_phi_trace.png')


log_sigma_plot, ax = plt.subplots(1, 1, sharex=True)
for ch in chains:
    ax.plot(ch['log_sigma'], alpha=0.33)

ax.set_title(r'$\log \sigma$')
ax.set_xlabel('iteration')

log_sigma_plot.set_size_inches(8, 2)
log_sigma_plot.tight_layout()
log_sigma_plot.savefig('model_3/trace_plots/' + _file + '_log_sigma_trace.png')

lp_plot, ax = plt.subplots(1, 1, sharex=True)
for ch in chains:
    ax.plot(ch['lp__'], alpha=0.33)

ax.set_title(r'lp__')
ax.set_xlabel('iteration')

lp_plot.set_size_inches(8, 2)
lp_plot.tight_layout()
lp_plot.savefig('model_3/trace_plots/' + _file + '_lp__.png')

tau_plot, ax = plt.subplots(5, 2, sharex=True)
for ch in chains:
    ax[0, 0].plot(ch['tau.1'], alpha=0.33)
    ax[0, 1].plot(ch['tau.2'], alpha=0.33)

    ax[1, 0].plot(ch['tau.3'], alpha=0.33)
    ax[1, 1].plot(ch['tau.4'], alpha=0.33)

    ax[2, 0].plot(ch['tau.5'], alpha=0.33)
    ax[2, 1].plot(ch['tau.6'], alpha=0.33)

    ax[3, 0].plot(ch['tau.7'], alpha=0.33)
    ax[3, 1].plot(ch['tau.8'], alpha=0.33)

    ax[4, 0].plot(ch['tau.9'], alpha=0.33)
    ax[4, 1].plot(ch['tau.10'], alpha=0.33)


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
tau_plot.savefig('model_3/trace_plots/' + _file + '_tau_trace.png')


