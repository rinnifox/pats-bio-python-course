import re

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
    pass


def isIPv4(s):
    pattern = r'[^0-9\.]'
    ip_unlike = re.findall(pattern, s)
    if ip_unlike or len(s) == 0:
        return False
    else:
        numbers = s.split('.')
        for number in numbers:
            if number.isdigit():
                if int(number) < 0 or int(number) > 255:
                    return False
                if number[0] == '0' and len(number) != 1:
                    return False
                return True
            else:
                return False


def pascals():
    pass


# HARD

def spiral(n):
    pass


def fibonacci(n):
    pass


def brackets2(n, m):
    pass

