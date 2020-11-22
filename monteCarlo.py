from mpi4py import MPI
import numpy

def paralelo_pi(n):
    count = 0
    for x, y in n:
        if x**2 + y**2 <= 1:
            count += 1
    pi = 4*float(count)/len(n)
    return pi

comm = MPI.COMM_WORLD
processadores = comm.Get_size()
oRank = comm.Get_rank()

if oRank == 0:
    N = 100000
    n = numpy.random.random((processadores, N, 2))
else:
    n = None
n = comm.scatter(n, root=0)

piBuffer = paralelo_pi(n) / processadores

pi = comm.reduce(piBuffer, root=0)

if oRank == 0:
    error = abs(pi - numpy.pi)
    print("pi: %.16f, erro: %.16f" % (pi, error))