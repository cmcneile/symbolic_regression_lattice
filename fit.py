#!/usr/bin/env python

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import os
import yaml

import time



from pysr import PySRRegressor
import sympy
from sympy import Symbol 
import os

#-------------
import model_list


if len(sys.argv) != 2:
   print("ERRor useage " , sys.argv[0] , "input file")
   sys.exit(0)
else:
    yaml_f = sys.argv[1]

with open(yaml_f) as f:
    
    data = yaml.safe_load(f)
    print(data)


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

print("x_val = " , x_val)
print("y_val = " , y_val)    
print('corr_mean = ' , corr_mean)
print('corr_err = ' , corr_err)

sn = np.max(corr_err/corr_mean)
nomeas=data["nomeas"]
print(f"Signal to noise = {sn:.2e} meas={nomeas}")


#sys.exit(0)

y = corr_mean
x = x_val

plt.errorbar(x,y,corr_err, fmt= "ro")

plt.xlabel(r"$G_A(Q^2)$")
plt.ylabel(r"$Q^2$ GeV$^2$")

#plt.xlabel(r"x")
#plt.ylabel(r"y")


if 0 :
  plt.show()
  sys.exit(0)


print("Starting symbolic regression")


xp = x
yp = y

D = len(x)
x = x.reshape(D,1)

start = time.time()


#model = model_list.model_A()
#model = model_list.model_C()
#model = model_list.model_D()
#model = model_list.model_E()
#model = model_list.model()

model = model_list.model_G()

model.fit(x, y)


# weight  https://ai.damtp.cam.ac.uk/pysr/examples/
#model = model_list.model_F()

sigma = 1/corr_err**2
#sigma = sigma.reshape(D,1)

#model.fit(x, y, weights=sigma)

##

print(model)


x0=Symbol('x0')

ans = model.sympy()

print(ans)


##
##  plot the fit
##

xx = np.linspace(xp[0], xp[-1], num=100 )
yy = [  ans.subs(x0, xx_) for xx_ in xx  ]

#print(xx)
#print(yy)


plt.plot(xx,yy, "k", label="symbolic regression fit")

#plt.errorbar(x,y,corr_err, fmt= "ro" , label="simulation")
plt.errorbar(x,y,corr_err, fmt= "ro" , label="lattice data")

plt.title("Model function versus fit")

plt.legend()
#plt.xlabel(r"x")
#plt.ylabel(r"y")
plt.ylabel(r"$G_A(Q^2)$")
plt.xlabel(r"$Q^2$ GeV$^2$")



plt.savefig("symbolic_plot.png")
plt.show()

###
###  ----------------------------------------
###

def compute_res(ans_,xp_, yp_) :

  yy_test = [  ans_.subs(x0, xx_) for xx_ in xp_  ]
  dim = len(yy_test)

  rse = 0.0
  for i in range(0,dim) :
      rse += (yp_[i] - yy_test[i] )**2

  rse /= dim
#  rse = math.sqrt(rse)
  
  print("rse = " , rse)


def compute_chisq(ans_,xp_, yp_, yp_err_) :

  yy_test = [  ans_.subs(x0, xx_) for xx_ in xp_  ]
  dim = len(yy_test)

  rse = 0.0
  for i in range(0,dim) :
      rse += (yp_[i] - yy_test[i] )**2 / yp_err_[i]**2

  rse /= dim
#  rse = math.sqrt(rse)
  
  print("chi**2 = " , rse)



##
##  -------------
##


#print(model_list.model().__doc__)


print(model.latex() )

print("Known model function " , data["func"])
print(f"Signal to noise = {sn:.2e} meas={nomeas}")

if 0 :
  compute_res(ans,xp, yp) 
  compute_chisq(ans,xp, yp, corr_err)


tend = time.time() - start
print(f"Time taken {tend:.3f} s")

