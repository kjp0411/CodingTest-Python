# https://www.acmicpc.net/problem/7569
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())     # M=열, N=행, H=높이
grid = [[[0] * M for _ in range(N)] for _ in range(H)]

for z in range(H):
    for y in range(N):
        row = list(map(int, input().split()))
        grid[z][y] = row

queue = deque()
unripe = 0  # 안 익은 토마토 수

for z in range(H):
    for y in range(N):
        for x in range(M):
            if grid[z][y][x] == 1:
                queue.append((z, y, x))     # 멀티 소스 시작점
            elif grid[z][y][x] == 0:
                unripe += 1

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

days = 0
while queue and unripe > 0:
    for _ in range(len(queue)):
        z, y, x = queue.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and grid[nz][ny][nx] == 0:
                grid[nz][ny][nx] = 1
                unripe -= 1
                queue.append((nz, ny, nx))
    days += 1

print(days if unripe == 0 else -1)