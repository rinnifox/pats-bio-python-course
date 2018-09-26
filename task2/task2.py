#  Returns string representing this list
def listToString(a):
    return str(a)


# Adds border around a picture
def addBorder(a):
    newlist = []
    for elem in a:
        newlist.append('|' + elem + '|')
    newlist.insert(0, '+' + '-' * len(a[0]) + '+')
    newlist.append('+' + '-' * len(a[0]) + '+')
    return newlist


# Returns reductions of strings of list
def shorting(e):
    new_list = []
    for elem in e:
        if len(elem) <= 10:
            new_list.append(elem)
        else:
            new_list.append(str(elem[0]) + str(len(elem)-2) +
                            str(elem[len(elem) - 1]))
    return new_list


# Returns number of participants who will advance to the next round
def competition(e, k):
    next_round = []
    for elem in e:
        if elem >= e[k] and elem != 0:
            next_round.append(elem)
        else:
            break
    return len(next_round)


# Returns sorted list of integers s = i ** 2 + j ** 2 if (i, j) is 'good'
def goodPairs(a, b):
    s = []
    for i in a:
        for j in b:
            if (i * j) % (i + j) == 0:
                s.append(i ** 2 + j ** 2)
    return sorted(set(s))


# Returns list a of length 2 * n - 1. Its i-th element is list of some zeros
def makeShell(n):
    shell = []
    i = 1
    j = n-1
    for first in range(n):
        shell.append([0] * i)
        i += 1
    for second in range(n, 2 * n - 1):
        shell.append([0] * j)
        j -= 1
    return shell


if __name__ == '__main__':
    assert listToString([]) == "[]"
    assert listToString([1, 2, 3]) == "[1, 2, 3]"
    assert listToString([-5]) == "[-5]"

    assert addBorder(['abc',
                      'def']) == ['+---+',
                                  '|abc|',
                                  '|def|',
                                  '+---+']

    assert shorting(['word', 'localization', 'internationalization',
                     'pneumonoultramicroscopicsilicovolcanoconiosis']) \
        == ['word', 'l10n', 'i18n', 'p43s']

    assert competition([5, 4, 3, 2, 1], 2) == 3
    assert competition([1, 0, 0, 0], 3) == 1
    assert competition([10, 9, 8, 7, 7, 7, 5, 5], 4) == 6

    assert goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == [128, 160, 180]
    assert goodPairs([2], [2]) == [8]
    assert goodPairs([7, 8, 9], [5, 3, 2]) == []

    assert makeShell(1) == [[0]]
    assert makeShell(2) == [[0], [0, 0], [0]]
    assert makeShell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]]
