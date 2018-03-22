# Rofael Aleezada
# CS 355 Homework 8
# March 22 2018
# Python implementation of Queuing System Simulation

import numpy as np
from math import log10 as log
from random import random as rand
from random import randint


def one_server_day(Twork, Njobs, Wmean, Wmax, Nwithdr, Nav, Nat10):
    k = 4
    mu = 4
    alpha = [6, 10, 7, 5]
    lamb = [0.3, 0.2, 0.7, 1.0]

    arrival = []
    start = []
    finish = []
    server = []
    j = 0
    T = 0
    A = np.zeros((1, k))

    while T < 840:
        T = T - mu*log(rand())
        arrival.append(T)

        Nfree = len(A[np.where(A<T)])
        u = 0

        if Nfree == 0:
            for v in range(1, k):
                if A[0][v] < A[0][u]:
                    u = v
            if A[0][u] - T > 15:
                start.append(T + 15)
                finish.append(T + 15)
                u = -1
            else:
                start.append(A[0][u])
        else:
            u = randint(0, k-1)
            while A[0][u] > T:
                u = randint(0, k-1)
            start.append(T)
        server.append(u)

        if u >= 0:
            S = np.sum(np.random.gamma(alpha[u], lamb[u]))
            finish.append(start[j] + S)
            A[0][u] = start[j] + S

        j = j + 1

    arrival = np.asarray(arrival)
    start = np.asarray(start)
    finish = np.asarray(finish)
    server = np.asarray(server)

    Twork_day = []
    Njobs_day = []

    for u in range(k):
        Twork_day.append(np.sum(finish[np.where(server == u)] - start[np.where(server == u)]))
        Njobs_day.append(len(server[np.where(server == u)]))

    Twork.append(Twork_day)
    Njobs.append(Njobs_day)

    Wmean += np.mean(start - arrival)
    Wmax += np.max(start - arrival)
    Nwithdr += len(np.where(server == -1)[0])
    Nav += len(np.where(start - arrival < 0.00001)[0])
    Nat10 += len(np.where(finish > 840)[0])

    return Twork, Njobs, Wmean, Wmax, Nwithdr, Nav, Nat10


def simulate(days):
    Twork = []
    Njobs = []
    Wmean = 0
    Wmax = 0
    Nwithdr = 0
    Nav = 0
    Nat10 = 0
    for _ in range(days):
        Twork, Njobs, Wmean, Wmax, Nwithdr, Nav, Nat10 = one_server_day(Twork, Njobs, Wmean, Wmax, Nwithdr, Nav, Nat10)

    Twork = np.asarray(Twork).mean(axis = 0)
    Njobs = np.asarray(Njobs).mean(axis = 0)
    Wmean = Wmean / days
    Wmax = Wmax / days
    Nwithdr = Nwithdr / days
    Nav = Nav / days
    Nat10 = Nat10 / days

    print("Average work done by each server per day (mins): ", end='')
    print(Twork)
    print("Average number of jobs done by each server per day: ", end='')
    print(Njobs)
    print("Average job waiting time per day (mins): " + str(Wmean))
    print("Average longest waiting time per day (mins): " + str(Wmax))
    print("Average number of withdrawn jobs per day: "+ str(Nwithdr))
    print("Average number of non-waiting jobs per day: " + str(Nav))
    print("Average number of jobs left after 10PM per day: " + str(Nat10))


simulate(365)
