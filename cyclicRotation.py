def solution(A, K):
    if A:
        for _ in range(K):
            A.insert(0, A.pop())

    return A
