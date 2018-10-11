import itertools
from functools import reduce


""" GENERATORS """


# Yields square of each element from the sequence
def squares(a):
    for elem in a:
        yield elem ** 2


# Yields elements from list n times
def repeatntimes(elems, n):
    rep = itertools.tee(elems, n)
    for elem in rep:
        yield from elem


# Yields even numbers starting from x (or from closest even number to x)
def evens(x):
    if x % 2:
        x += 1
    while True:
        yield x
        x += 2


# Yields numbers, which sum of digits is multiple of p in ascending order
def digitsumdiv(p):
    for i in itertools.count(1):
        if sum(map(int, str(i))) % p == 0:
            yield i


""" FUNCTIONAL PROGRAMMING """


# Yields digits from s
def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


#  Yield all symbols from string s
#  If symbol is english letter changes its case
def changecase(s):
    return map(lambda x: x.swapcase() if x.isalpha() else x, s)


# Returns product of elements from elems such that corresponding element of
# conds is True
def productif(elems, conds):
    return reduce(lambda x, y: x * y, map(lambda x: x[0] if x[1] else 1,
                  zip(elems, conds)), 1)
