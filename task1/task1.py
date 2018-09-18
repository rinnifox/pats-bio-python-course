import time

#  This function should return sorted list of distinct elements of e
def unique(e):
    return sorted(set(e))


#  This function should return transposed dict d. It is garantueed that all the values of dict d are distinct
def transposeDict(d):
    return {v: k for k, v in d.items()}


#  This function should return minimal positive integer which is not present at list e
def mex(e):
    return min([x for x in range(1, len(e)+2) if x not in e])


#  This function should return dict with counts of every symbol from string
def frequencyDict(s):
    return {c:s.count(c) for c in sorted(set(s))}