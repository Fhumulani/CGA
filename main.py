import CGA
import Sphere
import time
import matplotlib.pyplot as plt
import numpy as np

now = time.time()


#define the global parameters such as, the targeted beam current, waiting time, number of generations, number of population

target = 35

wait = 5   

gen =40
M = 16
lb = [5.]
ub = [46.]
Pc = 0.95;
Pm = 0.;
Er = 0.1;
N = len(lb)


b = CGA.CGA(gen,lb,ub,M,N,Sphere,Pc,Pm,Er,target,wait)
run_time = time.time()-now
print("we are done and running time was {0} seconds".format(run_time))

