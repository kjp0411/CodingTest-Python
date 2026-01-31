# https://www.acmicpc.net/problem/15652
N, M = map(int, input().split())
S = [0] * M

def dfs(start, length):
    if length == M:
        print(' '.join(str(x) for x in S))
        return

    for i in range(start, N+1):
        S[length] = i
        dfs(i, length + 1)

dfs(1, 0)