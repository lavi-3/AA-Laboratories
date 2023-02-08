from timeit import default_timer as timer
from matplotlib import pyplot as plt
import prettytable as pt


# fibonacci number using golden ratio
def fib1(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** n - (-golden_ratio) ** (-n)) / 5 ** 0.5)


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
# calculate the time required to execute the first function
def time_complexity1():
    time1 = []
    for i in range(100):
        start = timer()
        fib1(i)
        end = timer()
        time1.append((end - start) * 1000)
    return time1


# calculate the time required to execute the second function
def time_complexity2():
    time2 = []
    for i in range(100):
        start = timer()
        fib2(i)
        end = timer()
        time2.append((end - start) * 1000)
    return time2


# calculate the time required to execute the third function
def time_complexity3():
    time3 = []
    for i in range(100):
        start = timer()
        fib3(i)
        end = timer()
        time3.append((end - start) * 1000)
    return time3


# calculate the time required to execute the fourth function
def time_complexity4():
    time4 = []
    for i in range(100):
        start = timer()
        fib4(i)
        end = timer()
        time4.append((end - start) * 1000)
    return time4


# calculate the time required to execute the fifth function
def time_complexity5():
    time5 = []
    for i in range(100):
        start = timer()
        fib5(i)
        end = timer()
        time5.append((end - start) * 1000)
    return time5


# calculate the time required to execute the sixth function
def time_complexity6():
    time6 = []
    for i in range(100):
        start = timer()
        fib6(i)
        end = timer()
        time6.append((end - start) * 1000)
    return time6
# ----------------------------------------------------------------------------------
# display the time complexity in a table
table = pt.PrettyTable()
table.field_names = ['n', 'fib1', 'fib2', 'fib3', 'fib4', 'fib5', 'fib6']
for i in range(40):
    table.add_row([i, time_complexity1()[i], time_complexity2()[i], time_complexity3()[i], time_complexity4()[i],
                   time_complexity5()[i], time_complexity6()[i]])
print(table)
# ----------------------------------------------------------------------------------
# display the time complexity in a graph
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
