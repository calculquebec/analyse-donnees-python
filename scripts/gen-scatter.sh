#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --mem-per-cpu=1500M
#SBATCH --time=0:10:00

source dat201/bin/activate
python gen-scatter.py
