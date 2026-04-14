# https://www.acmicpc.net/problem/15649
N, M = map(int, input().split())
S = [0] * M
visited = [False] * (N+1)

def dfs(length):
    if length == M:
        print(' '.join(str(x) for x in S))
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            S[length] = i
            dfs(length + 1)
            visited[i] = False

dfs(0)