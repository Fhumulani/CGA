import random
import numpy as np


def initialize(lower, upper, M, N):
    population = np.zeros((M, N))

    for i in range(M):
        for j in range(N):
           population[i][j] = round((upper[j]-lower[j])*np.random.random()+lower[j],4)

    return population
