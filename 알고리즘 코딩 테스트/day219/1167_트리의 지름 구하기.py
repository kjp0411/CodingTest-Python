# https://www.acmicpc.net/problem/1167
from collections import deque
import sys

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    data = list(map(int, input().split()))
    u = data[0]
    i = 1
    while data[i] != -1:
        v = data[i]
        dist = data[i+1]

        graph[u].append((v, dist))

        i += 2

def bfs(start):
    visited = [False] * (V + 1)
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    max_dist = 0
    max_node = start

    while queue:
        node, dist = queue.popleft()

        if dist > max_dist:
            max_dist = dist
            max_node = node

        for next_node, next_dist in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + next_dist))

    return max_node, max_dist

node, _ = bfs(1)
_, answer = bfs(node)
print(answer)