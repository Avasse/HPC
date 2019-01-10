#!/usr/bin/env python3

import hpcMpi
import sys
import time as t
import numpy
from mpi4py import MPI


if __name__ == '__main__':

    # parse command line arguments
    step = 1e-3
    if len(sys.argv) == 2:
        step = float(sys.argv[1])

    t0 = t.time()

    # compute
    comm = MPI.COMM_WORLD
    worldRank = comm.Get_rank()
    worldSize = comm.Get_size()
    rate = 1/worldSize
    node_result = numpy.empty(1, dtype=float)
    
    node_result[0] = hpcMpi.compute(hpcMpi.fPi, (worldRank*rate),(worldRank+1)*rate, step)
    
    
    all_results = numpy.empty(1, dtype=float)
    comm.Reduce(node_result, all_results,op=MPI.SUM)

    t1 = t.time()

    # output result
    time = t1 - t0
    if worldRank == 0 :
      print(step, worldSize, all_results[0], time)

  
