#!/usr/bin/env python
#
#
#
#Does Bayesian model averaging improve polynomial extrapolations? Two toy problems as tests
#    M.A. Connell   , I. Billig    , D.R. Phillips
#        J.Phys.G 48 (2021) 10, 104001
#
#        2106.05906 [stat.ME]


import numpy as  np
import math
import sys

import yaml

## model functions
from util_func import g1 
from util_func import g2
from util_func import g3

# simulation parameters
nsimp = 10000
mu = 0 
sigma = 0.2

model_pt = 2

#####


#---------------------------------

if model_pt == 0 :
  g = g2
  g_string = r"g(x) = $(1.3 / (x + 1.3) )^2 $  "
  out_name = "g2_model"
elif model_pt == 1 :
  g = g1
  g_string = r"g(x) = (1/2 + $\tan(\pi x/2))^2$  "
  out_name = "g1_model"
elif model_pt == 2 :
  g = g3
  g_string = r"g(x) = $0.3 +  0.5 x + 0.8 x^2$  "
  out_name = "g3_model"
else:
   print("function selection out of range")
   sys.exit(0)
  
###

##
##  create simulated data
##


x_val = np.arange(0.2,0.3,0.01)
y_val = [ g(x_) for x_ in x_val ] 

print("x=  " , x_val) 
print("y=  " , y_val) 


ndim = len(x_val)

corr = np.zeros((ndim, nsimp))
corrR = np.zeros((nsimp,ndim))

for i in range(0,nsimp) :
   s = y_val + np.random.normal(mu, sigma, ndim)
#   s = y_val
   corr[:,i] = s[:]
   corrR[i,:] = s[:]

#
#  average over MC samples
#

corr_mean = np.zeros(ndim)
corr_err   = np.zeros(ndim)



for i in range(0, ndim) :
  corr_mean[i] = np.mean(corr[i,:] )
  corr_err[i]  = np.std(corr[i,:] ) / math.sqrt(nsimp) 


#
#  save the data
#
nout = "np_" + out_name   +"_store.npy"
print("Saving simulation data to ", nout)
with open(nout, 'wb') as f:
    np.save(f, x_val)
    np.save(f, y_val)
    np.save(f, corr_mean)
    np.save(f, corr_err)
    np.save(f, corrR)

## metadata
info = dict()

info["filename"] = nout
info["func"] = g.__doc__
info["nomeas"] = nsimp
info["sigma"] = sigma
info["model_pt"] = model_pt



print("DEBUG ", info)

yaml_out = out_name  + ".yaml"

# Writing the data to a YAML file
with open(yaml_out, 'w') as file:
    yaml.dump(info, file)

print("Metadata has been written to ", yaml_out)

