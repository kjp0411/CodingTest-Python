# https://www.acmicpc.net/problem/15651
N, M = map(int, input().split())
S = [0] * M

def dfs(length):
    if length == M:
        print(' '.join(str(x) for x in S))
        return

    for i in range(1, N+1):
        S[length] = i
        dfs(length + 1)

dfs(0)