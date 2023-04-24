#!/bin/bash
#SBATCH --job-name=6.7_bl1_s4    # Job name
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --output=Fix_6.7_bl1_s4.log   # Standard output and error log
pwd; hostname; date

export OMP_NUM_THREADS=1
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/nfshare/lib
SECONDS=0
mpirun /mnt/nfshare/bin/openseesmp main.tcl
echo "Elapsed: $SECONDS seconds."
echo "Code finished succesfully."
echo "Ready to import files!"