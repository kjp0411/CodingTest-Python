# https://www.acmicpc.net/problem/15663
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

visited = [False] * N
S = []

def dfs(depth):
    if depth == M:
        print(' '.join(str(x) for x in S))
        return

    last = 0
    for i in range(N):
        if not visited[i] and A[i] != last:
            visited[i] =True
            S.append(A[i])
            last = A[i]

            dfs(depth + 1)

            visited[i] = False
            S.pop()

dfs(0)