#  This function should return sorted list of distinct elements of e
def unique(e):
    return sorted(set(e))


#  This function should return transposed dict d. It is garantueed that all the values of dict d are distinct
def transposeDict(d):
    return {v: k for k, v in d.items()}


#  This function should return minimal positive integer which is not present at list e
def mex(e):
    return 1 if 1 not in e else min([x+1 for x in [elem for elem in e if type(elem) == int] if x+1 not in e])

#  This function should return dict with counts of every symbol from string
def frequencyDict(s):
    return {c:s.count(c) for c in sorted(set(s))}