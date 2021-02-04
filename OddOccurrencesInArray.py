# write a function that given an arry of integers returns the odd occuring integer ie all others can be paired except that odd occurance


def solution(A):
    oddNum = 0
    for i in A:
        oddNum ^= i  # XOR operation.

    return oddNum
