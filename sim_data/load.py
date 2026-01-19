#!/usr/bin/env python


import numpy as  np
import matplotlib.pyplot as plt
import math
import gvar as gv
import lsqfit as lsq
import sys
import os.path

if len(sys.argv) != 2:
   print("ERRor useage " , sys.argv[0] , "input file")
   sys.exit(0)
else:
    nout = sys.argv[1]

    
   
#nout = "np_sim_store.npy"
print("Reading simulation data from ", nout)

if not os.path.exists(nout):
    print(f"The file '{nout}' does not exist.")
    # Handle the case where the file doesn't exist
    sys.exit(0)
    
with open(nout, 'rb') as f:
    corr_mean = np.load(f)
    corr_err  = np.load(f)

print('corr_mean = ' , corr_mean)

