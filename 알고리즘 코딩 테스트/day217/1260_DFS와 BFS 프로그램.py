# https://www.acmicpc.net/problem/1260
from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N+1):
    A[i].sort()

visited = [False] * (N + 1)

def dfs(v):
    print(v, end=' ')
    visited[v] = True

    for next in A[v]:
        if not visited[next]:
            dfs(next)

dfs(V)
print()

visited = [False] * (N + 1)
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for next in A[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

bfs(V)
