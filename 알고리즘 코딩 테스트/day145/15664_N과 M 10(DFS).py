# https://www.acmicpc.net/problem/15664
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

S = []

def dfs(start, depth):
    if depth == M:
        print(' '.join(str(x) for x in S))
        return

    last = 0
    for i in range(start, len(A)):
        if A[i] != last:
            S.append(A[i])
            last = A[i]

            dfs(i + 1, depth + 1)

            S.pop()

dfs(0, 0)