import csv
import sys
import numpy as np
import stan
import pickle
import math
import json
import read_data as dat

if len(sys.argv) != 6:
    print('<exec> k K alpha chain_no log_file')
    sys.exit()

k = int(sys.argv[1])
K = int(sys.argv[2])
alpha = float(sys.argv[3])
chain_no = str(sys.argv[4])
log_file = str(sys.argv[5])

bkm1 = math.pow( (k-1)/K, 1.0/alpha )

ss = str(k) + '_' + str(K) + '_' + str(alpha) + '_' + str(chain_no)

with open(log_file, 'a') as logf:
    logf.write('\n================================================\n')
    logf.write(ss)

    
code="""
data {
    int N;                               // number of obs
    int K;                               // number of groups
    int L;                               // number of materials
    vector<lower=0, upper=1>[N] Y;       // F / (F + C)
    vector[N] AH;
    array[N] int<lower=1,upper=K> batch;
    array[N] int<lower=1,upper=L> material;
    real<lower=0.0, upper=1.0> bkm1;
}
parameters {
    vector<lower=0, upper=1>[L] M;
    real beta_0;
    real beta_1;
    vector[L] log_phi;
    real log_sigma;
    vector<multiplier=10>[K] tau;
    vector<lower=0, upper=1>[N] T;
}
transformed parameters {
    vector[N] mu;

    {
        real ita;

        for(n in 1:N){
                ita = beta_0 + beta_1 * AH[n] + tau[batch[n]];
                mu[n] = inv_logit(ita)  * M[material[n]];
        }
    }
     
}
model {

    target += normal_lpdf( beta_0 | 0.0, 1e2 );
    target += normal_lpdf( beta_1 | 0.0, 1e2 );

    for(l in 1:L){
            target += exponential_lpdf( exp(log_phi[l]) | 1e-2 ) + log_phi[l];
    }
    
    target += exponential_lpdf( exp(log_sigma) | 1e-2 ) + log_sigma;

    for(k in 1:K){
            target += normal_lpdf( tau[k] | 0.0, exp(log_sigma) );
    }

    for(n in 1:N){
            target += beta_proportion_lpdf( T[n] | mu[n], exp(log_phi[material[n]]) );
    }

    real tmp = 0;
    
    for(n in 1:N){
            tmp += normal_lpdf( Y[n] | 0.1865*T[n], 0.0224*T[n] );
            }

    target += (tmp * bkm1);
}
"""

data = {"N": dat.N,
        "K": dat.K,
        "Y": dat.Y,
        "L": 5,
        "AH": dat.AH_centred,
        "batch": dat.translated_batch,
        "material": dat.mat,
        "bkm1": bkm1
        }


num_chains=4
num_samples=1000
num_thin=1
num_warmup=2000

with open(log_file, 'a') as logf:
    logf.write(code)
    logf.write('chains: %s\nsamples: %s\nthin: %s\nwarmup: %s\n' %(num_chains, num_samples, num_thin, num_warmup))
    logf.write('================================================\n')


posterior = stan.build(code, data)

    

fit = posterior.sample(num_chains=num_chains,
                       num_samples=num_samples,
                       num_thin=num_thin,
                       num_warmup=num_warmup,
                       save_warmup=1
                       ).to_frame()

fit.to_pickle('AH_model_3_DEFAULT_INIT_' + ss +  '.fit')


