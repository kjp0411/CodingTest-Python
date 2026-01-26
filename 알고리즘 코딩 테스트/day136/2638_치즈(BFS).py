# https://www.acmicpc.net/problem/2638
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0

# 외부 공기 판단하는 함수
def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return visited

while True:
    outside = bfs()
    remove_cheese = []

    for a in range(N):
        for b in range(M):
            if grid[a][b] == 1:
                cnt = 0
                for i in range(4):
                    na, nb = a + dx[i], b + dy[i]
                    if 0 <= na < N and 0 <= nb < M and outside[na][nb]:
                        cnt += 1
                if cnt >= 2:
                    remove_cheese.append((a, b))

    # 더 이상 녹을 치즈가 없다면 종료
    if not remove_cheese:
        print(time)
        break

    # 치즈 한번에 녹이기
    for x, y in remove_cheese:
        grid[x][y] = 0

    time += 1