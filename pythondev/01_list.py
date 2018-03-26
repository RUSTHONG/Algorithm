from timeit import *

def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        li += [i]


def test3():
    for i in range(10000):
        li = list(range(10000))


def test4():
    li = [i for i in range(10000)]


timer1 = Timer("test1()", "from __main__ import test1")
print("append:", timer1.timeit(1000))

timer2 = Timer("test2()", "from __main__ import test2")
print("append:", timer2.timeit(1000))

timer3 = Timer("test3()", "from __main__ import test3")
print("append:", timer3.timeit(1000))

timer4 = Timer("test4()", "from __main__ import test4")
print("append:", timer4.timeit(1000))

