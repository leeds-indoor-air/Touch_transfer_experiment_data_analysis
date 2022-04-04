# PROTECT-NCS WP2.2.4
Python3 code repository to accompany **WP2.2.4: Modelling environmental transmission via touch surfaces**, submitted 31 March 2022 as final report to HSE by University of Leeds for Theme 2 of the **National Core Study PROTECT** project.

## Usage
```
mkdir -p /path/to/Touch_transfer_experiment_data_analysis/
cd /path/to/Touch_transfer_experiment_data_analysis/
git clone git@github.com:leeds-indoor-air/Touch_transfer_experiment_data_analysis.git
```

You should append `/path/to/Touch_transfer_experiment_data_analysis/misc/` to your `PYTHONPATH` environment variable, so that scripts can `import read_data`.

## Directory contents

### `data/`

Contains:

single touch transfer experiment data for ABSS, ABST, kydex, melamine and stainless steel 304

contact area measurements for 1N and 15N

### `misc/`

Contains:

`read_data.py`

`calculate_bayesian_p_vals.py` for Bayesian p-values (Table A1).

`morris.py` generates plot in Figure 3.

### `model_n/`

`AH_model_n_DEFAULT_INIT.py` and `AH_model_n_DEFAULT_INIT_NO_BATCH_EFFECT.py` call Stan to sample from the posterior density for model `n`, with and without a random effect for the finger batch, for each of the four models described in Appendix A of the report.

Bayesian p-values were used to compare the fitted models, however these scripts were also intended to estimate the model evidence using the stepping stone method **(Xie, W., Lewis, P., Fan, Y. (2010).  Improving Marginal Likelihood Estimation for Bayesian Phylogenetic Model Selection. _Systematic Biology_)**.

Usage:

`python AH_model_n_DEFAULT_INIT.py k K alpha chain_no log_file` or

`python AH_model_n_DEFAULT_INIT_NO_BATCH_EFFECT.py k K alpha chain_no log_file`

to sample from 

<img src="https://render.githubusercontent.com/render/math?math=p(\theta \,|\, \mathbf{y}, \beta_{k}) = p(\mathbf{y}\,|\,\theta)^{\beta_{k}}p(\theta) ">, where <img src="https://render.githubusercontent.com/render/math?math=\beta_{k} = \left(\frac{k-1}{K}\right)^{\frac{1}{\alpha}}">.

**To sample from posterior, run with** <img src="https://render.githubusercontent.com/render/math?math=\beta_k = 1">, i.e., <img src="https://render.githubusercontent.com/render/math?math=K"> and <img src="https://render.githubusercontent.com/render/math?math=\alpha"> arbitrary, and k = K + 1. `chain_no` is an additional identifier appended to the output filen name and `log_file` is the path to a log file.

Within the scripts,

```
num_chains=4
num_samples=1000
num_thin=1
num_warmup=2000
```
should be set to desired number of independent MCMC chains, number of samples per chain, thinning interval and length of burn-in / adaptation phase.

Also contains scripts to generate trace and posterior predictive plots (e.g., Figure 2, report) - plots can be found in `model_n/trace_plots` and `model_n/post_predict_plots`.

Additionally, `model_3/` contains `make_univ_posterior_plot.py` and `make_biv_posterior_plots.py` to generate posterior summary plots (e.g., Figure 1, report) for chosen model 3.  These plots are found in `model_3/posterior_plots`.  Posterior summary statistics (Table A2) are calculated using the script `calculate_posterior_summary_stats.py`


## Environment set up

Using anaconda,

`conda create -n stan python=3.7; conda activate stan`

`python3 -m pip install pystan`

`conda install scipy pandas matplotlib statsmodels`

`python3 -m pip install pickle5`
