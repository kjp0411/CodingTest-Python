# https://www.acmicpc.net/problem/15654
N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
S = [0] * M
visited = [False] * (N+1)
def dfs(length):
    if length == M:
        print(' '.join(str(x) for x in S))
        return

    for i in range(len(A)):
        if not visited[i]:
            visited[i] = True
            S[length] = A[i]
            dfs(length + 1)
            visited[i] = False

dfs(0)