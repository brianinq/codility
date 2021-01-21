# This is the solution to the codility binary gap example
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
# Write a function:
# def solution(N)
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

def solution(N):
    return len(max(bin(N)[2:].strip("0").split('1')))
