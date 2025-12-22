# https://www.acmicpc.net/problem/23288
import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]  # 동 남 서 북
dy = [1, 0, -1, 0]

dice = [1, 2, 3, 4, 5, 6]  # 위, 북, 동, 서, 남, 바닥
x, y = 0, 0
dir = 0
score = 0

def roll(d, dir):
    top, north, east, west, south, bottom = d
    if dir == 0:
        return [west, north, top, bottom, south, east]
    elif dir == 1:
        return [north, bottom, east, west, top, south]
    elif dir == 2:
        return [east, north, bottom, top, south, west]
    else:
        return [south, top, east, west, bottom, north]

def bfs(x, y):
    visited = [[False]*M for _ in range(N)]
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    value = board[x][y]

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny] == value:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt * value

for _ in range(K):
    nx, ny = x + dx[dir], y + dy[dir]

    if not (0 <= nx < N and 0 <= ny < M):
        dir = (dir + 2) % 4
        nx, ny = x + dx[dir], y + dy[dir]

    dice = roll(dice, dir)
    x, y = nx, ny

    score += bfs(x, y)

    A = dice[5]
    B = board[x][y]

    if A > B:
        dir = (dir + 1) % 4
    elif A < B:
        dir = (dir - 1) % 4

print(score)