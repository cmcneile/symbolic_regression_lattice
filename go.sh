#!/bin/bash

./clean.sh

./fit.py ./data/g1_model.yaml
#./fit.py ./data/g3_model.yaml

echo "Job run at "
date
