#  This function should return sorted list of distinct elements of e
def unique(e):
    return sorted(set(e))


#  This function should return transposed dict d. It is garantueed that all the values of dict d are distinct
def transpose_dict(d):
    return {v: k for k, v in d.items()}


#  This function should return minimal positive integer which is not present at list e
def mex(e):
    return min([x for x in range(1, len(e)+2) if x not in e])


#  This function should return dict with counts of every symbol from string
def frequency_dict(s):
    return {c:s.count(c) for c in sorted(set(s))}


if __name__ == '__main__':
    assert unique([1, 2, 1, 3]) == [1, 2, 3]
    assert unique({5, 1, 3}) == [1, 3, 5]
    assert unique('adsfasdf') == ['a', 'd', 'f', 's']

    assert transpose_dict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}
    assert transpose_dict({1: 1}) == {1: 1}
    assert transpose_dict({}) == {}

    assert mex([1, 2, 3]) == 4
    assert mex(['asdf', 123]) == 1
    assert mex([0, 0, 1, 0]) == 2

    assert frequency_dict('') == {}
    assert frequency_dict('abacaba') == {'a': 4, 'b': 2, 'c': 1}


