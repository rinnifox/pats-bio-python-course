# Calculates factorial of n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


# Calculates n-th Fibonacci number
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


# Calculates  n-th number of the given recurrent formula
def recurrent(n):
    # f(0) = 0
    if n == 0:
        return 0
    # f(1) = 1
    if n == 1:
        return 1
    # f(2n) = f(n)
    if n % 2 == 0:
        return recurrent(n // 2)
    # f(2n+1) = f(n) + f(n+1)
    else:
        return recurrent((n - 1) // 2) + recurrent(((n - 1) // 2) + 1)


# Calculates the sum of digits of decimal representation of number n
def digitsum(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + digitsum(n // 10)


# Returns reversed string s
def reversestring(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reversestring(s[:-1])


# Calculates Ackermann number according to the given recurrent formula
def ackermann(m, n):
    # A(0, n) = n + 1
    if m == 0:
        return n + 1
    # A(m, 0) = A(m - 1, 1)
    if n == 0:
        return ackermann(m - 1, 1)
    # A(m, n) = A(m - 1, A(m, n - 1))
    return ackermann(m-1, ackermann(m, n - 1))


# Creates some borders in picture n x n
def drawborders(n):
    if n <= 1:
        return ['+']
    else:
        result = ['+' + '-' * (n - 2) + '+'] * 2
        pattern = drawborders(n - 2)
        for i in range(1, n - 1):
            result.insert(i, '|' + pattern[i - 1] + '|')
        return result


# Returns list of all binary strings of length n
def genbinarystrings(n):
    result = []
    if n == 0:
        return ['']
    else:
        zero = list(map(lambda x: '0' + x, genbinarystrings(n - 1)))
        one = list(map(lambda x: '1' + x, genbinarystrings(n - 1)))
        result += zero + one
    return result


# Finds if the given integer  is power of 2 or not
def istwopower(n):
    if n == 1:
        return True
    elif n <= 0:
        return False
    elif n % 2 == 0:
        return istwopower(n // 2)
    return False


# Finds integer c such that its decimal representation equals to concatenation
# of decimal representations of a and b
def concatnumbers(a, b):
    if b // 10 == 0:
        return a * 10 + b
    else:
        return concatnumbers(a, b // 10) * 10 + b % 10


# Returns a list with given pattern in its name
def abacaba(n):
    if n == 1:
        return [1]
    else:
        pattern = abacaba(n - 1)
        return pattern + [n] + pattern


# Adds some parentheses pairs to the string
def parentheses(s):
    base = [0, 1, 2]
    if len(s) in base:
        return '(' + s + ')'
    else:
        return '(' + s[0] + parentheses(s[1:-1]) + s[-1] + ')'


# Finds their greatest common divisor using Euclead algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Sorts a list of integers using Merge sort algorithm.
def mergesort(a):

    if len(a) > 1:
        middle = len(a) // 2
        lefthalf = a[:middle]
        righthalf = a[middle:]
        lefthalf = mergesort(lefthalf)
        righthalf = mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i += 1
            else:
                a[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            a[k] = righthalf[j]
            j += 1
            k += 1

    return a


if __name__ == "__main__":
    assert factorial(4) == 24
    assert factorial(0) == 1
    assert factorial(2) == 2
    print('factorial - PASSED')

    assert fibonacci(1) == 1
    assert fibonacci(4) == 3
    assert fibonacci(10) == 55
    print('fibonacci - PASSED')

    assert recurrent(2) == 1
    assert recurrent(3) == 2
    assert recurrent(5) == 3
    assert recurrent(7) == 3
    print('recurrent - PASSED')

    assert digitsum(0) == 0
    assert digitsum(123) == 6
    assert digitsum(192837465) == 45
    print('digitsum - PASSED')

    assert reversestring('') == ''
    assert reversestring('1') == '1'
    assert reversestring('asdf') == 'fdsa'
    assert reversestring('abacaba') == 'abacaba'
    print('reversestring - PASSED')

    assert ackermann(0, 10) == 11
    assert ackermann(1, 1) == 3
    assert ackermann(2, 2) == 7
    assert ackermann(2, 5) == 13
    assert ackermann(3, 3) == 61
    print('ackermann - PASSED')

    assert drawborders(1) == ['+']

    assert drawborders(2) == ['++',
                              '++']

    assert drawborders(3) == ['+-+',
                              '|+|',
                              '+-+']

    assert drawborders(4) == ['+--+',
                              '|++|',
                              '|++|',
                              '+--+']

    assert drawborders(5) == ['+---+',
                              '|+-+|',
                              '||+||',
                              '|+-+|',
                              '+---+']
    print('drawborders - PASSED')

    assert genbinarystrings(0) == ['']
    assert genbinarystrings(1) == ['0', '1']
    assert genbinarystrings(2) == ['00', '01', '10', '11']
    assert genbinarystrings(3) == ['000', '001', '010', '011', '100', '101',
                                   '110', '111']
    print('genbinarystrings - PASSED')

    assert istwopower(-5) is False
    assert istwopower(0) is False
    assert istwopower(1) is True
    assert istwopower(2) is True
    assert istwopower(4) is True
    assert istwopower(67) is False
    assert istwopower(1024) is True
    print('istwopower - PASSED')

    assert concatnumbers(1, 2) == 12
    assert concatnumbers(55, 88) == 5588
    assert concatnumbers(123, 789) == 123789
    assert concatnumbers(1000, 2) == 10002
    print('concatnumbers - PASSED')

    assert abacaba(1) == [1]
    assert abacaba(2) == [1, 2, 1]
    assert abacaba(3) == [1, 2, 1, 3, 1, 2, 1]
    assert abacaba(4) == [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]
    print('abacaba - PASSED')

    assert parentheses('example') == '(e(x(a(m)p)l)e)'
    assert parentheses('odd') == '(o(d)d)'
    assert parentheses('even') == '(e(ve)n)'
    print('parentheses - PASSED')

    assert gcd(1, 5) == 1
    assert gcd(4, 6) == 2
    assert gcd(18, 12) == 6
    assert gcd(283918822, 595730520) == 22
    print('gcd - PASSED')

    assert mergesort([]) == []
    assert mergesort([100]) == [100]
    assert mergesort([1, 3, 2]) == [1, 2, 3]
    assert mergesort([1, 3, 5, 4, 2]) == [1, 2, 3, 4, 5]
    print('mergesort - PASSED')