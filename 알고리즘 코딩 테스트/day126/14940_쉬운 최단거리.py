# https://www.acmicpc.net/problem/14940
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                sr, sc = i, j

    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = True

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr, nc = r + dx[d], c + dy[d]
            if 0 <= nr < N and 0 <= nc < M:
                cell = grid[nr][nc]
                if cell == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    dist[nr][nc] = dist[r][c] + 1

bfs()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            print(0, end=' ')
        elif grid[i][j] == 1 and not visited[i][j]:
            print(-1, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()