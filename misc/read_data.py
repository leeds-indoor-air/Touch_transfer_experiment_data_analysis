import csv
import numpy as np
import pickle
from scipy.stats import norm, beta, expon
import math

'''
F_corr = []
C_corr = []
batch = []
RH = []
temp = []
mat = []
'''

Material = {'ABSS':1
            ,'ABST':2
            ,'KYDEX': 3
            ,'MEL':4
            ,'SS304':5}

Material_titles = {'ABSS': 'ABSS',
                   'ABST': 'ABST',
                   'KYDEX': 'kydex',
                   'MEL': 'melamine',
                   'SS304': 'stainless steel 304'}

def convert_AH(RH, temp):
    return (6.112 * np.exp((17.67 * temp)/(temp + 243.5)) * RH * 2.1674)/(273.15 + temp)

def read_in(dat_path):

    F_corr = []
    C_corr = []
    batch = []
    RH = []
    temp = []


    first_line = True
    with open(dat_path) as csvfile:
        f = csv.reader(csvfile, delimiter='\t')
        for line in f:
            if first_line:
                first_line = False
                continue
            if( line[8] == '1' ):
                continue
            batch.append( int(line[0]) )
            F_corr.append( float(line[3]) )
            C_corr.append( float(line[5]) )
            RH.append( 100 * float(line[6]) )
            temp.append( float(line[7]) )

    Y = np.divide(F_corr, np.add(F_corr, C_corr))
    N = Y.size

    AH = convert_AH(np.array(RH), np.array(temp))
    AH_mean = np.average(AH)
    AH_centred = AH - AH_mean

    return Y, N, AH, AH_mean, AH_centred, RH, temp, batch

def translate_batch(batch):

    bid = 1
    batch_translate = {}

    for b in np.unique(batch):
        batch_translate[b] = bid
        bid += 1

    translated_batch = [ batch_translate[b] for b in batch ]
    K = len(batch_translate)
    
    return batch_translate, translated_batch, K



ABSS_dat = read_in( '/home/cenlb/Projects/touch_tx/data/ABSS_June2021.csv')
ABST_dat = read_in( '/home/cenlb/Projects/touch_tx/data/ABST_June2021.csv')
KYDEX_dat = read_in( '/home/cenlb/Projects/touch_tx/data/KYDEX_June2021.csv')
MEL_dat = read_in( '/home/cenlb/Projects/touch_tx/data/MEL_June2021.csv')
SS304_dat = read_in( '/home/cenlb/Projects/touch_tx/data/SS304_June2021.csv')

mat = np.repeat( [Material['ABSS'], Material['ABST'], Material['KYDEX'], Material['MEL'], Material['SS304']],
                 [ABSS_dat[0].size,  ABST_dat[0].size, KYDEX_dat[0].size, MEL_dat[0].size, SS304_dat[0].size] )


untranslated_batch = ABSS_dat[7]
untranslated_batch.extend(ABST_dat[7])
untranslated_batch.extend(KYDEX_dat[7])
untranslated_batch.extend(MEL_dat[7])
untranslated_batch.extend(SS304_dat[7])

_, translated_batch, K = translate_batch( untranslated_batch )

AH = np.hstack( (ABSS_dat[2], ABST_dat[2], KYDEX_dat[2], MEL_dat[2], SS304_dat[2]) )
AH_means = np.average(AH)
AH_means_material = [ABSS_dat[3], ABST_dat[3], KYDEX_dat[3], MEL_dat[3], SS304_dat[3]]
AH_centred = AH - AH_means
AH_centred_material = np.hstack(
    (ABSS_dat[4], ABST_dat[4], KYDEX_dat[4], MEL_dat[4], SS304_dat[4])
)



Y =  np.hstack( (ABSS_dat[0], ABST_dat[0], KYDEX_dat[0], MEL_dat[0], SS304_dat[0]) )
N = Y.size
'''
print(mat)
print(untranslated_batch)
print(translated_batch)
print(AH)
print(Y)
'''

