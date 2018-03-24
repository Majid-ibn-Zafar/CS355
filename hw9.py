# Rofael Aleezada
# CS355, Homework 9
# March 27 2018
# Implementation of the Rejection Algorithm

from math import ceil
import numpy as np
import matplotlib.pyplot as plt


def rejection_method():
    a = 0
    b = 3
    c = ceil((b - 1) ** 2 / 3)

    x = np.random.uniform(a, b)
    y = np.random.uniform(0, c)
    f_x = (x - 1) ** 2 / 3

    while y > f_x:
        x = np.random.uniform(a, b)
        y = np.random.uniform(0, c)
        f_x = (x - 1) ** 2 / 3

    return x


def simulate(count):
    results = []
    for _ in range(count):
        results.append(rejection_method())

    plt.hist(results, bins=np.arange(0, 3, 0.1))
    plt.show()


simulate(10000)
