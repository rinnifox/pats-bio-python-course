import numpy as np


# Returns dimension of array a
def getdimension(a):
    return np.ndim(a)


# Finds the diagonal.of 2-dimensional square array a
def getdiagonal(a):
    return np.diagonal(a)


# Returns copy of array a with some values replaces:
#   if entry x is less than minvalue, replace it with minvalue;
#   if entry x is greater than maxvalue, replace it with maxvalue;
#   otherwise you should not replace it
def cutarray(a, minvalue, maxvalue):
    return np.clip(a, minvalue, maxvalue)


# Returns tuple with two values:
#   mean value of entries of a;
#   mariance of entries of a
def getmoments(a):
    return tuple([np.mean(a), np.var(a)])


# Returns dot product of vectors a*b (1-dimensional arrays of the same length)
def getdotproduct(a, b):
    return np.dot(a, b)


# Returns the matrix of the same shape as a and b such that entry of result is
# True if corresponding elements of a and b are equal or False otherwise
def checkequal(a, b):
    return a == b


# Returns the  matrix of the same shape as a such that element of the result is
# True if corresponding element of a is less than bound and False otherwise
def comparewithnumber(a, bound):
    return a < bound


# Returns the product of matrices represented by the arrays a and b, which are
# 2-dimensional arrays of shapes (n, m) and (m, k), n, m, k > 0
def matrixproduct(a, b):
    return np.matmul(a, b)


# Finds the determinant of the matrix repr. by the square 2-dimensional array
def matrixdet(a):
    return np.linalg.det(a)


# Returns 2-dimensional array of shape (n, n) such that:
#   1.0 if j - i = k
#   0.0 otherwise
def getones(n, k):
    return np.eye(n, k=k)


if __name__ == '__main__':
    assert getdimension(np.array([1, 2, 3])) == 1
    assert getdimension(np.array([[1], [2], [3]])) == 2
    assert getdimension(np.array([[[[1]]]])) == 4
    print('getdimension - PASSED')

    assert np.array_equal(getdiagonal(np.array([[1]])), np.array([1]))
    assert np.array_equal(np.array(getdiagonal(np.array([[1, 2], [3, 4]]))),
                          np.array([1, 4]))
    print('getdiagonal - PASSED')

    assert np.array_equal(cutarray(np.array([1, 2, 3, 4]), 2, 3),
                          np.array([2, 2, 3, 3]))
    print('cutarray - PASSED')

    assert getmoments(np.array([2, 1, 9])) == (4.0, 12.666666666666666)
    print('getmoments - PASSED')

    assert getdotproduct(np.array([1, 2, 3]), np.array([4, 5, 6])) == 32
    print('getdotproduct - PASSED')

    assert np.array_equal(checkequal(np.array([1, 2, 3]), np.array([1, 5, 3])),
                          np.array([True, False, True]))
    print('checkequal - PASSED')

    assert np.array_equal(comparewithnumber(np.array([[1, 2], [3, 4]]), 4),
                          np.array([[True, True], [True, False]]))
    print('comparewithnumber - PASSED')

    assert np.array_equal(matrixproduct(np.array([[1, 2], [3, 4]]),
                                        np.array([[5, 6], [7, 8]])),
                          np.array([[19, 22], [43, 50]]))
    assert np.array_equal(matrixproduct(np.array([[1, 2]]),
                                        np.array([[3], [4]])),
                                        np.array([[11]]))
    print('matrixproduct - PASSED')

    assert int(matrixdet(np.array([[5, 6], [7, 8]]))) == -2
    assert int(round(matrixdet(np.array([[123]])))) == 123
    print('matrixdet - PASSED')

    assert np.array_equal(getones(3, 1), np.array([[0., 1., 0.],
                                                   [0., 0., 1.],
                                                   [0., 0., 0.]]))
    assert np.array_equal(getones(3, 9), np.array([[0., 0., 0.],
                                                   [0., 0., 0.],
                                                   [0., 0., 0.]]))
    print('getones - PASSED')