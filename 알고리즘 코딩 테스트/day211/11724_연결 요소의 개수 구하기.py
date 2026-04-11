# https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

count = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)