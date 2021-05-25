import init as it
import numpy as np
import pandas as pd
import selection as sl
import crossover as cs
import mutation as mt
import elitism as el
import matplotlib.pyplot as plt
import time
import epics


def CGA(generations,lb, ub, M, N, fit,Pc,Pm,Er,target,wait):
    population = it.initialize(lb, ub, M, N)
    #print(population)
    c = 0

    fitness = []
    fitnesses = []
    best = np.zeros((generations,N+1))
    for i in range(M):
        fitness.append(fit.fitnes(population[i],target,wait))
    fitt = []
    population = pd.DataFrame(population)
    population['fitness'] = fitness
    maxx = max(population.fitness)
        # print(maxx)
        # print(maxx,newpopulation.genes[newpopulation.fitness == maxx].iloc[0])
    fitnesses.append(maxx)
    #print("generation  #{0}".format(1))
    newpop = np.array(population.drop(['fitness'], axis=1))
    i = 0
    b_f = 100
    best_fit = 10
    
    while (b_f > 0.01 and i < generations):
        for j in range(0,M,2):

           p1, p2 = sl.selection(population)


           child1,child2 = cs.cross(p1,p2,Pc,lb,ub)

           child1 = mt.mutate(lb,ub,child1,Pm)
           child2 = mt.mutate(lb,ub, child2, Pm)

           newpop[j] = child1

           newpop[j + 1] = child2

        newpopulation = pd.DataFrame(newpop)

	#print(newpopulation)
	#name = input("Enter ")

        fitness1 = []
        for k in range(M):
            fitness1.append(fit.fitnes(newpopulation.iloc[k],target,wait))
        newpopulation['fitness'] = fitness1
        

        pop1 = population.copy()
        newpopulation = el.ellist(pop1,newpopulation, Er)


        fitt.append(fitness1)
        maxx = max(newpopulation.fitness)


        fitnesses.append(maxx)
        newpopulation= newpopulation.sort_values(by=['fitness'],ascending=False)
        newpopulation.reset_index(inplace=True)
        newpopulation = newpopulation.drop(['index'],axis=1)



        best[i] = newpopulation.iloc[0]
        best_fit = list(newpopulation.iloc[0])
        b_f = abs(list(newpopulation.iloc[0])[N])
	bend = round(abs(list(newpopulation.iloc[0])[0]),3)
	bend1 = epics.PV('bmag1q:put-I')
        bend1.put(round(bend,5))
        time.sleep(wait)
	cur = epics.PV('vartable.fcmux:actvalue')
        cur = cur.get()
	new_fit = abs(cur - target)
	#if b_f < abs(new_fit):
	 #  newpopulation.iloc[0][N] = -1*new_fit
	 #  print(b_f,new_fit)
	#b_f = abs(list(newpopulation.iloc[0])[N])
	print("generation  #{0} with fitness {1}".format(i + 1,b_f))
	with open("data.txt","a") as data:
	   data.write("{0},{1},{2},generation #{3} \n".format(bend,cur,b_f,i))
        population = newpopulation.copy()
        i = i + 1
    best = pd.DataFrame(best)
    best = best.drop(best[best[N] == 0].index)
    best= best.sort_values(by=[N],ascending=False,axis=0)
    best.reset_index(inplace=True)
    best = best.drop(['index'],axis=1)
    bend_c = epics.PV('bmag1q:put-I')
    bend_c.put(best.iloc[0][0])

    return list(best.iloc[0])
