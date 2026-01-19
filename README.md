# Symbolic regression lattice examples

Generate some functions with noise and then use symbolic
regression to try to reproduce the original function.

The symbolic regression library used is
https://github.com/MilesCranmer/PySR
There are installation instructions

The current functions come from the paper

Does Bayesian model averaging improve polynomial extrapolations? Two toy problems as tests
M.A. Connell   , I. Billig    , D.R. Phillips
J.Phys.G 48 (2021) 10, 104001
2106.05906 [stat.ME]

The simulation is generated in the **sim_data** directory.

The file simulate.py generates the simulated data.


The external data sets are stored in the directory **data**

To run the form factor data through the symbolic regression code
use.

python fit.py data/ga_etmc.yaml

This uses data from the paper for the axial form factor
of the nucleon from:

arXiv:2309.05774
Nucleon axial and pseudoscalar form factors using
twisted-mass fermion ensembles at the physical point

Data from TABLE XII