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
import matplotlib.pyplot as plt
import math
import gvar as gv
import lsqfit as lsq
import sys
import os

import yaml

## model functions
from util_func import g1 
from util_func import g2
from util_func import g3

## simulation extrapolation
from  util_extrap_func import  extrap3
from  util_extrap_func import  extrap3_rat
from  util_extrap_func import  extrap5


#model_pt = 0 
extrap_pt = 1

if len(sys.argv) != 2:
   print("ERRor useage " , sys.argv[0] , "input file")
   sys.exit(0)
else:
    yaml_f = sys.argv[1]

with open(yaml_f) as f:    
    data = yaml.safe_load(f)
    print(data)

model_pt = data["model_pt"]

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

##############################


ddd = os.path.dirname(yaml_f)

nout = ddd + "/" + data["filename"]


#----------------------
    
print("Reading simulation data from ", nout)
#sys.exit(0)

if not os.path.exists(nout):
    print(f"The file '{nout}' does not exist.")
    # Handle the case where the file doesn't exist
    sys.exit(0)
    
with open(nout, 'rb') as f:
    x_val     = np.load(f)
    y_val     = np.load(f)
    corr_mean = np.load(f)
    corr_err  = np.load(f)

ndim = len(x_val)
    
print("x_val = " , x_val)
print("y_val = " , y_val)    
print('corr_mean = ' , corr_mean)
print('corr_err = ' , corr_err)

sn = np.max(corr_err/corr_mean)
nomeas=data["nomeas"]
print(f"Signal to noise = {sn:.2e} meas={nomeas}")



###############################
plt.errorbar(x_val, corr_mean, corr_err, fmt = "go" , label="Simulation " + g_string )
plt.legend()


print("Start of GPL analysis")

gpl_data = [] 
for i in range(0, ndim) :
  gpl_data.append( gv.gvar(corr_mean[i], corr_err[i]  ))

print("gpl = ", gpl_data)




prior = {}
prior['a'] = [gv.gvar('0.0(2.0)'),gv.gvar(0,2),gv.gvar(0,2),gv.gvar(0,2),gv.gvar(0,2) ]
p0 = np.array([ 0.5, 1, 0 , 0 , 0])

if extrap_pt == 1 :
  extrap = extrap3_rat
  extrap_title = r"$(p_0  + p_1 x)/( 1 + p_2 x^2) $"
elif extrap_pt == 2 :
  extrap = extrap3
  extrap_title = r"$p_0  + p_1 x + p_2 x^2$"
elif extrap_pt == 3 :
  extrap = extrap5
  extrap_title = r"$p_0  + p_1 * x + p_2 x^2 + p_3 *x^3 + p_4 x^4$"
else:
  print("No extrapolation")    
  sys.exit(0)

  
#
##---------------------------------------------------


fit_A = lsq.nonlinear_fit(data=(x_val,gpl_data),prior=prior,fcn=extrap, p0=p0)

#----------------------------------------------------

print(g.__doc__)
print(extrap.__doc__)
print(fit_A)


fitline_A = extrap(x_val ,fit_A.p)

plt.plot(x_val,[ x.mean for x in fitline_A], "--ko" , label="fit f(x)= " + extrap_title)

plt.legend()
plt.xlabel("x")
plt.ylabel(r"y")

plt.savefig(out_name + ".png")
plt.show()
