#  This function should return sorted list of distinct elements of e
def unique(e):
    return sorted(set(e))

print('unique results:')
print(unique([1, 2, 1, 3]))
print(unique({5, 1, 3}))
print(unique('adsfasdf'))


#  This function should return transposed dict d. It is garantueed that all the values of dict d are distinct
def transposeDict(d):
    transpose = dict()
    for key, value in d.items():
        transpose.update({value:key})
    return transpose


print('transpose results')
print(transposeDict({1: 'a', 2: 'b'}))
print(transposeDict({1: 1}))
print(transposeDict({}))


#  This function should return minimal positive integer which is not present at list e
def mex(e):
    if 1 not in e:
        return 1
    else:
        for elem in e:
            if type(elem) == int:
                if elem+1 not in e:
                    return elem+1


print('mex results:')
print(mex([1, 2, 3]))
print(mex(['asdf', 123]))
print(mex([0, 0, 1, 0]))


#  This function should return dict with counts of every symbol from string s
def frequencyDict(s):
    numbers = {}
    for elem in s:
        number = s.count(elem)
        numbers.update({elem: number})
    return numbers

print('frequency results')
print(frequencyDict(''))
print(frequencyDict('abacaba'))