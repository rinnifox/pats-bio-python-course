#  This function returns string representing this list
def list_to_string(a):
    return str(a)


# This function adds border around a picture (nonempty list of nonempty strings of equal lengths).
# !!! Correct output - by using "for" !!! Using '\n'.join(b) -> not a list -> doesn't pass the assertion tests.
def add_border(a):
    b = []
    for elem in a:
        b.append('|'+elem+'|')
    b.insert(0, '+'+'-'*len(a[0])+'+')
    b.append('+'+'-'*len(a[1])+'+')
    return b


# This function returns reductions of strings of list
def shorting(e):
    new_list = []
    for elem in e:
        if len(elem) <= 10:
            new_list.append(elem)
        else:
            new_list.append(str(elem[0]) + str(len(elem)-2) + str(elem[len(elem)-1]))
    return new_list


# This function returns number of participants who will advance to the next round
def competition(e, k):
    next_round = []
    for elem in e:
        if elem >= e[k] and elem != 0:
            next_round.append(elem)
        else:
            break
    return len(next_round)


# This functiom returns sorted list of integers s = i ** 2 + j ** 2 if (i, j) is 'good'.
def good_pairs(a, b):
    s = []
    for i in a:
        for j in b:
            if (i*j) % (i+j) == 0:
                s.append(i**2+j**2)
    return sorted(s)


# This function returns list a of length 2 * n - 1. Its i-th element is list of some zeros.
def make_shell(n):
    shell = []
    i = 1
    j = n-1
    for first in range(n):
        shell.append([0]*i)
        i += 1
    for second in range(n, 2*n-1):
        shell.append([0] * j)
        j -= 1
    return shell


if __name__ == '__main__':
    assert list_to_string([]) == "[]"
    assert list_to_string([1, 2, 3]) == "[1, 2, 3]"
    assert list_to_string([-5]) == "[-5]"

    assert add_border(['abc', 'def']) == ['+---+', '|abc|', '|def|', '+---+']

    assert shorting(['word', 'localization', 'internationalization', 'pneumonoultramicroscopicsilicovolcanoconiosis']) \
        == ['word', 'l10n', 'i18n', 'p43s']

    assert competition([5, 4, 3, 2, 1], 2) == 3            # Participants with scores 5, 4, 3 are advanced
    assert competition([1, 0, 0, 0], 3) == 1               # Participants with zeros won't advance
    assert competition([10, 9, 8, 7, 7, 7, 5, 5], 4) == 6  # Participants with scores 10, 9, 8, 7, 7, 7 are advanced

    assert good_pairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == [128, 160, 180]
    assert good_pairs([2], [2]) == [8]
    assert good_pairs([7, 8, 9], [5, 3, 2]) == []

    assert make_shell(1) == [[0]]
    assert make_shell(2) == [[0], [0, 0], [0]]
    assert make_shell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]]