#!/bin/sh

#SBATCH -n 4 # Number of cores requested
#SBATCH -t 600 # Runtime in minutes (0~10080)
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH -p short
#SBATCH --mem=5G # Memory in GB (see also --mem-per-cpu)
#SBATCH -o ace_%j.out # Standard out goes to this file
#SBATCH -e ace_%j.err         # Standard err goes to this file
#SBATCH --mail-type=END        # Email
#SBATCH --mail-user=omwaring@mit.edu

# LOAD_MODULES
module load gcc/6.2.0
module load python/3.6.0

python3 generateMSA.py
../ACE/bin/ace -i ace -o ace-out -b 10000
