import numpy as np
import pandas as pd
def ellist(pop,pop1,Er):
    M = len(pop)
    Elit_no = int(round(M*Er))
    #pop1 = pop1.sort_values(by=['fitness'],ascending=True)
    fitness1 = pop1.fitness
    
  
    ww = pop.sort_values(by=['fitness'],ascending=False)
    

    sorted_idx= list(ww.index)    

    nom_fit = list(ww.fitness)

    ww.drop(['fitness'],inplace=True,axis=1)
    pop.drop(['fitness'], inplace=True, axis=1)
    ppp = pop1.drop(['fitness'], axis=1)
    
    newpopulation = np.array(pop)
    fitness = []
    for i in range(Elit_no+1):
        newpopulation[i] = ww.iloc[i]
        fitness.append(nom_fit[i])
   
    for i in range(Elit_no+1,M):
        newpopulation[i] = ppp.iloc[i]
        fitness.append(fitness1[i])
    newpopulation = pd.DataFrame(newpopulation)
    newpopulation['fitness'] = fitness

    return newpopulation

