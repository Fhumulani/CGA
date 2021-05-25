"""
Author: Fhumulani Nemulodi
Date: 20 September 2020
This is a fitness function. It takes the parameters values from population set them to the ion source 
and record the beam current extracted. The beam is compared with the targeted beam current and the difference 
is recorded as 

"""


import numpy as np
import epics
import time


def fitnes(X,target,wait):
    X = np.array(X)
    bend = epics.PV('bmag1q:put-I')
    with open("mag_values.txt","a") as file:
       file.write(str(round(X[0],5)))
       file.write("\n")
    bend.put(round(X[0],5))
    cur = epics.PV('vartable.fcmux:actvalue')
    time.sleep(wait)
    cur = cur.get()
    fitness_value = -1*abs(cur-target)
    with open("fitness.dat","a") as f:
        f.write(str(round(X[0],5))+","+str(cur)+","+str(-1*fitness_value)+"\n")
    return fitness_value
