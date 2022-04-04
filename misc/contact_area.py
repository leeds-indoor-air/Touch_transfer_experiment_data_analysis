import csv
import statsmodels.api as sm
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

data1 = []
data15 = []

fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)
fig.set_size_inches(4.5, 4.5)

with open('data/contact_15N.csv', 'r') as csvfile:
    f = csv.reader(csvfile, delimiter='\t')
    for line in f:
        data15.append(float(line[0]))


data15_normed = (data15 - np.average(data15))/np.std(data15, ddof=1)

pplot15 = sm.ProbPlot(data15_normed, norm)
pplot15.qqplot(ax=ax)

x = np.linspace(-1.5, 1.5, 1000)
ax.plot(x, x, 'r-')

fig.tight_layout()
fig.savefig('contact_area_QQ')




