# https://www.acmicpc.net/problem/2178
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))

bfs()
print(board[N-1][M-1])