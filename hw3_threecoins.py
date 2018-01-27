# Rofael Aleezada
# January 29 2018
# Flip Three Coins Program, CS 355
# Python port of MATLAB program calculating percentages of trials where
# flipping three coins gives either 0, 1, 2, or 3 heads

import numpy as np


def three_coin_tosses(n):
    u = np.asarray([[np.random.random() for i in range(n)] for j in range(3)]) # u = rand(3,n)
    y = u.copy()                                                               # y = (u < 0.5)
    y[ y < 0.5 ] = 1
    y[ y < 1 ] = 0

    x = [0, 0, 0, 0]                                                           # x = sum(y)
    for i in range(n):
        heads = y[0][i] + y[1][i] + y[2][i]
        x[int(heads)] += 1
    sum = np.asarray(x).sum()                                                  # convert to fractions
    for i in range(len(x)):
        x[i] = x[i]/sum
    return x


print(three_coin_tosses(10000))
