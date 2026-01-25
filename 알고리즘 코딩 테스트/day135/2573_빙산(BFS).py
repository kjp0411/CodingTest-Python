# https://www.acmicpc.net/problem/2573
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 빙산 좌표
icebergs = [(i, j) for i in range(N) for j in range(M) if grid[i][j] > 0]

def count_components():
    if not icebergs:
        return 0

    visited = [[False]*M for _ in range(N)]
    q = deque()

    sx, sy = icebergs[0]
    q.append((sx, sy))
    visited[sx][sy] = True
    visited_cnt = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] > 0:
                    visited[nx][ny] = True
                    visited_cnt += 1
                    q.append((nx, ny))

    return 2 if visited_cnt < len(icebergs) else 1


year = 0
while True:
    comp = count_components()

    if comp >= 2:
        print(year)
        break
    if comp == 0:
        print(0)
        break

    # 녹이기 계산
    melts = [[0]*M for _ in range(N)]
    for x, y in icebergs:
        melt = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                melt += 1
        melts[x][y] = melt

    # 녹이기 적용
    new_icebergs = []
    for x, y in icebergs:
        grid[x][y] = max(0, grid[x][y] - melts[x][y])
        if grid[x][y] > 0:
            new_icebergs.append((x, y))

    icebergs = new_icebergs
    year += 1