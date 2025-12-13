# https://www.acmicpc.net/problem/19238
from collections import deque
import sys
input = sys.stdin.readline

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

tx, ty = map(lambda x: int(x) - 1, input().split())

# 승객 정보: (sx, sy) -> (ex, ey)
passengers = {}
for _ in range(M):
    sx, sy, ex, ey = map(lambda x: int(x) - 1, input().split())
    passengers[(sx, sy)] = (ex, ey)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(start_x, start_y):
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((start_x, start_y))
    dist[start_x][start_y] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

for _ in range(M):
    dist = bfs(tx, ty)

    candidates = []
    for (sx, sy) in passengers:
        if dist[sx][sy] != -1:
            candidates.append((dist[sx][sy], sx, sy))

    if not candidates:
        print(-1)
        sys.exit()

    candidates.sort()
    d_to_passenger, px, py = candidates[0]

    if fuel < d_to_passenger:
        print(-1)
        sys.exit()

    fuel -= d_to_passenger
    tx, ty = px, py

    ex, ey = passengers[(px, py)]
    dist2 = bfs(tx, ty)

    d_to_dest = dist2[ex][ey]
    if d_to_dest == -1 or fuel < d_to_dest:
        print(-1)
        sys.exit()

    fuel += d_to_dest
    tx, ty = ex, ey
    del passengers[(px, py)]

print(fuel)
