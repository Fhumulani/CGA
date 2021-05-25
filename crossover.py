import numpy as np
def cross(p1,p2,Pc,lb,ub):
    child1 = np.zeros((len(p1)))
    child2 = np.zeros((len(p1)))
    
    for i in range(len(p1)):
        beta = np.random.random()
        child1[i] = beta*p1[i] + (1-beta)*p2[i]
        child2[i] = (1-beta)*p1[i] + beta*p2[i]
        #R2 = np.random.random()

    if child1[i] > ub[i]:
         child1[i]  =  ub[i]
    if child1[i] < lb[i]:
         child1[i]  =  lb[i]

    if child2[i] > ub[i]:
         child2[i]  =  ub[i]
    if child2[i] < lb[i]:
         child2[i]  =  lb[i]


    R1 = np.random.random()  
    if R1 > Pc:
        child1 = p1

    R2 = np.random.random()

    if R2 > Pc:
         child2 = p2

    return child1,child2
