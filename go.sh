#!/bin/bash

./clean.sh

#./fit.py ./sim_data/g1_model.yaml
#./fit.py ./sim_data/g3_model.yaml

#./fit.py ../formfactor/etmc/ga_etmc.yaml

./fit.py data/ga_etmc.yaml

echo "Job run at "
date
