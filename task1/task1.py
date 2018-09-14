def unique(e):
    return sorted(set(e))


print(unique([1, 2, 1, 3]))
print(unique({5, 1, 3}))
print(unique('adsfasdf'))


def transposeDict(d):
    transpose = dict()
    for key, value in d.items():
        transpose.update({value:key})
    return transpose


print(transposeDict({1: 'a', 2: 'b'}))
print(transposeDict({1: 1}))
print(transposeDict({}))


def mex(e):
    min_num = 2

    if 1 not in e:
        print(1)
    else:
        for elem in e:
            next_num = elem + 1
            if elem != min_num:
                if next_num not in e:
                    if next_num < min_num:
                        min_num=next_num
            else:
                min_num = next_num


mex([1, 2, 3])
mex(['asdf', 123])
mex([0, 0, 1, 0])


def frequencyDict(s):
    pass

frequencyDict('')
frequencyDict('abacaba')