# https://www.acmicpc.net/problem/15655
N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
S = [0] * M
visited = [False] * (N+1)

def dfs(start, length):
    if length == M:
        print(' '.join(str(x) for x in S))
        return

    for i in range(start, len(A)):
        S[length] = A[i]
        dfs(i+1, length + 1)

dfs(0, 0)