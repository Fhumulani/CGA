import numpy as np
import pandas as pd
import time
import random


def selection(population):
    # nom_sum = sum(population['fitness'])
    
    if any(i < 0 for i in population['fitness']):
        a = 1
        b = abs(min(population['fitness']))
        Scaled_fitness = a *  population['fitness'] + b
   
        normalized_fitness = Scaled_fitness / sum(Scaled_fitness)
    else:
        normalized_fitness = population['fitness'] / sum(population['fitness'])

    nom = normalized_fitness.sort_values(ascending=False)

    sorted_idx = list(nom.index)

    nom_fit = list(nom[:])

    temp_pop = np.array(population.drop(['fitness'], axis=1))

 
    population = population.drop(['fitness'],axis=1)
    fitness = []

    for i in range(len(population)):
        temp_pop[i] = population.iloc[sorted_idx[i]][:]
        fitness.append(nom_fit[i])


    # cumsums = np.zeros((len(population),1))
    cumsums = list([0] * len(population))

    for i in range(len(cumsums)):
        cumsums[i] = sum(fitness[i:])

    R = random.uniform(0.,1)
    
    parent1_idx = len(population) - 1
    for i in range(1, len(cumsums)):
        if R > cumsums[i]:
            parent1_idx = i - 1
            break;
    parent2_idx = parent1_idx
    R = random.uniform(0.,1)

    
    for i in range(1, len(cumsums)):
        #print(i,R,cumsums[i])
        if R > cumsums[i]:
            parent2_idx = i - 1
            if parent2_idx != parent1_idx:
                break;
        #c = input("Enter: ")
    #print(parent1_idx,parent2_idx)
    return temp_pop[parent1_idx], temp_pop[parent2_idx]
