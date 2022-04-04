import pickle5 as pickle
import numpy as np
import read_data as dat

nchains=4
nsamples=18000
nthin=1
nwarmup=2000

path = 'model_3/fits/pickle/AH_model_3_DEFAULT_INIT_11_10_0.3_1.fit'
fit = pickle.load(open(path, 'rb'))[int(nwarmup*nchains/nthin)::]

f = open('model_3/summary_stats.out', 'w')


M_cols =  [col for col in fit.columns if col.startswith('M.')]
log_phi_cols = [col for col in fit.columns if col.startswith('log_phi.')]

bet0_prime = fit['beta_0']
bet1 = fit['beta_1']
bet0 = bet0_prime - bet1 * dat.AH_means

s = bet0
avg = np.average(s)
stdev = np.std(s, ddof=1)
pc = np.percentile(s, [2.5, 50, 97.5])

print('bet0', avg, stdev, pc)
f.write( '%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t\n' %('bet0', avg, stdev, pc[0], pc[1], pc[2]) )

s = bet1
avg = np.average(s)
stdev = np.std(s, ddof=1)
pc = np.percentile(s, [2.5, 50, 97.5])

print('bet1', avg, stdev, pc)
f.write( '%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t\n' %('bet1', avg, stdev, pc[0], pc[1], pc[2]) )


for col in M_cols:
    s = fit[col]
    avg = np.average(s)
    stdev = np.std(s, ddof=1)
    pc = np.percentile(s, [2.5, 50, 97.5])

    print(col, avg, stdev, pc)
    f.write( '%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t\n' %(col, avg, stdev, pc[0], pc[1], pc[2]) )
    
for col in log_phi_cols:
    s = np.exp(fit[col])
    n = col.split('.')[1]
    avg = np.average(s)
    stdev = np.std(s, ddof=1)
    pc = np.percentile(s, [2.5, 50, 97.5])

    print(col, avg, stdev, pc)
    f.write( 'phi.%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t\n' %(n, avg, stdev, pc[0], pc[1], pc[2]) )

col = 'log_sigma'
s = np.exp(fit[col])
avg = np.average(s)
stdev = np.std(s, ddof=1)
pc = np.percentile(s, [2.5, 50, 97.5])

print(col, avg, stdev, pc)
f.write( '%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t\n' %(col, avg, stdev, pc[0], pc[1], pc[2]) )



