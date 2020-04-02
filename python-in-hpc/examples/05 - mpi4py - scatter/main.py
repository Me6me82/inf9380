from mpi4py import MPI
from numpy import array, zeros
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
buffer = zeros(10, float)  # prepare a receive buffer
if rank == 0:
    n = range(size)
    data = array(range(10*size), float) * 10
    comm.scatter(n, root=0)
    comm.Scatter(data, buffer, root=0)
else:
    n = comm.scatter(None, root=0)      # returns the value
    comm.Scatter(None, buffer, root=0)  # in-place modification
    print(rank, buffer)
