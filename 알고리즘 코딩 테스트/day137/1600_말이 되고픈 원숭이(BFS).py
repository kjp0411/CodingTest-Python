# https://www.acmicpc.net/problem/1600
import sys
from collections import deque

input = sys.stdin.readline

K = int(input().strip())
W, H = map(int, input().strip().split())
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[[False]*(K+1) for _ in range(W)] for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hdx = [-2, -2, 2, 2, 1, -1, 1, -1]
hdy = [1, -1, 1, -1, -2, -2, 2, 2]

def bfs():
    queue = deque()
    queue.append((0, 0, K, 0))
    visited[0][0][K] = True
    while queue:
        x, y, k, d = queue.popleft()
        if x == (H-1) and y == (W-1):
            return d

        if k > 0:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < H and 0 <= ny < W and visited[nx][ny][k] == False and board[nx][ny] == 0:
                    visited[nx][ny][k] = True
                    queue.append((nx, ny, k, d+1))

            for j in range(8):
                hnx, hny = x + hdx[j], y + hdy[j]
                if 0 <= hnx < H and 0 <= hny < W and visited[hnx][hny][k-1] == False and board[hnx][hny] == 0:
                    visited[hnx][hny][k-1] = True
                    queue.append((hnx, hny, k-1, d+1))
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < H and 0 <= ny < W and visited[nx][ny][k] == False and board[nx][ny] == 0:
                    visited[nx][ny][k] = True
                    queue.append((nx, ny, k, d+1))
    return -1

print(bfs())