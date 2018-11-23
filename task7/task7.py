import re
import itertools
import functools

# EASY

def valuesunion(*dicts):
    res = set()
    for i in dicts:
        res.update(i.values())
    return res


def popcount(n):
    binary = bin(n)
    return binary.count('1')


def powers(n, m):
    res = {}
    for i in range(1, n+1):
        res.update({i: (i ** i) % m})
    return res


def subpalindrome(s):

    res = ''

    def ispalindrome(string):
        if string[::-1] == string:
            return True
        else:
            return False

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if ispalindrome(s[i:j]):
                if len(res) < len(s[i:j]):
                    res = s[i:j]
                elif len(res) == len(s[i:j]):
                    if s[i:j] < res:
                        res = s[i:j]
    return res


def isIPv4(s):
    pattern = r'[^0-9\.]'
    ip_unlike = re.findall(pattern, s)
    if ip_unlike or len(s) == 0:
        return False
    elif re.search(r'\.{2,}',s):
        return False
    else:
        numbers = s.split('.')
        if len(numbers) != 4:
            return False
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
            if number[0] == '0' and len(number) != 1:
                return False
        return True


def pascals():

    prefix = (1,)

    for i in itertools.count():
        newline = list()
        newline.append(1)

        for k in range(len(prefix) - 1):
            newline.append(prefix[k] + prefix[k + 1])

        newline.append(1)
        yield tuple(prefix)
        prefix = newline


# HARD

def spiral(n):
    i = 1
    a = [[0 for i in range(n)] for j in range(n)]

    for l in range(n):
        a[0][l] = i
        i += 1

    h1 = 1
    h2 = n - 1

    v1 = 0
    v2 = n - 1

    while i <= (n*n):
        # down
        for l in range(h2 - h1 + 1):
            a[h1 + l][v2] = i
            i += 1
        v2 -= 1

        # left
        for l in range(v2 - v1 + 1):
            a[h2][v2 - l] = i
            i += 1
        h2 -= 1

        # up
        for l in range(h2 - h1 + 1):
            a[h2 - l][v1] = i
            i += 1
        v1 += 1

        # right
        for l in range(v2 - v1 + 1):
            a[h1][v1 + l] = i
            i += 1

        h1 += 1

    return a


def fibonacci(n):
    return functools.reduce(lambda x, n: [x[1], x[0] + x[1]], range(n),
                            [0, 1])[0]


def brackets2(n, m, prefix='', rbalance=0, sbalance=0):

    # counting round brackets
    def rcount(prefix):
        return sum(map(lambda x: 1 if x in ('(', ')') else 0, prefix))

    # counting square brackets
    def scount(prefix):
        return sum(map(lambda x: 1 if x in ('[', ']') else 0, prefix))

    # checking if there are brackets in the stack
    def stack_check(prefix):
        stack = []

        for el in prefix:
            n = len(stack)
            if n == 0:
                stack.append(el)
            elif stack[n - 1] == '(' and el == ')':
                stack.pop()
            elif stack[n - 1] == '['and el == ']':
                stack.pop()
            else:
                stack.append(el)

        if len(stack) == 0:
            return True
        else:
            return False

    # yield correct prefix in case of all the conditions are satisfied
    if rcount(prefix) == 2 * n and scount(prefix) == 2 * m\
       and rbalance == 0 and sbalance == 0 and stack_check(prefix):
        yield prefix

    # generate new prefix
    else:
        for i in ('(', ')', '[', ']'):
            new_prefix = prefix + i
            if i == '(':
                new_rbalance = rbalance + 1
                new_sbalance = sbalance
            elif i == ')':
                new_rbalance = rbalance - 1
                new_sbalance = sbalance
            elif i == '[':
                new_sbalance = sbalance + 1
                new_rbalance = rbalance
            elif i == ']':
                new_sbalance = sbalance - 1
                new_rbalance = rbalance

            # check again and yield correct prefix
            if rcount(new_prefix) <= 2 * n and scount(prefix) <= 2 * m and \
                    new_rbalance >= 0 and new_sbalance >= 0:
                yield from brackets2(n, m, new_prefix, new_rbalance,
                                     new_sbalance)


if __name__ == "__main__":
    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2}, {4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}
    print('valuesunion - PASSED')

    assert popcount(0) == 0
    assert popcount(1) == 1
    assert popcount(10) == 2
    assert popcount(1023) == 10
    print('popcount - PASSED')

    assert powers(3, 1000000000) == {1: 1, 2: 4, 3: 27}
    assert powers(4, 50) == {1: 1, 2: 4, 3: 27, 4: 6}
    assert powers(1, 1) == {1: 0}
    print('powers - PASSED')

    assert subpalindrome('abc') == 'a'
    assert subpalindrome('aaaa') == 'aaaa'
    assert subpalindrome('abaxfgf') == 'aba'
    assert subpalindrome('abacabad') == 'abacaba'
    assert subpalindrome('qfrkktzaggxy') == 'gg'
    print('subpalindrome - PASSED')

    assert isIPv4('192.168.0.15')
    assert isIPv4('255.255.255.255')
    assert not isIPv4('555.555.555.555')
    assert not isIPv4('190+2.168.0.0')
    assert not isIPv4('abacaba')
    assert not isIPv4('')
    assert not isIPv4('32.130..60.253')
    assert not isIPv4('170.216.9.7.155')
    print('isIPv4 - PASSED')

    it = pascals()
    pasc_list = []
    for i in range(6):
        pasc_list.append(next(it))

    assert pasc_list == [(1,), (1, 1), (1, 2, 1), (1, 3, 3, 1),
                         (1, 4, 6, 4, 1), (1, 5, 10, 10, 5, 1)]
    print('pascals - PASSED')

    assert spiral(1) == [[1]]
    assert spiral(2) == [[1, 2],
                         [4, 3]]
    assert spiral(4) == [[1, 2, 3, 4],
                         [12, 13, 14, 5],
                         [11, 16, 15, 6],
                         [10, 9, 8, 7]]
    print('spiral - PASSED')

    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    print('fibonacci - PASSED')

    assert list(brackets2(1, 0)) == ['()']
    assert list(brackets2(0, 1)) == ['[]']
    assert list(brackets2(1, 1)) == ['()[]', '([])', '[()]', '[]()']
    assert list(brackets2(3, 0)) == ['((()))', '(()())', '(())()', '()(())',
                                     '()()()']
    assert list(brackets2(2, 1)) == ['(())[]', '(()[])', '(([]))', '()()[]',
                                     '()([])', '()[()]', '()[]()', '([()])',
                                     '([]())', '([])()', '[(())]', '[()()]',
                                     '[()]()', '[](())', '[]()()']
    print('brackets - PASSED')