# https://www.acmicpc.net/problem/2667
import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sr, sc):
    queue = deque([(sr, sc)])
    visited[sr][sc] = True
    size = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and grid[nr][nc] == '1':
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    size += 1

    return size

sizes = []

for r in range(N):
    for c in range(N):
        if grid[r][c] == '1' and not visited[r][c]:
            sizes.append(bfs(r, c))

sizes.sort()
print(len(sizes))
for s in sizes:
    print(s)