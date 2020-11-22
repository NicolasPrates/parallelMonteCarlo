import random
from mpi4py import MPI

def monteCarloPiParalelo(n):
    comm = MPI.COMM_WORLD
    size = comm.Get_size
    rank = comm.Get_rank
    acertos = 0
    acertos1 = 0
    acertos2 = 0
    acertos3 = 0
    oldpi, pi, mypi = 0.0, 0.0, 0.0
    print('chegou até aqui')

    if (rank ==0):
        for i in range(int(n/4)):
            x = random.uniform(-1,1)
            y = random.uniform(-1,1)
        if((x*x) + (y*y) < 1):
            acertos = acertos + 1
        comm.Send(acertos, dest=3)
            #if(n %4 ==0):
            #   print('acertou no rank 0 seu arrombado\n')
    elif (rank ==1):
        for j in range(int(n/4)):
            x1 = random.uniform(-1,1)
            y1 = random.uniform(-1,1)
        if((x1*x1) + (y1*y1) < 1):
            acertos1 = acertos1 + 1
        comm.Send(acertos1, dest=3)
            #if(n %4 ==0):
            #   print('acertou no rank 1 seu arrombado\n')
    elif (rank ==2):
        for k in range(int(n/4)):
            x2 = random.uniform(-1,1)
            y2 = random.uniform(-1,1)
        if((x2*x2) + (y2*y2) < 1):
            acertos2 = acertos2 + 1
        comm.Send(acertos2, dest=3)
            #if(n %4 ==0):
            #    print('acertou no rank 2 seu arrombado\n')
    else:
        for l in range(int(n/4)):
            x3 = random.uniform(-1,1)
            y3 = random.uniform(-1,1)
        if((x3*x3) + (y3*y3) < 1):
            acertos3 = acertos3 + 1
        comm.Recv(acertos, source=0)
        comm.Recv(acertos1, source=1)
        comm.Recv(acertos2, source=2)
            #if(n %4 ==0):
            #    print('acertou no rank 3 seu arrombado\n')
        pi = 4*(acertos + acertos1 + acertos2 + acertos3)/n
    return(pi)

pi = monteCarloPiParalelo(10000)
print(pi)