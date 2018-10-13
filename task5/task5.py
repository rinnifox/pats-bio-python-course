def permutations(n):

    def perm_gen(n,  prefix=[]):
        if len(prefix) == n:
            yield tuple(prefix)
        for i in range(1, n+1):
            if i not in prefix:
                yield from perm_gen(n, prefix=prefix+[i])

    return list(perm_gen(n))


def correctbracketsequences(n):

    def brackets_gen(n, prefix=''):
        open = prefix.count('(')
        close = prefix.count(')')
        balance = open-close
        if len(prefix) == 2 * n and balance == 0:
            yield prefix
        else:
            for i in ['(', ')']:
                if len(prefix + i) <= (2 * n) and balance >= 0:
                    yield from brackets_gen(n, prefix=prefix + i)

    return list(brackets_gen(n))


def combinationswithrepeats(n, k):

    def comb_gen(n, k, prefix=[]):
        if len(prefix) == k:
            yield tuple(prefix)
        else:
            if len(prefix) > 0:
                startpoint = max(prefix)
            else:
                startpoint = 1
            for i in range(startpoint, n + 1):
                yield from comb_gen(n, k, prefix=prefix + [i])

    return list(comb_gen(n, k))


def unorderedpartitions(n):

    def part_gen(n, prefix=[]):
        if sum(prefix) == n:
            yield tuple(prefix)
        else:
            if len(prefix) > 0:
                startpoint = prefix[-1]
            else:
                startpoint = 1
            for i in range(startpoint, n - startpoint + 2):
                if sum(prefix + [i]) <= n:
                    yield from part_gen(n, prefix=prefix + [i])

    return list(part_gen(n))


if __name__ == "__main__":
    assert permutations(1) == [(1,)]
    assert permutations(2) == [(1, 2), (2, 1)]
    assert permutations(3) == [(1, 2, 3), (1, 3, 2), (2, 1, 3),
                               (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    print('permutations - PASSED')

    assert correctbracketsequences(1) == ['()']
    assert correctbracketsequences(2) == ['(())', '()()']
    assert correctbracketsequences(3) == ['((()))', '(()())', '(())()',
                                          '()(())', '()()()']
    print('correctbracketsequences - PASSED')

    assert combinationswithrepeats(1, 1) == [(1,)]
    assert combinationswithrepeats(2, 2) == [(1, 1), (1, 2), (2, 2)]
    assert combinationswithrepeats(3, 2) == [(1, 1), (1, 2), (1, 3), (2, 2),
                                             (2, 3), (3, 3)]
    print('combinationswithrepeats - PASSED')

    assert unorderedpartitions(1) == [(1,)]
    assert unorderedpartitions(3) == [(1, 1, 1), (1, 2), (3,)]
    assert unorderedpartitions(5) == [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 3),
                                      (1, 2, 2), (1, 4), (2, 3), (5,)]
    print('unorderedpartitions - PASSED')