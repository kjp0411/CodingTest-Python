# https://www.acmicpc.net/problem/13023
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N)]
visited = [False] * N
answer = False

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

def dfs(now, depth):
    global answer

    if answer:
        return

    visited[now] = True

    if depth == 4:
        answer = True
        visited[now] = False
        return
    for next in A[now]:
        if not visited[next]:
            dfs(next, depth + 1)
    visited[now] = False

for i in range(N):
    if answer:
        break
    dfs(i, 0)

if answer:
    print(1)
else:
    print(0)