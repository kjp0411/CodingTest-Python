# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
grid = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    grid.append(layer)

queue = deque()

for z in range(H):
    for x in range(N):
        for y in range(M):
            if grid[z][x][y] == 1:
                queue.append((z, x, y))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue:
    z, x, y = queue.popleft()
    for i in range(6):
        nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if grid[nz][nx][ny] == 0:
                grid[nz][nx][ny] = grid[z][x][y] + 1
                queue.append((nz, nx, ny))

zero_exist = False
days = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if grid[z][x][y] == 0:
                zero_exist = True
            elif grid[z][x][y] > 0:
                if grid[z][x][y] > days:
                    days = grid[z][x][y]

if zero_exist == True:
    print(-1)
else:
    print(days-1)