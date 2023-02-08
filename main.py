import time
from matplotlib import pyplot as plt
import numpy as np


# fibonacci number using golden ratio
def fib1(n):
    from math import sqrt
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))



# fibonacci number using iteration
def fib2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# fibonacci number using fast doubling
def fib3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib = [fib[1], fib[0] + fib[1]]
        return fib[1]



# fibonacci number using matrix multiplication
def fib4(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [[1, 1], [1, 0]]
        for i in range(2, n + 1):
            fib = [[fib[0][0] + fib[0][1], fib[0][0]], [fib[0][0], 0]]
        return fib[0][0]


# fibonacci number using dynamic programming
def fib5(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


# fibonacci number using recursion
def fib6(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


# ----------------------------------------------------------------------------------


# # calculate the time complexity for each function and muliply by 1000 to get the time in milliseconds
# def time_complexity():
#     time1 = []
#     time2 = []
#     time3 = []
#     time4 = []
#     time5 = []
#     time6 = []
#     for i in range(100):
#         start = time.time()
#         fib1(i)
#         end = time.time()
#         time1.append((end - start) * 1000)
#         start = time.time()
#         fib2(i)
#         end = time.time()
#         time2.append((end - start) * 1000)
#         start = time.time()
#         fib3(i)
#         end = time.time()
#         time3.append((end - start) * 1000)
#         start = time.time()
#         fib4(i)
#         end = time.time()
#         time4.append((end - start) * 1000)
#         start = time.time()
#         fib5(i)
#         end = time.time()
#         time5.append((end - start) * 1000)
#         start = time.time()
#         fib6(i)
#         end = time.time()
#         time6.append((end - start) * 1000)
#     return time1, time2, time3, time4, time5, time6
#
#
# # ----------------------------------------------------------------------------------
#
# # create a matrix to store the time complexity
# time1, time2, time3, time4, time5, time6 = time_complexity()
# time_complexity = np.array([time1, time2, time3, time4, time5, time6])
# # display the time complexity in a table
# print(time_complexity)
#
# # display the time complexity in a graph
# dev_x = [i for i in range(100)]
# plt.xlabel('number of fibonacci numbers')
# dev_y = time_complexity[0]
# plt.ylabel('time complexity, ms')
# plt.plot(dev_x, dev_y, label='fib1')
# dev_y = time_complexity[1]
# plt.plot(dev_x, dev_y, label='fib2')
# dev_y = time_complexity[2]
# plt.plot(dev_x, dev_y, label='fib3')
# dev_y = time_complexity[3]
# plt.plot(dev_x, dev_y, label='fib4')
# dev_y = time_complexity[4]
# plt.plot(dev_x, dev_y, label='fib5')
# dev_y = time_complexity[5]
# plt.plot(dev_x, dev_y, label='fib6')
# plt.legend()
# plt.show()


#calculate the time complexity for the first function
def time_complexity1():
    time1 = []
    for i in range(100):
        start = time.time()
        fib1(i)
        end = time.time()
        time1.append((end - start) * 1000)
    return time1
#calculate the time complexity for the second function
def time_complexity2():
    time2 = []
    for i in range(100):
        start = time.time()
        fib2(i)
        end = time.time()
        time2.append((end - start) * 1000)
    return time2
#calculate the time complexity for the third function
def time_complexity3():
    time3 = []
    for i in range(100):
        start = time.time()
        fib3(i)
        end = time.time()
        time3.append((end - start) * 1000)
    return time3
#calculate the time complexity for the fourth function
def time_complexity4():
    time4 = []
    for i in range(100):
        start = time.time()
        fib4(i)
        end = time.time()
        time4.append((end - start) * 1000)
    return time4
#calculate the time complexity for the fifth function
def time_complexity5():
    time5 = []
    for i in range(100):
        start = time.time()
        fib5(i)
        end = time.time()
        time5.append((end - start) * 1000)
    return time5
#calculate the time complexity for the sixth function
def time_complexity6():
    time6 = []
    for i in range(100):
        start = time.time()
        fib6(i)
        end = time.time()
        time6.append((end - start) * 1000)
    return time6

#display the time complexity in a graph
dev_x = [i for i in range(100)]
plt.xlabel('number of fibonacci numbers')
dev_y = time_complexity1()
plt.ylabel('time complexity, ms')
plt.plot(dev_x, dev_y, label='fib1')
dev_y = time_complexity2()
plt.plot(dev_x, dev_y, label='fib2')
dev_y = time_complexity3()
plt.plot(dev_x, dev_y, label='fib3')
dev_y = time_complexity4()
plt.plot(dev_x, dev_y, label='fib4')
dev_y = time_complexity5()
plt.plot(dev_x, dev_y, label='fib5')
dev_y = time_complexity6()
plt.plot(dev_x, dev_y, label='fib6')
plt.legend()
plt.show()





