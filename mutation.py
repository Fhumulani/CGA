import numpy as np
import random
def mutate(lower,upper,child,Pm):
   for i in range(len(child)):
      R1 = np.random.random()
      if R1 < Pm:
         child[i] = (upper[i]-lower[i])*np.random.random()+lower[i]

   return child
   
      
