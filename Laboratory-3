from math import sqrt
import timeit
import matplotlib.pyplot as plt
import numpy as np


def sieve1(n):
    c = [False] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        if c[i] == True:
            j = 2 * i
            while j <= n:
                c[j] = False
                j = j + i
        i = i + 1


def sieve2(n):
    c = [False] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j = j + i
        i = i + 1


def brute(n):
    c = [False] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        if c[i] == True:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j = j + 1
        i = i + 1


def trialdiv(n):
    c = [False] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 1
        while j < i:
            if i % j == 0:
                c[i] = False
            j = j + 1
        i = i + 1


def trialdiv_optimized(n):
    arr = [True] * (n + 1)
    arr[1] = False
    i = 2

    while i <= n:
        j = 2
        while j <= int(sqrt(i)):
            if i % j == 0:
                arr[i] = False
                break
            j += 1
        i += 1


# ------------------------------------------------------------------------
prime_algorithms = [
    {
        "name": "Sieve of Eratosthenes 1",
        "primes": lambda n: sieve1(n)
    },
    {
        "name": "Sieve of Eratosthenes 2",
        "primes": lambda n: sieve2(n)
    },
    {
        "name": "Brute algorithm",
        "primes": lambda n: brute(n)
    },
    {
        "name": "Trial division",
        "primes": lambda n: trialdiv(n)
    },
    {
        "name": "Trial division optimized",
        "primes": lambda n: trialdiv_optimized(n)
    }
]

elements = np.array([i * 100 for i in range(1, 50)])

for alg in prime_algorithms:
    times = list()
    start_time = timeit.default_timer()
    for i in range(1, 50):
        start_alg = timeit.default_timer()
        num = i * 100
        alg["primes"](num)
        end_alg = timeit.default_timer()
        times.append(end_alg - start_alg)
        print(alg["name"], "Calculated ", i * 1000, "Primes in ", end_alg - start_alg, "s")

    end_time = timeit.default_timer()
    print(alg["name"], "Calculated all Primes in", end_time - start_time, "s")

    plt.plot(elements, times, label=alg["name"])

plt.grid()
plt.legend()
plt.show()
