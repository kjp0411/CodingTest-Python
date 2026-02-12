# https://www.acmicpc.net/problem/4179
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
fire_time = [[-1] * C for _ in range(R)]
jh_time = [[-1] * C for _ in range(R)]

jx, jy = 0, 0
fire = []

for x in range(R):
    for y in range(C):
        if board[x][y] == 'J':
            jx = x
            jy = y
        elif board[x][y] == 'F':
            fire.append((x, y))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def F_bfs():
    queue = deque()

    for fx, fy in fire:
        queue.append((fx, fy))
        fire_time[fx][fy] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    queue.append((nx, ny))

def J_bfs():
    queue = deque()
    queue.append((jx, jy))
    jh_time[jx][jy] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 탈출 조건
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return jh_time[x][y] + 1

            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] != '#' and jh_time[nx][ny] == -1:
                    if fire_time[nx][ny] == -1 or fire_time[nx][ny] > jh_time[x][y] + 1:
                        jh_time[nx][ny] = jh_time[x][y] + 1
                        queue.append((nx, ny))
    return "IMPOSSIBLE"

F_bfs()
print(J_bfs())